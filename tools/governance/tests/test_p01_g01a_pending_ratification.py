"""Fail-closed documentary checks for the proposed G01a policy split.

Passing these checks does not authorize G01a implementation or release.
"""
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REQUIRED = (
    "AGENTS.md",
    "docs/P01_ENTRY_READINESS_2026-10-08.md",
    "docs/reviews/P01_G01_PREPARED_2026-10-08.md",
    "docs/MASTER_PLAN.md",
)
PENDING = "G01A_NOT_ACTIVATED"
NO_ADMISSIONS = "NO_ADMISSIONS"


def verify_doc(content: str) -> bool:
    return (
        PENDING in content
        and NO_ADMISSIONS in content
        and "SafeEvidence/issues/17" in content
        and "Issue #4" in content
        and "Issue #5" in content
        and "G01A_ACTIVE" not in content
        and "G01A_APPROVED" not in content
    )


class G01aRatificationBoundaryTests(unittest.TestCase):
    def test_all_authoritative_docs_preserve_pending_state(self):
        for relative in REQUIRED:
            with self.subTest(document=relative):
                self.assertTrue(
                    verify_doc((ROOT / relative).read_text(encoding="utf-8")),
                    f"{relative} must retain G01a pending state, issue 17, and gate #4/#5 links",
                )

    def test_removing_pending_marker_denies(self):
        sample = "G01A_NOT_ACTIVATED NO_ADMISSIONS SafeEvidence/issues/17 Issue #4 Issue #5"
        self.assertTrue(verify_doc(sample))
        self.assertFalse(verify_doc(sample.replace(PENDING, "G01A_ACTIVE")))

    def test_missing_clinical_or_rights_gate_denies(self):
        sample = "G01A_NOT_ACTIVATED NO_ADMISSIONS SafeEvidence/issues/17 Issue #4 Issue #5"
        self.assertFalse(verify_doc(sample.replace("Issue #4", "")))
        self.assertFalse(verify_doc(sample.replace("Issue #5", "")))

    def test_unapproved_source_admission_denies(self):
        sample = "G01A_NOT_ACTIVATED NO_ADMISSIONS SafeEvidence/issues/17 Issue #4 Issue #5"
        self.assertFalse(verify_doc(sample.replace(NO_ADMISSIONS, "COPY_ALLOWED")))


if __name__ == "__main__":
    unittest.main()
