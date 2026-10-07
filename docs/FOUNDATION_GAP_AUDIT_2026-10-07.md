# SafeEvidence Foundation Gap Audit — 2026-10-07

Status: `P00_OPEN_GAPS`

This audit re-checks the foundation after the SafeEvidence rename and the
reuse-first amendment. It focuses on gaps that could still cause unnecessary
greenfield work, unsafe evidence behavior, architectural lock-in, or misleading
clinical confidence.

## Executive verdict

The core thesis is strong: local-first evidence retrieval, exact source
provenance, claim support verification, explicit conflict, and calibrated
abstention are the correct differentiators.

The plan is **not yet implementation-freeze complete**. The major missing pieces
are not another LLM or RAG framework. They are:

1. a concrete evidence-update/retraction lifecycle;
2. item-level rights and redistribution semantics;
3. a promoted biomedical retrieval benchmark lane;
4. a concrete scientific claim-verification lane;
5. a defined calibration estimand/holdout protocol;
6. standards alignment for evidence objects;
7. systematic-review screening/dedup for Deep Review;
8. mobile Rust↔Swift/Kotlin binding strategy;
9. secure pack/application update metadata;
10. explicit donor-transplant and runtime anti-sprawl controls.

Two new binding documents close the process gaps:

- `docs/DONOR_TRANSPLANT_PROTOCOL.md`
- `docs/RUNTIME_BUDGET.md`

## P0 gaps

### SE-G001 — Evidence lifecycle is not concrete enough

**Failure mode:** an answer snapshot can contain an article that is later
corrected/retracted, while SafeEvidence has no authoritative update overlay.

**Resolution:**

```text
PubMed annual baseline
 + ordered daily updates
 + PMC/Europe PMC OA full text
 + Crossref metadata
 + Crossref Retraction Watch
        ↓
CanonicalPublicationIdentity
        ↓
CurrentValidityOverlay
        ↓
immutable historical AnswerSnapshot
```

PubMed updates must apply revised/deleted citations in order. Historical answer
snapshots remain immutable, but opening an old answer must show current
retraction/correction/supersession warnings.

**Sources:**

- NLM PubMed baseline + daily update files;
- PMC Open Access article datasets with per-article licenses;
- Europe PMC REST/OAI/bulk OA routes;
- Crossref REST metadata;
- Crossref Retraction Watch dataset/API.

**Reuse:** `API_ADAPTER / DATA_PIPELINE / REFERENCE`.

### SE-G002 — Rights model needs item-level export/sync semantics

Current source classes are not enough to decide whether bytes may move from
desktop to phone, be included in a pack, be exported, or be shared.

Add:

```text
content_rights
metadata_rights
local_index_allowed
local_fulltext_allowed
same_user_device_sync_allowed
institution_scope
redistribution_allowed
commercial_use_allowed
derivative_use_allowed
license_uri
license_snapshot
rights_checked_at
```

PMC explicitly warns that not every PMC article permits text mining/reuse and
OA licenses vary per article.

**Sources:** PMC OA license metadata, Crossref license metadata, EBMonFHIR
rights/free-to-share concepts.

### SE-G003 — Claim-support verification lacks a concrete promotion lane

P06 defines the behavior but not the development/evaluation stack.

Promote a verifier tournament:

```text
deterministic lexical/span checks
        vs
small NLI classifier
        vs
MultiVerS/SciFact research oracle
        vs
local LLM structured verifier
```

Required labels:

```text
SUPPORTS
PARTIALLY_SUPPORTS
CONTRADICTS
DOES_NOT_ESTABLISH
UNRESOLVED
```

**Sources:**

- SciFact claims/rationales and evaluation code;
- SciFact-Open for open-domain scientific verification;
- MultiVerS as a research implementation/oracle, not default runtime;
- HealthFC only as a research comparator where its non-commercial/no-derivatives
  data terms permit the exact use.

SafeEvidence ultimately needs a clinician-adjudicated biomedical claim/span
holdout because scientific fact-checking datasets do not prove clinical answer
support.

### SE-G004 — Displayed confidence has no frozen estimand

Before any percentage is shown, define exactly:

```text
P(material answer claim is adequately supported by the admitted evidence
  | SafeEvidence pipeline, target population, and evaluation protocol)
```

Do not calibrate "truth" from model softmax.

Use separate development/calibration/final holdouts. Report Brier, ECE/NLL,
reliability, selective risk, coverage, and subgroup/temporal shift.

**Sources:** DAL existing metrics/selective code; scikit-learn calibration;
MAPIE/conformal risk-control only as a challenger after assumptions are checked.

### SE-G005 — Donor extraction could still create a Frankenstein codebase

Resolved procedurally by `DONOR_TRANSPLANT_PROTOCOL.md`.

Specific correction: do not copy the current MedScale storage crate wholesale.
Extract the smallest coherent vault/keys/source slice and bring later security
fixes/tests.

