"""Synthetic-only G01a governance fixtures. No patient or third-party data."""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import g01a_synthetic_check as guard


ROOT = Path(__file__).resolve().parents[3]
INPUTS = (
    guard.MANIFEST, guard.FIXTURE, "Cargo.lock", "Cargo.toml",
    "rust-toolchain.toml", ".gitattributes", "crates/g01a-synthetic/Cargo.toml",
)


class SyntheticOnlyChecks(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for relative in INPUTS:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def denied(self):
        report = guard.check(self.root)
        self.assertEqual(report["structure"], "FAIL", report)
        self.assertIs(report["copy_authorized"], False)
        self.assertEqual(report["source_imports"], "BLOCKED")
        self.assertEqual(report["clinical_validation"], "NOT_PERFORMED")

    def edit_manifest(self, **changes):
        path = self.root / guard.MANIFEST
        document = json.loads(path.read_text(encoding="utf-8"))
        document.update(changes)
        path.write_text(json.dumps(document), encoding="utf-8")

    def test_valid_fixture_is_still_nonclinical(self):
        report = guard.check(self.root)
        self.assertEqual(report["structure"], "PASS", report)
        self.assertEqual(report["classification"], "SYNTHETIC_ONLY")
        self.assertIs(report["copy_authorized"], False)

    def test_fixture_byte_tamper_denied(self):
        fixture = self.root / guard.FIXTURE
        fixture.write_bytes(fixture.read_bytes() + b"MUTATED\n")
        self.denied()

    def test_fake_copy_permission_denied(self):
        self.edit_manifest(copy_authorized=True)
        self.denied()

    def test_fake_clinical_validation_denied(self):
        self.edit_manifest(clinical_validation="VERIFIED")
        self.denied()

    def test_path_traversal_denied(self):
        self.edit_manifest(fixture_path="../elsewhere.txt")
        self.denied()

    def test_new_dependency_denied(self):
        manifest = self.root / "crates/g01a-synthetic/Cargo.toml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8") + '\nserde = "1"\n',
            encoding="utf-8",
        )
        self.denied()

    def test_extra_lockfile_package_denied(self):
        lock = self.root / "Cargo.lock"
        lock.write_text(
            lock.read_text(encoding="utf-8")
            + '\n[[package]]\nname = "unreviewed"\nversion = "1.0.0"\n',
            encoding="utf-8",
        )
        self.denied()

    def test_checkout_line_ending_policy_denied(self):
        (self.root / ".gitattributes").write_text(
            "fixtures/g01a_synthetic_v1.txt text eol=crlf\n",
            encoding="utf-8",
        )
        self.denied()

    def test_wrong_toolchain_denied(self):
        config = self.root / "rust-toolchain.toml"
        config.write_text(
            config.read_text(encoding="utf-8").replace("1.97.1", "stable"),
            encoding="utf-8",
        )
        self.denied()

    def test_unknown_manifest_field_denied(self):
        self.edit_manifest(ready_for_release=True)
        self.denied()


if __name__ == "__main__":
    unittest.main()
