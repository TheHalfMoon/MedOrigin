"""Keep foundation and pre-entry checkout actions pinned to immutable commits."""
from __future__ import annotations

import re
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORKFLOWS = (
    ".github/workflows/p00-foundation-docs.yml",
    ".github/workflows/p01-preentry-governance.yml",
    ".github/workflows/g01a-synthetic-reproducibility.yml",
)
EXPECTED_CHECKOUT_SHA = "d23441a48e516b6c34aea4fa41551a30e30af803"
CHECKOUT_LINE = re.compile(r"^\s*uses:\s*actions/checkout@([^\s#]+)", re.MULTILINE)
# Reject additions to the execution surface, not just a moving checkout tag.
# These three tiny workflows require exactly one external action each.
# This line-level inventory includes step uses and reusable job-level uses.
USES_LINE = re.compile(r"^[ \t]*(?:-[ \t]*)?uses[ \t]*:[ \t]*([^#\r\n]*)", re.MULTILINE)
FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")


def workflow_action_references(source: str) -> list[str]:
    """Extract all action/reusable-workflow references, including unknown ones."""
    return [reference.strip() for reference in USES_LINE.findall(source)]


def action_checkout_pins(text: str) -> list[str]:
    return CHECKOUT_LINE.findall(text)


def workflow_inventory(root: Path) -> set[str]:
    """Include every entry, not just known *.yml files or action uses.

    A fourth workflow would otherwise bypass checks confined to WORKFLOWS;
    an unexpected directory, symlink or alternate *.yaml is also unreviewed.
    """
    directory = root / ".github/workflows"
    if (root / ".github").is_symlink() or directory.is_symlink() or not directory.is_dir():
        return set()
    entries = list(directory.iterdir())
    if any(path.is_symlink() for path in entries):
        return set()
    return {path.relative_to(root).as_posix() for path in entries}


