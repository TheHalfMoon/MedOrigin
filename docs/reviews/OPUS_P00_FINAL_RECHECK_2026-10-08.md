# SafeEvidence P00 — Final Independent Opus Re-check — 2026-10-08

Status: `INDEPENDENT_RECHECK_B` (Claude/Opus). Documentation review only. Not implementation authority.

## 0. Identity

| Item | Value |
|---|---|
| Reviewed exact SHA | `d2280cae49fe37c4b3621400788e61f113d83b46` |
| Branch reviewed | `reconcile/p00-repair-2026-10-08-final` (live head verified equal to the SHA above via `git ls-remote`) |
| Live `main` | `136cdffc2cd14133e01018ca56833241dd50bc4e` (unchanged) |
| Original Opus review | `review/opus-p00-kill-review-2026-10-07` @ `80e88a8a89f8509b0018a26b33407dadeda6a950` (2 P0, 17 P1, 12 P2, 3 P3) |
| Compared against | original base `136cdff`; failed reconciliation `83561a3` (`git diff 83561a3 d2280ca`: 26 files, +935/−69) |
| Reviewer | Claude Opus 5.5 |

Documents read in full at the exact SHA:
- `AGENTS.md`, `THIRD_PARTY_NOTICES.md`;
- `P00_REPAIR_CLOSEOUT_PLAN_2026-10-08.md`, `P00_REPAIR_CONSISTENCY_CHECK_2026-10-08.md`;
- `P00_DATA_PLACEMENT_CONTRACT.md`, `P00_VAULT_DURABILITY_CONTRACT.md`, `P00_STUDY_INDEPENDENCE_CONTRACT.md`, `P00_DECISION_ASSURANCE_CONTRACT.md`, `P00_PROOF_ADMISSION_CONTRACT.md`;
- `DONOR_RIGHTS_REGISTER.md`, both P1 acceptance registers;
- `P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md`, `RUNTIME_BUDGET.md`.

Other authority files were checked by targeted diff and search for stale directives:
- `ARCHITECTURE.md`, `MASTER_PLAN.md`, `COPY_FIRST_SOURCE_PLAN.md`;
- `REUSE_FIRST_IMPLEMENTATION_MAP.md`, `DONOR_TRANSPLANT_PROTOCOL.md`, `SOURCE_LEDGER.md`;
- `PRODUCT_THESIS.md`, `GAP_REVIEW.md`, `PREBUILD_KILL_REVIEW_2026-10-07.md`, `FOUNDATION_GAP_AUDIT_2026-10-07.md`;
- `P00_FOUNDATION_DECISIONS_2026-10-07.md`.

No donor source had to be re-inspected. Each finding below turns on the authority text, and the donor facts were established in the original review.

This re-check judges contracts as **documented design decisions and gates**. It does not treat any of them as tested implementation. None of the repaired documents claims otherwise (`P00_REPAIR_CONSISTENCY_CHECK` lists what was not executed).

## 1. Original P0 dispositions

| ID | Disposition | Evidence |
|---|---|---|
| OPUS-P00-001 data planes / corpus scope | `CLOSED_BY_RECONCILIATION` | See below. |
| OPUS-P00-002 third-party rights contamination | `CLOSED_BY_RECONCILIATION` | See below. |

**OPUS-P00-001.** `P00_DATA_PLACEMENT_CONTRACT.md` assigns each object class a store with backup, export, sync and delete semantics:
- public metadata;
- item-rights-admitted abstracts and full text;
- institution-licensed content;
- user PDFs and OCR intermediates;
- patient data and question history;
- private query embeddings;
- global indexes;
- packs, snapshots and proofs;
- the validity overlay.

The contract also provides:
- **Cross-store consistency:** an idempotent durable intent/outbox, with no false claim of two-phase commit.
- **Rights checks** at ingest, index, pack-build, export, backup, sync send and sync receive, failing closed.
- **`PARTIAL_REPRODUCTION`** for revoked bytes.
- **Corpus scope:** "not entire PubMed", with scope selected at P01 and count/bytes/update/build/distribution economics measured at P03 before the first pack.

