# SafeEvidence P00 Genuine Independent Codex Final Re-check

Review date: 2026-10-08 (Asia/Riyadh).
Verdict: **P00_READY_TO_CLOSE**.
Scope: repaired foundation planning contracts. Canonical P00 closure remains pending the distinct reviewer and CI gates below.

## Identity and immutable review boundary

| Item | Evidence |
|---|---|
| Reviewer | OpenAI Codex, the active Codex desktop agent in this session |
| Model | GPT-6, as identified by the session instructions; an exact deployment variant is not exposed and is not invented |
| Exact reviewed product SHA | `9368e09e3e31df3176404e7b2b86b54a6a5aac08` |
| Verified repair branch | `reconcile/p00-opus-minor-repair-2026-10-08` |
| Live repository | `TheHalfMoon/SafeEvidence`; existing renamed repository, not a new repository |
| Main observed during review | `136cdffc2cd14133e01018ca56833241dd50bc4e` |
| Original product review base | `136cdffc2cd14133e01018ca56833241dd50bc4e` |
| Original Codex review branch head | `f41c3ec063e6272a837ffc8ba45231345fc9c0ea` on `review/codex-p00-kill-review-2026-10-07` |
| Original Codex artifact | `docs/reviews/CODEX_P00_INDEPENDENT_KILL_REVIEW_2026-10-07.md`, read from that branch's actual Git object |
| This isolated evidence branch | `review/codex-p00-genuine-final-2026-10-08`, created directly from the reviewed product SHA |

This report was written by Codex. It was not delegated to Claude and is not a Claude-authored artifact presented under a Codex mandate. It is a fresh Codex re-check of the original Codex findings; it does not claim to reproduce the original reviewer process or the interrupted CLI run. The artifact on `review/codex-p00-final-recheck-2026-10-08` at `7bfc2ed2182865fbbb9f3f2b748af4d7816d85ed` is excluded as Codex approval because its disclosed author is Claude Opus 5.5. The account-limited CLI attempt supplies no complete verdict and is not used as approval.

## Method and evidence limitations

A normal clone fetched all repository branches and objects. The exact repair commit was checked out before review on the isolated branch. The original Codex report itself was read, including the original findings, reusable targets and probe limitations; the acceptance register was compared against it rather than substituted for it.

The binding foundation set read directly at the reviewed SHA comprises AGENTS.md, README.md, THIRD_PARTY_NOTICES.md, PRODUCT_THESIS.md, ARCHITECTURE.md, SOURCE_LEDGER.md, COPY_FIRST_SOURCE_PLAN.md, REUSE_FIRST_IMPLEMENTATION_MAP.md, DONOR_TRANSPLANT_PROTOCOL.md, RUNTIME_BUDGET.md, FOUNDATION_GAP_AUDIT_2026-10-07.md, P00_REPAIR_CLOSEOUT_PLAN_2026-10-08.md, all five P00 contract sheets, DONOR_RIGHTS_REGISTER.md, both P1 acceptance registers, P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md, P00_FOUNDATION_DECISIONS_2026-10-07.md, PREBUILD_KILL_REVIEW_2026-10-07.md, MASTER_PLAN.md, GAP_REVIEW.md and P00_REPAIR_CONSISTENCY_CHECK_2026-10-08.md. Live issue #1, GitHub refs, branch rules and exact-commit checks were inspected.

The independent findings and contract assessment were developed before reading the genuine final Opus report. Later, that report was read to verify the distinct reviewer gate and the exact R1/R2/R3 scope. This is a final reconciliation check, so known repair history is explicit rather than a claim of a blind first review.

No architecture research was restarted. Original donor-code observations and probes are historical evidence at their original pins, not newly executed tests. Live heads of ten relevant donor repositories were reverified below; no newer donor implementation is admitted or qualified by that inventory. No source choice in this review depends on assuming a changed donor head is equivalent to its historical pin. The empty import allowlist and pre-import inspection/qualification gates remain binding.

