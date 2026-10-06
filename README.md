# SafeEvidence

**Local clinical evidence and decision assurance, built for desktop and mobile without a mandatory cloud.**

> **Foundation status:** planning only. SafeEvidence is not a medical device, has not been clinically validated, and must not be used for diagnosis, treatment, triage, prescribing, or patient-care decisions until the relevant claims are independently qualified.

## Product thesis

SafeEvidence is a local-first clinical evidence workstation for clinicians and researchers. Its core question is not only:

> What does the literature say?

It must also answer:

> Does the available evidence justify an answer for this question, this patient context, this jurisdiction, and this point in time?

SafeEvidence should be able to answer, ask for missing information, expose conflicting evidence, or abstain. A fluent model response is never authority by itself.

## Founding invariants

- **Evidence first, language second.** Retrieval, source identity, claim support, contradiction, applicability, and sufficiency are evaluated before answer rendering.
- **Local-first by architecture.** Core record/evidence work, retrieval, inference, decision assurance, OCR, and saved history must have a useful offline path.
- **No silent cloud fallback.** External processing is explicit and optional. Failure of a local model or source does not silently move clinical data to a remote service.
- **No mandatory SafeEvidence cloud.** Desktop and mobile must remain useful without a SafeEvidence-hosted account, database, vector service, inference API, telemetry service, or storage backend.
- **Zero founder-funded runtime COGS as a design target.** User hardware and explicitly configured external sources perform ordinary work; founder-paid inference/storage/search is not a correctness dependency.
- **Confidence is not evidence strength.** Model probability, evidence quality, patient applicability, source authority, and review state remain separate concepts.
- **A real citation is not enough.** Material claims require support verification against exact source spans where available.
- **Abstention is a first-class correct outcome.** Missing, contradictory, stale, inaccessible, or inapplicable evidence may produce `ASK_MORE`, `CONFLICT`, or `ABSTAIN` instead of a forced answer.
- **Deterministic tools outrank generative text** for validated arithmetic, structured checks, policy gates, and other bounded functions.
- **Canonical truth is not a vector index, graph projection, AI summary, or model memory.** Derived indexes remain rebuildable projections over source-backed records.
- **Desktop and mobile are first-class surfaces.** Desktop is the complete clinical evidence workstation; iOS and Android are native companion/independent clients with dedicated mobile workflows.
- **Arabic and English are architectural requirements, not release polish.** Retrieval, UI, medical terminology, OCR/ASR evaluation, and safety behavior must be tested in both languages where applicable.
- **Provenance before reuse.** Permission makes a source eligible; exact revision, path, controlling terms, modifications, notices, threat placement, tests, and exit strategy make it adoptable.

## Intended product surfaces

### Desktop

A clinician-focused workstation for:

- clinical questions and patient-context evidence review;
- fast evidence answers and extended deep reviews;
- exact claim-to-source navigation;
- local literature/guideline packs;
- local document/PDF ingestion and OCR;
- guideline applicability and conflict review;
- read-only patient context import through bounded interoperability adapters;
- source, model, decision, and evidence diagnostics.

### Mobile

A native mobile product for:

- fast local evidence questions;
- camera/document capture and OCR;
- saved evidence briefs and specialty packs;
- bounded patient context;
- review of citations, conflicts, and uncertainty;
- local pairing/synchronization with an authorized desktop when desired.

Mobile is not required to replicate the complete desktop analytics/research workspace.

## Architecture direction

```text
Clinical question + optional patient context
                  |
                  v
          Query interpretation
                  |
        PICO / terminology / scope
                  |
          +-------+--------+
          |                |
          v                v
 Deterministic tools    Retrieval
                          |
          lexical + semantic + guideline + exact sources
                          |
                       rerank
                          |
                          v
                  Sufficiency gate
                          |
          +---------------+----------------+
          |               |                |
       ASK_MORE         ABSTAIN          CONTINUE
                                           |
                                           v
                                  Evidence appraisal
                                           |
                                  Claim/support checks
                                           |
                                  Contradiction analysis
                                           |
                                  Patient applicability
                                           |
                                  Local synthesis model
                                           |
                                  Post-answer verifier
                                           |
                                      Calibration
                                           |
                                           v
                                         Answer
```

The final implementation must preserve replaceable workers and SafeEvidence-owned contracts. No model family, RAG framework, vector database, OCR stack, or UI shell is canonical merely because it is listed as a candidate.

## Foundation documents

The initial planning authority will live under `docs/`:

- `docs/PRODUCT_THESIS.md`
- `docs/ARCHITECTURE.md`
- `docs/SOURCE_LEDGER.md`
- `docs/MASTER_PLAN.md`
- `docs/GAP_REVIEW.md`

`AGENTS.md` defines the planning/review contract for Codex, Claude/Opus, and other engineering agents.

## Implementation gate

No large implementation phase should begin until the foundation review has:

1. challenged the product thesis and trust boundaries;
2. closed or explicitly deferred material architecture gaps;
3. pinned source-adoption rules and exact-source intake requirements;
4. defined benchmark/evaluation contracts for retrieval, citation support, abstention, calibration, OCR, Arabic, privacy, and resource use;
5. separated research claims from product claims and clinical claims;
6. defined the desktop/mobile scope and local synchronization boundary;
7. recorded unresolved decisions as explicit gates rather than hidden assumptions.

## License

SafeEvidence-owned code license is not frozen by this initial planning commit. Third-party code, model weights, datasets, terminology, documents, fonts, and assets retain their own applicable rights and must be tracked independently.