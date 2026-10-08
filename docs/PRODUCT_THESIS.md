# SafeEvidence Product Thesis

Status: `FOUNDATION_DRAFT`

## 1. Product statement

SafeEvidence is a local-first clinical evidence and decision-assurance system for clinicians and researchers. It is designed to retrieve, verify, compare, and explain medical evidence while preserving the option to ask for missing context, expose conflicts, or abstain instead of forcing an answer.

The product is not defined as "an offline OpenEvidence clone." Its intended differentiation is verification and decision assurance:

```text
Discovery product:
find evidence -> summarize

SafeEvidence target:
find evidence
-> establish source identity
-> verify claim support
-> detect contradiction/staleness
-> assess applicability
-> assess information sufficiency
-> calibrate commit/abstain behavior
-> synthesize only within the verified boundary
```

## 2. Primary users

### Primary

- clinicians seeking evidence during or around patient care;
- clinicians reviewing guidelines, trials, safety information, and treatment evidence;
- clinical researchers performing bounded evidence review.

### Secondary

- trainees using source-linked evidence exploration;
- institutions using locally admitted guideline/evidence packs;
- technical evaluators studying medical retrieval, abstention, calibration, and evidence verification.

The initial product should not attempt to become a full EHR, hospital information system, billing system, scheduling system, or autonomous clinical agent.

## 3. Primary jobs to be done

### Fast evidence answer

Ask a focused clinical question and receive a concise answer whose material claims are linked to verified evidence, with visible uncertainty, conflict, and applicability.

### Deep review

Run a longer evidence workflow that exposes the research plan, searches, included/excluded sources, contradictions, appraisal, gaps, and immutable evidence snapshot.

### Guideline applicability

Inspect whether a guideline recommendation is applicable, partially applicable, contradicted, superseded, jurisdictionally mismatched, or blocked by missing context.

### Patient-context evidence review

Optionally provide bounded patient context so the system can distinguish evidence strength from patient applicability. Missing context must remain explicit.

### Document evidence work

Import local PDFs/documents/scans, extract source-linked evidence, and navigate from a claim to the exact page/region/table cell that supports or contradicts it.

### Mobile evidence access

Ask, scan, review, and save evidence on iOS/Android without requiring a SafeEvidence cloud account or mandatory remote inference.

## 4. Product surfaces

### Desktop: complete workstation

Desktop owns the full workflow:

- question decomposition;
- evidence discovery and local corpora;
- deep review;
- document ingestion/OCR;
- guideline analysis;
- patient-context adapters;
- pack/model/source management;
- benchmark and diagnostic surfaces;
- evidence export.

### Mobile: native focused product

Mobile owns high-frequency jobs:

- Ask;
- Scan;
- Saved evidence/briefs;
- bounded Patient Context;
- citation/conflict review;
- pack synchronization with an authorized desktop.

Mobile is not required to mirror full desktop research analytics.

## 5. Behavioral outcomes

SafeEvidence distinguishes bounded internal orchestration actions from final
clinician-facing assurance outcomes:

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

A ControlAction is never an answer commitment. `EMERGENCY_NOTICE` is disabled
in V1 pending a separately qualified clinician-facing notice policy; it is not
autonomous emergency triage. `ABSTAIN`, `ASK_MORE`, and `CONFLICT` are
valid terminal outcomes when the evidence or context does not justify a
supported answer. Final-text assurance additionally requires atomic proof
admission. The binding precedence, action limits, reason codes, and
commit/abstention definitions are in
`docs/P00_DECISION_ASSURANCE_CONTRACT.md`.

## 6. Trust semantics

SafeEvidence must keep these concepts separate:

```text
model probability
retrieval sufficiency
citation identity
claim support
evidence quality
patient applicability
guideline authority/jurisdiction
human review state
action authority
```

No single scalar may silently collapse them into "truth confidence."

If a user-facing percentage is shown, its meaning and calibration population must be defined and empirically validated. Raw language-model confidence must never be presented as probability that a medical answer is true.

## 7. Evidence answer contract

A material answer should be representable as:

```text
AnswerArtifact
  question identity
  interpretation / PICO(PICOTS) representation
  patient-context fields actually used
  jurisdiction/timeframe
  evidence snapshot identity
  material claims[]
    claim text
    claim kind
    supporting evidence refs[]
    contradicting evidence refs[]
    support state
    applicability state
  evidence profile
  missing information
  contradiction state
  decision/sufficiency result
  calibration identity if a calibrated score is displayed
  model/runtime identities
  retrieval/reranker identities
  generated timestamp
  limitations
```

