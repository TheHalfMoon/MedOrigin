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
SHA256 = "6d7d7070cb270e830b5d232f1aa127c0d5fa0eac1fdf1677c3de2898a417c3dd"
FIELDS = {
    "schema_version", "phase", "classification", "clinical_validation",
    "source_imports", "copy_authorized", "fixture_path", "fixture_sha256",
    "dependencies",
}


def check(root: Path) -> dict[str, object]:
    errors: list[str] = []
    try:
        manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
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

    pkgs = lock.get("package", []) if isinstance(lock, dict) else []
    if not isinstance(pkgs, list) or len(pkgs) != 1 or not isinstance(pkgs[0], dict) or (
        pkgs[0].get("name") != "safeevidence-g01a-synthetic"
        or set(pkgs[0]) != {"name", "version"}
    ):
        errors.append("Cargo lockfile must contain only one local crate")
    if cargo.get("workspace") != {
        "resolver": "3", "members": ["crates/g01a-synthetic"]
    }:
        errors.append("Unexpected Rust workspace contract")
    package = crate.get("package", {}) if isinstance(crate, dict) else {}
    if package.get("publish") is not False or package.get("rust-version") != "1.97.1":
        errors.append("Crate must remain unpublished and Rust pinned")
    if crate.get("dependencies") != {} or "dev-dependencies" in crate or "build-dependencies" in crate:
        errors.append("Third-party crate dependencies are forbidden in G01a")
    if toolchain.get("toolchain") != {
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
