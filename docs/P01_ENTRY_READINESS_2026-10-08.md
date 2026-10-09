# SafeEvidence P01 Entry Readiness — Authorization Ledger

Date: 2026-10-08 (Asia/Riyadh)
Status: **P01_PRE_ENTRY_GATES_PENDING / P01-G01 PREPARED_NOT_ACTIVATED**

## Verified existing foundation

P00 CLOSED_CANONICAL: main at start
`ad9f7b972d4d0cb3dc388ce4caa6c18e369e3b22`.
Genuine Codex + Opus planning acceptance at
`9368e09e3e31df3176404e7b2b86b54a6a5aac08`.
PR #2 normal merge, post-merge CI passed:
https://github.com/TheHalfMoon/SafeEvidence/actions/runs/37720457008

Existing first P01 grain is only prepared:
`docs/reviews/P01_G01_PREPARED_2026-10-08.md`.

GitHub authorities:
- P01 umbrella and owner tracker: https://github.com/TheHalfMoon/SafeEvidence/issues/3
- Founder/product/clinical decisions: https://github.com/TheHalfMoon/SafeEvidence/issues/4
- Source rights + signed-pack trust: https://github.com/TheHalfMoon/SafeEvidence/issues/5

## Proposed first-use wedge — NOT ratified

Adult population-level benefit, harm, comparison, conflict and uncertainty
questions from clinician/research users, in an English/Arabic local desktop
evidence workstation. Default medical answer requires traceable evidence and
may abstain or ask for context. Windows CPU-only 16 GB-class is the first
engineering measurement target, **not a verified product performance claim**.

Out of initial scope: patient-specific diagnosis/treatment/prescribing, doses,
autonomous triage, pregnancy, pediatrics, unsupported clinical drug interaction
or guideline execution, broad regulatory approval claims, and mandatory paid
inference/cloud.

Specialty, exact question inclusion/exclusion taxonomy, release jurisdiction,
clinician setting, dataset/corpus coverage, quantified risk/coverage thresholds,
clinical adjudicator source and funding are still UNDECIDED.

## Explicit entry gates

| Gate | Owner qualification needed | Required evidence | Current state |
|---|---|---|---|
| P00 independent closure | Engineering governance | Verified main + post-merge CI | PASS — planning only |
| Intended-use scope | Founder and qualified clinical safety owner | Signed taxonomy, setting, jurisdictions, Arabic lane and exclusions | UNAPPROVED — Issue #4 |
| Clinical evaluation | Founder and qualified evaluation lead | Ethical rater recruitment/consent/funding, gold protocol, independent adjudication, study/time split and acceptance plan | UNAPPROVED — Issue #4 |
| First corpus and import | Product/evidence rights owner | Concrete source/license/grant rights and separately eligible metadata/full-text | NO_ADMISSIONS — Issue #5 |
| TUF/pack trust before use | Release/security owner | Key custody, root/targets roles, expiry/freeze/rollback/compromise and offline clock | UNAPPROVED — Issue #5 |
| Original 41 P1 tracking | Named accountable phase owners | Issue/task per ID, actual approval and evidence at phase entry | ROLE_ONLY — Issue #3 |
| P01-G01 activation | P01 governance | All applicable entry approvals above checked at exact revision | BLOCKED |
| G01a synthetic-only proposal | Founder and named engineering owner | Explicit Option B at exact governance revision, accountable owner and separately reviewed ratification | G01A_NOT_ACTIVATED — Issue #17 |

## Proposed conditional sequencing — NOT EFFECTIVE

G01A_NOT_ACTIVATED. Current default is Option A: the existing full P01
prerequisite gate remains binding. Founder decision:
https://github.com/TheHalfMoon/SafeEvidence/issues/17.

If and only if the founder formally selects Option B at an exact governance
revision, names an accountable engineering owner, and ratifies the governing
documents, a separately reviewed G01a implementation may be authorized for
an offline, standard-library-only Rust workspace and nonclinical synthetic
tests. That conditional engineering exception includes no source/admitted
dependency imports (NO_ADMISSIONS), no patient/clinical data, no medical
answer UI or algorithms, no model or article text, no evidence-pack verifier
or signing, no remote runtime and no product release. It cannot itself close
P01 or start P02. The 41 original P1 acceptance gates remain intact.

Founder authorization of G01a is **not** an intended-use or clinical
evaluation signoff. All clinical/evaluation work remains blocked by Issue #4,
and donor/code/data/asset rights and pack/release trust by Issue #5.
Neither a generic continuation instruction nor this proposed text records
a qualified clinical, rights or security approval.

## Scope of authorized pre-entry activity

Allowed: document charter options, record tracking responsibilities, study
rights-admitted donor CI patterns without importing source bytes, plan baseline
checks, create draft PRs and validate documentation only.

Not authorized by this document: product-code implementation, P01-G01 closure,
clinical answer release, actual source import, TUF trust operation, use of
patient data or promotion to P02.

Missing qualified approver/rights/evidence is a stop condition, not a detail
that agents may fill in. The founder's general continuation request authorizes
preparation but does not constitute a specific clinical or legal approval.