Executed local checks: 26 current foundation Markdown files, zero missing explicit `docs/*.md` references; 24 unique Codex P1 register rows; 17 unique Opus P1 register rows; R1/R2/R3 source markers; no historical non-public guideline-source name in the current foundation set. Direct diff confirms the repair from `d2280cae49fe37c4b3621400788e61f113d83b46` is one normal commit affecting exactly six Markdown files (+46/-17), with no product code.

Jev CLI `2026.919.0` was used for public change-scope classification only. After the sandbox network attempt failed, the authorized network call succeeded: model `jev-1.13.0`, choice `docs`, confidence 1.0, input tokens 349, output tokens 31, latency 574 ms. This is not a medical, architectural or merge approval. No callable Alibaba Open Code Review capability was available. The available Code Review tool supplies PR CI diagnostics and is not Alibaba review. Neither unavailable tooling nor a typed scope classification replaces this direct review.

No Rust/Python product tests, donor suites, crash/power-loss tests, statistical or medical benchmarks, native-device tests, clinical adjudication, legal grant validation or post-merge CI were executed. Local document checks are not GitHub CI. Planning closure does not mean implemented, clinically validated, safe for patient care, compliant, secure or release-ready.

## Complete original Codex P0 assessment

`CLOSED` below means the original foundational planning defect is closed by this independent exact-SHA re-check. Each contract's implementation qualification remains an unpassed phase gate.

| Finding | Disposition | Direct repaired authority and assessment | Remaining implementation evidence |
|---|---|---|---|
| CODEX-P00-01 | CLOSED | P00_DATA_PLACEMENT_CONTRACT: per-object store/rights/backup/export/sync/delete table; private queries and their projections stay private; licensed content is rights-scoped; durable intent/outbox handles cross-store changes without claiming distributed atomicity. Immutable source/rights/version references and PARTIAL_REPRODUCTION prevent unavailable bytes being silently replaced. ARCHITECTURE and foundation D1 agree. | P02/P03 lifecycle traces and replay, grant denial at every transfer boundary; no restricted/private pack bytes. |
| CODEX-P00-02 | CLOSED | P00_VAULT_DURABILITY_CONTRACT chooses persistent SQLCipher/WAL authority, prohibits whole-file MedScale resealing, binds acknowledgement to successful durable COMMIT, treats uncertain outcomes as COMMIT_UNKNOWN, holds ownership through the lifecycle, and defines staged consistent backup/restore and recoverable migrations. No exit seal or lockfile-only ownership is accepted. | Integrated kill/WAL/lock/backup/migration/disk-full/key tests at P02; any acknowledged loss prevents adoption. Native custody must be tested per platform. |
| CODEX-P00-03 | CLOSED | P00_STUDY_INDEPENDENCE_CONTRACT gives report versions, arms, analyses, registered/reported outcomes, results, observations, comparisons/covariance, review membership and overlap explicit identities. Distinct reports/results are not independent participants. Unknown overlap/covariance produces POOLING_REFUSED_UNIT_OF_ANALYSIS unless a qualified method handles dependence. | P02 ontology and P18 qualification fixtures cover protocol, follow-up, multi-arm, mixed populations, repeated outcomes, pooled IPD and overlapping reviews; no unconfirmed extraction becomes an admitted effect. |
| CODEX-P00-04 | CLOSED | P00_DECISION_ASSURANCE_CONTRACT separates ControlAction/TerminalOutcome, gives ordered guards including ASK_MORE before generic ABSTAIN, bounded actions (2 retrieval rounds, 3 tools, one context request), reason codes and commit/non-commit denominators. Unsupported facts cannot be rescued by caution. Lexical symptom triage is disabled in V1. PRODUCT_THESIS section 5 now agrees. | P02/P08 termination/precedence/failure properties and bilingual intent/negation fixtures; clinician gold and learned-policy promotion remain gated. |
| CODEX-P00-05 | CLOSED | DONOR_RIGHTS_REGISTER exact import ledger is empty. Only VERIFIED_ALLOWED exact slices plus notices/transitive review permit import. Founder assertion is not external ownership, alternate grants require documentary rightsholder scope, and copyleft/model/data/terminology/publication rights remain independent. AGENTS, transplant protocol and copy-first corrections enforce this. | P01 signed first-import rows, SBOM/NOTICE and executable/asset admission before any donor bytes; later changes are re-admitted. |
| CODEX-P00-06 | CLOSED | P00_PROOF_ADMISSION_CONTRACT freezes final rendered text and material claims, verifies final exact spans/facets, compares local rights/validity epochs, and stores answer/proof/claim decisions/audit in one private transaction before assured display. Draft streaming is segregated and cannot copy/export as assured. Epoch races must fail or invalidate before current-assured display; historical proof does not assert offline global freshness. | P02/P06/P10 crash, retraction/revocation, text-change, disk-full, idempotency and stale-replica tests; current assurance rechecked on view/export/sync/resume. |