`RUNTIME_BUDGET.md` §10 separates the plane budgets and explicitly accepts user- or institution-built packs. The original P0 was that P02 would freeze a single-vault contract; that dependency is now removed. Corpus size remains an explicit pre-P03 gate, which is the correct place for it.

**OPUS-P00-002.**
- `DONOR_RIGHTS_REGISTER.md` keeps the founder assertion but requires a per-slice admission row.
- The import ledger is empty (`NO_ADMISSIONS`).
- An asserted but unverified grant is "deny-for-copy".
- GPL/AGPL code may not be silently relicensed.
- Model, data, terminology and publication rights are separate decisions.
- trialstreamer is `REFERENCE_ONLY_PENDING_RIGHTS`, robotreviewer is BENCHMARK/REFERENCE, Signthos is REFERENCE pending a verified relicense, and Slint is not admitted until a license and attribution record exists.
- `AGENTS.md` copy-first wording was corrected to "rights-admitted ready source".
- `COPY_FIRST_SOURCE_PLAN.md` §16 rows were corrected.
- `THIRD_PARTY_NOTICES.md` carries an admission freeze.

Copy-first intent survives: the ordering COPY → VENDOR → DEPEND is retained for admitted slices.

### New P0 introduced by the repair

**None found.**

The two residual authority inconsistencies in §4 are documentation defects in late-phase or descriptive text, not a new P0:
- The `AGENTS.md` "P00 repair authority" clause makes the binding contracts take precedence over older roadmap statements and requires a stop on conflict.
- The empty import ledger prevents any copy from occurring before the defects are corrected.

## 2. Original Opus P1 dispositions (17)

