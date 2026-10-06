# SafeEvidence Agent Rules

These rules apply to Codex, Claude/Opus, Cursor, and any other engineering agent working in this repository.

## Communication and repository language

- Repository code, comments, commands, commits, branches, issues, PRs, specs, reports, research notes, evidence, and review artifacts are **English only**.
- User-facing conversation may be Arabic.

## Current project state

SafeEvidence is in **P00 — Foundation challenge and freeze**.

Do **not** begin broad implementation merely because the repository exists. The current job is to challenge, refine, and close the foundation plan.

## Authority order

Read in this order before planning or changing architecture:

1. `AGENTS.md`
2. `README.md`
3. `docs/PRODUCT_THESIS.md`
4. `docs/ARCHITECTURE.md`
5. `docs/SOURCE_LEDGER.md`
6. `docs/COPY_FIRST_SOURCE_PLAN.md`
7. `docs/REUSE_FIRST_IMPLEMENTATION_MAP.md`
8. `docs/DONOR_TRANSPLANT_PROTOCOL.md`
9. `docs/RUNTIME_BUDGET.md`
10. `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md`
11. `docs/MASTER_PLAN.md`
12. `docs/GAP_REVIEW.md`
13. active specs/decision records once created

If documents conflict, stop treating the conflict as resolved and record it explicitly.

## Core invariants

- Local-first and useful offline.
- No mandatory SafeEvidence cloud.
- No silent remote inference, search, storage, telemetry, auth, or sync fallback.
- Zero founder-funded runtime COGS is a design target.
- Evidence first, language second.
- Model output never grants clinical or action authority.
- Confidence, evidence quality, applicability, authority, and review state remain separate.
- `ASK_MORE`, `CONFLICT`, `ABSTAIN`, `BLOCKED`, and negative results are legitimate outcomes.
- Deterministic validated tools/policies outrank generative text where applicable.
- Derived indexes/graphs/summaries are rebuildable projections, not canonical truth.
- Desktop is the complete workstation; mobile is native and scoped rather than a blind desktop clone.
- Arabic/English, RTL, accessibility, and resource limits are architecture concerns from the start.
- Source permission does not waive exact provenance, embedded third-party review, model/data/asset rights, notices, security review, or tests.

## Source reuse — mandatory copy-first rule

SafeEvidence MUST NOT rebuild a subsystem from scratch when an authorized ready source already implements it well.

Before greenfield implementation, inspect `docs/COPY_FIRST_SOURCE_PLAN.md`, actual donor code, and `docs/REUSE_FIRST_IMPLEMENTATION_MAP.md`.

Founder authorization permits copying, modifying, combining, adapting, vendoring, and rebranding the discussed source-code donors. For those authorized sources, permission to copy is not an implementation blocker.

Prefer in this order:

```text
COHERENT_COPY / VENDOR_SNAPSHOT
        ↓
DIRECT_DEPENDENCY when lower-maintenance
        ↓
ADAPT copied code behind SafeEvidence contracts
        ↓
PORT only for a real trust/platform boundary
        ↓
GREENFIELD_JUSTIFIED
```

Copying proven code is the default when it is suitable. Owning a SafeEvidence interface does not require owning an independently rewritten implementation.

Never wholesale-copy a repository merely because permission exists. Reuse the smallest coherent implementation slice that preserves correctness and maintainability.

For every implementation-relevant source, classify it as one of:

```text
COPY_BOUNDED
ADAPT
PORT_TO_RUST
DEPEND
VENDOR
FFI
WORKER
ARTIFACT_IMPORT
REFERENCE
BENCHMARK_ONLY
REJECT_DEFAULT
GREENFIELD_JUSTIFIED
```

A new subsystem may use `GREENFIELD_JUSTIFIED` only after a donor decision records the exact sources inspected and why reuse is materially worse on correctness, security/privacy, portability, maintenance, resource cost, provenance/rights, or product fit. "We prefer our own implementation" is not sufficient.

Before copied/adapted/vendored/runtime material becomes canonical, bind exact revision/digest, paths/artifacts, license/permission basis, transitive material, notices, modifications, trust placement, tests, update strategy, and exit strategy. Bring useful donor tests/fixtures with the implementation whenever possible.

Private source identities must not be disclosed in this public repository without explicit founder authorization for public disclosure.

## Evidence discipline

Never fabricate:

- tests;
- benchmark results;
- model quality;
- CI state;
- PR/issue state;
- SHAs;
- mergeability;
- source permissions;
- licenses;
- clinical claims;
- privacy/security guarantees;
- regulatory/compliance status.

Bind material claims to exact artifacts/revisions/evidence.

## Planning discipline

During P00:

- challenge the plan, do not defend it reflexively;
- search sibling/source repositories when a material decision depends on them;
- identify duplicate capability across SafeEvidence and sibling projects;
- minimize architecture before expanding it;
- prefer measurable promotion gates over framework preference;
- preserve genuine reviewer disagreement until evidence resolves it;
- convert gaps into explicit owners/phases/decision records;
- do not silently decide unresolved architecture questions.

Follow `docs/GAP_REVIEW.md` for independent Codex and Claude/Opus reviews.

## Implementation discipline after P00

Once implementation is authorized:

- use bounded branches/PRs;
- normal merge commits are preferred;
- no force-push;
- no rebase/history rewriting for shared review branches;
- verify exact PR head before merge;
- rerun/inspect relevant post-merge evidence;
- preserve provenance across copied/adapted code;
- keep migrations backward/recovery aware;
- avoid adding mandatory services before measured need.

## Review tools

Alibaba Open Code Review and Jev are required review components where they are applicable and available in the authorized environment. They complement, not replace, tests and human/agent reasoning.

Do not use CodeRabbit, Qodo, or Cubic as required proof/evidence for SafeEvidence.

Never claim a review tool ran unless exact output/evidence exists.

## Medical/scientific claim rule

Repository status words such as `CLOSED`, `PROVEN`, or `READY` apply only to the exact engineering/research scope defined by the owning artifact. They do not imply clinical validation, medical-device approval, patient safety, regulatory compliance, or superiority.

Any strong clinical or comparative claim requires a dedicated protocol, frozen evaluation boundary where appropriate, and evidence packet.

## Cost rule

Do not introduce paid APIs, paid compute, paid SaaS, or paid cloud infrastructure as mandatory development/product gates without explicit founder authorization.

Optional institution/user-provided external services may exist behind explicit adapters, but the supported local product must not silently depend on them.

## Completion rule

Agent self-report is not completion authority.

A task is complete only when its owning acceptance criteria are satisfied and evidence is bound to the exact revision. If evidence is incomplete, report the task as partial, blocked, or not proven instead of forcing `done`.

## SafeEvidence 2026-10-07 P00 amendment

The findings in `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md` are mandatory P00
inputs. Agents must not close P00 by reviewing only the older foundation set.

In particular, do not:
- ignore PubMed update/delete/retraction lifecycle;
- omit item-level rights from packs/sync/export;
- build retrieval without benchmarking MedCPT;
- build claim verification without scientific-rationale evaluation and a
  clinician-adjudicated SafeEvidence holdout;
- display a confidence percentage without a frozen estimand/calibration split;
- invent mobile FFI before evaluating UniFFI;
- author generic parser/OCR/search/update frameworks when admitted donors exist.
