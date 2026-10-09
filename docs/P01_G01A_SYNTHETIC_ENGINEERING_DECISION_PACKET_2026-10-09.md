# SafeEvidence P01-G01a — Synthetic-Only Engineering Sequencing Decision Packet

Date: 2026-10-09 (Asia/Riyadh)
Status: **PROPOSED_ONLY / NOT_RATIFIED / NOT_EFFECTIVE**
Owning founder decision: https://github.com/TheHalfMoon/SafeEvidence/issues/17
Original gate tracking: https://github.com/TheHalfMoon/SafeEvidence/issues/3
Clinical evaluation: https://github.com/TheHalfMoon/SafeEvidence/issues/4
Rights and trust: https://github.com/TheHalfMoon/SafeEvidence/issues/5

## Authority and default

This packet neither authorizes implementation nor changes the current 
`P01_PRE_ENTRY_GATES_PENDING / P01-G01 PREPARED_NOT_ACTIVATED` state.
The existing AGENTS, P01 Entry Readiness and G01 Prepared authority remains
binding until an explicitly signed founder decision, named engineering owner
acceptance, reconciled governance changes and a separately qualified PR are
recorded. General 'continue' instructions are not clinical/legal approvals.

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

## Required explicit founder decision and ownership

| Requirement | Status |
|---|---|
| Named founder's A/B selection with exact governance PR revision | PENDING |
| Signed or otherwise attributable durable approval consistent with repository policy | PENDING |
| Named accountable engineering owner and acceptance of scoped work | PENDING |
| Qualified review of updated AGENTS/P01 entry/G01 prepared/MASTER_PLAN conflicts | PENDING |
| Exact-PR-head and post-main checks on governance ratification | PENDING |
| Original #4 intended use and independent clinical evaluation | UNAPPROVED — unaffected by G01a |
| Original #5 source/contributor rights and release/TUF trust | NO_ADMISSIONS / UNAPPROVED — unaffected by G01a |

## Proposed ratification sequence

1. Founder records A or B and names the engineering owner on Issue #17.
2. Reviewers create a *separate* atomic governance PR reflecting that signed
   choice across AGENTS, entry readiness, G01 prepared and MASTER_PLAN.
3. Qualify exact PR head CI; record approval credentials/evidence; normal
   merge and inspect post-main checks.
4. Only then activate bounded G01a and implement synthetic Rust workspace
   via a separately reviewed PR. Maintain G01b and all other gates.
5. Do not promote a synthetic build result to user-facing medical safety,
   scholarly validity, data redistribution permission or product completion.

## Exit-state invariant

Until the explicit ratification path is completed: 
`P01_PRE_ENTRY_GATES_PENDING`, `P01-G01 PREPARED_NOT_ACTIVATED`,
`G01A_NOT_ACTIVATED`, `NO_ADMISSIONS`, no product implementation.

