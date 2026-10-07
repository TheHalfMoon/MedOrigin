# SafeEvidence P00 Repair Closeout Plan — 2026-10-08

Status: `P00_REPAIR_PREPARED_PENDING_INDEPENDENT_RECHECK`
Original independent review base:
`136cdffc2cd14133e01018ca56833241dd50bc4e`
Failed reconciliation head:
`83561a305cea265845a19535f9808ac92fec623c`

This document records a documentation-only P00 repair, not product
implementation, validated code, source-rights certification or independent
reviewer approval. The repair head is the exact final commit on its GitHub
branch and must be verified live before a review begins.

## Repair basis and P0 dispositions

The earlier independent Opus and Codex reviews returned P00_NOT_READY. The
ChatGPT document re-check of the failed reconciliation identified Codex's
six P0 as five partial, one still open; no newly discovered P0 class.

The following are **submitted for review**, not self-certified closed:

| P0 ID | Original deficiency | Binding repair | Closure evidence expected from re-check |
|---|---|---|---|
| CODEX-P00-01 / OPUS-P00-001 | Mixed public corpus/private vault and unspecified placement | `P00_DATA_PLACEMENT_CONTRACT.md` | Each canonical class has store/rights/backup/sync/export/delete and cross-store recovery semantics |
| CODEX-P00-02 / OPUS-P00-003 | Whole-file MedScale vault cannot guarantee acknowledged crash durability | `P00_VAULT_DURABILITY_CONTRACT.md` | Persistent SQLCipher/WAL acknowledged commit, lock, backup/migration/failure contract; P02 qualification still required |
| CODEX-P00-03 / OPUS-P00-008 | Same participants/results can be counted repeatedly | `P00_STUDY_INDEPENDENCE_CONTRACT.md` | Typed arm, analysis, outcome, result, overlap/review membership and refusal criteria |
| CODEX-P00-04 / OPUS-P00-005/006 | Actions mixed with terminal outcomes; lexical emergency misfires | `P00_DECISION_ASSURANCE_CONTRACT.md` | Total precedence, bounded actions, reason codes, explicit denominators, V1 emergency rule disabled |
| CODEX-P00-05 / OPUS-P00-002 | Blanket founder permission inferred as external rights | `DONOR_RIGHTS_REGISTER.md` + corrected donor docs | Empty import allowlist, per-slice documentary rights, third-party/copyleft/asset admission, stale copy directives removed |
| CODEX-P00-06 | Streaming/retraction races could admit unverified final text | `P00_PROOF_ADMISSION_CONTRACT.md` | Frozen final-text proof, local epoch/rights check, atomic durable write and invalidation/replay semantics |

`P00_FOUNDATION_DECISIONS_2026-10-07.md` and
`P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md` retain history but defer
to these binding contracts where the old summary was underspecified.

## P1 traceability

All original 24 Codex P1 items have individual owner, timing and tests in
`P00_CODEX_P1_ACCEPTANCE_REGISTER.md`.

All original 17 Opus P1 items have individual owner, timing and tests in
`P00_OPUS_P1_ACCEPTANCE_REGISTER.md`.

These registers preserve reviewer IDs and each item's exact phase-entry
constraint. `RESOLVED_PLANNING` is a document decision, not a claim of tested
software. `OPEN_PHASE_GATES` require an issue, accountable owner and acceptance
packet. No founder-funded services, clinicians, licenses, credentials or model
weights are assumed to already exist.

## Initial product and cost boundary

The first implementation/evaluation target is a local, CPU-only 16 GB-class
Windows clinician/research evidence workstation for adult **population-level**
treatment benefit/harm and contradiction questions, supporting English/Arabic
retrieval/citations as evaluation lanes.

Not initially admitted: autonomous diagnosis, treatment orders, emergency
triage, individual dosing, unsourced drug interaction advice, mandatory
meta-analysis, regulatory certification, broad patient-specific recommendations,
unrestricted model downloads, or clinical confidence percentages.

P01 must freeze exact clinician/user cohort, specialty/question inclusion and
exclusion, jurisdiction/setting for any public claims, evaluation/risk goals,
adjudicator/label financing and corpus default scope. Until rights approval,
the default corpus can contain synthetic development fixtures but **no**
uncleared journal/article bytes. P03 signs and measures only rights-admitted
public/optional packs, with owner-funded or user/institution-driven build and
distribution chosen explicitly, never an implicit per-query founder cloud cost.

## Mandatory re-check

1. Verify live main and repair branch exact SHA; do not silently replace review
   base with a different revision.
2. Have **Codex and Claude/Opus separately** review the same repair head.
3. For all six Codex P0 plus overlapping Opus P0, return CLOSED /
   PARTIALLY_CLOSED / STILL_OPEN / REGRESSED with evidence.
4. For each original P1 in both acceptance registers, return
   RESOLVED / PRECISELY_PHASE_BOUND / INSUFFICIENTLY_BOUND / REGRESSED.
5. Explicitly search for NEW P0 and source-authority contradictions.
6. Any remaining P0 or insufficient phase boundary is repaired on a new exact
   head and rechecked; do not downgrade because a repair seems small.
7. Only after both reviewers agree on zero unresolved P0 and adequately bound
   P1 may the docs be merged by **normal merge commit** to main, with exact-head
   CI and post-merge verification.

## Hard gates

- Do not start P01 implementation or source copying while P00 is open.
- Do not merge this documentation repair merely because a commit exists.
- Do not rebase, squash, force-push, or rewrite history.
- Do not use invented tests, licenses, independent reviewer results or claims of
  clinical/medical-device compliance.
- All repository content and evidence remain English only.
