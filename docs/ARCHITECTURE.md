# SafeEvidence Architecture

Status: `FOUNDATION_DRAFT`

## 1. Architectural objective

Build a local-first clinical evidence system in which source custody, retrieval, evidence verification, decision assurance, calibration, document processing, patient context, and presentation are explicit modules with narrow trust boundaries.

The system must remain useful without a SafeEvidence backend and must never treat model output, vector similarity, graph projection, or fluent synthesis as clinical authority.

## 2. Top-level shape

```text
                         SafeEvidence Core (Rust)
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
          v                       v                       v
     Desktop Client          iOS Client              Android Client
  Tauri/React candidate    Swift/SwiftUI          Kotlin/Compose
          |                       |                       |
          +-----------------------+-----------------------+
                                  |
                         SafeEvidence contracts
                                  |
        +-------------+-----------+----------+-------------+
        |             |                      |             |
        v             v                      v             v
   Evidence       Decision              Document/OCR    Network
   Workers        Workers               Workers         Broker
        |             |                      |             |
        +-------------+----------+-----------+-------------+
                                  |
                            Local Vault
```

Clients are presentation surfaces. They do not become evidence authority by owning UI state.

## 3. Trust zones

### Trusted core

Owns:

- canonical source identities and custody metadata;
- evidence snapshots;
- answer/claim records;
- explicit patient-context fields supplied or admitted;
- policy and behavioral-state transitions;
- pack admission state;
- durable audit/event records;
- disclosure/export decisions;
- cryptographic key references and storage contracts.

Trusted core should not receive unrestricted network capability.

### Rebuildable projections

Examples:

- FTS/BM25 index;
- vector index;
- evidence graph projection;
- caches;
- UI materialized views;
- generated summaries.

A projection may be deleted and rebuilt from canonical source-backed state. It does not silently become truth.

### Bounded workers

Examples:

- local LLM generation;
- embeddings/reranking;
- typed decision models;
- OCR/document parsing;
- ASR later;
- external validators.

Workers receive bounded inputs, no vault master key, no unrestricted DB handle, and no ambient network unless their specific capability requires it.

Worker results are proposals/evidence artifacts. Core admission decides what is durable.

### Network broker

All external acquisition/connector traffic goes through an explicit broker boundary. The core does not silently open sockets.

Requests should carry:

```text
actor/principal
purpose
destination
method/path
source class
data classification
patient-context egress classification
credential handle
size/time limits
redirect/DNS policy
```

No patient data or query history is sent merely because evidence update networking is enabled.

## 4. Canonical data concepts

### SourceArtifact

Immutable or versioned evidence source identity.

```text
source_id
source_type
external identifiers (DOI/PMID/PMCID/etc.)
content_digest
source_version
publication/update date
retrieval date
rights/access class
correction/retraction/supersession state
local blob reference
```

### EvidenceSpan

A precise reference into a source.

```text
evidence_span_id
source_id
page/section/paragraph/table/cell coordinates where available
character/token offsets when stable
bounding region for visual sources
extracted text digest
extractor/parser identity
OCR confidence where applicable
```

### Claim

```text
claim_id
claim_kind
claim_text
support_refs[]
contradict_refs[]
support_state
applicability_state
human_review_state
```

Support states include at least:

```text
SUPPORTS
PARTIALLY_SUPPORTS
CONTRADICTS
DOES_NOT_ESTABLISH
UNRESOLVED
SOURCE_UNAVAILABLE
```

### EvidenceSnapshot

Binds an answer/deep-review to the exact source set, versions, retrieval plan, ranking identities, and rights scope used at the time.

### PatientContext

Only explicit admitted context is used for applicability. Unknown remains unknown.

Candidate fields include:

```text
age
sex
pregnancy
weight
renal status
hepatic status
conditions
medications
allergies
relevant labs
jurisdiction
care setting
```

The structure must remain extensible and provenance-aware rather than becoming a second EHR schema.

### AnswerArtifact

Binds question, claims, source spans, contradictions, evidence profile, missing context, decision result, model/runtime identities, and calibration identity.

## 4A. Study-level evidence model

SafeEvidence distinguishes a source/report from the underlying study.

Canonical additions:

```text
Study
StudyReportLink
OutcomeDefinition
EffectEstimate
ReviewProtocol
SynthesisProtocol
SynthesisResult
```

A single Study may link to multiple SourceArtifact records. Retrieval, appraisal,
and synthesis must not count multiple reports of the same study as independent
studies.

