"""Keep foundation and pre-entry checkout actions pinned to immutable commits."""
from __future__ import annotations

import re
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
