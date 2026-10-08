"""Fail-closed P01 pre-entry register regression fixtures; all synthetic."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import p01_preentry_check as check


class GateFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for path in [*check.ORIGINAL_PATHS.values(), check.TRACKER,
                     check.ENTRY, check.CHARTER, check.RIGHTS]:
            (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        for reviewer, path in check.ORIGINAL_PATHS.items():
            content = "".join(
                f"| {ident} | Phase-{ident} | Reviewer-{reviewer} | Required decision | Evidence-{ident} |\n"
                for ident in sorted(check.EXPECTED[reviewer])
            )
            self.write(path, content)
        all_ids = sorted(set().union(*check.EXPECTED.values()))
        content = "Status: OPEN_OWNER_ASSIGNMENT; unassigned\n" + "".join(
            f"| {ident} | Phase-{ident} | Reviewer-{ident.split('-')[0]} | "
            f"[#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | "
            f"OPEN — owner unassigned | Evidence-{ident} |\n"
            for ident in all_ids
        )
        self.write(check.TRACKER, content)
        self.write(check.ENTRY, "P01_PRE_ENTRY_GATES_PENDING; PREPARED_NOT_ACTIVATED; UNAPPROVED; BLOCKED")
        self.write(check.CHARTER, "DRAFT_UNAPPROVED; NOT_SIGNED; NOT_IDENTIFIED")
        self.write(check.RIGHTS, "NO_ADMISSIONS, VERIFIED_ALLOWED (deny by default)")

    def write(self, path: str, text: str) -> None:
        (self.root / path).write_text(text, encoding="utf-8")

    def edit(self, path: str, old: str, new: str) -> None:
        p = self.root / path
        t = p.read_text(encoding="utf-8")
        self.assertIn(old, t)
        self.write(path, t.replace(old, new, 1))

    def assert_deny(self, explanation: str) -> None:
        out = check.validate(self.root)
        self.assertEqual(out["structure"], "FAIL")
        self.assertEqual(out["p01_g01_activation"], "BLOCKED")
        self.assertTrue(any(explanation in e for e in out["errors"]), out["errors"])

    def test_valid_register_is_still_not_authorized(self):
        out = check.validate(self.root)
        self.assertEqual(out["structure"], "PASS", out["errors"])
        self.assertEqual(out["original_codex_p1"], 24)
        self.assertEqual(out["original_opus_p1"], 17)
        self.assertEqual(out["p01_g01_activation"], "BLOCKED")
        self.assertFalse(out["clinical_evaluation_verified"])

    def test_missing_tracker_id_rejected(self):
        self.edit(check.TRACKER, "| CODEX-P00-07 |", "| LOST-P00-07 |")
        self.assert_deny("P01 tracker missing IDs")

    def test_duplicate_id_rejected(self):
        p = self.root / check.TRACKER
        lines = p.read_text(encoding="utf-8").splitlines()
        p.write_text("\n".join([*lines, lines[1], ""]), encoding="utf-8")
        self.assert_deny("Duplicate P1 ID")

    def test_evidence_drift_rejected(self):
        self.edit(check.TRACKER, "Evidence-CODEX-P00-07", "UNQUALIFIED")
        self.assert_deny("drift in acceptance evidence")

    def test_role_drift_rejected(self):
        self.edit(check.TRACKER, "Reviewer-CODEX", "Invented-Signer")
        self.assert_deny("drift in owner role")

    def test_phase_gate_drift_rejected(self):
        self.edit(check.TRACKER, "Phase-OPUS-P00-003", "Later-Phase")
        self.assert_deny("drift in phase entry")

    def test_fabricated_approval_rejected(self):
        self.edit(check.TRACKER, "OPEN — owner unassigned", "APPROVED")
        self.assert_deny("unexpected status")

    def test_loss_of_clinical_blocker_rejected(self):
        self.edit(check.CHARTER, "DRAFT_UNAPPROVED", "SIGNED")
        self.assert_deny("missing fail-closed marker")

    def test_loss_of_import_denial_rejected(self):
        self.edit(check.RIGHTS, "NO_ADMISSIONS", "FULL_ADMISSIONS")
        self.assert_deny("missing fail-closed marker")

    def test_missing_issue_link_rejected(self):
        self.edit(check.TRACKER, "issues/3", "issues/99")
        self.assert_deny("missing durable issue")

    def test_source_finding_missing_rejected(self):
        p = check.ORIGINAL_PATHS["CODEX"]
        self.edit(p, "| CODEX-P00-07 |", "| NON-P1-07 |")
        self.assert_deny("source IDs missing")


if __name__ == "__main__":
    unittest.main()
