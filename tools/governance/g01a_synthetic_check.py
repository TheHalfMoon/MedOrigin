#!/usr/bin/env python3
"""Fail-closed verification of an offline, synthetic-only G01a engineering fixture."""
from __future__ import annotations

import argparse
import hashlib
import json
import tomllib
from pathlib import Path

MANIFEST = "docs/evidence/g01a_synthetic_manifest.json"
FIXTURE = "fixtures/g01a_synthetic_v1.txt"
SOURCE = "crates/g01a-synthetic/src/lib.rs"
SOURCE_SHA256 = "35356b0c9d5bcd70231fd6c038574ebc5951530f03c50235d4a0447049761860"
SHA256 = "6d7d7070cb270e830b5d232f1aa127c0d5fa0eac1fdf1677c3de2898a417c3dd"
FIELDS = {
    "schema_version", "phase", "classification", "clinical_validation",
    "source_imports", "copy_authorized", "fixture_path", "fixture_sha256",
    "dependencies", "source_path", "source_sha256",
}

# All inputs affecting the frozen synthetic build must be ordinary in-tree
# files. Reject links at every path component, not just the final file, so
# an outside tree cannot supply Cargo/toolchain policy or frozen evidence.
TRUSTED_INPUTS = (
    MANIFEST, FIXTURE, SOURCE, "Cargo.lock", "Cargo.toml",
    "crates/g01a-synthetic/Cargo.toml", "rust-toolchain.toml", ".gitattributes",
)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Reject ambiguous JSON records instead of accepting the final duplicate value."""
    record: dict[str, object] = {}
    for key, value in pairs:
        if key in record:
            raise ValueError(f"Duplicate JSON key: {key}")
        record[key] = value
    return record


def check(root: Path) -> dict[str, object]:
    errors: list[str] = []
    # Do not read any trusted input through a symlink, including a symlink
    # to an ancestor directory. Checking content alone is not enough: the
    # referenced out-of-tree file can change after admission but before Cargo.
    for relative in TRUSTED_INPUTS:
        current = root
        for part in Path(relative).parts:
            current = current / part
            if current.is_symlink():
                errors.append(f"Symbolic link in trusted G01a input: {relative}")
                break
    if errors:
        return {
            "structure": "FAIL",
            "classification": "SYNTHETIC_ONLY",
            "clinical_validation": "NOT_PERFORMED",
            "source_imports": "BLOCKED",
            "copy_authorized": False,
            "frozen_fixture_sha256": SHA256,
            "frozen_source_sha256": SOURCE_SHA256,
            "errors": errors,
        }
    try:
        manifest = json.loads(
            (root / MANIFEST).read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
        lock = tomllib.loads((root / "Cargo.lock").read_text(encoding="utf-8"))
        cargo = tomllib.loads((root / "Cargo.toml").read_text(encoding="utf-8"))
        crate = tomllib.loads(
            (root / "crates/g01a-synthetic/Cargo.toml").read_text(encoding="utf-8")
        )
        toolchain = tomllib.loads(
            (root / "rust-toolchain.toml").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"Unreadable bootstrap record: {type(exc).__name__}")
        manifest, lock, cargo, crate, toolchain = {}, {}, {}, {}, {}

    expected = {
        "schema_version": 1,
        "phase": "G01A_ENGINEERING_ONLY",
        "classification": "SYNTHETIC_ONLY",
        "clinical_validation": "NOT_PERFORMED",
        "source_imports": "BLOCKED",
        "copy_authorized": False,
        "fixture_path": FIXTURE,
        "fixture_sha256": SHA256,
        "dependencies": "STANDARD_LIBRARY_ONLY",
        "source_path": SOURCE,
        "source_sha256": SOURCE_SHA256,
    }
    if not isinstance(manifest, dict) or set(manifest) != FIELDS or manifest != expected:
        errors.append("Synthetic manifest schema or immutable denial values differ")

    path = root / FIXTURE
    try:
        if path.is_symlink() or not path.is_file():
            errors.append("Fixture is absent or a symbolic link")
        else:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != SHA256:
                errors.append("Frozen synthetic fixture digest mismatch")
    except OSError:
        errors.append("Fixture is unreadable")

    source = root / SOURCE
    try:
        if source.is_symlink() or not source.is_file():
            errors.append("Reviewed Rust source absent or symbolic link")
        elif hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_SHA256:
            errors.append("Frozen reviewed Rust source digest mismatch")
    except OSError:
        errors.append("Reviewed Rust source is unreadable")

    for config_dir in (
        root / ".cargo",
        root / "crates/.cargo",
        root / "crates/g01a-synthetic/.cargo",
    ):
        if config_dir.exists() or config_dir.is_symlink():
            errors.append("Unreviewed Cargo configuration directory exists")

    try:
        attributes = (root / ".gitattributes").read_text(encoding="utf-8")
        if attributes.splitlines() != [
            "fixtures/g01a_synthetic_v1.txt text eol=lf",
            "crates/g01a-synthetic/src/lib.rs text eol=lf",
        ]:
            errors.append("Synthetic fixture checkout must enforce LF line endings")
    except (OSError, UnicodeError):
        errors.append("Missing synthetic fixture LF checkout policy")

    # A Cargo build.rs is executable even with zero dependencies. Implicit
    # binary/example/bench targets similarly bypass manifest dependency checks.
    # Keep G01a's source inventory limited to the reviewed synthetic lib.
    crate_root = root / "crates/g01a-synthetic"
    allowed_files = {"Cargo.toml", "src/lib.rs"}
    try:
        observed_files = {
            path.relative_to(crate_root).as_posix()
            for path in crate_root.rglob("*")
            if path.is_file() or path.is_symlink()
        }
        if (crate_root.is_symlink() or (crate_root / "src").is_symlink()
                or observed_files != allowed_files):
            errors.append("Unexpected G01a crate source or executable target")
    except OSError:
        errors.append("Cannot inspect G01a crate source inventory")

    pkgs = lock.get("package", []) if isinstance(lock, dict) else []
    if not isinstance(pkgs, list) or len(pkgs) != 1 or not isinstance(pkgs[0], dict) or (
        pkgs[0].get("name") != "safeevidence-g01a-synthetic"
        or pkgs[0].get("version") != "0.0.0"
        or set(pkgs[0]) != {"name", "version"}
    ):
        errors.append("Cargo lockfile must contain only one local crate")
    if set(lock) != {"version", "package"} or lock.get("version") != 4:
        errors.append("Unexpected Cargo.lock sections or format version")
    if set(cargo) != {"workspace"} or cargo.get("workspace") != {
        "resolver": "3", "members": ["crates/g01a-synthetic"]
    }:
        errors.append("Unexpected Rust workspace contract")
    package = crate.get("package", {}) if isinstance(crate, dict) else {}
    if set(crate) != {"package", "dependencies"} or package != {
        "name": "safeevidence-g01a-synthetic",
        "version": "0.0.0",
        "edition": "2024",
        "rust-version": "1.97.1",
        "publish": False,
    }:
        errors.append("Unapproved crate manifest section or target configuration")
    if crate.get("dependencies") != {}:
        errors.append("Third-party crate dependencies are forbidden in G01a")
    if set(toolchain) != {"toolchain"} or toolchain.get("toolchain") != {
        "channel": "1.97.1", "profile": "minimal",
        "components": ["rustfmt", "clippy"]
    }:
        errors.append("Rust toolchain pin differs")

    return {
        "structure": "PASS" if not errors else "FAIL",
        "classification": "SYNTHETIC_ONLY",
        "clinical_validation": "NOT_PERFORMED",
        "source_imports": "BLOCKED",
        "copy_authorized": False,
        "frozen_fixture_sha256": SHA256,
        "frozen_source_sha256": SOURCE_SHA256,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true")
    opts = parser.parse_args()
    report = check(opts.root.resolve())
    if opts.json:
        print(json.dumps(report, sort_keys=True, indent=2))
    else:
        print(f"synthetic integrity: {report['structure']}")
        for error in report["errors"]:
            print("ERROR:", error)
    return 0 if report["structure"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
