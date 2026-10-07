# SafeEvidence P00 Independent Review Reconciliation — 2026-10-07

Status: `SUPERSEDED_BY_2026_10_08_REPAIR` (historical reconciliation)

Frozen review base: `136cdffc2cd14133e01018ca56833241dd50bc4e`.

Independent inputs:
- Claude/Opus: `review/opus-p00-kill-review-2026-10-07`
- Codex: `review/codex-p00-kill-review-2026-10-07`

Both returned `P00_NOT_READY`.

No material P0/P1 finding is rejected. Overlapping findings are merged and
phase-specific findings are bound to their owning phase.

## P0 reconciliation

1. **Data planes — ACCEPTED.** Separate public/rebuildable evidence from
   encrypted private authority. Never place a PubMed-scale corpus in the private
   whole-file vault.
2. **Vault lifecycle — ACCEPTED.** Do not transplant MedScale EncryptedVault
   whole-file seal/unseal. P02 primary hypothesis is ottari SQLCipher/WAL vault
   plus compatible MedScale lock/claim slices after qualification.
3. **Evidence ontology — ACCEPTED.** Add StudyArm, AnalysisPopulation,
   ArmObservation, Result/OutcomeReport, Comparison, ReportVersionLink,
   SystematicReviewIncludedStudy and participant-overlap semantics.
4. **Assurance contract — ACCEPTED.** Separate ControlAction from
   TerminalOutcome. Reuse commandMed mechanics, not patient lexical rule
   content. DAL negative Study-0 results are prior evidence.
5. **Donor rights — ACCEPTED.** Founder permission assertions are preserved,
   but external copying requires an admissible public license or recorded
   documentary permission reference. See DONOR_RIGHTS_REGISTER.md.
6. **Atomic proof admission — ACCEPTED.** Generated text is committed only
   after an AnswerProofManifest binds evidence, validity, rights, models/tools,
   policy and post-verification result.

## P1 binding

- P01: donor rights, provenance, SBOM/NOTICE and transitive executable/model/data admission.
- P02: placement, vault lifecycle, key custody, ontology, state semantics,
  proof manifest, coordinate/privacy boundaries.
- P03: PubMed sequence completeness, lifecycle, rights, default corpus and
  distribution budget.
- P04/P05: study-level recall, source-family coverage, Arabic/cross-language
  retrieval, no auto-download.
- P06: multidimensional support, typed result extraction, SafeOCR reuse.
- P07: design/result-specific appraisal, temporal patient context, tool catalog.
- P08/P09: deterministic sufficiency incumbent; no V1 confidence percentage.
- P10: no ambient generator tools/network; production pack trust before use.
- P11: Slint vs Tauri remains an open measured tournament.
- P12: narrow offline parser features, sandboxing, SafeOCR critical-value gate.
- P13: CQL correctness is not guideline semantic correctness.
- P14: explicit FHIR loss/reference ledger.
- P15/P16: bounded FFI, native protectors, real-device privacy tests.
- P17: separate pairing/sync capability-rights-revocation contract.
- P18: screening prioritization is not review completeness; refuse unsupported pooling.
- P19: voice remains proposed input until confirmed.
- P20: intended-use cohort, human adjudication and Arabic expertise move earlier.
- P21/P22: OS residuals, confinement, TUF trust and no synthetic release keys.
- P23: claims register is bound to the initial intended-use wedge.

## Initial intended-use wedge

Desktop clinician evidence workstation for population-level medical evidence
questions with exact provenance, claim-to-span verification, current-validity
state, conflict visibility and fail-closed abstention.

Not initially qualified unless separately promoted: autonomous diagnosis,
autonomous treatment ordering, autonomous emergency triage, medication-dose
execution, broad patient-specific recommendation authority, mandatory
meta-analysis, mandatory executable guidelines, voice authority, or full mobile
parity.

## V1 confidence

No user-facing clinical confidence percentage in V1.

## SafeOCR correction

The prior statement that SafeOCR is empty is superseded. SafeOCR is an actual
critical-value OCR verification donor candidate, subject to qualification.

## Status

The initial reconciliation was found insufficient on 2026-10-08. The binding
repair is `docs/P00_REPAIR_CLOSEOUT_PLAN_2026-10-08.md`. No original P0 is
closed until independent reviewer re-checks accept the exact repaired head.

Next: update authority documents, freeze the reconciliation head, obtain
independent Codex and Opus re-checks on that exact head, require zero unresolved
P0, then merge closeout normally to main. No product implementation starts
before P00 closeout.

## Binding P1 acceptance correction

The phase bullets in this historical reconciliation are not executable acceptance criteria. They are superseded by `docs/P00_CODEX_P1_ACCEPTANCE_REGISTER.md` (24 P1) and `docs/P00_OPUS_P1_ACCEPTANCE_REGISTER.md` (17 P1). Each phase gate requires named owner and evidence.