| ID | Topic | Disposition | Basis |
|---|---|---|---|
| OPUS-P00-003 | vault durability / donor | `PRECISELY_PHASE_BOUND` | SQLCipher+WAL, acknowledgement only after COMMIT under a tested profile, `COMMIT_UNKNOWN`, writer guard across open/txn/close, online consistent backup, journaled migration, opaque blob names. ottari is "primary copy-first candidate, not proof". The P02 kill/backup/disk-full/spill test list says any acknowledged-loss blocks adoption. |
| OPUS-P00-004 | pack trust / TUF | `PRECISELY_PHASE_BOUND` | P01 trust ADR (role keys, threshold root, offline clock, rotation) before P10. Synthetic signing key banned from release (Opus and CODEX-08 rows). |
| OPUS-P00-005 | state semantics | `RESOLVED` (design); tests at P02/P08 | `ControlAction` / `TerminalOutcome` split, a total 7-guard precedence, action caps (2 retrieval rounds, 3 tools, 1 REQUEST_CONTEXT → ASK_MORE), closed reason codes, explicit commit/unsafe-commit/over-abstention/false-escalation denominators, and lexical EMERGENCY disabled in V1 with negation fixtures required. Residual vocabulary defect in `PRODUCT_THESIS.md` §5 (§4 item R1). |
| OPUS-P00-006 | DAL negative prior | `RESOLVED` | The decision contract records DAL Study-0 as prior evidence and the deterministic policy plus per-claim verification as the V1 incumbent. Learned models are challengers on fresh, blinded, group-separated data, and PubMedQA contamination is excluded (register). |
| OPUS-P00-007 | calibration estimand | `RESOLVED` | No V1 clinical confidence percentage. Any future number needs whole-pipeline identity, holdout and drift. |
| OPUS-P00-008 | study model | `RESOLVED` (design); fixtures at P02/P18 | Typed StudyArm, Analysis (incl. PooledStudySet), RegisteredOutcome↔ReportedOutcome, Result, ArmObservation, Comparison with covariance, ReviewIncludedStudyLink, ParticipantOverlapGroup (CONFIRMED/POSSIBLE/UNKNOWN), ReportVersionLink, SynthesisInputDecision, and `POOLING_REFUSED_UNIT_OF_ANALYSIS`. The fixture list covers every case in the original finding. |
| OPUS-P00-009 | statistical synthesis | `PRECISELY_PHASE_BOUND` | P18 statistician gate. Estimand/method/refusal matrix and a metafor or equivalent oracle are required before pooling. Rare/zero/multi-arm/cluster fixtures listed (also CODEX-14). |
| OPUS-P00-010 | PubMed XML / JATS / ingest | `PRECISELY_PHASE_BOUND` | P03 source-ingestion gate: DeleteCitation, CommentsCorrections, JATS license, checksum/restart. Ordered replay is in CODEX-10. |
| OPUS-P00-011 | SafeOCR status | `RESOLVED` (planning); P12 qualification gate | Stale "empty" statements superseded in ledger, audit, master plan and AGENTS. Arabic-Indic decimal fixture required. |
| OPUS-P00-012 | Arabic cross-language | `PRECISELY_PHASE_BOUND` | P05 owner. Multilingual vs translate-then-biomedical comparison, visible translation, negation/dose controls, cross-language qrels. |
| OPUS-P00-013 | runtime sprawl | `PRECISELY_PHASE_BOUND` | `RUNTIME_BUDGET.md` §11 and the inference admission section: ORT is a candidate (not a winner), one generator runtime, default download/telemetry features disabled, offline model-load test. |
| OPUS-P00-014 | medication / FHIR | `PRECISELY_PHASE_BOUND` | P14 gate: Medication*/Allergy or typed loss. Unsupported interaction → ABSTAIN/ESCALATE with reason. The closeout plan excludes "unsourced drug interaction advice" from initial scope. |
| OPUS-P00-015 | guidelines / non-public donor | `INSUFFICIENTLY_BOUND` | The register restricts early guidelines and forbids unqualified private-donor disclosure. However, canonical `COPY_FIRST_SOURCE_PLAN.md` §11 still reads "guideline verification semantics \| ProtocolWISE \| COPY/ADAPT", and `MASTER_PLAN.md` P00A still says "P13 uses ProtocolWISE semantics". The non-public donor's name remains in 4 public files with no recorded founder disclosure decision. See §4 item R2. |
| OPUS-P00-016 | snapshot vs deletion / revocation | `RESOLVED` (design) | Snapshot as identities/digests, tombstones, `PARTIAL_REPRODUCTION`, `CURRENTLY_INVALIDATED` (data placement and proof admission contracts). |
| OPUS-P00-017 | support labels / facets | `PRECISELY_PHASE_BOUND` | P06 gate: span relation + source validity + mismatch facets, deterministic numeric/unit before AI, SOURCE_UNAVAILABLE. CODEX-12 adds the P02 contract entry. |
| OPUS-P00-018 | desktop shell conflict | `PRECISELY_PHASE_BOUND` | Open tournament with no preference, license/attribution record, RTL/screen-reader/cache benchmark (also CODEX-22). The remaining "Tauri candidate" wording in `ARCHITECTURE.md`/`MASTER_PLAN.md` states no preference, so this is acceptable. |
| OPUS-P00-019 | adjudication resourcing | `PRECISELY_PHASE_BOUND` | P01 evaluation charter: qualification, compensation/ethics, sample size/split, budget. Phase is BLOCKED if unavailable (also CODEX-27). |

Totals: **RESOLVED 6**, **PRECISELY_PHASE_BOUND 10**, **INSUFFICIENTLY_BOUND 1**, **REGRESSED 0**.

## 3. Codex P1 register (24) — cross-check

All 24 rows (CODEX-P00-07 … 30) name an owner role, a pre-work gate, an acceptance contract and evidence. The enforcement clause requires the first PR of each phase to link the row and exact SHA, and makes the phase BLOCKED when a reviewer, permission, device or label is unavailable.

- No contradiction with the Opus register or the binding contracts was found.
- CODEX-25/26 (residual surfaces, coordinate mapping) and CODEX-28/29 (intended use, corpus budget) correctly front-load cross-cutting decisions to P01/P02/P03.
- Their requirements are consistent with OPUS-001/013/019.

## 4. Remaining minimal repairs (required before closeout)

**R1 — `PRODUCT_THESIS.md` §5 state vocabulary contradicts the binding decision contract.**

