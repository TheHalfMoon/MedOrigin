#!/usr/bin/env python3
"""Offline external-byte comparison for unadmitted reference-only donor files.

A successful MATCH is identity evidence, never source import or clinical approval.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from p01_candidate_integrity import MANIFEST, check


def verify(root: Path, repo: str, path: str, blob: Path) -> dict[str, object]:
    report: dict[str, object] = {
        "byte_integrity": "BLOCKED", "source_imports": "BLOCKED",
        "copy_authorized": False, "clinical_validation": "NOT_PERFORMED",
        "errors": [],
    }

    def deny(reason: str, status: str = "BLOCKED") -> dict[str, object]:
        report["byte_integrity"] = status
        report["errors"].append(reason)
        return report

    root = root.resolve()
    if check(root)["structure"] != "PASS":
        return deny("Canonical reference evidence failed")
    try:
        data = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
        candidates = [item for item in data["entries"]
                      if item["repo"] == repo and item["path"] == path]
        if len(candidates) != 1:
            return deny("No exact unique candidate")
        item = candidates[0]
        if item["copy_authorized"] is not False or item["admission_state"] != "REFERENCE_ONLY":
            return deny("Candidate no longer reference-only")
        size, expected_sha, expected_oid = (
            item["byte_count"], item["raw_sha256"], item["git_blob_oid"]
        )
        if size is None or expected_sha is None:
            return deny("Candidate lacks raw byte fingerprint")
        if blob.is_symlink():
            return deny("Symbolic links not accepted")
        actual = blob.resolve(strict=True)
        if actual.is_relative_to(root) or not actual.is_file():
            return deny("Input must be an external regular file")
        before = actual.stat()
        if before.st_size != size:
            return deny("Byte count mismatch", "MISMATCH")
        # A matching digest only describes a stable observed file. Checking
        # length alone would accept same-sized in-place changes during a read.
        def identity(info: os.stat_result) -> tuple[int, int, int, int, int]:
            return (info.st_dev, info.st_ino, info.st_size,
                    info.st_mtime_ns, info.st_ctime_ns)

        sha = hashlib.sha256()
        git_oid = hashlib.sha1(usedforsecurity=False)
        git_oid.update(b"blob " + str(size).encode("ascii") + b"\0")
        count = 0
        with actual.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            if not stat.S_ISREG(opened.st_mode) or identity(before) != identity(opened):
                return deny("Input changed before read", "MISMATCH")
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                count += len(chunk)
                sha.update(chunk)
                git_oid.update(chunk)
            finished = os.fstat(stream.fileno())
        after = actual.stat()
        if (count != size or identity(before) != identity(finished)
                or identity(before) != identity(after)):
            return deny("Input changed during read or replaced on disk", "MISMATCH")
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, RuntimeError) as exc:
        return deny("Input unavailable or unsafe: " + type(exc).__name__)
    if sha.hexdigest() != expected_sha or git_oid.hexdigest() != expected_oid:
        return deny("Byte identity differs from ledger", "MISMATCH")
    report["byte_integrity"] = "MATCH"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--repo", required=True)
    parser.add_argument("--path", required=True)
    parser.add_argument("--blob", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.root, args.repo, args.path, args.blob)
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0 if report["byte_integrity"] == "MATCH" else 2


if __name__ == "__main__":
    raise SystemExit(main())
