# SafeEvidence P00 Reconciliation Re-check — 2026-10-08

**Reviewer:** ChatGPT/GPT-6, independent document-based re-check of the earlier Codex and Opus findings. This is **not** a new run by either Codex or Claude/Opus and does not satisfy a requirement for both of those models to independently approve the repaired revision.

**Reviewed exact reconciliation SHA:** `83561a305cea265845a19535f9808ac92fec623c`

**Original reviewed base:** `136cdffc2cd14133e01018ca56833241dd50bc4e`

**Branch:** `reconcile/p00-reviews-2026-10-07-final`

**Original review artifacts:**
- `review/codex-p00-kill-review-2026-10-07:docs/reviews/CODEX_P00_INDEPENDENT_KILL_REVIEW_2026-10-07.md`
- `review/opus-p00-kill-review-2026-10-07:docs/reviews/OPUS_P00_INDEPENDENT_KILL_REVIEW_2026-10-07.md`

**FINAL VERDICT: `P00_RECONCILIATION_FAILED`**

This is a planning-contract and internal consistency review, **not** a product test, clinical validation, device qualification, legal opinion or downstream donor qualification. Neither `main` nor the reconciliation branch was modified in the course of this re-check. The review artifact is attached on an isolated review branch only.

## 1. Scope and method

GitHub branch and commit refs were checked. The exact reconciliation branch head equals the requested SHA; `main` remains `136cdffc2cd14133e01018ca56833241dd50bc4e`. The compare is five commits ahead, zero behind, changing sixteen planning/governance files only.

The original Codex review (36 findings: 6 P0, 24 P1, 5 P2, 1 P3) and Opus review (34 findings: 2 P0, 17 P1, 12 P2, 3 P3) were read from their respective immutable review branches.

The following authority was read at the requested exact SHA: `AGENTS.md`, `README.md`, `THIRD_PARTY_NOTICES.md`, `docs/PRODUCT_THESIS.md`, `docs/ARCHITECTURE.md`, `docs/MASTER_PLAN.md`, `docs/COPY_FIRST_SOURCE_PLAN.md`, `docs/REUSE_FIRST_IMPLEMENTATION_MAP.md`, `docs/DONOR_TRANSPLANT_PROTOCOL.md`, `docs/SOURCE_LEDGER.md`, `docs/RUNTIME_BUDGET.md`, `docs/GAP_REVIEW.md`, `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md`, `docs/PREBUILD_KILL_REVIEW_2026-10-07.md`, `docs/P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md`, `docs/P00_FOUNDATION_DECISIONS_2026-10-07.md`, and `docs/DONOR_RIGHTS_REGISTER.md`.

No broader architecture redesign, donor execution, independent model invocation or implementation was performed.

## 2. Codex original P0 disposition

| Finding | Disposition | Exact remaining reason |
|---|---|---|
| CODEX-P00-01, data planes | PARTIALLY_CLOSED | Two planes are named in D1, but the pre-P01 required per-object placement/custody matrix, licensed document placement, cross-store transaction/reference rules, GC, backup/sync/export/delete mapping and private query projections are not specified. |
| CODEX-P00-02, durable vault | PARTIALLY_CLOSED | MedScale whole-file EncryptedVault is demoted and ottari selected as primary candidate. However D2 still calls it a P02 hypothesis and does not freeze acknowledgement semantics, process-lock lifetime, persistent DB/WAL checkpoint policy, backup barrier, crash ordering or recovery authority before P01. |
| CODEX-P00-03, statistical independence | PARTIALLY_CLOSED | Canonical concept names were added in D3, but typed identities/foreign keys, analysis-set/arm denominators, adjusted estimand, variance/covariance, registry-report pairing, participant overlap, review membership and human-confirmation semantics are not frozen. |
| CODEX-P00-04, decision semantics | PARTIALLY_CLOSED | ControlAction and TerminalOutcome are separated in D4. Missing: total precedence, reason codes, explicit finite numeric budgets, worker-failure rule, final per-claim publication rule and frozen commit/abstain/false-escalation denominators. D4 defers metrics until P08 although the original P0 required semantic definitions before P01. |
| CODEX-P00-05, donor rights | STILL_OPEN | DONOR_RIGHTS_REGISTER introduces a safer deny-by-default condition, but `DONOR_TRANSPLANT_PROTOCOL.md` section 11 still says remaining copying questions are technical, and the old source matrices still propose copying unlicensed/copyleft source. Register rows are not typed by actual rights basis per exact revision/file/asset. |
| CODEX-P00-06, atomic proof admission | PARTIALLY_CLOSED | D6 names AnswerProofManifest and prohibits committing unverified streamed text. It does not define an atomic verified-to-committed transition, stale watermark/revocation race behavior, worker-crash rollback, admission failure state, publication observability or replay contract. |

