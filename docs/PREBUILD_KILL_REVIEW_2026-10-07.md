# SafeEvidence Pre-Build Kill Review — 2026-10-07

Status: P00_INTERNAL_REVIEW_COMPLETE

## Executive verdict

An internal review previously found no known P0 planning gap. Two later independent reviews found material P0 gaps. That earlier statement is superseded by `docs/P00_INDEPENDENT_REVIEW_RECONCILIATION_2026-10-07.md`.

This is not implementation authority and is not a clinical, safety, security, or compliance claim. The remaining P00 gate is independent adversarial review by Codex and Claude/Opus against the exact post-audit commit.

## Final architectural corrections

### PB-G001 — Study identity is distinct from publication identity

A clinical study may have multiple reports: journal article, conference abstract, follow-up publication, subgroup analysis, registry record, protocol, correction, and regulatory report.

SafeEvidence therefore adds these canonical concepts:

~~~text
Study
  study_id
  registry_ids
  sponsor_study_ids
  design
  population
  interventions
  arms
  recruitment_period
  sites
  sample_size
  funding
  conflicts_of_interest
  status

StudyReportLink
  study_id
  source_artifact_id
  report_role
  linkage_method
  linkage_evidence
  linkage_confidence_state
  human_review_state

OutcomeDefinition
  study_id
  outcome_id
  definition
  timepoint
  analysis_population
  measurement_method

EffectEstimate
  study_id
  outcome_id
  comparison
  effect_measure
  estimate
  interval
  variance_or_se
  adjusted_state
  source_span_refs
~~~

SourceArtifact remains immutable report/document identity. Study is the evidence unit.

Ready sources:
- Cochrane study-vs-report methodology;
- ClinicalTrials.gov identifiers/status;
- evidence-surveillance/es3 / Trial2rev for trial-review-registry-report linkage patterns;
- Trialstreamer for living RCT acquisition and PICO extraction patterns.

### PB-G002 — Duplicate publication and trial linkage

SafeEvidence distinguishes:
- same bibliographic record;
- same publication/version;
- same study, different report;
- different studies with similar titles/authors.

Resolution order:
1. exact PMID, PMCID, DOI, version;
2. exact registry identifier;
3. explicit publication-registry links;
4. sponsor study identifiers;
5. structured investigator/site/intervention/sample-size/date matching;
6. fuzzy candidate only;
7. human confirmation for ambiguous same-study linkage.

Automatic fuzzy matching may propose a Study link but cannot silently merge ambiguous trials.

Ready sources:
- ASReview and ASReview datatools dedup;
- Trial2rev/ES3;
- systematic-review-pipeline dedup tests as reference;
- ClinicalTrials.gov.

### PB-G003 — Structured effect extraction

Claim verification alone is insufficient for quantitative evidence synthesis.

Promote:
- PICO span extraction;
- arm extraction;
- sample-size extraction;
- outcome and timepoint extraction;
- comparative direction;
- exact result/effect estimate;
- denominator and analysis set;
- uncertainty interval;
- extraction provenance.

Ready sources:
- jayded/evidence-inference;
- Evidence Inference 2.0 datasets/evaluation;
- WengLab-InformaticsResearch/PICOX;
- bwallace/RRnlp;
- Trialstreamer/RobotReviewer research code.

All automatic extraction remains proposal-level until admitted.

### PB-G004 — Risk-of-bias appraisal is design-specific

SafeEvidence does not invent one universal quality score.

Versioned appraisal profiles:
- randomized trials: RoB 2 family;
- non-randomized intervention studies: ROBINS-I, version-pinned;
- exposure studies: ROBINS-E when relevant;
- diagnostic accuracy: current qualified QUADAS family;
- systematic reviews: AMSTAR 2-style critical-domain appraisal.

Tool content and terms remain independently governed. RobotReviewer/RRnlp can be research automation/oracles. Automated judgement never becomes authority by itself.

### PB-G005 — Quantitative synthesis is explicit

Deep Review supports a bounded quantitative-synthesis lane without making meta-analysis mandatory.

Required concepts:
- SynthesisProtocol;
- EligibleEffectEstimate;
- UnitOfAnalysisDecision;
- EffectMeasureTransform;
- SynthesisModel;
- HeterogeneityResult;
- SensitivityAnalysis;
- optional PublicationBiasAssessment;
- SynthesisResult.

Safeguards:
- study, not report, is the unit;
- no participant/group double counting;
- multi-arm correlation handled explicitly;
- selected outcome/timepoint rule is protocol-bound where possible;
- no pooling when inappropriate;
- narrative synthesis is a valid result;
- transformed values trace back to original source fields.

Ready implementation:
- statsmodels.stats.meta_analysis for basic fixed/random effects, effect-size utilities, heterogeneity, and HKSJ-style uncertainty;
- mature external statistical packages as benchmark oracles;
- existing plotting libraries for forest/funnel visualization.