Study/report linkage is evidence-bearing and may be exact, proposed, confirmed,
overridden, or unresolved. Registry identifiers, publication identifiers,
investigators, sites, intervention details, sample size, and dates may support
linkage, but ambiguous fuzzy matches require review.

EffectEstimate records are source-span backed and preserve outcome definition,
timepoint, analysis population, comparison, effect measure, estimate,
uncertainty, and transformation provenance.

Deep Review owns ReviewProtocol and optional quantitative synthesis. Meta-analysis
is never mandatory when pooling is inappropriate.

## 5. Question pipeline

```text
raw question
   -> intent + ambiguity check
   -> PICO/PICOTS representation where applicable
   -> terminology normalization/expansion
   -> patient-context requirement analysis
   -> retrieval plan
```

Missing clinical details are not silently inferred. The pipeline may return `ASK_MORE` before retrieval when required.

## 6. Retrieval architecture

Default V1 is layered and local:

```text
scope filter
 -> exact/identifier lookup
 -> FTS/BM25 candidates
 -> optional semantic candidates
 -> optional guideline/source-family candidates
 -> fusion
 -> local reranker
 -> diversity/authority/recency constraints
 -> evidence resolver
```

Principles:

- lexical search works without model inference;
- semantic/vector retrieval is optional and benchmark-gated;
- source authority and relevance are distinct;
- source permissions scope caches/indexes;
- retracted/corrected/superseded sources remain visible with explicit state;
- no vector server is required for the default local product;
- retrieval snapshots are reproducible.

## 7. Decision assurance

Decision assurance is not the language model deciding whether it feels confident.

Candidate inputs:

```text
retrieval coverage
source-family coverage
missing required patient context
source freshness
contradiction state
directness/applicability
citation-support coverage
guideline conflict
worker availability
```

Typed control and terminal outcomes:

```text
ControlAction = RETRIEVE_EVIDENCE | USE_TOOL | REQUEST_CONTEXT
TerminalOutcome = ANSWER | ANSWER_WITH_CAUTION | ASK_MORE | CONFLICT |
                  ABSTAIN | ESCALATE | BLOCKED | EMERGENCY_NOTICE
```

The terminal precedence, finite action budgets, reason codes and commit
metrics are binding in `docs/P00_DECISION_ASSURANCE_CONTRACT.md`.
EMERGENCY_NOTICE is disabled in V1 absent separate qualified policy; symptom
substrings are never a triage gate.

Model-assisted typed decisions may contribute, but deterministic rules may override them when a frozen policy/tool applies.

A decision model never receives authority to mutate patient data, prescribe, order, or bypass policy.

## 8. Calibration

SafeEvidence must not expose raw model probability as medical truth.

Separate calibration targets may include:

- evidence sufficiency;
- claim-support correctness;
- answer-supported-by-evidence probability;
- abstention correctness;
- patient-applicability classification.

Each displayed calibrated probability records:

```text
calibrator identity
training/calibration benchmark identity
applicable domain/population
sample size
calibration date
metrics
known shift limits
```

No calibrated score is valid outside its measured scope by default.

## 9. Evidence appraisal

Evidence profile dimensions should remain inspectable rather than collapsed prematurely:

- study design;
- risk of bias;
- consistency;
- directness;
- precision;
- magnitude/effect uncertainty;
- population match;
- intervention/comparator match;
- outcome match;
- recency;
- guideline/jurisdiction relevance;
- contradiction;
- correction/retraction state.

Formal GRADE equivalence must not be claimed unless that exact implementation has been independently validated for the claim.

## 10. Synthesis

The local generative model is a renderer/synthesizer over admitted evidence, not a source of medical truth.

The synthesis request should include bounded evidence and explicit missing/conflict states. Post-generation verification checks material claims before presentation.

If the generator adds an unsupported high-consequence claim, the answer must be repaired, downgraded, or rejected.

## 11. Guideline engine

Guidelines are modeled as versioned, jurisdiction-aware evidence objects rather than generic PDFs.

Candidate representation includes:

```text
issuer
title/version/date
jurisdiction
population
recommendation identifier
recommendation text/span
stated strength/certainty
criteria/conditions
contraindications/exclusions
supersession state
rights/access class
```

Generated computable logic remains separate from source meaning and requires verification. Compilation or schema validity is necessary but not sufficient proof of semantic correctness.

## 12. Document and OCR architecture

### Document IR

Parsers output a SafeEvidence-owned IR:

```text
Document
 -> Section/Page/Slide/Sheet
    -> Block
       -> Heading
       -> Paragraph
       -> List
       -> Table -> Row -> Cell
       -> Figure/Image/Chart
       -> Formula
       -> Annotation
```