**Codex P0 totals:** CLOSED_BY_RECONCILIATION 0; PARTIALLY_CLOSED 5; STILL_OPEN 1; REGRESSED 0. Six original P0s remain unresolved as closure requirements.

## 3. Codex original P1 disposition

`RESOLVED` means the planning issue is materially closed; `PRECISELY_PHASE_BOUND` means the owning phase and its meaningful prerequisite are identified. It does not mean product/runtime qualification passed.

| Finding | Disposition | Assessment / remaining work |
|---|---|---|
| CODEX-P00-07 | INSUFFICIENTLY_BOUND | No per-OS KEK/DEK, recovery, user-presence, rotation, copied-backup and membership-leak contract. |
| CODEX-P00-08 | INSUFFICIENTLY_BOUND | TUF named, but no threshold, trusted-clock/expiry or compromised-targets/offline-role policy freeze. |
| CODEX-P00-09 | INSUFFICIENTLY_BOUND | Network boundary lacks DNS/redirect/rebinding/proxy/connection-bound IP and worker packet-denial contract. |
| CODEX-P00-10 | PRECISELY_PHASE_BOUND | P03 owns PubMed ordered-update completeness, replay, lifecycle and freshness; execute adversarial fixtures before ingest promotion. |
| CODEX-P00-11 | PRECISELY_PHASE_BOUND | P04/P05 own study/report qrels, source-family and Arabic retrieval, model admission. |
| CODEX-P00-12 | INSUFFICIENTLY_BOUND | No authoritative per-claim `mismatch_facets`, SOURCE_UNAVAILABLE treatment, numeric-first verifier and support/applicability split. |
| CODEX-P00-13 | PRECISELY_PHASE_BOUND | P06 owns typed Result grammar and human-confirmed extraction, not research-oracle authority. |
| CODEX-P00-14 | INSUFFICIENTLY_BOUND | P18 still lacks an explicit accepted method/design/estimand/defaults/refusal matrix and statistical oracle policy. |
| CODEX-P00-15 | INSUFFICIENTLY_BOUND | Search completeness, dual screening, stopping/residual recall and PRISMA counting are not explicitly phase-gated. |
| CODEX-P00-16 | INSUFFICIENTLY_BOUND | No result-specific rubric/version/reviewer/adjudication/invalidation contract. |
| CODEX-P00-17 | RESOLVED | D5 and reconciled plan prohibit a user-facing clinical confidence percentage in V1. |
| CODEX-P00-18 | INSUFFICIENTLY_BOUND | Temporal patient-context fields and a per-tool authority/formula/reference-vector catalog are not specified. |
| CODEX-P00-19 | PRECISELY_PHASE_BOUND | P13 separates CQL syntax from guideline semantics, jurisdiction/version/rights qualification. |
| CODEX-P00-20 | PRECISELY_PHASE_BOUND | P12 requires narrow offline parser features, isolation and resource limits before parser admission. |
| CODEX-P00-21 | RESOLVED | SafeOCR is no longer classified as empty; re-use still requires component/clinical qualification. |
| CODEX-P00-22 | INSUFFICIENTLY_BOUND | Shell open-tournament declaration conflicts with old Slint-favored audit language. License/accessibility/exposure acceptance is not uniformly authoritative. |
| CODEX-P00-23 | PRECISELY_PHASE_BOUND | P15/P16 own bounded UniFFI, key protector and real-device privacy/lifecycle qualification. |
| CODEX-P00-24 | INSUFFICIENTLY_BOUND | P17 heading is not a pairing protocol: replay, out-of-band confirmation, rights checks, revocation, tombstones and relay policy are not frozen. |
| CODEX-P00-25 | INSUFFICIENTLY_BOUND | No early per-platform allowed-residuals/retention/worker-exposure matrix; P21 alone cannot retroactively protect P02. |
| CODEX-P00-26 | INSUFFICIENTLY_BOUND | Source byte/codepoint/normalized/rendered region transforms and Arabic dose/identifier safety are only named, not bound. |
| CODEX-P00-27 | INSUFFICIENTLY_BOUND | The human-gold plan lacks an owner, adjudicator acquisition/funding, label/sample budget, subgroup and split protocol before tournaments. |
| CODEX-P00-28 | INSUFFICIENTLY_BOUND | The initial population-evidence wedge is narrowed, but geography, care setting, specialty/question classes, devices and risk/coverage target are still undefined. |
| CODEX-P00-29 | PRECISELY_PHASE_BOUND | P03 owns measurable corpus/pack/install/build/distribution economics before source-pack promotion. |
| CODEX-P00-30 | PRECISELY_PHASE_BOUND | P01 binds transitive executable/model/data/asset rights and dependency/feature admission before first transplant. |

