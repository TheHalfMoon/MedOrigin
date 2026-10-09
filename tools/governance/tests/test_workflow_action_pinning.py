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
FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")


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
