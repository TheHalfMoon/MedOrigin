# SafeEvidence: Final P00 Closeout Re-check (Codex review mandate)

Review date: 2026-10-08. Verdict: **`P00_READY_TO_CLOSE`**.

## 0. Identity and scope

- Reviewed branch: `reconcile/p00-opus-minor-repair-2026-10-08`.
- Exact reviewed SHA: `9368e09e3e31df3176404e7b2b86b54a6a5aac08`. The live remote
  branch head matched this SHA when the review was performed.
- Live `main`: `136cdffc2cd14133e01018ca56833241dd50bc4e`. This matches the
  original frozen review base and is an ancestor of the reviewed SHA. `main` is
  unchanged.
- Original review compared against:
  `review/codex-p00-kill-review-2026-10-07` →
  `docs/reviews/CODEX_P00_INDEPENDENT_KILL_REVIEW_2026-10-07.md`.
  That review contains 6 P0, 24 P1, 5 P2 and 1 P3 findings.
- Opus re-check consulted only to locate R1–R3:
  `review/opus-p00-final-recheck-2026-10-08`. Each Opus conclusion was checked
  again directly against the reviewed tree.
- Diff `main..9368e09`: 26 files, all Markdown under `docs/` or at the repository
  root. No product code, build files or binaries were added.

**Reviewer identity disclosure.** This re-check was produced by Claude
(Opus 5.5) under the Codex final-reviewer mandate. It was not produced by the
OpenAI Codex agent that wrote the original review. Repository governance
(`MASTER_PLAN.md` "P00 closes only after Codex and Opus independently re-check"
and `P00_CODEX_P1_ACCEPTANCE_REGISTER.md` "original reviewers to confirm") names
distinct reviewers. The founder must decide whether this artifact satisfies the
Codex leg. The technical findings below do not depend on that decision.

**Method limits.** This review covers document consistency and contract
adequacy only. No donor, vault, statistical, OCR, security, native-platform or
clinical test was executed. Every contract is treated as a binding design and
gate, not as implemented or qualified capability.

## 1. Original Codex P0 dispositions

| Finding | Binding repair | Verification against the original failure mode | Status |
|---|---|---|---|
| CODEX-P00-01 data planes | `P00_DATA_PLACEMENT_CONTRACT.md` | The per-object table assigns every original object class (public metadata/full text, institution-licensed content, user PDF/OCR, patient/question history, private query embeddings, global index, packs, EvidenceSnapshot, AnswerArtifact+proof, validity overlay) to a store with backup/export/sync/deletion semantics. Private query-derived indexes stay private. The contract states that public visibility is not permission to redistribute and does not claim cross-plane 2PC. A durable PREPARED/ADMITTED/FAILED outbox and rights checks at ingest, index, pack-build, export, backup and sync send/receive are present. The acceptance walk matches the original verification requirement. Corpus scope is bounded and is not set to the whole of PubMed. | **CLOSED** |
| CODEX-P00-02 vault durability | `P00_VAULT_DURABILITY_CONTRACT.md` | MedScale whole-file decrypt/edit/reseal is rejected as canonical. AGENTS, ARCHITECTURE, MASTER_PLAN, SOURCE_LEDGER and REUSE map all agree. The contract defines a persistent SQLCipher/WAL store with one logical writer. It acknowledges a write only after COMMIT under a tested durability profile, and explicitly states that a checkpoint is not an acknowledgement barrier. It adds a COMMIT_UNKNOWN state, writer guard across open/txn/close, no live-file backup, staged validated atomic backup publish, quiesced restore with the prior DB retained, and journaled migrations. The P02 fault-injection suite covers every step the original named, and any acknowledged loss blocks adoption. | **CLOSED** (P02 qualification pending) |
| CODEX-P00-03 study/result independence | `P00_STUDY_INDEPENDENCE_CONTRACT.md` | The contract adds typed identities for Study, Report/Version, Arm, Analysis, Outcome (registered vs reported), Result, ArmObservation, Comparison, EffectEstimate, ReviewIncludedStudyLink, ParticipantOverlapGroup (CONFIRMED/POSSIBLE/UNKNOWN), ReportVersionLink and SynthesisInputDecision. It states that different reports, timepoints, subgroups, pooled IPD or reviews are not independent studies. Pooling is refused (`POOLING_REFUSED_UNIT_OF_ANALYSIS`) unless independence or covariance is qualified. Machine links stay PROPOSED. The fixture list covers every original double-counting scenario. | **CLOSED** |
| CODEX-P00-04 decision contract | `P00_DECISION_ASSURANCE_CONTRACT.md` | ControlAction and TerminalOutcome are separate types, with exactly one terminal outcome per request. The 7-guard precedence is deterministic and evaluated after bounded actions. ASK_MORE is ordered before ABSTAIN, so clarification stays reachable. Action caps are 2 retrieval rounds and 3 tool calls, and one REQUEST_CONTEXT ends the request (no loop). Reason codes form a closed set. Commit, unsafe-commit, useful-coverage, over-abstention and false-escalation denominators are defined. Lexical EMERGENCY is disabled in V1, and negation and clinician-question fixtures are required in both languages. A population answer with unresolved applicability can be issued through ANSWER_WITH_CAUTION, and unsupported claims are always refused. | **CLOSED** |
| CODEX-P00-05 rights boundary | `DONOR_RIGHTS_REGISTER.md`; COPY_FIRST §1; TRANSPLANT §11; AGENTS | The founder assertion is preserved, but it no longer authorizes copying. Separate bases cover code, models, data, terminology, publications and assets. The exact-slice ledger is EMPTY (`NO_ADMISSIONS`). Only VERIFIED_ALLOWED plus notices plus transitive review permits copying, and asserted grants are deny-for-copy. Trialstreamer is reference-only, RobotReviewer/Signthos are not relicensed to Apache, and the Slint license must be selected. The contract states that worker separation does not waive obligations, and contributor ownership is required for founder-owned code. P01 needs a signed per-component row. The original blanket wording ("no longer a blocker") no longer appears in the canonical docs. | **CLOSED** |
| CODEX-P00-06 atomic proof admission | `P00_PROOF_ADMISSION_CONTRACT.md` | The contract defines the state machine DRAFT_PRIVATE→…→COMMITTED/REJECTED. The manifest binds the final rendered text digest, source bytes/spans, rights version and validity epoch. Final displayed claims are verified, with no silent repair. Answer, manifest, per-claim outcomes and audit are written in one private transaction, and the assured UI shows the answer only after durable acknowledgement. An epoch race either fails before commit or invalidates the result before current display. Historical bytes stay immutable while current-validity overlays can change. V1 withholds drafts by default, and segregated drafts cannot be copied, exported or shared. Adversarial race and crash tests match the original verification list. | **CLOSED** |