Totals: **6 CLOSED, 0 PARTIALLY_CLOSED, 0 STILL_OPEN, 0 REGRESSED**.
New P0: **none found** in the defined planning review scope.

## All 24 original Codex P1 dispositions

Each row was compared with its original finding. Owner roles are accountability requirements, not assertions that a person has accepted appointment. The registers require durable task/issue owners before activation, exact-revision first-PR evidence, and BLOCKED behavior when rights, reviewers, devices or gold labels are unavailable. A future test is not counted as passed.

| Finding | Disposition | Owner and gate | Original failure addressed and required evidence |
|---|---|---|---|
| CODEX-P00-07 | PRECISELY_PHASE_BOUND | Storage/security; P02, native P15 | Platform KEK/DEK/user-presence/rotation/recovery and opaque private blob IDs; wrong key, stale backups, reinstall and real protector tests. Vault custody contract supplies the early boundary. |
| CODEX-P00-08 | PRECISELY_PHASE_BOUND | Release/security; P01 trust design before any signed-pack consumption | Root/targets thresholds, custody, offline time, expiry/freeze/rollback/compromise and synthetic-key exclusion; TUF conformance. The row's P10 label cannot postpone its explicit before-any-signed-pack condition to after P03/P05. Foundation D9 also prohibits earlier unqualified consumption. |
| CODEX-P00-09 | PRECISELY_PHASE_BOUND | Network/security; P03 first outbound adapter | Exact disclosed query, DNS/redirect/proxy/connection-bound IP policy plus OS worker socket denial; SSRF/rebinding/IPv6 packet probes and no PHI logs. Host parsing remains distinct from confinement. |
| CODEX-P00-10 | PRECISELY_PHASE_BOUND | Evidence acquisition; before P03 ingest | Ordered complete baseline/daily replay, watermark and lifecycle taxonomy; missing/duplicate/out-of-order update, deletion/correction and stale-overlay fixtures. Deleted citation is not implicitly scientific retraction. |
| CODEX-P00-11 | PRECISELY_PHASE_BOUND | Retrieval/evaluation; P04 design/P05 promotion | Report/study qrels, source/language/rights strata and grouped temporal split before tournament; study recall and cross-language/no-download cases. MedCPT remains a candidate rather than an interchangeable unpaired encoder or winner. |
| CODEX-P00-12 | PRECISELY_PHASE_BOUND | Clinical evidence/safety; P02 contract/P06 verifier | Orthogonal availability/validity, precise claim-result support and deterministic numeric mismatch facets; wrong denominator/timepoint/region, abstract/full-text and SOURCE_UNAVAILABLE fixtures. Applicability cannot erase support failure. |
| CODEX-P00-13 | PRECISELY_PHASE_BOUND | Extraction/evidence science; P06 | Typed Result, AUTO_PROPOSED/HUMAN_CONFIRMED and worker/data/format rights; arms/events/denominators, HR/RR/OR/CI, mixed ITT and ambiguous table/decimal tests. PICO/direction research code is not a complete numeric extractor. |
| CODEX-P00-14 | PRECISELY_PHASE_BOUND | Statistician; before P18 pooling | Supported estimator/design/default/refusal matrix and mature independent oracle; DL/PM/REML/HKSJ, nonfinite/negative output, covariance, zero events, multi-arm/cluster/crossover cases. statsmodels stays restricted, and unsupported pooling is refused. |
| CODEX-P00-15 | PRECISELY_PHASE_BOUND | Review-methods lead; P18 promotion | Search completeness, dual-screen adjudication, human stop and residual recall uncertainty, PRISMA report/study counts; missed-tail, protocol-change/disagreement/overlap/living-update fixtures. Budget stop never establishes exhaustive completion. |
| CODEX-P00-16 | PRECISELY_PHASE_BOUND | Clinical methods; P07 before rating | Versioned design/result-specific rubric, reviewer state, spans and invalidation; RoB2/ROBINS/QUADAS/AMSTAR mismatch, conflicting raters and changed input. No universal quality score or perpetual confirmation badge. |
| CODEX-P00-17 | RESOLVED | Clinical safety; V1 planning prohibition | No clinical truth-confidence percentage across thesis/architecture/master/contracts. Future percentages need their own estimand, separate holdouts and full-pipeline invalidation. DAL negative prior remains binding; UI and qualification tests are still required before shipping. |
| CODEX-P00-18 | PRECISELY_PHASE_BOUND | Clinical+FHIR; P07 applicability | Timestamped context/missingness/jurisdiction and vetted formula catalog before patient-context promotion; stale lab/AKI, pregnancy, renal status, weight, dose/units and tool-boundary tests. Initial wedge excludes unqualified patient-specific calculations. |
| CODEX-P00-19 | PRECISELY_PHASE_BOUND | Guidelines owner; P13 promotion | Issuer/version/jurisdiction and narrative versus executable semantics; wrong comparator/value set/supersession/conflicting issuer. Early guideline inputs are rights-admitted user/institution documents or public metadata links. R2 removes the unqualified donor instruction. |
| CODEX-P00-20 | PRECISELY_PHASE_BOUND | Document/security; before P12 parsing | Feature/model pinning, no sockets/keys, bounded hostile-input resource/deadline contract; cold offline cache, malicious file, hang, remote resource, zip-bomb and retained source regions. Reuse engines after qualification; no new parser framework. |
| CODEX-P00-21 | RESOLVED | OCR owner; planning correction, P12 qualification still open | SafeOCR is consistently a real critical-value donor candidate. Exact source/tests/model rights and decimal/unit/Arabic/negation/crop/patient/table fixtures remain required. Availability supplies neither clinical fidelity nor independence of correlated OCR reads. |
| CODEX-P00-22 | PRECISELY_PHASE_BOUND | Desktop/accessibility; before P11 shell selection | OPEN_TOURNAMENT, Slint/Tauri rights/attribution, RTL/screenreader/privacy/startup/RSS evidence. Native appearance is not a privacy guarantee. |
| CODEX-P00-23 | PRECISELY_PHASE_BOUND | Mobile/security; P15 native | UniFFI ownership/lifetimes and bounded handles/file-backed inputs, native custody and backup/display posture; physical iOS/Android low-memory/cancel/lock/reinstall/preview cases. Bridge parity is not native-device proof. |
| CODEX-P00-24 | PRECISELY_PHASE_BOUND | Sync/security; P17 | Expiring single-use enrollment, explicit peer confirmation, revocation/tombstones, grant checks on send/receive and explicit relay policy; race/replay/stale-grant/interrupted-resume fixtures. No immediate erasure guarantee for offline peers. |
| CODEX-P00-25 | PRECISELY_PHASE_BOUND | Privacy/security; P02 entry, P21 hardening | Early per-OS retention/residual boundary and minimum worker context; no PHI CLI paths, redacted logs/support and canaries in WAL/temp/swap/dumps/indexers/backups. Late hardening cannot defer the early privacy design. |
| CODEX-P00-26 | PRECISELY_PHASE_BOUND | Arabic clinical+localization; P02 coordinates, P05/P12 Arabic | Byte/codepoint/normalized/rendered mappings and bidi dose/identifier isolation before spans; Arabic digits/separators/diacritics/negation/mixed-script/exact-highlight fixtures. Original text survives normalization. |
| CODEX-P00-27 | PRECISELY_PHASE_BOUND | Clinical evaluation lead+founder; P01 charter before P04 | Qualified external adjudicators, consent/funding, rubric, independent double review, sample/split uncertainty and holdout custody; signed label packet/agreement/leakage checks. Unavailable adjudication blocks promotion; model gold cannot substitute. |
| CODEX-P00-28 | PRECISELY_PHASE_BOUND | Product+clinical safety; P01 entry, before UX/model promotion | Adult population-level benefit/harm/contradiction research wedge is now explicit. Exact question cohort/setting/jurisdiction/acceptable coverage/cost still need owner approval and clinician task/exclusion/claims trace before affected work. The broad roadmap is not the initial claim. |
| CODEX-P00-29 | PRECISELY_PHASE_BOUND | Runtime/distribution owner; before P03, P05 budgets | Bounded corpus/install/index/model/build/update bytes and builder/distribution ownership; CPU-only 16 GB cold offline/low-disk/interrupted-update/egress-cost evidence. Local-first does not imply cost-free corpus generation or distribution. |
| CODEX-P00-30 | PRECISELY_PHASE_BOUND | Supply-chain/rights; P01 first transplant | Exact code/features/weights/data/NOTICE and executable model admission before any import; SBOM/license closure, hostile plugin/pickle and auto-fetch probes. Empty VERIFIED_ALLOWED ledger prevents source availability becoming import authority. |