SafeEvidence does not reimplement meta-analysis formulas from scratch.

### PB-G006 — Reporting bias and unpublished evidence

Evidence profile records:
- registry_results_available;
- publication_found;
- registry_publication_discrepancy;
- outcome_reporting_discrepancy;
- selective_timepoint_risk;
- funding_source;
- declared_conflicts;
- sponsor_role;
- preprint_status;
- peer_review_status.

Registry records are complementary evidence, not proof that a published conclusion is correct.

### PB-G007 — ReviewProtocol is canonical

Deep Review adds ReviewProtocol:
- question/PICO;
- eligibility criteria;
- source set;
- exact search strings;
- search dates;
- language/date restrictions;
- screening protocol;
- reviewer roles;
- extraction schema;
- risk-of-bias profile;
- synthesis plan;
- deviation log;
- registration identifiers such as PROSPERO when available.

Every include/exclude decision has a reason so PRISMA-compatible flow counts are deterministic. PRISMA is a reporting reference, not a correctness certificate.

### PB-G008 — Living evidence surveillance

Saved evidence questions/reviews may opt into local surveillance.

~~~text
new PubMed update
new/changed registry record
new publication-trial link
correction/retraction/expression of concern
new guideline version
pack/source update
  -> candidate relevance evaluation
  -> CURRENT_VALIDITY_CHANGED?
  -> user-visible delta
~~~

Historical answers are never overwritten.

Ready sources:
- PubMed baseline/daily update semantics;
- Crossref Retraction Watch;
- Trial2rev/ES3 monitoring model;
- Trialstreamer update patterns.

### PB-G009 — Publication state is explicit

Classification:
- PEER_REVIEWED;
- PREPRINT;
- CONFERENCE_ABSTRACT;
- PROTOCOL;
- REGISTRY_RESULT;
- REGULATORY_REPORT;
- CORRECTION;
- RETRACTION_NOTICE;
- OTHER.

A preprint is never silently presented as equivalent to a peer-reviewed publication.

### PB-G010 — Funding and conflict provenance

Store/display when available:
- funder;
- sponsor;
- author COI declaration;
- sponsor involvement in design/analysis/writing;
- unavailable/unknown state.

Unknown remains unknown.

### PB-G011 — Search completeness and source-class coverage

Deep Review reports:
- bibliographic databases searched;
- trial registries searched;
- guideline sources searched;
- local/institution sources searched;
- citation snowballing performed;
- grey/unpublished evidence strategy;
- last search date.

High retrieval relevance from a single source family is not evidence of comprehensive search.

### PB-G012 — Statistical multiplicity

The synthesis layer models:
- multiple outcomes;
- multiple timepoints;
- multiple analyses;
- multiple arms;
- subgroup analyses;
- repeated reports.

Selection rules are protocol-bound to prevent result-driven cherry-picking.

### PB-G013 — Appraisal automation states

Separate:
- AUTO_EXTRACTED;
- AUTO_PROPOSED_JUDGEMENT;
- HUMAN_CONFIRMED;
- HUMAN_OVERRIDDEN;
- UNRESOLVED.

A model score does not directly become a risk-of-bias judgement.

### PB-G014 — Evidence certainty remains multidimensional

SafeEvidence does not claim official GRADE implementation unless separately qualified.

Store explicit dimensions:
- risk of bias;
- inconsistency;
- indirectness;
- imprecision;
- publication/reporting bias;
- magnitude/effect uncertainty;
- applicability;
- source freshness;
- conflict.

### PB-G015 — Deterministic quantitative tools carry provenance

Every calculator/statistical transform records:
- tool_id;
- tool_version;
- formula/method;
- inputs;
- units;
- source refs;
- output;
- rounding;
- warnings.

Generated language cannot silently recompute or alter numeric results.

### PB-G016 — Online search disclosure

The existing two-mode rule is binding:
- LOCAL_PACK_SEARCH;
- EXPLICIT_ONLINE_DISCOVERY.

Online discovery does not receive raw patient narrative by default. Query minimization/de-identification is explicit and auditable.

### PB-G017 — Failure and partial-data semantics

Every stage distinguishes:
- NOT_RUN;
- NOT_AVAILABLE;
- FAILED;
- PARTIAL;
- UNRESOLVED;
- COMPLETE_FOR_DEFINED_SCOPE.

Missing full text, failed OCR, parser error, unavailable registry, or failed model execution cannot silently become no evidence.

### PB-G018 — Evidence export/import portability

Exports preserve:
- source identities;
- rights;
- study/report links;
- evidence spans;
- review protocol;
- screening decisions;
- extracted effects;
- appraisal states;
- model/tool identities;
- current-validity overlay;
- provenance.

A generated answer alone is not a complete evidence export.

## New copy/reference sources from this kill review

