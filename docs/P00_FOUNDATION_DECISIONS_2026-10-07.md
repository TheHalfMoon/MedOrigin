# SafeEvidence P00 Foundation Decisions — 2026-10-07

Status: `P00_BINDING_RECONCILIATION` (supplemented by specific 2026-10-08 contracts)

## D1 — Data planes

**Binding detailed contract:** `docs/P00_DATA_PLACEMENT_CONTRACT.md`.

SafeEvidence has two primary local planes.

### Public / rebuildable evidence plane

May contain rights-admitted public metadata/content, signed packs, corpus
manifests, lexical/vector projections and current-validity overlays.

It must not contain patient context, private query history, private documents or
institution-only content unless explicitly placed in a rights-scoped private
store.

It is not encrypted with the user's private vault DEK by default.

### Private authority plane

Contains questions, query history, patient context, private/user documents,
institution-licensed private content, saved reviews/screening decisions,
AnswerArtifact/AnswerProofManifest and private query-derived projections.

Private data never enters distributable public packs.

Cross-plane references use immutable IDs/digests plus version and rights
identity.

## D2 — Private vault

**Binding detailed contract:** `docs/P00_VAULT_DURABILITY_CONTRACT.md`.

MedScale `EncryptedVault` whole-file seal/unseal is not the canonical
SafeEvidence vault donor.

P02 primary hypothesis:
- ottari persistent SQLCipher/WAL vault + snapshot/backup/protector slices.

Potential MedScale additions:
- writer-lock semantics;
- path/claim validation;
- selected recovery/key helpers;
- compatible adversarial tests.

P02 qualification includes crash/power-loss, concurrent writer, backup during
writes, interrupted migration, wrong/lost keys and plaintext-spill tests.

Private blob identifiers must not expose plaintext content membership where
that violates the private threat model.

## D3 — Evidence ontology

**Binding detailed contract:** `docs/P00_STUDY_INDEPENDENCE_CONTRACT.md`.

Minimum canonical concepts:

```text
Study
StudyArm
StudyReportLink
ReportVersionLink
AnalysisPopulation
OutcomeDefinition
OutcomeReport / Result
ArmObservation
Comparison
EffectEstimate
SystematicReviewIncludedStudy
ParticipantOverlapGroup
ReviewProtocol
SynthesisProtocol
SynthesisResult
```

Report identity does not imply study independence. Study identity does not
imply result independence. Synthesis inputs must declare independence/covariance
or be refused.

EBMonFHIR is a semantic crosswalk/reference, not the canonical database.

## D4 — Assurance semantics

**Binding detailed contract:** `docs/P00_DECISION_ASSURANCE_CONTRACT.md`.

```text
ControlAction:
  RETRIEVE_EVIDENCE
  USE_TOOL
  REQUEST_CONTEXT

TerminalOutcome:
  ANSWER
  ANSWER_WITH_CAUTION
  ASK_MORE
  CONFLICT
  ABSTAIN
  ESCALATE
  BLOCKED
  EMERGENCY_NOTICE
```

commandMed mechanics and fixtures may be reused. Its patient-facing lexical
rule content is not copied unchanged.

Population-level evidence may be answered while patient applicability remains
unresolved.

EMERGENCY_NOTICE is not autonomous triage.

Clarification/retrieval rounds are bounded. Commit, abstention, false
escalation and useful coverage receive frozen metric definitions before P08.

DAL negative Study-0 results are binding prior evidence. Learned decision models
remain challengers to deterministic sufficiency.

## D5 — No V1 clinical percentage

SafeEvidence V1 shows no user-facing clinical confidence percentage.

Any future percentage requires a frozen estimand, clinician rubric,
calibration/final separation, temporal and subgroup validation, uncertainty
intervals and invalidation whenever the qualified pipeline identity changes.

## D6 — Atomic proof admission

**Binding detailed contract:** `docs/P00_PROOF_ADMISSION_CONTRACT.md`.

A generated answer becomes committed only after a successful post-verification
admission producing `AnswerProofManifest`.

The manifest binds at least:
- question/context snapshot;
- source/version identities;
- evidence spans;
- rights scope;
- current-validity watermark;
- study/result identities;
- claim-support results;
- applicability;
- tool/model/runtime/policy identities;
- terminal outcome.

Draft/streamed text is not an admitted answer. Historical answers remain
immutable; current-validity may change.

## D7 — Online discovery

Online discovery never auto-sends raw patient narrative.

The user can see the exact outbound query. Default search construction uses
structured clinical concepts/keywords. Query-derived remote results and caches
remain private.

## D8 — Runtime and distribution

Near-zero founder per-query COGS remains a design goal, not a claim of zero
pack-build or distribution cost.

Before P03 bind default corpus scope, install/update size, build workspace,
embedding precision/size, builder ownership, update frequency and bandwidth/
storage scenario.

No mandatory founder-paid inference, search, vector, auth or storage service is
allowed.

## D9 — Pack/update trust

Synthetic signing seeds are test-only.

Production pack trust requires a qualified TUF-compatible model with root/key
custody, threshold/rotation, rollback/freeze/expiry behavior and explicit
offline stale-bundle semantics before production pack consumption.

## D10 — Initial intended use

First qualified target:
desktop clinician evidence workstation for population-level evidence questions.

Patient-specific treatment authority, dose execution, emergency triage,
mandatory meta-analysis, executable guidelines, voice authority and full mobile
parity require separate promotion.

## Re-check precedence

The P00 contract sheets resolve earlier underspecified headings. If older text here gives a weaker interpretation, the detailed contract controls. Independent reviewers must assess the exact repair head; P00 is not automatically closed.