Totals: **2 RESOLVED, 22 PRECISELY_PHASE_BOUND, 0 INSUFFICIENTLY_BOUND, 0 REGRESSED**. These are planning dispositions. All associated implementation tests and first-import approvals remain outstanding.

## Opus register cross-check and three direct corrections

The genuine Opus final re-check is `docs/reviews/OPUS_P00_FINAL_RECHECK_2026-10-08.md` on `review/opus-p00-final-recheck-2026-10-08` at branch head `93f7f16ba1b679756f199d0d83a227b770bc41e1`, authored as Claude Opus 5.5. Its reviewed product SHA is **d2280cae49fe37c4b3621400788e61f113d83b46**, and its verdict is P00_RECONCILIATION_NEEDS_MINOR_REPAIR. Its two original P0 were closed; its unresolved P1 was the guideline/non-public-source conflict. It explicitly permits a targeted R1/R2/R3 confirmation rather than another full re-review. It is genuine Opus evidence, but is not approval of 9368e09e by its original reviewer.

Direct inspection at 9368e09e confirms:

- **R1 corrected:** PRODUCT_THESIS section 5 defines RETRIEVE_EVIDENCE/USE_TOOL/REQUEST_CONTEXT as ControlAction, the complete eight-state TerminalOutcome vocabulary, disabled V1 EMERGENCY_NOTICE and the binding decision-contract reference. Architecture and master plan agree.
- **R2 corrected:** COPY_FIRST_SOURCE_PLAN section 11 makes the non-public unqualified research source REFERENCE_ONLY with no code copy/adaptation/readiness. MASTER_PLAN P00A limits early guidelines to rights-admitted user/institution documents and metadata links; semantic verification stays research-only. SOURCE_LEDGER and FOUNDATION_GAP_AUDIT use a neutral label. No name remains in the current foundation set. The conditional generic reuse row in REUSE_FIRST_IMPLEMENTATION_MAP does not authorize this donor: exact rights admission and the specific reference-only restriction control. Historical branches/commits still exist; no erasure claim or history rewrite is made.
- **R3 corrected:** the PREBUILD_KILL_REVIEW internal readiness matrix is explicitly SUPERSEDED_BY_P00_REPAIR_2026_10_08, and says its RESOLVED entries do not close independent findings or certify code, copying or clinical capability.