### SE-G006 — Project license/notice baseline was missing

Resolved in this review:

- root `LICENSE`: Apache-2.0;
- `THIRD_PARTY_NOTICES.md`: created;
- third-party code/model/data terms remain independently tracked.

### SE-G007 — Secure update/rollback metadata is underspecified

SafeEvidence signs/adopts packs, but distribution needs freeze/rollback/key-
compromise protection beyond a single digest.

Use TUF semantics for:

- application updates;
- model packs;
- evidence packs;
- terminology packs;
- trust-root rotation/revocation.

**Candidates:** `awslabs/tough`, `theupdateframework/rust-tuf`, TUF
conformance suite.

Do not preselect `tough`: current 2026 compatibility issues with some modern
TUF roots mean it must pass a SafeEvidence/TUF conformance qualification first.
`rust-tuf` is also explicitly beta. TUF is the required security model; the
Rust implementation remains a tournament.

### SE-G008 — SafeOCR donor status changed after the original audit

`AbdulazizShehri/SafeOCR` was later verified by both independent reviews as
non-empty and containing a critical-value verification implementation and
tests. The earlier empty-repository statement is superseded.

SafeOCR is now a donor candidate, not a clinically qualified component.

Use SafeOCR as a bounded critical-value verification donor candidate alongside:
- Xberg/docling.rs for document parsing;
- qualified OCR backends/models;
- OpenMed offset/document tests where useful.

SafeEvidence owns the critical medical OCR benchmark for decimals, doses, units,
lab values, negation, tables, Arabic/Latin mixtures, and source-region lineage.

## P1 gaps

### SE-G009 — Biomedical retrieval candidate missing: MedCPT

Add NCBI MedCPT to P05.

MedCPT provides a biomedical query encoder, article encoder and cross-encoder
reranker trained from PubMed search behavior. Do not assume it wins in 2026;
benchmark it against Qwen3/BGE-family candidates.

**Benchmark sources:**

- BEIR TREC-COVID;
- BEIR NFCorpus;
- BioASQ where terms allow;
- SafeEvidence clinical query set;
- SYNERGY for systematic-review retrieval/screening.

### SE-G010 — Deep Review lacks a proven screening/dedup workflow

Use ASReview as a code/pattern donor or isolated research worker for
human-in-the-loop screening. Use SYNERGY as a benchmark for sparse inclusion
retrieval.

SafeEvidence must preserve reviewer decisions, inclusion/exclusion reasons and
stopping-rule evidence. Active learning never silently declares the review
complete.

### SE-G011 — Evidence schema risks reinventing standards

SafeEvidence should keep a compact internal canonical schema, but map it against
HL7 Evidence Based Medicine on FHIR.

EBMonFHIR provides profiles/concepts for:

- publication/citation records;
- Evidence/EvidenceVariable;
- RiskOfBias;
- CertaintyOfEvidence;
- ArtifactAssessment;
- recommendation rating/justification;
- rights/free-to-share metadata.

**Decision:** `REFERENCE / EXPORT_ADAPTER / SCHEMA_CROSSWALK`, not a requirement
to store the entire internal database as FHIR.

### SE-G012 — Guideline execution needs a reference validator

ProtocolWISE remains the SafeEvidence-specific verification research source.

Add the official CQL toolchain as an external validator/reference worker:

- `cqframework/clinical_quality_language`;
- CQL-to-ELM;
- CQL engine / FHIR utilities;
- `cqf-tooling` where needed.

Do not make a Java server mandatory. Use it for conformance and bounded
guideline validation unless a measured product workflow requires more.

### SE-G013 — Mobile FFI strategy was not frozen

Promote Mozilla UniFFI as the default candidate for the shared Rust core to
Swift/Kotlin boundary.

Benefits:

- generated Swift and Kotlin bindings;
- production use in Mozilla products;
- keeps native UI while sharing SafeEvidence semantics.

Because UniFFI is MPL-2.0 and not yet 1.0, use it as a dependency with exact
versioning and covered-file obligations reviewed; do not fork it into
SafeEvidence casually.

### SE-G014 — Desktop shell decision should exploit existing native donor code

The plan still treats Tauri/React as a generic candidate. Re-evaluate against
MedScale's existing Slint-based native desktop patterns.

Run a focused shell spike:

```text
Slint native
vs
Tauri/React
```

Measure privacy surfaces, accessibility, startup/RAM, developer velocity,
rendering quality, and platform packaging.

Neither Slint nor Tauri is a preferred or qualified shell. Both remain unranked
candidates in an OPEN_TOURNAMENT requiring licensing, accessibility,
Arabic/bidi, privacy residuals, startup/RAM and packaging evidence.

### SE-G015 — Query privacy during public evidence search is underspecified

A remote PubMed/Europe PMC search can disclose the clinical question even if no
patient record is uploaded.