**Codex P1 totals:** RESOLVED 2; PRECISELY_PHASE_BOUND 8; INSUFFICIENTLY_BOUND 14; REGRESSED 0.

## 4. Opus cross-check (not an Opus re-run)

### Opus P0

| Finding | Disposition | Assessment |
|---|---|---|
| OPUS-P00-001 | PARTIALLY_CLOSED | Public/private plane split exists; missing item-level field placement, scoped corpus rights, snapshot reference/deletion semantics and measured source/build/distribution profile. |
| OPUS-P00-002 | STILL_OPEN | Per-donor rights register introduced, but no file/pin/grant-level evidence and conflicting copy-first instructions persist. |

### Opus P1

| Finding | Disposition | Assessment |
|---|---|---|
| OPUS-P00-003 | INSUFFICIENTLY_BOUND | Vault lifecycle still a candidate, not an explicit durability contract. |
| OPUS-P00-004 | INSUFFICIENTLY_BOUND | No frozen TUF root threshold, custody, offline-clock/stale-bundle details. |
| OPUS-P00-005 | INSUFFICIENTLY_BOUND | State names split, but no total precedence or metric/cost contract. |
| OPUS-P00-006 | INSUFFICIENTLY_BOUND | DAL negative Study-0 is noted but exact prior-result identity and contaminated split exclusion are missing. |
| OPUS-P00-007 | RESOLVED | V1 clinical confidence percentage prohibited. |
| OPUS-P00-008 | INSUFFICIENTLY_BOUND | Arm/result/analysis labels lack mandatory fields and independence relationships. |
| OPUS-P00-009 | INSUFFICIENTLY_BOUND | No supported-design/method/refusal matrix for quantitative synthesis. |
| OPUS-P00-010 | INSUFFICIENTLY_BOUND | PubMed XML DeleteCitation/CommentsCorrections, JATS license and resumable bulk ingest acceptance not specifically captured. |
| OPUS-P00-011 | RESOLVED | Live SafeOCR implementation is recognized as an eligible candidate, not certified. |
| OPUS-P00-012 | INSUFFICIENTLY_BOUND | Arabic normalization, translated-query visibility and semantic-preservation fixtures not defined. |
| OPUS-P00-013 | INSUFFICIENTLY_BOUND | Missing explicit primary tensor/ONNX vs LLM runtime decisions and complete feature closure. |
| OPUS-P00-014 | INSUFFICIENTLY_BOUND | MedicationRequest/MedicationStatement/AllergyIntolerance and contraindication/interaction fail-closed rules missing. |
| OPUS-P00-015 | INSUFFICIENTLY_BOUND | No explicit V1 guideline document rights scope or founder decision about private donor disclosure. |
| OPUS-P00-016 | INSUFFICIENTLY_BOUND | Snapshot tombstone/redaction/revoked-byte/partial-reproduction contract absent. |
| OPUS-P00-017 | INSUFFICIENTLY_BOUND | No mandatory mismatch facet schema and independent current-validity axis. |
| OPUS-P00-018 | INSUFFICIENTLY_BOUND | Shell declaration is not consistent across audit, source plan and architecture. |
| OPUS-P00-019 | INSUFFICIENTLY_BOUND | No label-count rationale, adjudicator/resourcing/funding decision record. |

**Opus P1 cross-check totals:** RESOLVED 2; PRECISELY_PHASE_BOUND 0; INSUFFICIENTLY_BOUND 15; REGRESSED 0.

These are overlapping assessments of 41 P1 review entries, **not 41 unique product gaps**. The 8 Codex/2 Opus P0 entries likewise overlap, so they are not ten unique foundational failures.

## 5. New P0 and regressions

**New P0:** 0. The previous P0s have not been fully closed; the defects are continuations/authority contradictions, not a newly observed failure class.

**Governance inconsistencies requiring repair:**

1. `docs/DONOR_TRANSPLANT_PROTOCOL.md` section 11 says founder permission removes copyright copying as a blocker and that remaining questions are technical. `docs/DONOR_RIGHTS_REGISTER.md` sections 2-3 require independent documentary external rights. The agent explicitly must stop when authority conflicts (`AGENTS.md` authority order).
2. Stale normative choices remain in upstream documents:
   - `docs/MASTER_PLAN.md` initial reuse section still says P02 starts from MedScale vault;
   - `docs/REUSE_FIRST_IMPLEMENTATION_MAP.md` section 4.1 still promotes `encrypted_vault.rs` and its P02 phase table still names MedScale keys/storage as default;
   - `docs/COPY_FIRST_SOURCE_PLAN.md` mobile table still offers Signthos `COPY/ADAPT`;
   - `docs/PREBUILD_KILL_REVIEW_2026-10-07.md` still lists Trialstreamer `COPY_BOUNDED`;
   - `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md` still favors Slint before the shell tournament.