Codex's independent cross-check of every original Opus P1 is:

| Original Opus ID | Codex disposition of repaired planning requirement | Basis |
|---|---|---|
| OPUS-P00-003 | PRECISELY_PHASE_BOUND | P02 durability/custody contract, integrated crash/backup/key qualification. |
| OPUS-P00-004 | PRECISELY_PHASE_BOUND | P01 trust ADR and before-use trust condition; TUF and synthetic-key exclusion. |
| OPUS-P00-005 | RESOLVED | Binding state/precedence/caps/metrics contract and R1; P02/P08 tests unpassed. |
| OPUS-P00-006 | PRECISELY_PHASE_BOUND | Deterministic incumbent and negative prior are fixed; exact DAL metric packet/fresh holdout required before P08. |
| OPUS-P00-007 | RESOLVED | No V1 clinical percentage; future full-pipeline calibration gate. |
| OPUS-P00-008 | RESOLVED | Typed study/result/overlap/refusal planning semantics; P02/P18 tests unpassed. |
| OPUS-P00-009 | PRECISELY_PHASE_BOUND | P18 method/default/refusal matrix and mature statistical oracle. |
| OPUS-P00-010 | PRECISELY_PHASE_BOUND | P03 PubMed/JATS rights, ordered replay and correction/delete/checksum fixtures. |
| OPUS-P00-011 | RESOLVED | Real SafeOCR candidate correction; P12 rights and Arabic critical-field tests unpassed. |
| OPUS-P00-012 | PRECISELY_PHASE_BOUND | P05 bilingual retrieval/translation/numeric-negation qrels. |
| OPUS-P00-013 | PRECISELY_PHASE_BOUND | P05/P10/P12 one-primary-runtime, feature closure, offline/no-network/resource tests. |
| OPUS-P00-014 | PRECISELY_PHASE_BOUND | P14 medication/allergy fields or explicit typed loss; unqualified interaction refusal. |
| OPUS-P00-015 | PRECISELY_PHASE_BOUND | P13 narrative/source-rights/issuer/jurisdiction/semantic gate and direct R2 correction. |
| OPUS-P00-016 | RESOLVED | Historical identity/tombstone/PARTIAL_REPRODUCTION and current invalidation semantics. |
| OPUS-P00-017 | PRECISELY_PHASE_BOUND | P06 support facets/deterministic checks/source-unavailable cases. |
| OPUS-P00-018 | PRECISELY_PHASE_BOUND | P11 unranked shell rights/accessibility/privacy/resource tournament. |
| OPUS-P00-019 | PRECISELY_PHASE_BOUND | P01 founder/clinical charter, ethics/funding/labels/splits; blocked if unavailable. |

