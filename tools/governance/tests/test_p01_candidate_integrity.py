"""Negative and positive synthetic metadata tests; no donor code or network."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from p01_candidate_integrity import MANIFEST, SOURCE, check

REPO = Path(__file__).resolve().parents[3]


class SourceCandidateIntegrityTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in (MANIFEST, SOURCE):
            src = REPO / name
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(src.read_bytes())
        self.original = json.loads((self.root / MANIFEST).read_text(encoding="utf-8"))

    def write(self, obj):
        (self.root / MANIFEST).write_text(
            json.dumps(obj, indent=2) + "\n", encoding="utf-8",
        )

    def deny(self, obj, expected):
        self.write(obj)
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertIs(result["copy_authorized"], False)
        self.assertEqual("BLOCKED", result["source_imports"])
        self.assertTrue(
            any(expected in error for error in result["errors"]), result["errors"],
        )

    def test_ledger_intact_still_denies_copy(self):
        result = check(self.root)
        self.assertEqual("PASS", result["structure"], result)
        self.assertEqual(11, result["candidate_count"])
        self.assertEqual(6, result["raw_fingerprints_recorded"])
        self.assertIs(result["copy_authorized"], False)
        self.assertEqual("BLOCKED", result["source_imports"])

    def test_missing_candidate_is_not_silent(self):
        obj = copy.deepcopy(self.original)
        obj["entries"].pop()
        self.deny(obj, "Candidate set differs")

    def test_duplicate_candidate_is_denied(self):
        obj = copy.deepcopy(self.original)
        obj["entries"].append(copy.deepcopy(obj["entries"][0]))
        self.deny(obj, "duplicate exact source")

    def test_authorization_cannot_be_forged(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["copy_authorized"] = True
        self.deny(obj, "unauthorized elevation")

    def test_verified_allowed_cannot_be_claimed(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["admission_state"] = "VERIFIED_ALLOWED"
        self.deny(obj, "unauthorized elevation")

    def test_new_approval_field_cannot_be_injected(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["approved_by"] = "AI"
        self.deny(obj, "schema mismatch")

    def test_path_traversal_fails_closed(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["path"] = "../LICENSE"
        self.deny(obj, "unsafe source path")

    def test_changed_blob_is_detected(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["git_blob_oid"] = "a" * 40
        self.deny(obj, "Git blob differs")

    def test_changed_commit_is_detected(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["source_commit"] = "f" * 40
        self.deny(obj, "inconsistent source commit")

    def test_fake_empty_digest_is_denied(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["raw_sha256"] = (
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )
        self.deny(obj, "invalid/empty-byte SHA256")

    def test_fingerprint_requires_byte_count(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][0]["byte_count"] = None
        self.deny(obj, "fingerprint and byte size")

    def test_unverified_blob_cannot_gain_unobserved_hash(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][2]["raw_sha256"] = "a" * 64
        obj["entries"][2]["byte_count"] = 12
        self.deny(obj, "raw fingerprint not in written evidence")

    def test_unapproved_phase_is_not_silently_promoted(self):
        obj = copy.deepcopy(self.original)
        obj["phase"] = "P01_G01_ACTIVE"
        self.deny(obj, "Phase must remain pre-entry")

    def test_missing_source_evidence_is_denied(self):
        (self.root / SOURCE).unlink()
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"])
        self.assertEqual("BLOCKED", result["source_imports"])

    def test_missing_donor_ledger_marker_is_denied(self):
        p = self.root / SOURCE
        s = p.read_text(encoding="utf-8")
        p.write_text(s.replace("NO_ADMISSIONS", "ALLOW_ALL"), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"])
        self.assertTrue(any("fails closed markers" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
