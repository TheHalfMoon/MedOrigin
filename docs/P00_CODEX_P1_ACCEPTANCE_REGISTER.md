# P00 Codex P1 Acceptance Register

Status: `OPEN_PHASE_GATES` (planning requirements, NOT passed tests)
Frozen review base: `136cdffc2cd14133e01018ca56833241dd50bc4e`
Source: `review/codex-p00-kill-review-2026-10-07`.
Reconciliation base: `83561a305cea265845a19535f9808ac92fec623c`.

Every entry below has a decision owner, entry gate, and falsifiable evidence.
Phase-bound means **cannot begin the affected subsystem** without its gate,
not that implementation or clinical qualification is complete.

| Finding | Gate (before affected work) | Owner | Mandatory acceptance contract | Required evidence |
|---|---|---|---|---|
| CODEX-P00-07 | P02; native P15 | Storage/security | Freeze per-OS KEK/DEK, unlocked presence, recovery/rotation, opaque private blob IDs before private authority implementation | Wrong key, reinstallation/restore, stale backup, raw-hash filename and native keychain tests |
| CODEX-P00-08 | P01 trust design; P10 first pack | Release/security | Approve root/targets threshold, key custody, offline trust clock, expiry/rollback/freeze/compromise policy before any signed pack is consumed | Expired/frozen/rollback/root rotation/compromised targets conformance; synthetic key absent from release |
| CODEX-P00-09 | P03 first network adapter | Network/security | Exact query-disclosure, transport+DNS+redirect policy, connection-bound egress scope, OS worker socket denial before first outbound connector | DNS rebinding/proxy/IPv6/redirect/SSRF packet probes, no PHI logs |
| CODEX-P00-10 | P03 ingest | Evidence acquisition | Bind feed watermark, complete ordered baseline/daily replay and rights/lifecycle taxonomy before incremental corpus adoption | Missing/duplicate/out-of-order files, corrected/deleted PubMed XML and stale offline overlay |
| CODEX-P00-11 | P04 design; P05 promotion | Retrieval/evaluation | Approve report+study qrels, source-family/Arabic strata, time/study split and offline model admission before tournament | Study recall, rights exclusions, cross-language queries and zero auto-download |
| CODEX-P00-12 | P02 contract; P06 verifier | Clinical evidence/safety | Define source availability/validity, numeric mismatch facets and precise claim-result support outside applicability before verifier implementation | Wrong numeric/denominator/timepoint/ROI/abstract/fulltext plus SOURCE_UNAVAILABLE cases |
| CODEX-P00-13 | P06 extraction | Extraction/evidence science | Admit typed Result and stage AUTO_PROPOSED/HUMAN_CONFIRMED and worker format/data rights | Arms, events/total, HR/RR/OR, CI, mixed ITT and table/decimal ambiguity |
| CODEX-P00-14 | P18 quantitative promotion | Statistician | Freeze supported estimator/design/refusal matrix and independent metafor or other qualified method oracle before pooling | DL/PM/REML/HKSJ, missing covariance, zero event/multiarm/cluster/crossover refusal fixtures |
| CODEX-P00-15 | P18 review promotion | Review-methods lead | Define search completeness, dual-screen adjudication, human stop rule, residual recall uncertainty and PRISMA counts | Missed tail, disagreement, overlapping studies, protocol change and living-update cases |
| CODEX-P00-16 | P07 appraisal | Clinical methods | Bind study/outcome-level rubric version, review state, span and invalidation semantics before rating | RoB2/ROBINS/QUADAS/AMSTAR mismatch and conflicting adjudicators |
| CODEX-P00-17 | RESOLVED_PLANNING | Clinical safety | V1 prohibits user-facing clinical truth-confidence percentage; future percentage needs independent estimand/holdouts | Scan all V1 UI and claims for percentage; model/pack changes invalidate future estimates |
| CODEX-P00-18 | P07 applicability | Clinical+FHIR | Freeze timestamped context, missingness, jurisdiction and vetted calculator/formula catalog before patient-context promotion | AKI/stale lab, pregnancy, renal function, weight, dose units, tool boundary |
| CODEX-P00-19 | P13 guideline promotion | Guidelines owner | Issuer/version/jurisdiction/semantics and narrative-vs-CQL distinction before guideline authority | Syntax-valid wrong comparator, value-set mismatch, supersession/conflicting issuer |
| CODEX-P00-20 | P12 parsing | Document/security | Pin minimal features and model bytes, deny worker sockets/keys, cap pages/memory/decompression/runtime before untrusted file admission | Offline cold cache, malicious PDF, hang, remote URL, zip-bomb and source-region retention |
| CODEX-P00-21 | RESOLVED_PLANNING; P12 qualification | OCR owner | SafeOCR is live candidate: admit exact source/test revision, never claim clinical qualification by availability | Critical decimal, unit, Arabic digit/negation, wrong crop/patient/table link |
| CODEX-P00-22 | P11 shell selection | Desktop/accessibility | Set OPEN_TOURNAMENT, freeze Slint/Tauri licensing, RTL, screenreader and privacy benchmark | Arabic mixed dose, keyboard reader, Windows/macOS cache/dump and startup RSS |
| CODEX-P00-23 | P15 native | Mobile/security | Specify UniFFI data lifetime, bounded handles/files, native vault custody and OS backup/display posture | Physical iOS/Android low-memory/cancel/lock/reinstall/app preview cases |
| CODEX-P00-24 | P17 sync | Sync/security | Specify expiring enrollment, explicit peer confirmation, revocation/tombstones, rights checks and LAN/relay policy | Bootstrap race/replay, stale/denied grants and interrupted resume |
| CODEX-P00-25 | P02 entry; P21 hardening | Privacy/security | Freeze per-OS allowed residuals/retention, worker minimum context, no PHI CLI paths; redact crash/log/support | PHI canaries in WAL/temp/pagefile/dumps/indexers/backups/support |
| CODEX-P00-26 | P02 source spans; P05/P12 Arabic | Arabic clinical+localization | Choose byte/codepoint/normalized/rendered mappings and isolate bidi identifiers/drug doses before provenance store | Arabic digits/separators, diacritics, negation, mixed script and exact highlights |
| CODEX-P00-27 | P01 evaluation charter; before P04 | Clinical evaluation lead+founder | Approve external adjudicator sourcing/consent, funding plan, gold rubric, double review, sample/split uncertainty protocol | Signed label packet, agreement, subgroup/temporal leakage/holdout custody |
| CODEX-P00-28 | P01 entry | Product+clinical safety | Freeze target user, population-level adult evidence classes, care setting, jurisdictional claim exclusions and acceptable coverage/cost before UX/model promotion | Clinician task scenarios, excluded patient-specific cases, claim-vs-evaluation trace |
| CODEX-P00-29 | P03 entry; P05 budgets | Runtime/distribution owner | Freeze corpus scope, index/model/install/update bytes, builder ownership and no founder-paid backend before pack work | 16GB CPU-only cold install/offline/low-disk, interrupted update and egress cost |
| CODEX-P00-30 | P01 first transplant | Supply-chain/rights | Approve exact slices, dependency features/weights/data/NOTICE, reject executable model formats without isolation | SBOM/license closure, hostile model/plugin/pickle and network-auto-fetch probe |

## Enforcement

Each phase's first PR must link this row, name the exact reviewed SHA, and
attach a corresponding test/decision artifact. If needed reviewer, permission,
device or gold labels are unavailable, the phase is BLOCKED; it does not
auto-waive the gate. No volunteer reviewer, benchmark success, or empirical
performance is asserted by this planning file.

Rows marked RESOLVED_PLANNING only certify the specific planning decision.
Tests and clinical claims remain unqualified.

P01 must create a durable issue/task owner and scope for the rows before the
associated phase is activated. P00 acceptance requires the original reviewers
to confirm the timing and gates are sufficiently explicit.