Totals in this Codex cross-check: **5 RESOLVED, 12 PRECISELY_PHASE_BOUND, 0 INSUFFICIENTLY_BOUND, 0 REGRESSED**. These are not new Opus sign-offs or an alteration of Opus's original report.

## New findings, regressions and remaining defects

No new P0 or insufficiently bound original P1 was found. There is no remaining R1/R2/R3 source repair required at this SHA. Named clinical/rights/platform qualifications remain unproven; this is intentional phase gating, not a downgrade of P0 severity.

Nonblocking historical cleanup persists: the foundation audit's old repository-slug note and donor pin/path drift identified as CODEX-P00-36. Live SafeEvidence identity is verified, and pre-import exact-pin/path/license/test verification prevents those historical discovery values from authorizing bytes. CODEX-P00-31 through 35 remain P2 refinements in the original review (FHIR loss, safe diagnostics, voice confirmation, typed source qualification and projection authority), carried by the relevant master-plan phases and contracts. They are not falsely reported as implemented or newly tested.

Two closure evidence gates are currently missing, separate from architecture acceptance:

1. **Distinct Opus exact-head confirmation:** GAP_REVIEW and the repair plan require both reviewers to independently re-check the same repaired head. The genuine Opus report targets the prior SHA and requests corrections. Codex can verify the corrections but cannot author an Opus approval. Smallest next action: genuine Claude/Opus targeted R1/R2/R3 confirmation explicitly naming 9368e09e, its original P0/P1 carry-forward and any new P0. No full architecture review or named-reviewer policy change is needed.
2. **Exact-head and post-merge CI evidence:** GitHub returns no workflow runs, zero check runs and zero status contexts on 9368e09e; combined status is pending with total_count 0. The tree has no CI workflow. Main is unprotected, branch-protection GET returned 404 and repository rulesets are empty. Those facts are not passing CI or permission to bypass the repair plan's exact-head CI condition. Smallest next action after the review gate is satisfied: provision a bounded documentation consistency/review-evidence check on the proposed merge head and inspect its actual result; qualify the workflow and resulting changed head through the existing review process. Then use a normal merge commit and verify main/CI before issue closure. Local checks alone do not satisfy the GitHub gate.

