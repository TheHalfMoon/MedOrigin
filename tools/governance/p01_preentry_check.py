#!/usr/bin/env python3
"""Validate P01 pre-entry documentation; never authorize clinical implementation.

No third-party packages, network access, medical decisions, or privileged actions.
Successful structural checks mean the evidence register is intact, NOT approved.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

ID_RE = re.compile(r"^\|\s*(CODEX-P00-\d{2}|OPUS-P00-\d{3})\s*\|")
EXPECTED = {
    "CODEX": {f"CODEX-P00-{n:02d}" for n in range(7, 31)},
    "OPUS": {f"OPUS-P00-{n:03d}" for n in range(3, 20)},
}
ORIGINAL_PATHS = {
    "CODEX": "docs/P00_CODEX_P1_ACCEPTANCE_REGISTER.md",
    "OPUS": "docs/P00_OPUS_P1_ACCEPTANCE_REGISTER.md",
}
TRACKER = "docs/P01_P1_GATE_TRACKER_2026-10-08.md"
ENTRY = "docs/P01_ENTRY_READINESS_2026-10-08.md"
CHARTER = "docs/P01_CLINICAL_EVALUATION_CHARTER_DRAFT_2026-10-08.md"
RIGHTS = "docs/DONOR_RIGHTS_REGISTER.md"


def read(root: Path, relative: str, problems: list[str]) -> str:
    path = root / relative
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        problems.append(f"Required readable file missing: {relative} ({type(exc).__name__})")
        return ""


def rows(text: str, path: str, problems: list[str]) -> dict[str, list[str]]:
    """Read P1 findings only from the single canonical Markdown table.

    Rows in notes, fenced examples or detached tables are not authority.
    """
    expected_header = "ID" if path == TRACKER else "Finding"
    found: dict[str, list[str]] = {}
    in_table = False
    header_count = 0
    for line in text.splitlines():
        if line.startswith("|"):
            columns = [value.strip() for value in line.split("|")[1:-1]]
            if columns and columns[0] == expected_header:
                header_count += 1
                if header_count > 1:
                    problems.append(f"Duplicate P1 table header in {path}")
                in_table = header_count == 1
                continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if not line.endswith("|"):
            problems.append(f"Malformed P1 row in {path}")
            continue
        columns = [value.strip() for value in line.split("|")[1:-1]]
        if columns and columns[0] == "---":
            continue
        if not ID_RE.match(line):
            problems.append(f"Unexpected row in P1 table {path}")
            continue
        key = columns[0]
        if key in found:
            problems.append(f"Duplicate P1 ID {key} in {path}")
        else:
            found[key] = columns
    if header_count != 1:
        problems.append(f"Missing or duplicated P1 table in {path}")
    return found

def validate(root: Path, expected_sha: str | None = None) -> dict[str, object]:
    """Return structural status and explicit BLOCKED activation separately."""
    problems: list[str] = []
    if expected_sha:
        try:
            head = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            problems.append("Cannot resolve exact Git HEAD")
        else:
            if head != expected_sha:
                problems.append("Git HEAD does not match expected exact SHA")
    expected_all = set().union(*EXPECTED.values())
    originals: dict[str, list[str]] = {}
    for reviewer, path in ORIGINAL_PATHS.items():
        found = rows(read(root, path, problems), path, problems)
        missing = sorted(EXPECTED[reviewer] - set(found))
        extra = sorted(set(found) - EXPECTED[reviewer])
        if missing:
            problems.append(f"{reviewer} source IDs missing: {','.join(missing)}")
        if extra:
            problems.append(f"{reviewer} source IDs unexpected: {','.join(extra)}")
        originals.update(found)
    actual = rows(read(root, TRACKER, problems), TRACKER, problems)
    missing = sorted(expected_all - set(actual))
    extra = sorted(set(actual) - expected_all)
    if missing:
        problems.append(f"P01 tracker missing IDs: {','.join(missing)}")
    if extra:
        problems.append(f"P01 tracker unexpected IDs: {','.join(extra)}")
    for key in sorted(expected_all & set(actual) & set(originals)):
        original = originals[key]
        tracked = actual[key]
        if len(original) != 5 or len(tracked) != 6:
            problems.append(f"{key}: malformed source/tracker column count")
            continue
        for orig_index, tracker_index, field in [
            (1, 1, "phase entry"), (2, 2, "owner role"),
            (4, 5, "acceptance evidence"),
        ]:
            if original[orig_index] != tracked[tracker_index]:
                problems.append(f"{key}: drift in {field} from original review")
        if not re.fullmatch(
            r"\[#(?P<issue>[345])\]\(https://github\.com/TheHalfMoon/SafeEvidence/issues/(?P=issue)\)",
            tracked[3],
        ):
            problems.append(f"{key}: missing durable issue #3/#4/#5")
        if tracked[4] != "OPEN — owner unassigned":
            problems.append(f"{key}: unexpected status; human approval needs separate governance review")
    charter = read(root, CHARTER, problems)
    entry = read(root, ENTRY, problems)
    rights = read(root, RIGHTS, problems)
    tracker = read(root, TRACKER, problems)
    for name, content, required in [
        (CHARTER, charter, ("DRAFT_UNAPPROVED", "NOT_SIGNED", "NOT_IDENTIFIED")),
        (ENTRY, entry, ("P01_PRE_ENTRY_GATES_PENDING", "PREPARED_NOT_ACTIVATED",
                         "UNAPPROVED", "BLOCKED")),
        (TRACKER, tracker, ("OPEN_OWNER_ASSIGNMENT", "unassigned")),
        (RIGHTS, rights, ("NO_ADMISSIONS", "VERIFIED_ALLOWED")),
    ]:
        for marker in required:
            if marker not in content:
                problems.append(f"{name}: missing fail-closed marker {marker}")
    return {
        "check": "SafeEvidence P01 pre-entry documentary consistency",
        "structure": "PASS" if not problems else "FAIL",
        "original_codex_p1": len(EXPECTED["CODEX"] & set(actual)),
        "original_opus_p1": len(EXPECTED["OPUS"] & set(actual)),
        "named_human_approvals_verified": 0,
        "clinical_evaluation_verified": False,
        "source_imports_authorized": False,
        "p01_g01_activation": "BLOCKED",
        "note": (
            "Structure-only: passing cannot approve clinical evaluation, "
            "named owners, rights, product implementation, or release."
        ),
        "errors": problems,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--expected-sha", default=None)
    parser.add_argument("--json", action="store_true")
    opts = parser.parse_args()
    report = validate(opts.root.resolve(), opts.expected_sha)
    if opts.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Structural result: {report['structure']}")
        print("P01-G01 authorization: BLOCKED, not inferred from this check")
        for issue in report["errors"]:
            print("ERROR:", issue)
    return 0 if report["structure"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