Saved answers bind immutable evidence snapshots. New evidence creates a new evaluation; it does not rewrite historical answers silently.

## 8. Evidence-source philosophy

SafeEvidence should support four product-level pack classes:

```text
Open Evidence Pack
Institution-Licensed Evidence Pack
User-Provided Evidence Pack
Metadata-Only Connector
```

Access and redistribution rights are separate questions. A technically retrievable article is not automatically permitted for local packaging, redistribution, or team sharing.

## 9. Competitive thesis

SafeEvidence should compete on measurable properties rather than branding claims:

- citation identity accuracy;
- exact claim-support accuracy;
- retrieval recall/precision;
- contradiction detection;
- retraction/correction behavior;
- calibrated abstention;
- patient-context applicability;
- guideline conflict handling;
- offline/privacy behavior;
- Arabic/English performance;
- local latency/resource efficiency;
- source traceability;
- clinician usability.

Any comparison with OpenEvidence, Abridge, OpenMed, or another product must use dated, matched conditions and disclose differences in licensed-content access.

## 10. Local-first and cost boundary

A useful SafeEvidence installation must not require:

- a SafeEvidence account;
- a SafeEvidence backend;
- hosted vector storage;
- hosted telemetry;
- hosted authentication;
- founder-funded model inference;
- founder-funded search/storage;
- automatic remote fallback.

Network access may be used for explicit evidence updates, user-authorized source connectors, or institution-authorized integrations. Egress must be scoped and visible.

## 11. Research and clinical claim boundary

The project may research medical evidence retrieval, decision assurance, abstention, calibration, guideline verification, and clinical applicability. Research success does not automatically authorize clinical use.

Release claims must be scoped to exact evidence. The repository must be able to say `NOT_PROVEN`, `BLOCKED`, `NEGATIVE_RESULT`, or `INSUFFICIENT_EVIDENCE` without treating those outcomes as project failure.

## 12. Non-goals for the initial product

- autonomous diagnosis or treatment authority;
- autonomous prescribing/order entry;
- autonomous emergency triage;
- replacing a clinician;
- becoming the canonical EHR database;
- silently learning clinical truth from prior generated answers;
- mandatory cloud synchronization;
- mandatory multi-user server infrastructure;
- a large service fleet merely to provide local search;
- a single foundation model owning retrieval, safety, decision assurance, and authority.

## 13. Success definition

SafeEvidence succeeds when a clinician can locally ask a clinical question, inspect the exact evidence behind the answer, see what is uncertain or conflicting, understand whether the evidence applies to the supplied patient context, and trust that the system will decline to overstate what the evidence does not establish.

## P00 reconciliation — initial qualified wedge

The roadmap remains broad, but the first qualification target is intentionally
narrower:

> A desktop clinician evidence workstation for population-level medical
> evidence questions with exact provenance, claim-to-span verification,
> current-validity state, conflict visibility, and fail-closed abstention.

This initial claim does not include autonomous diagnosis, autonomous treatment
ordering, autonomous emergency triage, medication-dose execution, broad
patient-specific recommendation authority, mandatory meta-analysis, mandatory
executable guideline authority, voice authority, or full mobile parity.

SafeEvidence V1 does not display a clinical truth-confidence percentage.

## P00 initial evaluation scope decision

The first evaluation target is a CPU-only 16 GB-class Windows desktop evidence
workstation for clinicians/researchers reviewing **population-level medical
evidence on adult treatments, benefits, harms and contradictions**. English and
Arabic query, UI and citation pathways are evaluation scope, not validated.

It is an evidence-research setting, not autonomous point-of-care diagnosis,
prescribing or emergency triage. No specialty-wide, Saudi-guideline, global
jurisdictional or regulatory conformity claim is made by P00. Pregnancy,
pediatrics, individual dosing and unqualified interaction authority are out of
initial scope. P01 product/clinical owners must approve the exact question
taxonomy, care setting, target release jurisdiction, gold-review protocol and
risk/useful-coverage goals before model or UX promotion.

If qualified clinical reviewers or evaluation funding are unavailable, clinical
validation is blocked rather than silently replaced by model-generated gold.
