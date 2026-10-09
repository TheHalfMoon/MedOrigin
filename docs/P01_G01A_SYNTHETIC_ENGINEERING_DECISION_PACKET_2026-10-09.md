# SafeEvidence P01-G01a — Synthetic-Only Engineering Sequencing Decision Packet

Date: 2026-10-09 (Asia/Riyadh)
Status: **FOUNDER_OPTION_B_RATIFIED / G01A_SYNTHETIC_QUALIFIED / INDEPENDENT_REVIEW_PENDING / NO_ADMISSIONS**
Owning founder decision: https://github.com/TheHalfMoon/SafeEvidence/issues/17
Original gate tracking: https://github.com/TheHalfMoon/SafeEvidence/issues/3
Clinical evaluation: https://github.com/TheHalfMoon/SafeEvidence/issues/4
Rights and trust: https://github.com/TheHalfMoon/SafeEvidence/issues/5

## Ratified authority and bounded result

The founder selected Option B and accepted G01a engineering ownership in Issue #17.
Signed governance PR #19 merged at 5f1623c9cdd11cf43989efe37f638cba230e7ff2.
Synthetic implementation PR #20 merged at 91bd597e377a8b902499a6e0b66e567e89ba7bd5.
Signed hardening PR #21 merged at d6645e169d643b6b6eae7ad06e17a605edcb0687.
Exact-main P00, P01 and G01a Windows/Ubuntu CI passed.

