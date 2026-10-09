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
        self.assertEqual(11, result["raw_fingerprints_recorded"])
        self.assertIs(result["copy_authorized"], False)
        self.assertEqual("BLOCKED", result["source_imports"])

    def test_conflicting_duplicate_copy_authorization_denied(self):
        path = self.root / MANIFEST
        original = path.read_text(encoding="utf-8")
        marker = '"copy_authorized": false'
        self.assertEqual(original.count(marker), 11)
        path.write_text(
            original.replace(
                marker, '"copy_authorized": true, "copy_authorized": false', 1
            ), encoding="utf-8",
        )
        self.assertEqual(check(self.root)["structure"], "FAIL")
        self.assertIs(check(self.root)["copy_authorized"], False)

    def test_conflicting_duplicate_admissions_denied(self):
        path = self.root / MANIFEST
        original = path.read_text(encoding="utf-8")
        marker = '"admissions": []'
        self.assertEqual(original.count(marker), 1)
        path.write_text(
            original.replace(marker, '"admissions": ["bad"], "admissions": []'),
            encoding="utf-8",
        )
        report = check(self.root)
        self.assertEqual(report["structure"], "FAIL")
        self.assertEqual(report["source_imports"], "BLOCKED")

    def test_identical_duplicate_fingerprint_denied(self):
        path = self.root / MANIFEST
        original = path.read_text(encoding="utf-8")
        marker = '"byte_count": 17423'
        self.assertEqual(original.count(marker), 1)
        path.write_text(
            original.replace(marker, '"byte_count": 17423, "byte_count": 17423'),
            encoding="utf-8",
        )
        self.assertEqual(check(self.root)["structure"], "FAIL")

    def test_fenced_fingerprint_evidence_is_not_authority(self):
        p = self.root / SOURCE
        original = p.read_text(encoding="utf-8")
        marker = "## Byte-level SHA-256 observations"
        start = original.index(marker)
        end = original.find("\n## ", start + 3)
        self.assertGreater(end, start)
        for opener, closer in ((chr(96) * 3 + "markdown", chr(96) * 3),
                               ("~~~~markdown", "~~~~")):
            with self.subTest(opener=opener):
                p.write_text(original[:start] + opener + "\n"
                             + original[start:end] + "\n" + closer + "\n"
                             + original[end:], encoding="utf-8")
                report = check(self.root)
                self.assertEqual(report["structure"], "FAIL", report)
                self.assertEqual(report["source_imports"], "BLOCKED")

    def test_commented_blob_table_is_not_authority(self):
        p = self.root / SOURCE
        original = p.read_text(encoding="utf-8")
        start = original.index("## Candidate exact file identities (Git blob OIDs)")
        end = original.find("\n## ", start + 3)
        self.assertGreater(end, start)
        p.write_text(original[:start] + "<!--\n" + original[start:end]
                     + "\n-->\n" + original[end:], encoding="utf-8")
        report = check(self.root)
        self.assertEqual(report["structure"], "FAIL", report)
        self.assertEqual(report["source_imports"], "BLOCKED")

    def test_fenced_blob_table_is_not_authority(self):
        p = self.root / SOURCE
        original = p.read_text(encoding="utf-8")
        start = original.index("## Candidate exact file identities (Git blob OIDs)")
        end = original.find("\n## ", start + 3)
        p.write_text(original[:start] + "~~~~\n" + original[start:end]
                     + "\n~~~~\n" + original[end:], encoding="utf-8")
        self.assertEqual(check(self.root)["structure"], "FAIL")

    def test_hidden_duplicate_examples_do_not_override_visible_ledger(self):
        p = self.root / SOURCE
        original = p.read_text(encoding="utf-8")
        fake = ("## Candidate exact file identities (Git blob OIDs)\n"
                "| Source | Path | Blob OID |\n|---|---|---|\n")
        p.write_text(
            "<!--\n" + fake + "-->\n" + chr(96) * 3
            + "md\n" + fake + chr(96) * 3 + "\n" + original,
            encoding="utf-8",
        )
        report = check(self.root)
        self.assertEqual(report["structure"], "PASS", report)
        self.assertFalse(report["copy_authorized"])

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

    def test_displaced_blob_row_is_not_replaced_by_unbound_prose(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        line = "| MedScale | `crates/medscale-core/src/release_sbom.rs` | `" + (
            self.original["entries"][0]["git_blob_oid"]
        ) + "` |"
        self.assertEqual(body.count(line), 1)
        body = body.replace(line + "\n", "", 1)
        p.write_text(body + "\nUnbound source note: " + line + "\n", encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertTrue(any("Git blob differs" in e for e in result["errors"]), result["errors"])

    def test_duplicate_blob_row_is_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        line = "| MedScale | `crates/medscale-core/src/release_sbom.rs` | `" + (
            self.original["entries"][0]["git_blob_oid"]
        ) + "` |"
        self.assertEqual(body.count(line), 1)
        p.write_text(body.replace(line, line + "\n" + line, 1), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertIs(result["copy_authorized"], False)

    def test_swapped_blob_rows_are_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        first, second = self.original["entries"][:2]
        needle1 = "| MedScale | `" + first["path"] + "` | `" + first["git_blob_oid"] + "` |"
        needle2 = "| MedScale | `" + second["path"] + "` | `" + second["git_blob_oid"] + "` |"
        self.assertIn(needle1, body)
        self.assertIn(needle2, body)
        changed = body.replace(needle1, "__FIRST_BLOB__", 1)
        changed = changed.replace(needle2, needle2.replace(second["git_blob_oid"], first["git_blob_oid"]), 1)
        changed = changed.replace("__FIRST_BLOB__", needle1.replace(first["git_blob_oid"], second["git_blob_oid"]), 1)
        p.write_text(changed, encoding="utf-8")
        self.assertEqual("FAIL", check(self.root)["structure"])

    def test_unexpected_blob_table_source_is_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        existing = "| MedScale | `crates/medscale-core/src/release_sbom.rs` |"
        injected = "| Unknown | `example.py` | `" + "a" * 40 + "` |"
        self.assertIn(existing, body)
        p.write_text(body.replace(existing, injected + "\n" + existing, 1), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"])
        self.assertTrue(any("Blob table" in e for e in result["errors"]), result["errors"])

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

    def test_altered_recorded_hash_cannot_gain_unobserved_value(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][2]["raw_sha256"] = "a" * 64
        obj["entries"][2]["byte_count"] = 12
        self.deny(obj, "raw fingerprint not in written evidence")

    def test_displaced_fingerprint_is_not_accepted_from_unbound_prose(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        line = next(row for row in body.splitlines()
                    if row.startswith("| MedScale `release_sbom.rs` |"))
        body = body.replace(line + "\n", "", 1)
        body += "\nUnbound note: " + self.original["entries"][0]["raw_sha256"] + " | 17423 |\n"
        p.write_text(body, encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertTrue(any("fingerprint" in e for e in result["errors"]), result["errors"])

    def test_duplicate_fingerprint_evidence_row_is_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        line = next(row for row in body.splitlines()
                    if row.startswith("| MedScale `release_sbom.rs` |"))
        p.write_text(body.replace(line, line + "\n" + line, 1), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertEqual("BLOCKED", result["source_imports"])

    def test_fingerprint_on_wrong_source_row_is_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        row1 = next(row for row in body.splitlines()
                    if row.startswith("| MedScale `release_sbom.rs` |"))
        row2 = next(row for row in body.splitlines()
                    if row.startswith("| MedScale `release_sbom_054.rs` test |"))
        parts1 = row1.split("|")
        parts2 = row2.split("|")
        parts1[3], parts2[3] = parts2[3], parts1[3]
        altered = body.replace(row1, "__ROW1__", 1).replace(row2, "|".join(parts2), 1)
        p.write_text(altered.replace("__ROW1__", "|".join(parts1), 1), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertTrue(any("exact source row" in e for e in result["errors"]), result["errors"])

    def test_unexpected_fingerprint_source_row_is_rejected(self):
        p = self.root / SOURCE
        body = p.read_text(encoding="utf-8")
        row = next(line for line in body.splitlines()
                   if line.startswith("| MedScale `release_sbom.rs` |"))
        injected = "| UnknownDonor `unexpected.py` | 100 | `" + "f" * 64 + "` |"
        p.write_text(body.replace(row, row + "\n" + injected, 1), encoding="utf-8")
        result = check(self.root)
        self.assertEqual("FAIL", result["structure"], result)
        self.assertEqual("BLOCKED", result["source_imports"])

    def test_missing_recorded_digest_is_denied(self):
        obj = copy.deepcopy(self.original)
        obj["entries"][2]["raw_sha256"] = None
        obj["entries"][2]["byte_count"] = None
        self.deny(obj, "Exactly eleven verified fingerprints expected")

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
