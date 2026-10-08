#!/usr/bin/env python3
"""Offline integrity guard for unadmitted donor candidate *metadata*.

This does not download source, verify contributor rights, or allow imports.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MANIFEST = "docs/evidence/p01_donor_candidates_2026-10-08.json"
SOURCE = "docs/P01_PINNED_SOURCE_EVIDENCE_2026-10-08.md"
EXPECTED = {
    ("MedScale", "crates/medscale-core/src/release_sbom.rs"),
    ("MedScale", "crates/medscale-core/tests/release_sbom_054.rs"),
    ("MedScale", "scripts/generate-release-sbom.ps1"),
    ("MedScale", ".github/workflows/ci.yml"),
    ("ottari", "tools/provenance.py"),
    ("ottari", "tools/provenance_gate.py"),
    ("ottari", ".github/workflows/ci.yml"),
    ("kernux", ".github/workflows/ci.yml"),
    ("Ascout", ".github/workflows/self-verify.yml"),
    ("MESC", "src/medscale/provenance.py"),
    ("MESC", "tests/test_provenance.py"),
}
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
ENTRY_KEYS = {
    "repo", "source_commit", "path", "git_blob_oid", "byte_count",
    "raw_sha256", "admission_state", "copy_authorized",
}


def check(root: Path) -> dict[str, object]:
    errors: list[str] = []
    manifest_path = root / MANIFEST
    source_path = root / SOURCE
    try:
        document = json.loads(manifest_path.read_text(encoding="utf-8"))
        source = source_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as exc:
        return {"structure": "FAIL", "errors": [f"Unreadable evidence: {type(exc).__name__}"],
                "copy_authorized": False, "source_imports": "BLOCKED"}
    if not isinstance(document, dict) or set(document) != {
        "schema_version", "purpose", "phase", "admissions", "entries",
    }:
        errors.append("Unexpected manifest schema or authority field")
        document = document if isinstance(document, dict) else {}
    if document.get("schema_version") != 1:
        errors.append("Unrecognized schema version")
    if document.get("phase") != "P01_PRE_ENTRY_GATES_PENDING":
        errors.append("Phase must remain pre-entry")
    if document.get("admissions") != []:
        errors.append("Candidate manifest cannot admit any source")
    if not isinstance(document.get("purpose"), str) or "never an import allowlist" not in document["purpose"]:
        errors.append("Missing explicit non-admission purpose")
    entries = document.get("entries")
    if not isinstance(entries, list):
        errors.append("Entries must be an array")
        entries = []
    seen: set[tuple[str, str]] = set()
    sha_count = 0
    commits: dict[str, str] = {}
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != ENTRY_KEYS:
            errors.append(f"Entry {i}: schema mismatch")
            continue
        repo = entry["repo"]
        path = entry["path"]
        oid = entry["git_blob_oid"]
        sha = entry["raw_sha256"]
        size = entry["byte_count"]
        commit = entry["source_commit"]
        if not isinstance(repo, str) or not repo.startswith("TheHalfMoon/"):
            errors.append(f"Entry {i}: invalid source repository")
            continue
        short = repo.removeprefix("TheHalfMoon/")
        if not isinstance(path, str) or (
            not path or path.startswith(("/", "\\")) or "\\" in path
            or any(part in ("", ".", "..") for part in path.split("/"))
            or ":" in path
        ):
            errors.append(f"Entry {i}: unsafe source path")
            continue
        key = (short, path)
        if key in seen:
            errors.append(f"Entry {i}: duplicate exact source")
        seen.add(key)
        if key not in EXPECTED:
            errors.append(f"Entry {i}: unexpected candidate")
        if not isinstance(oid, str) or not HEX40.fullmatch(oid):
            errors.append(f"Entry {i}: invalid Git blob")
        elif f"| {short} | `{path}` | `{oid}` |" not in source:
            errors.append(f"Entry {i}: Git blob differs from source ledger")
        if not isinstance(commit, str) or not HEX40.fullmatch(commit):
            errors.append(f"Entry {i}: invalid source commit")
        else:
            if short in commits and commits[short] != commit:
                errors.append(f"Entry {i}: inconsistent source commit")
            commits[short] = commit
            if f"/{short}/tree/{commit}" not in source:
                errors.append(f"Entry {i}: source revision absent from ledger")
        if entry["admission_state"] != "REFERENCE_ONLY" or entry["copy_authorized"] is not False:
            errors.append(f"Entry {i}: unauthorized elevation of source admission")
        if (sha is None) != (size is None):
            errors.append(f"Entry {i}: fingerprint and byte size must be paired")
        elif sha is not None:
            if not isinstance(sha, str) or not HEX64.fullmatch(sha) or sha == EMPTY_SHA256:
                errors.append(f"Entry {i}: invalid/empty-byte SHA256")
            elif not isinstance(size, int) or isinstance(size, bool) or size <= 0:
                errors.append(f"Entry {i}: invalid byte count")
            elif f"`{sha}`" not in source or f"| {size} |" not in source:
                errors.append(f"Entry {i}: raw fingerprint not in written evidence")
            sha_count += 1
    if seen != EXPECTED:
        errors.append(f"Candidate set differs: missing={len(EXPECTED - seen)} extra={len(seen - EXPECTED)}")
    if sha_count != 6:
        errors.append("Exactly six verified fingerprints expected; others unverified")
    if "NO_ADMISSIONS" not in source or "REFERENCE_ONLY" not in source:
        errors.append("Source ledger fails closed markers")
    return {
        "structure": "PASS" if not errors else "FAIL",
        "candidate_count": len(entries),
        "raw_fingerprints_recorded": sha_count,
        "copy_authorized": False,
        "source_imports": "BLOCKED",
        "clinical_validation": "NOT_PERFORMED",
        "note": "Metadata consistency only; no live GitHub, bytes, licenses or signers checked.",
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    result = check(args.root.resolve())
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if result["structure"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
