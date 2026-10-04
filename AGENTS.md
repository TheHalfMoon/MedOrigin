# MedOrigin Agent Rules

These rules apply to Codex, Claude/Opus, Cursor, and any other engineering agent working in this repository.

## Communication and repository language

- Repository code, comments, commands, commits, branches, issues, PRs, specs, reports, research notes, evidence, and review artifacts are **English only**.
- User-facing conversation may be Arabic.

## Current project state

MedOrigin is in **P00 — Foundation challenge and freeze**.

Do **not** begin broad implementation merely because the repository exists. The current job is to challenge, refine, and close the foundation plan.

## Authority order

Read in this order before planning or changing architecture:

1. `AGENTS.md`
2. `README.md`
3. `docs/PRODUCT_THESIS.md`
4. `docs/ARCHITECTURE.md`
5. `docs/SOURCE_LEDGER.md`
6. `docs/MASTER_PLAN.md`
7. `docs/GAP_REVIEW.md`
8. active specs/decision records once created

If documents conflict, stop treating the conflict as resolved and record it explicitly.

## Core invariants

- Local-first and useful offline.
- No mandatory MedOrigin cloud.
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

## Source reuse

Never wholesale-copy a repository merely because permission exists.

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
```

Before copied/adapted/vendored/runtime material becomes canonical, bind exact revision/digest, paths/artifacts, license/permission basis, transitive material, notices, modifications, trust placement, tests, update strategy, and exit strategy.

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
- identify duplicate capability across MedOrigin and sibling projects;
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

Do not use CodeRabbit, Qodo, or Cubic as required proof/evidence for MedOrigin.

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