# P01 P1-Gate Tracker — All Original Independent Findings

Date: 2026-10-08. Status: **OPEN_OWNER_ASSIGNMENT**.
This is a traceability/index record, not a clinical approval or claim that
implementation tests passed.

Main P01 tracking issue: https://github.com/TheHalfMoon/SafeEvidence/issues/3
Clinical charter gate: https://github.com/TheHalfMoon/SafeEvidence/issues/4
Rights/pack trust gate: https://github.com/TheHalfMoon/SafeEvidence/issues/5

Every row maps one original P1 ID to its prior phase-entry constraint, owner
**role** (not an appointed named approver), objective evidence, and provisional
durable issue. Do not start a dependent phase unless an individual owner,
ID-specific task and actual acceptance artifacts are assigned and verified.
An unassigned role makes its affected phase BLOCKED.

| ID | Original phase entry | Unappointed owner role | Tracking issue | State | Required objective evidence |
|---|---|---|---|---|---|
| CODEX-P00-07 | P02; native P15 | Storage/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Wrong key, reinstallation/restore, stale backup, raw-hash filename and native keychain tests |
| CODEX-P00-08 | P01 trust design; P10 first pack | Release/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Expired/frozen/rollback/root rotation/compromised targets conformance; synthetic key absent from release |
| CODEX-P00-09 | P03 first network adapter | Network/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | DNS rebinding/proxy/IPv6/redirect/SSRF packet probes, no PHI logs |
| CODEX-P00-10 | P03 ingest | Evidence acquisition | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Missing/duplicate/out-of-order files, corrected/deleted PubMed XML and stale offline overlay |
| CODEX-P00-11 | P04 design; P05 promotion | Retrieval/evaluation | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Study recall, rights exclusions, cross-language queries and zero auto-download |
| CODEX-P00-12 | P02 contract; P06 verifier | Clinical evidence/safety | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Wrong numeric/denominator/timepoint/ROI/abstract/fulltext plus SOURCE_UNAVAILABLE cases |
| CODEX-P00-13 | P06 extraction | Extraction/evidence science | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Arms, events/total, HR/RR/OR, CI, mixed ITT and table/decimal ambiguity |
| CODEX-P00-14 | P18 quantitative promotion | Statistician | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | DL/PM/REML/HKSJ, missing covariance, zero event/multiarm/cluster/crossover refusal fixtures |
| CODEX-P00-15 | P18 review promotion | Review-methods lead | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Missed tail, disagreement, overlapping studies, protocol change and living-update cases |
| CODEX-P00-16 | P07 appraisal | Clinical methods | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | RoB2/ROBINS/QUADAS/AMSTAR mismatch and conflicting adjudicators |
| CODEX-P00-17 | RESOLVED_PLANNING | Clinical safety | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Scan all V1 UI and claims for percentage; model/pack changes invalidate future estimates |
| CODEX-P00-18 | P07 applicability | Clinical+FHIR | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | AKI/stale lab, pregnancy, renal function, weight, dose units, tool boundary |
| CODEX-P00-19 | P13 guideline promotion | Guidelines owner | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Syntax-valid wrong comparator, value-set mismatch, supersession/conflicting issuer |
| CODEX-P00-20 | P12 parsing | Document/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Offline cold cache, malicious PDF, hang, remote URL, zip-bomb and source-region retention |
| CODEX-P00-21 | RESOLVED_PLANNING; P12 qualification | OCR owner | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Critical decimal, unit, Arabic digit/negation, wrong crop/patient/table link |
| CODEX-P00-22 | P11 shell selection | Desktop/accessibility | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Arabic mixed dose, keyboard reader, Windows/macOS cache/dump and startup RSS |
| CODEX-P00-23 | P15 native | Mobile/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Physical iOS/Android low-memory/cancel/lock/reinstall/app preview cases |
| CODEX-P00-24 | P17 sync | Sync/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Bootstrap race/replay, stale/denied grants and interrupted resume |
| CODEX-P00-25 | P02 entry; P21 hardening | Privacy/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | PHI canaries in WAL/temp/pagefile/dumps/indexers/backups/support |
| CODEX-P00-26 | P02 source spans; P05/P12 Arabic | Arabic clinical+localization | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Arabic digits/separators, diacritics, negation, mixed script and exact highlights |
| CODEX-P00-27 | P01 evaluation charter; before P04 | Clinical evaluation lead+founder | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Signed label packet, agreement, subgroup/temporal leakage/holdout custody |
| CODEX-P00-28 | P01 entry | Product+clinical safety | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Clinician task scenarios, excluded patient-specific cases, claim-vs-evaluation trace |
| CODEX-P00-29 | P03 entry; P05 budgets | Runtime/distribution owner | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | 16GB CPU-only cold install/offline/low-disk, interrupted update and egress cost |
| CODEX-P00-30 | P01 first transplant | Supply-chain/rights | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | SBOM/license closure, hostile model/plugin/pickle and network-auto-fetch probe |
| OPUS-P00-003 | P02 vault | Storage/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Crash/backup/concurrency/restore/key-loss across target OS and donor |
| OPUS-P00-004 | P01 trust ADR; P10 use | Release/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | TUF expired/freeze/rollback/revoked target and synthetic signing key ban |
| OPUS-P00-005 | P02 decision contract; P08 metrics | Clinical safety | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Bilingual clinician symptoms/negation + bounded termination and risk coverage |
| OPUS-P00-006 | P08 entry | Decision evaluation | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Frozen negative artifact ref, truly fresh clinical holdout and deterministic comparator |
| OPUS-P00-007 | RESOLVED_PLANNING | Clinical safety | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | UI claim audit, holdout and drift tests before any future numeric assurance |
| OPUS-P00-008 | P02 ontology | Evidence science/statistics | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Multi-report trial, follow-up, pooled analysis, timepoint and multiarm overlap fixtures |
| OPUS-P00-009 | P18 quantitative | Statistician | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Two/rare/zero event, multiarm, cluster, covariance, DL/PM/HKSJ/metafor comparisons |
| OPUS-P00-010 | P03 corpus | Source ingestion | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | DeleteCitation, CommentsCorrections, retraction, JATS license and failed checksum/restart |
| OPUS-P00-011 | RESOLVED_PLANNING; P12 gate | OCR/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Arabic-indic decimal, mg/mcg, signed numeric and matched source crop |
| OPUS-P00-012 | P05 Arabic retrieval | Clinical Arabic lead | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Arabic/English negation and dose, visible translation, cross-language qrels |
| OPUS-P00-013 | P05/P10/P12 runtime | Runtime/security | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Offline model-load with no network/proxies, measured RSS and dependency feature closure |
| OPUS-P00-014 | P14 FHIR/patient context | Clinical/FHIR | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Medication-allergy and contraindication unsupported -> ABSTAIN/ESCALATE with reason |
| OPUS-P00-015 | P13 guideline | Guideline and rights owner | [#5](https://github.com/TheHalfMoon/SafeEvidence/issues/5) | OPEN — owner unassigned | Jurisdiction/version/issuer/scope, source-rights and semantics vs CQL regression |
| OPUS-P00-016 | P02 snapshots; P03 rights | Privacy/provenance | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Expiring license, deleted user file, invalid private sync and stale historical view |
| OPUS-P00-017 | P06 support | Evidence verification | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | Wrong subgroup/timepoint/adjustment/relative-vs-absolute, SOURCE_UNAVAILABLE cases |
| OPUS-P00-018 | P11 shell | Desktop accessibility/legal | [#3](https://github.com/TheHalfMoon/SafeEvidence/issues/3) | OPEN — owner unassigned | License notice and cross-platform RTL/screenreader/caches/resource report |
| OPUS-P00-019 | P01 evaluation charter | Founder/clinical evaluation lead | [#4](https://github.com/TheHalfMoon/SafeEvidence/issues/4) | OPEN — owner unassigned | Independent double-review packet, interrater agreement, variance and locked holdout |

Coverage checks: **24 Codex IDs CODEX-P00-07..30; 17 Opus IDs
OPUS-P00-003..019; 41 unique IDs total**. Named accountable
approvers verified: **zero**. Signed source imports: **zero**.

Consult `docs/P00_CODEX_P1_ACCEPTANCE_REGISTER.md` and
`docs/P00_OPUS_P1_ACCEPTANCE_REGISTER.md` for the complete binding decisions.
Do not treat original `RESOLVED_PLANNING` dispositions as passed software tests.
