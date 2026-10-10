"""Synthetic tests: no donor bytes, model calls, network or source admission."""
import hashlib
import json
import os
from types import SimpleNamespace
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from p01_candidate_byte_verify import verify
import p01_candidate_integrity as candidate_guard
from p01_candidate_integrity import MANIFEST, SOURCE, check

ORIGIN = Path(__file__).resolve().parents[3]
REPO = "TheHalfMoon/MedScale"
TARGET = "crates/medscale-core/src/release_sbom.rs"


class ExternalByteCheckTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.workspace = Path(tmp.name)
        self.root = self.workspace / "repo"
        self.root.mkdir()
        self.blob = self.workspace / "synthetic.bin"
        payload = b"SYNTHETIC FIXTURE, NO DONOR BYTES\n"
        self.blob.write_bytes(payload)
        for f in (MANIFEST, SOURCE):
            dest = self.root / f
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((ORIGIN / f).read_bytes())
        manifest_file = self.root / MANIFEST
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        row = manifest["entries"][0]
        old_oid, old_sha, old_size = row["git_blob_oid"], row["raw_sha256"], row["byte_count"]
        row["byte_count"] = len(payload)
        row["raw_sha256"] = hashlib.sha256(payload).hexdigest()
        row["git_blob_oid"] = hashlib.sha1(
            b"blob " + str(len(payload)).encode() + b"\0" + payload,
            usedforsecurity=False
        ).hexdigest()
        manifest_file.write_text(json.dumps(manifest), encoding="utf-8")
        # This test fixture deliberately uses invented synthetic byte identities.
        # Scoped mock keeps production's independently pinned 11 candidates intact.
        synthetic_pin = patch.object(
            candidate_guard,
            "FROZEN_CANDIDATE_IDENTITY_SHA256",
            candidate_guard.candidate_identity_digest(manifest["entries"]),
        )
        synthetic_pin.start()
        self.addCleanup(synthetic_pin.stop)
        source_file = self.root / SOURCE
        written = source_file.read_text(encoding="utf-8").replace(old_oid, row["git_blob_oid"])
        tick = chr(96)
        old = f"| MedScale {tick}release_sbom.rs{tick} | {old_size} | {tick}{old_sha}{tick} |"
        new = f"| MedScale {tick}release_sbom.rs{tick} | {len(payload)} | {tick}{row['raw_sha256']}{tick} |"
        self.assertIn(old, written)
        source_file.write_text(written.replace(old, new), encoding="utf-8")
        self.assertEqual("PASS", check(self.root)["structure"])

    def result(self, path=TARGET, blob=None):
        return verify(self.root, REPO, path, blob if blob is not None else self.blob)

    def assert_status(self, result, status):
        self.assertEqual(status, result["byte_integrity"], result)
        self.assertIs(result["copy_authorized"], False)
        self.assertEqual(result["source_imports"], "BLOCKED")

    def test_match_still_refuses_copy(self):
        self.assert_status(self.result(), "MATCH")

    def test_same_size_tamper(self):
        self.blob.write_bytes(b"X" + self.blob.read_bytes()[1:])
        self.assert_status(self.result(), "MISMATCH")

    def test_stable_file_does_not_require_identical_path_and_handle_metadata(self):
        """Path stat and handle fstat may differ on Windows without file mutation."""
        real_fstat = os.fstat

        def alternate_fstat(fd):
            record = real_fstat(fd)
            return SimpleNamespace(
                st_mode=record.st_mode,
                st_dev=record.st_dev,
                st_ino=record.st_ino,
                st_size=record.st_size,
                st_mtime_ns=record.st_mtime_ns,
                st_ctime_ns=record.st_ctime_ns + 123_456,
            )

        with patch("p01_candidate_byte_verify.os.fstat", side_effect=alternate_fstat):
            self.assert_status(self.result(), "MATCH")

    def test_same_size_mutation_during_read_is_not_a_match(self):
        """A file altered after its original bytes are read cannot claim MATCH."""
        original = self.blob.read_bytes()
        changed = b"!" + original[1:]
        real_open = Path.open
        target = self.blob.resolve()

        class MutatingStream:
            def __init__(self, stream):
                self.stream = stream
                self.mutated = False

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return self.stream.__exit__(*args)

            def fileno(self):
                return self.stream.fileno()

            def read(self, *args, **kwargs):
                chunk = self.stream.read(*args, **kwargs)
                if chunk and not self.mutated:
                    self.mutated = True
                    target.write_bytes(changed)
                return chunk

        def mutating_open(path, mode="r", *args, **kwargs):
            handle = real_open(path, mode, *args, **kwargs)
            if path == target and mode == "rb":
                return MutatingStream(handle)
            return handle

        with patch.object(Path, "open", mutating_open):
            self.assert_status(self.result(), "MISMATCH")
        self.assertEqual(self.blob.read_bytes(), changed)

    def test_wrong_size(self):
        self.blob.write_bytes(b"short")
        self.assert_status(self.result(), "MISMATCH")

    def test_other_fingerprinted_candidate_mismatches_synthetic_bytes(self):
        self.assert_status(self.result("scripts/generate-release-sbom.ps1"), "MISMATCH")

    def test_unknown_candidate_remains_blocked(self):
        self.assert_status(self.result("scripts/unknown-source.ps1"), "BLOCKED")

    def test_nonexistent_blob(self):
        self.assert_status(self.result(blob=self.workspace / "missing"), "BLOCKED")

    def test_inside_checkout(self):
        inside = self.root / "unadmitted.bin"
        inside.write_bytes(self.blob.read_bytes())
        self.assert_status(self.result(blob=inside), "BLOCKED")

    def test_unknown_candidate(self):
        self.assert_status(self.result(path="../unknown"), "BLOCKED")

    def test_authority_tampering(self):
        f = self.root / MANIFEST
        manifest = json.loads(f.read_text(encoding="utf-8"))
        manifest["entries"][0]["copy_authorized"] = True
        f.write_text(json.dumps(manifest), encoding="utf-8")
        self.assert_status(self.result(), "BLOCKED")


if __name__ == "__main__":
    unittest.main()