The reconciliation appendices announce supremacy but do not remove all directly competing normative instructions. Calling these only "historical" is not sufficient while agents are explicitly directed to consult them.

## 6. Smallest exact documentation/decision repairs

No product implementation or donor-code copying is required to address the planning gaps.

### Repair A — coherent authority and rights (P0)

Edit these existing files in place, not merely append more contradictory notes:
- `docs/DONOR_TRANSPLANT_PROTOCOL.md` section 11: replace blanket-rights/technical-only assertion with required `DONOR_RIGHTS_REGISTER` admission.
- `docs/COPY_FIRST_SOURCE_PLAN.md`: demote the Signthos QR default to `REFERENCE_PENDING_RIGHTS_AND_IMPLEMENTATION`, restrict Trialstreamer/RobotReviewer instructions and fix source modes.
- `docs/REUSE_FIRST_IMPLEMENTATION_MAP.md`: replace MedScale whole-file vault default with ottari qualification; preserve MedScale only for independently qualified helpers/tests.
- `docs/PREBUILD_KILL_REVIEW_2026-10-07.md` historical matrix: clearly mark Trialstreamer/RobotReviewer lines as superseded and non-copyable pending grants.
- `docs/MASTER_PLAN.md`: change original P02 donor statement to match new authority.
- `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md`: demote Slint to an unranked candidate.
- `docs/DONOR_RIGHTS_REGISTER.md`: one exact row per imported revision/slice with SPDX/terms, owner class, permission link/evidence, allowed modes and independent asset-rights columns; `SEPARATE_PERMISSION_ASSERTED` remains copy-deny until verified. Do not invent grants.

### Repair B — six P0 contract sheets (P0)

Expand `docs/P00_FOUNDATION_DECISIONS_2026-10-07.md` or add six focused ADRs containing:

1. **D1 placement matrix:** public citations/metadata, public licensed content, user PDF, institution full text, patient context, private embeddings/cache, pack manifest, source snapshot, committed proof; for each bind store, encryption, grants, backup, delete/tombstone, export/sync, cross-plane references and pack eligibility.
2. **D2 durability lifecycle:** persistent SQLCipher/WAL design choice, acknowledged commit point, lock lifetime, WAL/checkpoint semantics, backup barrier, recovery/restore ownership and what happens on a crash at every step. Keep device qualification for P02.
3. **D3 statistical ontology:** typed IDs and cardinalities, arm/analysis/result denominators, measured estimand, adjusted model, variance/covariance, registry pairing, participant overlap, membership and human linkage state. Make independence a required, testable synthesis-input decision.
4. **D4 terminal contract:** total precedence, failure/unknown handling, concrete action round cap, reason codes, source-applicability separation, accepted versus refused per-claim publication, and commit/abstention/false-escalation denominators. Avoid importing lexical emergency rules.
5. **D5 rights precedence:** explicit owner/license/permission type and default deny, consistent with every copy matrix; no source-code rights transfer to independent model/data/medical-publication assets.
6. **D6 proof admission:** candidate/draft/verified/committed/invalidated lifecycle; atomic proof and text write; concurrent source correction/retraction/grant revocation behavior; error/worker-crash rollback; replay/cached/mobile freshness and unavailable-source behavior.

### Repair C — P1 phase-bound acceptance register

Replace the generic bullets under `docs/P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md` with a per-finding table: original reviewer ID, disposition, owning phase, exact phase-entry/closure gate, acceptance fixtures/tests, decision owner role and evidence location.

Do not mark P1 as "phase-bound" when the rule is only "address in PXX". The key omitted requirements to bind include native key/OS residuals; TUF root/offline policy; network DNS/socket isolation; per-claim mismatch facets; statistical method/screening refusal; rubric/version; Arabic coordinates; clinical calculator/interaction source admission; human adjudicator funding and split custody; intended-use geography and setting.

Then freeze a new repair SHA and obtain **actual separate Codex and Opus re-checks against that same SHA**. This review cannot impersonate their sign-offs.

## 7. Required final summary

Reviewed reconciliation SHA: `83561a305cea265845a19535f9808ac92fec623c`

Original P0 closed: **0**.

Original P0 still open: **6 total** (Codex: 5 partially closed, 1 still open).

New P0: **0**.

P1 resolved: **Codex 2; Opus 2**.

P1 precisely phase-bound: **Codex 8; Opus 0**.

P1 still insufficient: **Codex 14; Opus 15**.

Regressions: **2 unresolved document-authority inconsistencies**, neither a new distinct P0 threat category.

**Final verdict: `P00_RECONCILIATION_FAILED`.**

No clinical/device qualification was performed. `main` and the reviewed reconciliation branch are unchanged.