No separate founder-only P00 merge approval was found in the repository rules; the user's current request authorizes normal merge after the documented gates. Founder/clinical/rights approvals of the P01 intended-use/evaluation charter and exact donor rows remain required at their owning boundaries. They have not been fabricated or waived.

## Foundation coverage matrix

The states below assess planning coverage at the reviewed SHA. Deferred entries all remain bounded by original finding IDs, named owner roles and acceptance registers.

| Dimension | Planning coverage state | Owner / phase and evidence |
|---|---|---|
| Product | CHALLENGED_AND_DEFERRED_WITH_OWNER | Product+clinical, P01; CODEX-28 exact intended-use charter within the fixed adult population research wedge. |
| Clinical safety | CHALLENGED_AND_DEFERRED_WITH_OWNER | Clinical safety, P02/P08/P20; bounded outcomes/no triage/no action authority; CODEX-04/12/18/27. |
| Evidence science | CHALLENGED_AND_RESOLVED | Study/result/participant-independence planning contract; implementation at P02/P18 remains gated. |
| Retrieval | CHALLENGED_AND_DEFERRED_WITH_OWNER | Retrieval/evaluation, P04/P05; CODEX-11 study/report/language/rights qrels and candidate tournaments. |
| Claim/citation verification | CHALLENGED_AND_DEFERRED_WITH_OWNER | Clinical evidence/safety, P02/P06; CODEX-12/13 orthogonal support and typed extraction fixtures. |
| Decision assurance | CHALLENGED_AND_RESOLVED | Control/terminal precedence, action bounds, non-commit/commit reasons and disabled V1 emergency classification. |
| Calibration | CHALLENGED_AND_RESOLVED | No clinical percentage in V1; any future metric requires CODEX-17/27 qualification and full-pipeline scope. |
| Guidelines | CHALLENGED_AND_DEFERRED_WITH_OWNER | Guidelines/rights, P13; CODEX-19/OPUS-15, R2 reference-only donor and narrative-first source authority. |
| Documents/OCR | CHALLENGED_AND_DEFERRED_WITH_OWNER | Document/security/OCR, P12; CODEX-20/21 narrow workers and critical medical fields. |
| Interoperability/patient context | CHALLENGED_AND_DEFERRED_WITH_OWNER | Clinical+FHIR, P07/P14; CODEX-18/31 and OPUS-14 context freshness, explicit subset/loss and no writes. |
| Vault/storage | CHALLENGED_AND_RESOLVED | Persistent SQLCipher/WAL lifecycle and per-object placement chosen as contracts; P02 integrated qualification still required. |
| Privacy | CHALLENGED_AND_DEFERRED_WITH_OWNER | Privacy/security, P02 then P21; CODEX-07/25 permitted OS residuals, keys, private projections and canary evidence. |
| Security | CHALLENGED_AND_DEFERRED_WITH_OWNER | Security/release/network, P01/P03/P10/P21; CODEX-08/09/30 trust, confinement and transitive executable admission. |
| Desktop | CHALLENGED_AND_DEFERRED_WITH_OWNER | Desktop/accessibility, P11; CODEX-22 measured Slint/Tauri OPEN_TOURNAMENT. |
| Mobile | CHALLENGED_AND_DEFERRED_WITH_OWNER | Mobile/security, P15/P16; CODEX-23 native protector/FFI/device qualification. |
| Pairing/sync | CHALLENGED_AND_DEFERRED_WITH_OWNER | Sync/security, P17; CODEX-24 grant/enrollment/revocation/relay/resume fixtures. |
| Arabic/i18n | CHALLENGED_AND_DEFERRED_WITH_OWNER | Arabic clinical/localization, P02/P05/P12; CODEX-26/OPUS-12 coordinate, concept, digit, negation and bidi fidelity. |
| Accessibility | CHALLENGED_AND_DEFERRED_WITH_OWNER | Desktop/accessibility and mobile, P11/P15; CODEX-22/23 real readers, focus and RTL evidence. |
| Performance/resources | CHALLENGED_AND_DEFERRED_WITH_OWNER | Runtime/distribution, P03/P05/P10/P12/P15; CODEX-29 measured CPU-only 16 GB and device/resource budgets. |
| Provenance/licenses | CHALLENGED_AND_RESOLVED | Empty deny-by-default exact import allowlist, per-slice rights/notice/model/data separation; P01 signed admissions remain mandatory. |
| Benchmarks/statistics | CHALLENGED_AND_DEFERRED_WITH_OWNER | Clinical evaluation/founder/statistician/review methods, P01/P18/P20; CODEX-14/15/27 actual gold, split, covariance/refusal and uncertainty. |
| Release/update/recovery | CHALLENGED_AND_DEFERRED_WITH_OWNER | Release/security/storage, P01/P02/P10/P22; CODEX-02/08/30 durable recovery and qualified TUF trust before use. |
| Regulatory/claims | CHALLENGED_AND_RESOLVED | Research/clinical/release claims are separate; no clinical-validation/device/compliance/superiority claim is admitted by planning closure. |
| Cost/zero-cloud assumptions | CHALLENGED_AND_DEFERRED_WITH_OWNER | Runtime/distribution/product/founder, P01/P03; CODEX-27/29 label/build/distribution costs explicit, no mandatory founder-paid runtime/cloud. |

