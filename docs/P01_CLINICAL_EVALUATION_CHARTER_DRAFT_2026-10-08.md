# SafeEvidence P01 Intended Use and Clinical Evaluation Charter

**Status: DRAFT_UNAPPROVED.** No individual has signed this document; it is not
medical validation or a claim that patient data/clinical gold are available.
Ratification: https://github.com/TheHalfMoon/SafeEvidence/issues/4

## A. Initial intended use submitted for approval

Research desktop for a licensed clinician or clinical investigator to explore
population-level evidence in adults: treatment benefit, harm, comparative
estimates, contradictions and uncertainty. It displays exact source provenance,
claim support and current validity. It may abstain or request context.

No autonomous diagnosis, patient-specific therapy, prescribing, emergency
triage, pediatric/pregnancy/dosing or unqualified guideline decisions.
English and Arabic lanes are both evaluation targets, not already validated.

To approve the intended use, qualified clinical safety and founder reviewers
must specify: clinician role/cohort; specialty and included/excluded question
taxonomy; medical setting; country/market/jurisdiction; source corpus bounds;
risk acceptance; numeric useful coverage and unsafe commitment criteria.

## B. Illustrative fixture categories — not clinical truth labels

| Class | Required behavior to evaluate | Status |
|---|---|---|
| Adult population intervention versus comparator | Source/study identity, applicability and exact supportive spans | Synthetic fixture only |
| Benefit/harm with denominator and timepoint | Preserve RR versus absolute risk and confidence interval | Synthetic fixture only |
| Material contradictory review evidence | CONFLICT or justified non-commit | Synthetic fixture only |
| Retracted/licensed source or offline stale data | Current-validity or PARTIAL_REPRODUCTION and abstention | Synthetic fixture only |
| Arabic/English negation and mixed-script units | Exact span/semantic conservatism | Synthetic fixture only |
| Patient-specific dosing, pediatric pregnancy or emergency triage | BLOCKED/ESCALATE/out-of-scope; no autonomous recommendations | Synthetic fixture only |

## C. Proposed gold-label adjudication

1. Qualified independent subject-matter reviewers are recruited with documented
   expertise, ethics/consent, conflicts, financing or acceptable volunteer
   engagement. No fabricated signers or AI-labeled "clinician gold".
2. Freeze target question and evidence-sampling protocol, sample-size rationale
   and analysis before experiments. Group by StudyId/Report versions, overlap
   and temporal strata; reserve sealed time/study holdouts.
3. Two blinded independent annotators classify question answerability, terminal
   outcome, clinical applicability, study/result identity, citation support,
   exact span, units/denominator/timepoint, currentness and contradictions.
4. Disagreement is adjudicated by an approved third reviewer or prespecified
   method. Record inter-rater agreement, uncertainty and review revisions.
5. No model is permitted to train, tune or choose its own evaluation labels;
   no reserved holdout/source leak through retrieval, translation or prompting.
6. Article text, PHI and licensed guideline content remain rights-scoped;
   no patient data in public repositories or test logs.

## D. Predeclare metrics and uncertainty

- Unsafe commit rate on cases independently judged to require non-commit;
  report numerator/denominator, language/source/risk strata and confidence
  intervals, including zero-event uncertainty.
- Useful correct-supported coverage on eligible answerable cases; report
  needless abstention and false escalation separately.
- Per-claim exact span and numerical/statistical support, source version and
  legal availability; no generic clinical confidence percentage.
- Negative lanes for mixed Arabic, ambiguous unit/negation, duplicate reports,
  unsupported clinical intent, revoked source and offline freshness.
- Reproducibility/performance (non-clinical): actual CPU/RAM/disk/offline
  cold-start measurements at frozen artifact revisions.

No performance threshold, sample count, comparator superiority, regulatory
claim or power calculation is asserted before qualified protocol approval.

## E. Signoff and resourcing ledger

| Actual required approver | Status | Evidence pending |
|---|---|---|
| Founder/product | NOT_SIGNED | Included questions, geography, corpus/cost and intended-use |
| Qualified clinical safety lead | NOT_IDENTIFIED | Risk matrix, exclusions and clinical approval |
| Qualified evaluation lead | NOT_IDENTIFIED | Human raters, funding, gold rubric, split and thresholds |
| Evidence/document rights owner | NOT_IDENTIFIED | Allowed article/corpus terms and retention |
| Release/security owner | NOT_IDENTIFIED | Offline trust and model/data distribution policy |

Approval event ID: PENDING
Accepted charter revision/SHA: PENDING
Qualified signer identity/role proof: PENDING
Consent/ethics and funding plan: PENDING
Approved quantitative risk/coverage targets: PENDING

Until the relevant signatures and resources exist, all clinical evaluation,
promotion, product claims and imported rights-sensitive source material remain
BLOCKED. General founder project-continuation authorization does not waive this
decision record.