Objects carry source digest, page/region, extracted representation, parser/OCR identity, confidence, and relationships.

### Hostile-input boundary

Untrusted documents are quarantined before parsing. Defenses include bounded size/page/decompression limits, path traversal protection, active-content denial, external-resource controls, parser isolation, cancellation, and resource budgets.

### Critical medical OCR

Generic OCR confidence is not enough for:

- doses;
- decimal points;
- units;
- medication names;
- negation;
- lab values;
- dates/times.

Critical fields require cross-checking/second-pass validation or explicit uncertainty. A disagreement may produce a null/unresolved field rather than an invented value.

## 13. FHIR and patient-context interoperability

FHIR is an interchange boundary, not the SafeEvidence canonical database.

V1 direction:

- bounded local FHIR R4 import;
- explicit supported-resource/profile matrix;
- source-preserving mapping;
- unsupported/loss report;
- read-only patient-context extraction;
- local export where justified;
- provenance preserved through round trip.

SMART/NPHIES/live connectors are separately qualified future adapters. No write-back, prescribing, order placement, or autonomous clinical effect is implied.

## 14. Local vault

Target properties:

- transactional local metadata store;
- encrypted sensitive metadata at rest;
- encrypted immutable blobs/assets;
- OS-backed secure key custody where available;
- explicit unlock/recovery design;
- bounded backup/restore with manifests;
- deletion/tombstone propagation to projections/caches;
- crash-safe migration and recovery;
- one authoritative writer per vault or an explicitly qualified multi-writer design.

A future storage implementation must prove actual WAL/temp/crash/cache behavior rather than inferring privacy from an encryption library name.

## 15. Desktop architecture

Desktop is the full product. Tauri 2 + React is a candidate, not a constitutional requirement.

The shell must be benchmarked/qualified for:

- startup/memory;
- accessibility;
- keyboard/focus behavior;
- offline installation;
- secure storage integration;
- file open/save and drag/drop;
- clipboard behavior;
- WebView cache/storage;
- crash dumps;
- screenshots/app previews;
- update path;
- PHI leakage tests.

If the shell cannot meet the privacy contract, the shell changes; the privacy contract does not.

## 16. Mobile architecture

Shared correctness-sensitive behavior should live in Rust where practical, but platform-native integration is first-class:

```text
iOS/iPadOS: Swift/SwiftUI + Rust core
Android: Kotlin/Compose + Rust core
```

Native responsibilities include secure storage, biometrics, camera, share/import/export, background lifecycle, notification privacy, app-switch previews, and platform ML acceleration.

Initial mobile tabs/jobs:

```text
Ask
Scan
Saved
Patient
```

Mobile stores bounded evidence/model packs selected for device capacity rather than mirroring the entire desktop corpus.

## 17. Desktop-mobile local pairing and sync

Candidate flow:

```text
Desktop creates short-lived one-time pairing bootstrap
 -> displays QR
 -> mobile scans and authenticates
 -> user confirms target/device/session
 -> encrypted local session established
 -> selected packs/artifacts/context synchronize
 -> bootstrap invalidated
```

Security properties:

- unpredictable single-use bootstrap;
- short expiry;
- atomic redemption;
- replay/race denial;
- revocation/cancellation;
- no raw patient data or long-lived secret in QR;
- no raw key transfer;
- user-visible sync scope;
- no silent public relay.

The phone remains useful when disconnected from desktop.

## 18. Evidence/model/terminology packs

Pack classes:

```text
EvidencePack
GuidelinePack
TerminologyPack
ModelPack
BenchmarkPack
```

Each records:

```text
identity/version
digests
source manifest
rights/notices
build recipe
runtime requirements
resource estimates
language/jurisdiction
validation/evaluation evidence
expiry/staleness policy
revocation/rollback metadata
```

Updates create new pack identities. Old saved answers remain bound to the old snapshot.

## 19. Network and update model

Evidence updates may contact approved public/institutional sources without creating a SafeEvidence cloud dependency.

The user can operate in:

```text
NETWORK_LOCKED
EVIDENCE_UPDATE_ONLY
SELECTED_CONNECTORS
```

No remote model fallback exists implicitly.

## 20. Observability and diagnostics

Default:

```text
remote telemetry = none
remote analytics = none
remote crash upload = none
```

Local diagnostics should minimize clinical content. Any support bundle is previewable/redactable before explicit export.

## 21. Resource profiles

At minimum:

```text
LOW_POWER
BALANCED
ACCURACY
```