class WorkflowCheckoutPinTests(unittest.TestCase):
    def test_all_three_workflows_use_identical_immutable_checkout(self):
        for workflow in WORKFLOWS:
            with self.subTest(workflow=workflow):
                source = (ROOT / workflow).read_text(encoding="utf-8")
                self.assertEqual(
                    [EXPECTED_CHECKOUT_SHA],
                    action_checkout_pins(source),
                    "Checkout must be a reviewed immutable action revision",
                )

    def test_entire_workflow_directory_is_the_reviewed_allowlist(self):
        self.assertEqual(set(WORKFLOWS), workflow_inventory(ROOT))
        workflow_directory = ROOT / ".github/workflows"
        self.assertFalse(workflow_directory.is_symlink())
        for name in WORKFLOWS:
            with self.subTest(path=name):
                self.assertTrue((ROOT / name).is_file())
                self.assertFalse((ROOT / name).is_symlink())

    def test_new_yaml_workflow_or_unreviewed_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / ".github/workflows"
            folder.mkdir(parents=True)
            for name in WORKFLOWS:
                shutil.copyfile(ROOT / name, root / name)
            self.assertEqual(set(WORKFLOWS), workflow_inventory(root))
            for extra in ("unreviewed.yml", "unreviewed.yaml", "unreviewed"):
                with self.subTest(unreviewed=extra):
                    path = folder / extra
                    if extra == "unreviewed":
                        path.mkdir()
                    else:
                        path.write_text(
                            "name: Unreviewed\non: [pull_request]\n"
                            "jobs:\n  external:\n    runs-on: ubuntu-latest\n"
                            "    steps:\n      - uses: attacker/unreviewed@v1\n",
                            encoding="utf-8",
                        )
                    try:
                        self.assertNotEqual(
                            set(WORKFLOWS), workflow_inventory(root),
                            "New workflow/executable surface must fail PR CI",
                        )
                    finally:
                        if path.is_dir():
                            path.rmdir()
                        else:
                            path.unlink()

    def test_unreviewed_symlinked_workflow_not_silently_allowed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / ".github/workflows"
            folder.mkdir(parents=True)
            for name in WORKFLOWS:
                shutil.copyfile(ROOT / name, root / name)
            target = root / "external.yml"
            target.write_text("name: external\n", encoding="utf-8")
            injected = folder / "extra.yml"
            try:
                injected.symlink_to(target)
            except OSError as exc:
                self.skipTest(f"Symlinks unavailable on host: {exc}")
            self.assertNotEqual(set(WORKFLOWS), workflow_inventory(root))
            self.assertTrue(injected.is_symlink())

    def test_existing_workflow_symlink_is_not_trusted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / ".github/workflows"
            folder.mkdir(parents=True)
            for name in WORKFLOWS:
                shutil.copyfile(ROOT / name, root / name)
            source = root / WORKFLOWS[0]
            outside = root / "external-copy.yml"
            shutil.copyfile(source, outside)
            source.unlink()
            try:
                source.symlink_to(outside)
            except OSError as exc:
                self.skipTest(f"Symlinks unavailable on host: {exc}")
            self.assertNotEqual(set(WORKFLOWS), workflow_inventory(root))

    def test_parent_directory_symlink_is_not_trusted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / ".github/workflows"
            folder.mkdir(parents=True)
            for name in WORKFLOWS:
                shutil.copyfile(ROOT / name, root / name)
            outside = root / "external-workflows"
            folder.rename(outside)
            try:
                folder.symlink_to(outside, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Symlinks unavailable on host: {exc}")
            self.assertNotEqual(set(WORKFLOWS), workflow_inventory(root))

    def test_no_unreviewed_actions_in_any_governance_workflow(self):
        only_approved = [f"actions/checkout@{EXPECTED_CHECKOUT_SHA}"]
        for workflow in WORKFLOWS:
            with self.subTest(workflow=workflow):
                source = (ROOT / workflow).read_text(encoding="utf-8")
                self.assertEqual(
                    only_approved,
                    workflow_action_references(source),
                    "All action/reusable workflow uses must be explicitly reviewed",
                )

    def test_extra_unpinned_action_does_not_hide_behind_pinned_checkout(self):
        source = ("steps:\n"
                  "  - uses: attacker/unreviewed-egress@v1\n"
                  f"    uses: actions/checkout@{EXPECTED_CHECKOUT_SHA}\n")
        self.assertEqual([EXPECTED_CHECKOUT_SHA], action_checkout_pins(source))
        self.assertNotEqual(
            [f"actions/checkout@{EXPECTED_CHECKOUT_SHA}"],
            workflow_action_references(source),
        )

    def test_extra_sha_pinned_action_still_needs_explicit_review(self):
        source = ("steps:\n"
                  f"  - uses: actions/checkout@{EXPECTED_CHECKOUT_SHA}\n"
                  "  - uses: attacker/unreviewed@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
        self.assertEqual(2, len(workflow_action_references(source)))
        self.assertNotEqual(
            [f"actions/checkout@{EXPECTED_CHECKOUT_SHA}"],
            workflow_action_references(source),
        )

    def test_unreviewed_job_level_reusable_workflow_rejected(self):
        source = ("jobs:\n"
                  "  run-external:\n"
                  "    uses: attacker/repo/.github/workflows/unsafe.yml@v1\n"
                  f"  - uses: actions/checkout@{EXPECTED_CHECKOUT_SHA}\n")
        self.assertNotEqual(
            [f"actions/checkout@{EXPECTED_CHECKOUT_SHA}"],
            workflow_action_references(source),
        )

    def test_missing_uses_value_is_not_valid_action(self):
        source = f"steps:\n  - uses:\n  - uses: actions/checkout@{EXPECTED_CHECKOUT_SHA}\n"
        self.assertEqual(2, len(workflow_action_references(source)))
        self.assertEqual("", workflow_action_references(source)[0])

    def test_synthetic_and_preentry_ci_include_macos(self):
        for workflow in WORKFLOWS[1:]:
            with self.subTest(workflow=workflow):
                source = (ROOT / workflow).read_text(encoding="utf-8")
                self.assertIn(
                    "os: [ubuntu-latest, windows-latest, macos-15]",
                    source,
                )
                self.assertIn("matrix.os", source)

    def test_g01a_macos_ci_preserves_exact_head_and_source_guard(self):
        source = (ROOT / WORKFLOWS[2]).read_text(encoding="utf-8")
        self.assertIn('test "$(git rev-parse HEAD)" = "$EXPECTED_SHA"', source)
        self.assertLess(
            source.index("- name: Gate frozen source and cargo configuration"),
            source.index("- name: Install explicitly pinned development toolchain"),
        )
        self.assertIn("cargo test --offline --locked --workspace --all-targets", source)

    def test_moving_action_tag_is_rejected(self):
        self.assertNotEqual(
            [EXPECTED_CHECKOUT_SHA],
            action_checkout_pins("steps:\n  - uses: actions/checkout@v4\n"),
        )

    def test_short_sha_is_rejected(self):
        self.assertIsNone(FULL_SHA.fullmatch("d23441a"))

    def test_pinned_sha_is_full_length(self):
        self.assertIsNotNone(FULL_SHA.fullmatch(EXPECTED_CHECKOUT_SHA))


if __name__ == "__main__":
    unittest.main()