FOUNDER_OPTION_B_RATIFIED / G01A_SYNTHETIC_QUALIFIED / INDEPENDENT_REVIEW_PENDING / NO_ADMISSIONS.
Only the standard-library Rust synthetic reproducibility baseline is qualified.
Independent review is not verified; no clinical, legal, source-admission or release approval exists.
Full P01_PRE_ENTRY_GATES_PENDING and P01-G01 PREPARED_NOT_ACTIVATED continue.
Original 41 P1 findings, accountable ownership (Issue #3), qualified clinical evaluation
(Issue #4) and source rights/pack trust (Issue #5) remain BLOCKED for dependent work.

## Narrow decision

Option A — retain unified G01: require the currently adopted prerequisite
approvals before starting any product-code work. This is the effective default.

Option B — authorize a separate, limited G01a with **only** synthetic local
engineering reproducibility. Permit development of a small Rust workspace
after founder and engineering-owner ratification of an exact scope/commit.
Keep G01b for all clinical/use-case, evidence-rights, source-code donor,
pack-trust, and scientific work. G01a completion cannot close P01 or P02.

## G01a strict scope if ratified

| May implement or test | Explicitly forbidden |
|---|---|
| Pinned stdlib-only Rust toolchain and workspace | Unadmitted dependency or donor source import |
| Deterministic synthetic fixture with non-sensitive marker | Patient records, PHI, clinical source/article text |
| Offline-locked cargo build, test, clippy and format | Medical decision logic, diagnostic or answer UI |
| Cross-platform exact-head CI, build receipts, no hidden service | Runtime network/model download or paid SaaS fallback |
| Namespaced synthetic local diagnostics, no private paths | Signed evidence packs, verification/admission to production |
| Owner-reviewed replayable proof, negative tests and rollback | Publishing clinical claims, deployment or P01 closure |

No G01a code enters canonical main unless signed authority exists and that
code's own exact-revision tests and review pass. The source-admission ledger
remains `NO_ADMISSIONS`; the source candidate list is never a copy allowlist.

## Technical acceptance for separately authorized G01a

1. Freeze a minimal Rust version (proposed host-proven 1.97.1), workspace
   manifest and Cargo.lock; avoid any third-party crates at bootstrap.
2. Demonstrate a fresh checkout with `cargo test --offline --locked
   --all-targets`, `cargo fmt --all -- --check`, and `cargo clippy --offline
   --locked --all-targets -- -D warnings` on Windows and Ubuntu.
3. Use synthetic fixtures only, with stable SHA-256 identities and explicit
   `SYNTHETIC_ONLY` labels. No medical or restricted data in CI artifacts.
4. Bind exact PR head SHA before normal merge; rerun workflow jobs on final
   main merge commit. Preserve exact-head requirement, no force/rebase/squash.
5. Record build host/toolchain identities, immutable input/file digests and
   real failure/no-network evidence without claiming clinical validation.
6. Require any new module to cite an admitted reuse candidate or
   GREENFIELD_JUSTIFIED with explicit rationale; trivial compiler plumbing
   need not import a donor. No clinical model, dataset or parser promotion.
7. Keep original 24 Codex and 17 Opus P1 tasks open until their own accepted
   evidence and qualified human decisions are recorded.

## Local scratch feasibility — NOT project implementation

On the authorized Windows host and Ubuntu WSL, a short-lived synthetic Rust
library probe was initialized outside the SafeEvidence repository and tested
without dependencies or source imports. Rust and Cargo each reported 1.97.1.

| Check | Windows | Ubuntu WSL |
|---|---|---|
| `cargo fmt --all -- --check` | PASS | PASS |
| `cargo test --offline --locked --all-targets` | PASS (1 synthetic test) | PASS (1 synthetic test) |
| `cargo clippy --offline --locked --all-targets -- -D warnings` | PASS | PASS |

`src/lib.rs` SHA-256 on both operating systems:
`52c4e77054e6622a1658dafbfc872246dda3b9f69867a28d7d42a6e5c3250255`.
`Cargo.lock` SHA-256 from Ubuntu:
`70b67ce62b24c125d2d737bf97c1b64482d05549783ad7301af199aac4c9136b`.

This test shows local compiler/tooling viability only; it does **not** prove
a production build, cold/offline dependency acquisition, a zero-egress
instrumented check, clinical correctness, legal rights or release readiness.
No executable Rust product code is submitted as part of this packet.

## Actual founder decisions and remaining qualifications

| Requirement | Verified state |
|---|---|
| Founder selection | OPTION_B_RATIFIED — Issue #17 |
| Signed governance, DCO and normal merge | PASS — PR #19 |
| Named G01a engineering owner | FOUNDER_ASSUMED_ACCOUNTABILITY — Issue #17 |
| Synthetic-only Rust implementation | G01A_SYNTHETIC_QUALIFIED — PR #20 |
| Hardened Rust source admission | PASS — PR #21 |
| Exact-main cross-platform tests | PASS — P00/P01/G01a on Windows and Ubuntu |
| Independent code/security review | INDEPENDENT_REVIEW_PENDING — Issue #17 |
| Qualified clinical intended use/evaluation | UNAPPROVED — Issue #4 |
| Third-party rights and release trust | NO_ADMISSIONS / UNAPPROVED — Issue #5 |
| Full P01 phase entry, 41 original P1 findings | BLOCKED — Issue #3 |

## Actual ratification sequence

1. Founder selected narrow Option B for synthetic G01a and accepted ownership.
2. Signed and DCO-trailed governance PR #19 normally merged; exact-main CI passed.
3. Signed synthetic implementation PR #20 normally merged; cross-platform CI passed.
4. Signed fail-closed hardening PR #21 normally merged; cross-platform CI passed.
5. Independent technical review and P01 clinical/rights/phase gates remain open.

No user-facing medical product or clinical conclusion follows from this engineering milestone.

## Current invariant

FOUNDER_OPTION_B_RATIFIED / G01A_SYNTHETIC_QUALIFIED / INDEPENDENT_REVIEW_PENDING / NO_ADMISSIONS.
Qualified engineering main: d6645e169d643b6b6eae7ad06e17a605edcb0687.
Full P01_PRE_ENTRY_GATES_PENDING / P01-G01 PREPARED_NOT_ACTIVATED; source imports BLOCKED.
No clinical product implementation, patient data, external donor admission, product release or P02.