Routing depends on measured task/device eligibility, not brand. Desktop deep review may run larger sequential workers; mobile should prefer compact specialist models and bounded packs.

## 22. Arabic and multilingual architecture

Arabic/RTL support must be tested in:

- UI layout and typography;
- query understanding;
- terminology expansion;
- cross-language retrieval;
- document OCR;
- future ASR;
- safety triggers;
- answer synthesis;
- citation/span navigation;
- benchmark review.

Cross-language retrieval must preserve source language and never imply that a translation is the authoritative source text.

## 23. Security invariants

- source/document text is data, never system/tool instruction authority;
- model workers do not receive vault master keys;
- no worker gets ambient network by default;
- secrets are handles, not copied into prompts/logs;
- external actions are separately authorized from evidence answers;
- unknown effect/result states never authorize blind retry;
- model agreement is not correctness;
- missing data is not absence;
- every sensitive cache/index inherits source scope and deletion rules;
- backup/restore is part of the security model.

## 24. Architecture decisions that remain open

The foundation review must explicitly select or reject:

- final desktop shell;
- exact encrypted metadata implementation and key hierarchy;
- Rust<->Swift and Rust<->Kotlin FFI mechanism;
- first evidence embedding/reranker pair;
- first local generator;
- decision-model tournament winner(s);
- vector projection implementation;
- document parser combination;
- OCR engine(s);
- pack signing/update mechanism;
- local sync transport;
- exact guideline intermediate representation;
- clinical terminology pack strategy;
- release signing/distribution strategy.

No open decision may be silently resolved by an agent choosing its favorite framework.

# P00 reconciliation architecture amendment

Canonical details: `docs/P00_FOUNDATION_DECISIONS_2026-10-07.md`.

## Data planes

SafeEvidence separates:
1. a public/rebuildable evidence plane for rights-admitted corpus material,
   signed packs and projections; and
2. an encrypted private authority plane for questions, patient context, private
   documents, saved reviews, answers and private projections.

Private records cannot enter distributable public packs. Cross-plane references
use immutable IDs/digests plus source version and rights identity.

## Private authority

The current MedScale whole-file EncryptedVault lifecycle is not a canonical
SafeEvidence storage decision. P02 qualifies the ottari SQLCipher/WAL vault
slice as the primary hypothesis, with compatible MedScale writer-lock/path
claims only after integrated crash/backup tests.

## Evidence independence

The canonical model includes StudyArm, AnalysisPopulation, ArmObservation,
Result/OutcomeReport, Comparison, ReportVersionLink,
SystematicReviewIncludedStudy and ParticipantOverlapGroup.

Distinct reports do not imply distinct studies. Distinct results within a study
do not imply statistically independent evidence.

## Assurance semantics

Orchestration actions are not terminal outcomes.

```text
ControlAction:
  RETRIEVE_EVIDENCE | USE_TOOL | REQUEST_CONTEXT

TerminalOutcome:
  ANSWER | ANSWER_WITH_CAUTION | ASK_MORE | CONFLICT |
  ABSTAIN | ESCALATE | BLOCKED | EMERGENCY_NOTICE
```

EMERGENCY_NOTICE is not autonomous triage.

## Atomic proof admission

Generated text is a draft until post-answer verification creates an
AnswerProofManifest. User-visible streaming must not masquerade as committed
evidence.

AnswerProofManifest binds source/version/span, current-validity, rights,
study/result identity, claim support, applicability, tools/models/policy and the
terminal outcome.

Historical answers are immutable; current-validity overlays may change.

## Confidence

V1 exposes categorical evidence/support/applicability states and reasons. It
does not expose a clinical truth-confidence percentage.

## Canonical P00 contract references

The older narrative architecture is subordinate to:
- `docs/P00_DATA_PLACEMENT_CONTRACT.md` (store/grant/backup/export/sync/delete);
- `docs/P00_VAULT_DURABILITY_CONTRACT.md` (commit/lock/WAL/backup);
- `docs/P00_STUDY_INDEPENDENCE_CONTRACT.md` (typed result and overlap);
- `docs/P00_DECISION_ASSURANCE_CONTRACT.md` (control vs terminal precedence);
- `docs/P00_PROOF_ADMISSION_CONTRACT.md` (atomic assured answer);
- `docs/DONOR_RIGHTS_REGISTER.md` (per-slice admission).

Any older text suggesting a competing vault, nine interchangeable terminal
states or a clinical confidence percentage in V1 is superseded. Real
qualification still belongs to the owning phase.