§5 still lists `RETRIEVE_EVIDENCE`, `USE_TOOL` and `EMERGENCY` as "behavioral outcomes". The binding contract makes the first two internal `ControlAction`s and replaces EMERGENCY with a disabled `EMERGENCY_NOTICE`. PRODUCT_THESIS ranks #3 in the AGENTS authority order, above the contracts (#11–19), so the conflict sits in the product-defining document for the core differentiator.

Repair: replace the §5 code block with the `ControlAction` / `TerminalOutcome` definitions and a pointer to `P00_DECISION_ASSURANCE_CONTRACT.md`. Optionally, update the commandMed row of `SOURCE_LEDGER.md` §2 to say "donor vocabulary".

**R2 — Stale guideline-donor copy directives and undisclosed-source naming (OPUS-P00-015).**

Make all of the following changes:
- Change `COPY_FIRST_SOURCE_PLAN.md` §11 row 1 from `COPY/ADAPT` to `REFERENCE (research thesis only; no implementation code observed; no copy)`.
- Align the `MASTER_PLAN.md` P00A P13 bullet with the Opus register row: early guidelines limited to user/institution-provided documents plus metadata links, with semantic verification as a research lane.
- Record a founder decision in `DONOR_RIGHTS_REGISTER.md` either authorizing public naming of that non-public source, or replacing its name with a neutral label in `COPY_FIRST_SOURCE_PLAN.md`, `MASTER_PLAN.md`, `SOURCE_LEDGER.md` and `FOUNDATION_GAP_AUDIT_2026-10-07.md`.

**R3 (recommended, P2 hygiene; original OPUS-P00-030).**

`PREBUILD_KILL_REVIEW_2026-10-07.md` readiness matrix rows still read `RESOLVED` for:
- rights/licensing (L394);
- decision assurance (L399);
- calibration (L400);
- documents/OCR (L406).

Add one line above the matrix marking it `SUPERSEDED_BY_P00_REPAIR_2026_10_08`. The executive verdict was already superseded.

These are text-only edits that require no new design. After they land, a check that confirms only R1–R2 (and R3 if applied) changed is sufficient. A full re-review is not required.

## 5. Priority checks requested

| Priority | Result |
|---|---|
| Data architecture | Adequate. Per-class placement, backup/export/sync/delete, outbox recovery, rights checkpoints. |
| Vault durability | Adequate. ottari correctly classified as a candidate requiring P02 qualification. MedScale whole-file vault forbidden as canonical. |
| Study/result independence | Adequate. Arms, analyses, results, overlap, review membership and refusal codes are explicit. |
| Decision assurance | Adequate in contract. One vocabulary defect in the thesis (R1). |
| Atomic proof admission | Adequate as a contract. Frozen final-text digest verification, local epoch/rights watermark compared inside the private transaction, assured display only after durable acknowledgement, crash/revocation/replay states, historical vs current separation. No 2PC overclaim. |
| Rights and copy-first | Adequate for the named sources. Residual stale directive (R2). |
| P1 registers | 40 of 41 adequately bound. OPUS-015 needs R2. |
| Local-first / zero mandatory cloud | Adequate. No hosted inference, auth, vector DB, paid API or per-query founder compute is required. Corpus build and distribution cost is explicitly a P03 decision (owner-funded or user/institution-built), not hidden. |
| Initial scope | Adequate. Local CPU-only 16 GB Windows desktop, population-level adult treatment benefit/harm and contradiction questions. Triage, dosing, unsourced DDI, mandatory meta-analysis and percentages are excluded. |

## 6. Verdict

**`P00_RECONCILIATION_NEEDS_MINOR_REPAIR`**

No material P0 remains. Both original Opus P0 findings are closed by reconciliation, and no new P0 was found. 16 of 17 Opus P1 findings are resolved or precisely phase-bound. Repairs R1 and R2 are small, precisely specified documentation edits needed before closeout.

This verdict is not a statement that SafeEvidence is medically validated, clinically safe, compliant, secure or release-ready. It is also not a statement that any contract has been implemented or tested.
