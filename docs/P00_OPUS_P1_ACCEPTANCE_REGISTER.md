# P00 Opus P1 Acceptance Register

Status: `OPEN_PHASE_GATES` (not completed qualification)
Original independent source: `review/opus-p00-kill-review-2026-10-07`;
reviewed base: `136cdffc2cd14133e01018ca56833241dd50bc4e`.

This register binds each original Opus P1 to a named owner, exact phase-entry
gate and objective acceptance evidence. It does not claim the reviewer ran the
new tests or accepted the repair.

| Finding | Binding phase/entry gate | Responsible owner role | Required decision BEFORE affected work | Acceptance evidence |
|---|---|---|---|---|
| OPUS-P00-003 | P02 vault | Storage/security | Choose and verify SQLCipher/WAL lifecycle, ack durability, HMAC/opaque names, native keys before authority slice promotion | Crash/backup/concurrency/restore/key-loss across target OS and donor |
| OPUS-P00-004 | P01 trust ADR; P10 use | Release/security | Freeze role keys, threshold root, offline-clock/stale warning, root rotation and signed release distinction | TUF expired/freeze/rollback/revoked target and synthetic signing key ban |
| OPUS-P00-005 | P02 decision contract; P08 metrics | Clinical safety | Freeze precedence, action caps, reason outcomes, clinical-intent handling, commit mapping and false escalation | Bilingual clinician symptoms/negation + bounded termination and risk coverage |
| OPUS-P00-006 | P08 entry | Decision evaluation | Record exact DAL negative Study-0 metrics, exclude prior PubMedQA contamination and keep learned model challenger-only | Frozen negative artifact ref, truly fresh clinical holdout and deterministic comparator |
| OPUS-P00-007 | RESOLVED_PLANNING | Clinical safety | No V1 user-facing clinical truth percentage; future calibrated identity uses whole pipeline | UI claim audit, holdout and drift tests before any future numeric assurance |
| OPUS-P00-008 | P02 ontology | Evidence science/statistics | Bind arm and observation denominators, analysis populations, effect scope, review membership, registry/report/outcome pair | Multi-report trial, follow-up, pooled analysis, timepoint and multiarm overlap fixtures |
| OPUS-P00-009 | P18 quantitative | Statistician | Freeze supported FE/RE estimands, method defaults, numerical validity, refusal and mature oracle scope | Two/rare/zero event, multiarm, cluster, covariance, DL/PM/HKSJ/metafor comparisons |
| OPUS-P00-010 | P03 corpus | Source ingestion | Select PubMed XML, PMC JATS and resumable bulk ingest parser/adapters with article license mapping | DeleteCitation, CommentsCorrections, retraction, JATS license and failed checksum/restart |
| OPUS-P00-011 | RESOLVED_PLANNING; P12 gate | OCR/security | SafeOCR is a real candidate; re-use its critical-value gate only after exact tests/model rights | Arabic-indic decimal, mg/mcg, signed numeric and matched source crop |
| OPUS-P00-012 | P05 Arabic retrieval | Clinical Arabic lead | Compare multilingual encoder to translate-then-biomedical route; preserve translated query with numeric/negation controls | Arabic/English negation and dose, visible translation, cross-language qrels |
| OPUS-P00-013 | P05/P10/P12 runtime | Runtime/security | Freeze primary ONNX/tensor and LLM runtime candidates, disable default downloads, minimize features | Offline model-load with no network/proxies, measured RSS and dependency feature closure |
| OPUS-P00-014 | P14 FHIR/patient context | Clinical/FHIR | Add MedicationRequest/MedicationStatement/AllergyIntolerance or typed loss; interaction authority requires licensed evidence | Medication-allergy and contraindication unsupported -> ABSTAIN/ESCALATE with reason |
| OPUS-P00-015 | P13 guideline | Guideline and rights owner | Restrict early guidelines to user/institution provided docs plus metadata links; no unqualified private donor disclosure | Jurisdiction/version/issuer/scope, source-rights and semantics vs CQL regression |
| OPUS-P00-016 | P02 snapshots; P03 rights | Privacy/provenance | Use identifier-only public proof references; rights revocation/deletion tombstones and PARTIAL_REPRODUCTION | Expiring license, deleted user file, invalid private sync and stale historical view |
| OPUS-P00-017 | P06 support | Evidence verification | Explicit span relation + source validity + mismatch facets; deterministic numeric/unit checks before AI | Wrong subgroup/timepoint/adjustment/relative-vs-absolute, SOURCE_UNAVAILABLE cases |
| OPUS-P00-018 | P11 shell | Desktop accessibility/legal | No Slint preference until licensing/attribution+security+Arabic/reader benchmark wins | License notice and cross-platform RTL/screenreader/caches/resource report |
| OPUS-P00-019 | P01 evaluation charter | Founder/clinical evaluation lead | Bind adjudicator qualification, compensation or volunteer ethics, sample size/split and gold-label budget before training/promotions | Independent double-review packet, interrater agreement, variance and locked holdout |

## Rule

A requirement remains OPEN_PHASE_GATE until its owner provides the linked,
revision-bound test or decision. If clinical adjudicators, licensed assets,
a qualified runtime or device evidence are unavailable, do not bypass gates.

P00 re-check asks whether these obligations are adequately scoped and binding,
not whether P18 meta-analysis or P15 mobile have been implemented.