**Original P0: 6 closed, 0 remaining.**

## 2. R1–R3 verification (commit `9368e09`)

The commit changes 6 Markdown files (+46/−17).

- **R1 FIXED.** `PRODUCT_THESIS.md` §5 now lists ControlAction
  {RETRIEVE_EVIDENCE, USE_TOOL, REQUEST_CONTEXT} and TerminalOutcome {ANSWER,
  ANSWER_WITH_CAUTION, ASK_MORE, CONFLICT, ABSTAIN, ESCALATE, BLOCKED,
  EMERGENCY_NOTICE}. These are identical to `P00_DECISION_ASSURANCE_CONTRACT.md`,
  `ARCHITECTURE.md` (two blocks) and `MASTER_PLAN.md` P08. The section states that
  EMERGENCY_NOTICE is disabled in V1 and that commitment requires atomic proof
  admission, and it points to the contract. The thesis (authority rank #3) no
  longer contradicts the binding contract.
- **R2 FIXED.** `git grep -i protocolwise` over the reviewed tree returns zero
  hits. The guideline row in `COPY_FIRST_SOURCE_PLAN.md` §11 is now
  REFERENCE_ONLY with no copy, adaptation or readiness claim. The `MASTER_PLAN.md`
  P13 bullet now matches OPUS-P00-015: user- or institution-provided documents
  plus metadata links, CQL as syntax/execution reference only, and semantic
  verification as research-only. `SOURCE_LEDGER.md` and `FOUNDATION_GAP_AUDIT`
  use a neutral label. This meets the "neutral label" option of R2, so no
  separate founder naming decision is required. The name remains in git history
  and in prior review branches. History rewriting is prohibited, so this is
  recorded as a disclosure limitation, not a defect.
- **R3 FIXED.** The `PREBUILD_KILL_REVIEW` readiness matrix is now headed
  `SUPERSEDED_BY_P00_REPAIR_2026_10_08`, and the header explicitly denies that
  its RESOLVED rows close independent findings or authorize copying.
- **No new contradiction introduced.** The new P13 wording agrees with
  CODEX-P00-19 and OPUS-P00-015. The new thesis wording agrees with every other
  state vocabulary instance. No contract file was modified by the commit.

## 3. Codex P1 dispositions (24)

Every row in `P00_CODEX_P1_ACCEPTANCE_REGISTER.md` has an owner role, an entry
gate placed no later than the first affected work, a decision contract and
falsifiable evidence. These requirements trace to the original
PROPOSED_RESOLUTION and VERIFICATION_REQUIRED fields. The enforcement clause
blocks a phase rather than waiving its gate, and requires the first PR to link
the row and the exact SHA.

| Finding | Disposition | Gate check |
|---|---|---|
| 07 key custody/blob privacy | PHASE_BOUND | P02 (+P15 native); also embedded in vault contract §Key and blob custody |
| 08 pack trust | PHASE_BOUND | P01 design; condition "before any signed pack is consumed" also covers P03 pack import |
| 09 broker confinement | PHASE_BOUND | P03 first outbound connector |
| 10 lifecycle completeness | PHASE_BOUND | P03 ingest |
| 11 retrieval strata/language | PHASE_BOUND | P04 design / P05 promotion |
| 12 multidimensional support | PHASE_BOUND | P02 contract / P06 verifier |
| 13 quantitative extraction | PHASE_BOUND | P06; Result typing already in study contract |
| 14 meta-analysis methods | PHASE_BOUND | P18; refusal matrix + independent oracle |
| 15 review completeness | PHASE_BOUND | P18 |
| 16 result/design appraisal | PHASE_BOUND | P07 |
| 17 no V1 percentage | RESOLVED_PLANNING | Consistent across AGENTS, THESIS, ARCH, MASTER_PLAN, contracts |
| 18 temporal context/tools | PHASE_BOUND | P07 (earlier than P14) |
| 19 guideline semantics | PHASE_BOUND | P13; reinforced by R2 |
| 20 parser features | PHASE_BOUND | P12 |
| 21 SafeOCR donor | RESOLVED_PLANNING + P12 qualification | No "empty" description remains |
| 22 desktop shell | PHASE_BOUND | P11 OPEN_TOURNAMENT |
| 23 FFI/mobile custody | PHASE_BOUND | P15 |
| 24 pairing/sync | PHASE_BOUND | P17; Signthos REFERENCE_ONLY |
| 25 platform exposure | PHASE_BOUND | P02 entry (earliest private-data phase) + P21; enforcement re-links per affected phase |
| 26 Arabic coordinates | PHASE_BOUND | P02 source spans; P05/P12 |
| 27 human gold resourcing | PHASE_BOUND | P01 evaluation charter, before P04 |
| 28 intended-use wedge | PHASE_BOUND (partially decided) | PRODUCT_THESIS initial scope; P01 approves taxonomy |
| 29 distribution/pack COGS | PHASE_BOUND | P03 entry; P05 budgets |
| 30 transitive admission | PHASE_BOUND | P01 first transplant; rights ledger empty |

**P1: 2 resolved (planning), 22 precisely phase-bound, 0 insufficient.**
P2/P3 findings 31–36 do not block closure. P3-36 (pin drift) is handled by the
requirement in the rights ledger to record a full SHA and digest for each
admission.

## 4. Search for new P0 and regressions

Checks performed against the reviewed tree:

- Vault: every reference to `EncryptedVault` is now a rejection or a superseded
  historical path list. `REUSE_FIRST_IMPLEMENTATION_MAP.md` L107 explicitly
  supersedes L84.
- Rights: no canonical file restores blanket copy authority, and every
  founder-assertion paragraph ends in a per-source admission requirement.
- State vocabulary: no remaining standalone `EMERGENCY` terminal in authority
  docs (see O1).
- Percentages: every mention is a prohibition or a future-gated condition.
- Proof: the data-placement table and proof contract agree (one private
  transaction; PARTIAL_REPRODUCTION on missing bytes).
- Precedence: ARCHITECTURE §Canonical P00 contract references and
  MASTER_PLAN §P00 repaired-contract precedence state that contracts supersede
  older narrative.
- Fabrication: the repair documents explicitly disclaim executed tests, legal
  grants, clinical validation and release readiness.

**New P0: none. Material regressions: none.**

Non-blocking observations (no repair required for closeout):

- **O1 (P3 hygiene).** `COPY_FIRST_SOURCE_PLAN.md` L124 still reads
  "ASK_MORE/ABSTAIN/ESCALATE/EMERGENCY behavior | commandMed | COPY tests + port
  only trusted runtime". `SOURCE_LEDGER.md` L33 describes commandMed's own donor
  vocabulary, which is accurate as a donor description. L124 is an older donor
  hypothesis that the explicit contract-precedence clauses override (AGENTS §P00
  repair authority; MASTER_PLAN §P00 repaired-contract precedence). Its "only
  trusted runtime" qualifier already excludes the disabled lexical emergency
  path. Optionally edit it to read "EMERGENCY_NOTICE (disabled in V1) fixtures
  only" when P01 next touches that file.
- **O2 (governance).** See the reviewer identity disclosure in §0.

## 5. Final verdict

**`P00_READY_TO_CLOSE`**

All 6 original Codex P0 findings are closed by binding contracts. All 24 Codex
P1 findings are resolved at planning level or precisely phase-bound, with owner,
gate and evidence. R1, R2 and R3 are fixed without new contradictions. No new P0
or material regression was found.

The foundation may proceed to a normal-merge (no squash, rebase or force-push)
P00 closeout of `reconcile/p00-opus-minor-repair-2026-10-08`, followed by P01
implementation under the acceptance-register gates. This assumes the founder
accepts this artifact as the Codex leg (O2).

This verdict is not a statement that SafeEvidence is clinically safe, medically
validated, regulatorily compliant, secure or release-ready. It also does not
state that any contract has been implemented or tested.
