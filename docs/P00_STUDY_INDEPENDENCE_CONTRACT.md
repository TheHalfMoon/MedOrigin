# P00 Study/Result Independence Contract

Status: P00_BINDING_CONTRACT
Owners: evidence-science architect and statistician.
Resolves missing contract aspects of CODEX-P00-03 and OPUS-P00-008.

## Required identities and cardinality

- StudyId: investigation/trial/cohort, not PMID/DOI.
- ReportId/ReportVersionId: immutable artifact/version; Study M:N Report,
  with evidence-bearing StudyReportLink and status.
- StudyArmId: Study 1:N arms, intervention and randomized/eligible/analyzed N.
- AnalysisId: one Study or explicit PooledStudySet, analysis population
  (ITT/mITT/PP/subgroup), model, adjusted covariates, timepoint, estimand.
- OutcomeId: registered or observed definition, unit, timepoint and method;
  RegisteredOutcome ↔ ReportedOutcome preserves discrepancies.
- ResultId: Analysis + Outcome + timepoint + source/version/span,
  not just one EffectEstimate for every publication.
- ArmObservationId: Result + Arm with events/total or mean/SD/N,
  denominator/source provenance, missingness and units.
- ComparisonId: arm contrast, shared comparator and covariance reference.
- EffectEstimateId: Result + Comparison, RR/OR/HR/RD/SMD etc., adjusted state,
  point/CI/SE/variance, transform provenance and supplied covariance.
- ReviewIncludedStudyLink: Review/Study/Result membership with decisions.
- ParticipantOverlapGroupId: overlapping participants/reports/reviews/pooled
  analyses; overlap can be CONFIRMED, POSSIBLE or UNKNOWN.
- ReportVersionLink: protocol/preprint/published/follow-up/correction/
  expression of concern/retraction with current validity.
- SynthesisInputDecision: accepted or refused ResultIds, independence
  evidence, supported model and source version.

Every typed ID is scoped and versioned; unknown is explicit, not coerced null.
Machine-suggested study/registry links remain PROPOSED until corroborated
or confirmed by the admitted linkage policy/human reviewer.

## Double-count protection

A different report, journal, timepoint, study subgroup, pooled IPD synthesis,
or systematic review is NOT a new independent study. Pooling requires either
one independent contribution per participant group or a qualified method using
known covariance/cluster/repeated-measure structure. Otherwise emit
POOLING_REFUSED_UNIT_OF_ANALYSIS. Narrative synthesis remains available.

Each quantitative result preserves original text/table row+column coordinates,
sample denominator, chosen timepoint, adjusted estimand, uncertainty method,
extraction status and human adjudication; no OCR proposal silently becomes an
admitted effect.

## P02/P18 qualification fixtures

Protocol/registry/abstract/preprint/primary/follow-up/correction of one RCT;
different trials with matching titles; shared-control multi-arm; mixed ITT/PP;
subgroup plus parent cohort; repeat timepoints; pooled IPD plus component
trials; review plus included trial publications; trial outcome switched after
registration; unknown covariance and missing denominator. Validate no
false merge, false split or double counted participant contribution.
EBMonFHIR is the interop crosswalk, not the database authority.
