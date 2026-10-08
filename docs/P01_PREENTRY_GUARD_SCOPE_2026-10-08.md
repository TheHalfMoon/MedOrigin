# P01 Pre-entry Guard: scope and verification

Status: **ENGINEERING PREPARATION ONLY**; P01-G01 is **NOT ACTIVATED**.

This reviewable gate checks the 41 original P1 IDs, immutable evidence/role/
phase mappings, durable issue references and explicit unresolved clinical/
rights/ownership markers in the current source. It runs on Windows and Linux,
with no external Python packages, no model, no patient data and no network calls
from the checker. Its 11 synthetic tests include ID loss/duplication, evidence
drift, phase and role drift, fabricated approval and lost denial markers.

It is intentionally **impossible** for this gate to declare P01 activated.
An exit code 0 means only that documentary pre-entry guardrails are intact.
The JSON report always distinguishes `structure=PASS` from
`p01_g01_activation=BLOCKED`.

The first implementation remains forbidden until the qualified authorizations
in Issues #3, #4 and #5 are completed. This validation does not verify
legal rights, clinical gold labels, signers, software security, donor code,
scientific correctness, patient safety, or release readiness.

## Source reuse research

No copy from a donor codebase was required: this narrow fail-closed Markdown
register consistency check uses the Python standard library. CI conventions
follow the GitHub Actions pattern already in SafeEvidence and the exact-head
cross-platform workflow inspected in TheHalfMoon/MedScale. No third-party
source bytes, model/data artifacts or re-licensed dependency code are imported.

## Developer commands

```text
python tools/governance/p01_preentry_check.py --root . --json
python -m unittest discover -s tools/governance/tests -v
```

For CI, the validator receives the exact checked-out event SHA to prevent
mistaking a stale checkout for the reviewed head.