| Source | Observed head | Role | Default disposition |
|---|---|---|---|
| evidence-surveillance/es3 | fa845217690e179d3f8151e97773aabc035d6cfe | trial-review linkage, surveillance/update patterns | COPY_BOUNDED / REFERENCE |
| ijmarshall/trialstreamer | a97cb8332c039e228ef42188c9d966440894e354 | living RCT acquisition/PICO/quality patterns | REFERENCE_ONLY_PENDING_RIGHTS; no copy without verified grant |
| ijmarshall/robotreviewer | 9a2781974c3edc6322b4fb329b1ea0348af7b8a1 | RCT PICO/risk-of-bias automation oracle | REFERENCE / BENCHMARK; GPL compliance or verified separate grant before distribution |
| bwallace/RRnlp | e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0 | EBM NLP implementation/model research | COPY_BOUNDED / BENCHMARK |
| jayded/evidence-inference | a661e8c14f973398380c8865cf2f27a535aaaf6d | intervention-comparator-outcome result and evidence extraction | COPY_BOUNDED / BENCHMARK |
| WengLab-InformaticsResearch/PICOX | f3351c4786bf197efacfcefc1c1e66c36c245842 | overlapping PICO extraction | COPY_BOUNDED / BENCHMARK |
| statsmodels/statsmodels | 8278e2d218cc85bac2c7af02feb9a19a0e499b04 | quantitative synthesis/statistics | DEPEND / VENDOR selected modules |
| PRISMA 2020 | current official checklist | review reporting/reproducibility | METHOD_REFERENCE |
| Cochrane Handbook | current | study/report linkage, unit-of-analysis, synthesis | METHOD_REFERENCE |
| RoB 2 / ROBINS family | current version-pinned | design-specific risk-of-bias | METHOD_REFERENCE |
| AMSTAR 2 | current | systematic-review appraisal | METHOD_REFERENCE |

## Phase bindings

P02 adds Study, StudyReportLink, OutcomeDefinition, EffectEstimate, and ReviewProtocol contracts.

P03 adds publication-state, study/report linkage candidates, funding/COI, registry links, living-update triggers, and source-class coverage.

P04/P05 evaluate retrieval at report level and study-recall level. Multiple reports for one study do not count as multiple successful study retrievals.

P06 adds structured result/effect extraction and Evidence Inference/PICOX benchmark lanes.

P07 adds design-specific appraisal profiles and automation/human review states.

P18 Deep Review owns ReviewProtocol, screening audit, study-level linkage, structured extraction, risk-of-bias workflow, optional quantitative synthesis, PRISMA-compatible counts/flow, and living-review surveillance.

P20 SafeEvidenceBench adds study-linkage precision/recall, false merge/miss rates, outcome/effect extraction accuracy, numeric span faithfulness, appraisal agreement, meta-analysis golden fixtures, double-counting adversarial cases, review-screening recall/workload, living-update detection delay, and funding/COI extraction coverage.

## Internal P00 readiness matrix

| Dimension | Internal status |
|---|---|
| product definition | RESOLVED |
| copy-first source strategy | RESOLVED |
| canonical evidence contracts | RESOLVED |
| study/report identity | RESOLVED |
| source acquisition/update | RESOLVED |
| rights/licensing | RESOLVED |
| retrieval | RESOLVED |
| claim/evidence verification | RESOLVED |
| effect extraction | RESOLVED |
| appraisal | RESOLVED |
| decision assurance | RESOLVED |
| calibration | RESOLVED |
| synthesis/generation | RESOLVED |
| systematic/deep review | RESOLVED |
| quantitative synthesis | RESOLVED |
| guidelines | RESOLVED |
| FHIR/patient context | RESOLVED |
| documents/OCR | RESOLVED |
| desktop | RESOLVED_WITH_TOURNAMENT |
| mobile | RESOLVED_WITH_TOURNAMENT |
| pairing/sync | DEFERRED_WITH_OWNER_P17 |
| voice | DEFERRED_WITH_OWNER_P19 |
| Arabic/i18n | RESOLVED_WITH_BENCHMARK |
| privacy/security | RESOLVED_WITH_QUALIFICATION |
| release/update | RESOLVED_WITH_QUALIFICATION |
| regulatory/claims | RESOLVED_AS_GATED |

RESOLVED means the plan has an explicit architecture, owner, source, failure semantics, and verification gate. It does not mean implementation or clinical validity is proven.

## Final P00 rule

Broad implementation begins only after:
1. Codex independently attacks this exact foundation;
2. Claude/Opus independently attacks this exact foundation;
3. findings are reconciled;
4. no unresolved P0 remains;
5. every P1 is resolved or phase-bound with owner;
6. the exact post-reconciliation commit becomes the P01 base.


## Supersession notice

Do not use the internal readiness matrix in this file as current closure
authority.

The independent Codex and Claude/Opus reviews found P0/P1 issues that supersede
several `RESOLVED` rows, including storage/data planes, evidence/result
identity, decision semantics, donor rights and proof admission.

Current status is defined only by the reconciliation documents and subsequent
independent re-checks.