Provide two modes:

```text
LOCAL_PACK_SEARCH
  query never leaves device

EXPLICIT_ONLINE_DISCOVERY
  show destination + exact query disclosure
  strip patient identifiers/context by default
```

Evidence pack updates should prefer generic/bulk update channels over
patient-specific remote queries.

### SE-G016 — Terminology pack strategy needs concrete open baselines

Promote:

- MeSH for biomedical query expansion/indexing;
- UCUM for units;
- NLM public-domain RxNorm normalized concepts where usable;
- licensed RxNorm/UMLS content only behind explicit license gates.

Do not treat a free download as unrestricted redistribution.

### SE-G017 — Trial registry linkage is not integrated into evidence identity

Add ClinicalTrials.gov study identifiers/status snapshots to study identity.
Published papers should link to NCT identifiers when available.

Use registry status as context/provenance, not proof of trial results.

### SE-G018 — Document parser choice is still too broad

P12 must run one medical-document tournament and choose one primary engine:

```text
Xberg
vs
docling.rs
```

PaddleOCR may remain an OCR backend. The default app must not ship multiple
large overlapping parser stacks without a measured reason.

### SE-G019 — Arabic evaluation needs datasets, not only a requirement

Create SafeEvidence-owned synthetic/curated challenge sets for:

- Arabic/English code switching;
- drug names and transliteration;
- decimal separators;
- units;
- negation;
- RTL citation navigation;
- Arabic query -> English evidence retrieval;
- Arabic document OCR.

Public datasets can supplement this, but final safety cases need
SafeEvidence-specific clinician-reviewed fixtures.

### SE-G020 — Current validity and historical reproducibility need two views

Do not mutate old answers when evidence changes.

Store:

```text
HistoricalSnapshot
CurrentValidityOverlay
```

The user can reproduce what the system knew at answer time and also see that a
source has since been retracted/corrected/superseded.

## New source promotion table

| Source | Gap filled | Disposition |
|---|---|---|
| NLM PubMed baseline/daily | canonical citation updates/deletes | DATA_ADAPTER |
| PMC OA datasets | rights-aware reusable full text | DATA_ADAPTER |
| Europe PMC | OA/full-text/metadata alternate acquisition | DATA_ADAPTER |
| Crossref Retraction Watch | retraction/update overlay | DATA_ADAPTER |
| NCBI MedCPT | biomedical retrieval/rerank challenger | MODEL/BENCHMARK |
| BEIR | retrieval evaluation framework/datasets | BENCHMARK |
| SciFact / SciFact-Open | claim-support/rationale evaluation | BENCHMARK / CODE_REFERENCE |
| MultiVerS | scientific verifier research oracle | WORKER/BENCHMARK_ONLY |
| ASReview | deep-review screening workflow | WORKER/COPY_BOUNDED |
| SYNERGY | systematic-review inclusion benchmark | BENCHMARK |
| HL7/ebm | evidence/citation/assessment schema crosswalk | STANDARD/REFERENCE |
| CQL/CQF tooling | guideline conformance validator | WORKER/REFERENCE |
| Mozilla UniFFI | Rust↔Swift/Kotlin bindings | DEPEND |
| TUF spec + Rust candidates | signed update/freeze/rollback defense | STANDARD / QUALIFY |
| MeSH | query expansion/biomedical terminology | DATA_PACK |
| RxNorm | drug normalization under exact terms | DATA_PACK / RIGHTS_GATED |
| Tantivy | large lexical-index challenger if FTS5 loses | DEPEND/BENCHMARK |

## P00 freeze requirements added by this audit

P00 cannot close until:

1. SE-G001 through SE-G008 are resolved in canonical docs or have an explicit
   blocking owner;
2. P03 source adapters define update/delete/retraction semantics;
3. P05 benchmarks MedCPT and at least one general modern embedding/reranker;
4. P06 has a concrete verifier dataset/oracle/human-adjudication plan;
5. P09 defines the confidence estimand and frozen split policy;
6. the internal Evidence schema has an EBMonFHIR crosswalk decision;
7. mobile FFI has a selected candidate and rejection fallback;
8. default desktop shell has an evidence-backed selection plan;
9. update security is bound to TUF semantics or an explicitly stronger
   alternative;
10. every P01-P10 greenfield component has passed the donor-transplant gate.

## Product identity note

The canonical product name is **SafeEvidence**. The GitHub repository slug
remains `TheHalfMoon/MedOrigin` until separately renamed; repository content
must use SafeEvidence as the product name.


## Independent-review supersession

This foundation audit remains useful historical context but is no longer the
highest P00 authority. Independent Codex and Claude/Opus reviews found
additional P0/P1 gaps.

Canonical current authority:
- `docs/P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md`
- `docs/P00_FOUNDATION_DECISIONS_2026-10-07.md`
- `docs/DONOR_RIGHTS_REGISTER.md`
