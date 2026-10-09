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
    "crates/g01a-synthetic/src/lib.rs",
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
        self.assertEqual(report["frozen_source_sha256"], guard.SOURCE_SHA256)
        self.assertIs(report["copy_authorized"], False)

    def test_fixture_byte_tamper_denied(self):
        fixture = self.root / guard.FIXTURE
        fixture.write_bytes(fixture.read_bytes() + b"MUTATED\n")
        self.denied()

    def test_rust_source_change_denied(self):
        source = self.root / guard.SOURCE
        source.write_bytes(source.read_bytes() + b"// unreviewed change\n")
        self.denied()

    def test_missing_rust_source_denied(self):
        (self.root / guard.SOURCE).unlink()
        self.denied()

    def test_source_digest_elevation_denied(self):
        self.edit_manifest(source_sha256="0" * 64)
        self.denied()

    def test_additional_cargo_configuration_denied(self):
        for relative in (".cargo/config.toml", "crates/.cargo/config.toml"):
            with self.subTest(path=relative):
                config = self.root / relative
                config.parent.mkdir(parents=True, exist_ok=True)
                config.write_text('[build]\nrustflags = ["-Dwarnings"]\n', encoding="utf-8")
                self.denied()
                config.unlink()
                config.parent.rmdir()

    def test_gate_runs_before_cargo_in_ci(self):
        workflow = (ROOT / ".github/workflows/g01a-synthetic-reproducibility.yml").read_text(
            encoding="utf-8"
        )
        gate = workflow.index("- name: Gate frozen source and cargo configuration")
        setup = workflow.index("- name: Install explicitly pinned development toolchain")
        self.assertLess(gate, setup)
        self.assertIn(guard.SOURCE_SHA256, workflow)

    def test_fake_copy_permission_denied(self):
        self.edit_manifest(copy_authorized=True)
        self.denied()

    def test_fake_clinical_validation_denied(self):
        self.edit_manifest(clinical_validation="VERIFIED")
        self.denied()

    def test_path_traversal_denied(self):
        self.edit_manifest(fixture_path="../elsewhere.txt")
        self.denied()

    def test_unreviewed_build_script_denied(self):
        script = self.root / "crates/g01a-synthetic/build.rs"
        script.write_text("fn main() {}\n", encoding="utf-8")
        self.denied()

    def test_unreviewed_binary_target_denied(self):
        binary = self.root / "crates/g01a-synthetic/src/main.rs"
        binary.write_text("fn main() {}\n", encoding="utf-8")
        self.denied()

    def test_new_dependency_denied(self):
        manifest = self.root / "crates/g01a-synthetic/Cargo.toml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8") + '\nserde = "1"\n',
            encoding="utf-8",
        )
        self.denied()

    def test_custom_build_path_denied(self):
        manifest = self.root / "crates/g01a-synthetic/Cargo.toml"
        content = manifest.read_text(encoding="utf-8")
        manifest.write_text(
            content.replace("publish = false", 'publish = false\nbuild = "custom.rs"'),
            encoding="utf-8",
        )
        self.denied()

    def test_unreviewed_manifest_target_denied(self):
        manifest = self.root / "crates/g01a-synthetic/Cargo.toml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8")
            + '\n[[example]]\nname = "extra"\npath = "src/lib.rs"\n',
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

    def test_unlisted_source_module_denied(self):
        module = self.root / "crates/g01a-synthetic/src/extra.rs"
        module.write_text("pub fn extra() {}\n", encoding="utf-8")
        self.denied()

    def test_unreviewed_workspace_section_denied(self):
        manifest = self.root / "Cargo.toml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8") + "\n[patch.crates-io]\n",
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