Study-level synthesis is also explicitly challenged: the independence contract fixes ontology, and statistician/review-methods owners retain P18 refusal, completeness, multiplicity and method qualification gates.

## Live donor-head inventory

Observed on 2026-10-08 using GitHub's current default-branch commit endpoint. These are discovery observations only, not reviewed/admitted source slices. Changed heads must be inspected at the owning transplant before adoption, with the original review's historical pins preserved.

| Repository | Observed live SHA |
|---|---|
| TheHalfMoon/MedScale | `37f5ae8a965c1e49d961010c3135a5b5dde12d67` |
| TheHalfMoon/ottari | `73706029849bcbe51243624e37f03a1969dc74ca` |
| TheHalfMoon/DAL | `81da6c58bdc2d67e888c78bedac9e25f02070eb3` |
| TheHalfMoon/commandMed | `51f73ec05750137e5bd94ffa0765f6383f475fee` |
| AbdulazizShehri/SafeOCR | `d2e2ea815b17a7a3f0e59ce43dbdd160966e73a4` |
| maziyarpanahi/openmed | `ea920f36fadd7b45935247d639f0ffa1ef493b23` |
| xberg-io/xberg | `af3f243cca94205de42dfc78a636d8f11340f38b` |
| docling-project/docling.rs | `6e1689c555002349bf86868733e8b3801ea323cc` |
| anush008/fastembed-rs | `916bd37f2bb4cad2b2f47a6a966643d5f42d883d` |
| mozilla/uniffi-rs | `2588c486ac7d6cf191511ac24147d7b541ce64e5` |

The P01-P10 reuse decisions remain explicit in the copy plan, reuse map and original review: governance/provenance patterns, SQLCipher/qualified donor custody, immutable source/lifecycle patterns, FTS5 baseline, existing local encoder/reranker runtime, source-backed verifier/extraction oracles, official rubrics/context contracts, commandMed mechanics/DAL evaluation, existing calibration metrics and local pack/generator machinery. Generic database/crypto/vector/parser/FFI/statistical frameworks are not scheduled for unnecessary greenfield construction. Original GF01-GF08 are bounded SafeEvidence integration semantics; an actual implementation still needs its GREENFIELD_JUSTIFIED record and inspected alternatives at the owning grain. No code reuse is authorized by this report alone.

## Verdict and authorized next boundary

**P00_READY_TO_CLOSE** is the independent Codex planning verdict for **9368e09e3e31df3176404e7b2b86b54a6a5aac08**: all 6 original P0 closed, all 24 original P1 resolved or precisely phase-bound, no new P0 found, R1/R2/R3 verified directly.

This verdict is not canonical closure, a GitHub approving review, an Opus sign-off or passing CI. Publish this genuine evidence normally, prepare pending closeout and the first bounded P01 grain, obtain the missing targeted Opus exact-head confirmation and exact-head CI, merge through a normal merge commit only after gates pass, verify post-merge main/CI, then close issue #1. **P01 implementation is not authorized until that canonical P00 closure is confirmed.** No additional full review loop is required solely because these two recorded evidence gates are missing.
