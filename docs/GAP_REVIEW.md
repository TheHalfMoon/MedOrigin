# SafeEvidence Foundation Gap Review Protocol

Status: `FOUNDATION_DRAFT`

This document defines how Codex, Claude/Opus, and other reviewers must challenge the SafeEvidence foundation before implementation is promoted.

The goal is not to agree with the plan. The goal is to find what would make the product unsafe, scientifically weak, architecturally expensive, privacy-breaking, non-portable, untestable, or impossible to release.

## 1. Independent review rule

Run at least two independent reviews before reconciliation:

```text
Review A: Codex
Review B: Claude/Opus
```

Each reviewer reads the repository authority directly and produces its own gap report before reading the other reviewer's conclusions when practical.

Model agreement is not correctness. A shared blind spot remains a blind spot.

## 2. Required authority to review

At minimum:

- `README.md`
- `docs/PRODUCT_THESIS.md`
- `docs/ARCHITECTURE.md`
- `docs/SOURCE_LEDGER.md`
- `docs/MASTER_PLAN.md`
- `docs/GAP_REVIEW.md`
- `AGENTS.md`

Reviewers must inspect relevant donor/source repositories rather than trusting SafeEvidence's summary when a material design choice depends on them.

## 3. Gap severity

```text
P0  The plan must not proceed while this is unresolved.
P1  Material gap; must have an owner, explicit resolution/defer decision, and owning phase.
P2  Important refinement; safe to schedule after the first implementation horizon if dependencies permit.
P3  Nice-to-have/product optimization/documentation improvement.
```

A gap's severity is based on consequence and architectural lock-in, not how easy it is to fix.

## 4. Required review dimensions

### A. Product definition

Challenge:

- primary user and workflow;
- whether desktop/mobile scopes are coherent;
- whether SafeEvidence duplicates MedScale or another sibling product unnecessarily;
- whether the product has a sufficiently narrow initial wedge;
- whether Deep Review, Guidelines, FHIR, OCR, voice, and mobile are correctly sequenced;
- whether non-goals are strong enough to prevent product sprawl.

### B. Clinical/safety boundary

Challenge:

- diagnosis/treatment/triage/prescribing implications;
- emergency behavior;
- deterministic tool boundaries;
- missing-context handling;
- unsafe overcommitment;
- conflict handling;
- clinician review expectations;
- evidence vs recommendation vs action authority;
- research-vs-clinical claim separation.

### C. Evidence science

Challenge:

- source identity;
- retraction/correction/supersession;
- rights/access classes;
- retrieval evaluation;
- citation existence vs claim support;
- evidence appraisal;
- patient applicability;
- guideline conflicts;
- rapidly changing evidence;
- benchmark leakage/contamination;
- source diversity;
- human adjudication.

### D. Decision assurance and calibration

Challenge:

- whether proposed targets/estimands are well-defined;
- whether probabilities can be calibrated with realistic data;
- whether selective-risk metrics match product harm;
- whether threshold tuning can leak final evaluation;
- whether high-confidence wrong cases are explicitly tested;
- whether model disagreement is mishandled as confidence;
- whether deterministic controls remain competitive baselines;
- whether domain/temporal shift invalidates displayed probabilities.

### E. Retrieval/RAG architecture

Challenge:

- lexical baseline adequacy;
- vector/reranker value vs complexity;
- offline index build/update;
- multilingual retrieval;
- chunking/source-span stability;
- permission-scoped caches;
- stale/deleted source propagation;
- prompt injection from retrieved content;
- memory/disk/latency on target hardware.

### F. Document/OCR pipeline

Challenge:

- hostile documents;
- parser/OCR isolation;
- page/region/table lineage;
- scanned vs born-digital behavior;
- Arabic OCR;
- medication/numeric/unit/negation errors;
- visual/table ambiguity;
- correction provenance;
- large-file cancellation/recovery.

### G. Guideline verification

Challenge:

- source-faithful semantic representation;
- version/jurisdiction/population;
- non-computability;
- CQL/CPG-on-FHIR correctness assumptions;
- recommendation strength/certainty separation;
- human review;
- conflicting/superseded guidelines.

### H. Patient context and interoperability

Challenge:

- whether context fields are sufficient/too broad;
- identity mismatch;
- FHIR profile/version loss;
- missing/unknown semantics;
- source provenance;
- read-only boundary;
- Saudi/NPHIES expansion;
- accidental EHR/product-scope expansion.

### I. Privacy and data lifecycle

Challenge every data class through:

```text
collect/import
 -> decrypt/use
 -> cache/index
 -> model context
 -> log/diagnostic
 -> backup
 -> sync
 -> export
 -> delete/revoke
```

Include OS snapshots, swap, temp files, WAL/journals, crash dumps, screenshots, clipboard, notification previews, mobile backups, support bundles, and model caches.

### J. Security/trust boundaries

Challenge:

- UI-to-core authentication;
- capability issuance;
- worker sandboxing;
- secrets;
- network broker;
- SSRF/redirect/DNS policy;
- update/supply chain;
- untrusted documents/web content;
- prompt/tool injection;
- pack signatures/revocation;
- backup/restore integrity;
- local attacker assumptions.

### K. Desktop architecture

Challenge:

- Tauri/WebView privacy;
- startup/RAM;
- native file integration;
- accessibility;
- offline install/update;
- Windows/macOS/Linux behavioral differences;
- signing/distribution cost/requirements.

### L. Mobile architecture

Challenge:

- Rust FFI complexity;
- SwiftUI/Compose divergence;
- model size/RAM/thermal/battery;
- background restrictions;
- camera/import flow;
- Keychain/Keystore;
- biometric fallback;
- notification/app-preview privacy;
- pack size/storage quotas;
- offline operation;
- App Store/Play policy/distribution.

### M. Pairing and synchronization

Challenge:

- bootstrap replay/race;
- device revocation;
- conflict resolution;
- source/evidence snapshot identity;
- selective sync;
- key ownership;
- lost/stolen device;
- public relay behavior;
- interrupted transfers;
- backup interaction.

### N. Arabic/internationalization

Challenge:

- RTL;
- Arabic medical terminology;
- mixed Arabic/Latin drug names;
- cross-language retrieval;
- Arabic OCR/ASR;
- translation provenance;
- Arabic safety triggers;
- locale/jurisdiction distinctions.

### O. Accessibility

Challenge keyboard, focus, screen reader, contrast, reflow, large text, touch targets, non-visual alternatives to graphs/heatmaps, and error/uncertainty semantics.

### P. Performance and resource budgets

Challenge:

- CPU-only minimum;
- hardware acceleration optionality;
- peak RAM;
- disk/index growth;
- mobile thermal/battery;
- long deep-review jobs;
- cancellation;
- OOM/disk-full behavior;
- pack update bandwidth;
- cold-start latency.

### Q. Source/license/provenance

For every proposed donor/dependency/model/data/asset:

- exact revision/digest;
- source path;
- code license;
- model/data/asset license;
- separate permission if relied upon;
- embedded/transitive material;
- notices;
- trademark/branding boundaries;
- commercial redistribution;
- app-store distribution implications;
- update and exit strategy.

### R. Benchmark and statistical methodology

Challenge:

- benchmark representativeness;
- calibration/test separation;
- hidden/final holdout governance;
- sample-size/power rationale where claims require it;
- confidence intervals;
- multiple comparisons;
- adjudication;
- inter-rater agreement;
- subgroup reporting;
- contamination;
- reproducibility.

### S. Release and operational resilience

Challenge:

- migrations;
- rollback;
- corrupted pack/model/index;
- revoked source;
- stale evidence;
- clean install;
- updater failure;
- offline recovery;
- backup restore;
- diagnostics/support without PHI leakage.

### T. Regulatory/claims boundary

Challenge whether any README/UI/marketing/benchmark wording could imply:

- medical-device clearance;
- clinical validation;
- diagnosis/treatment authority;
- HIPAA/GDPR/PDPL compliance;
- SFDA approval;
- formal GRADE equivalence;
- OpenEvidence/Abridge superiority;
- safety guarantees.

Software must not self-certify those claims.

## 5. Required gap format

Every material finding must use:

```text
GAP_ID:
SEVERITY: P0 | P1 | P2 | P3
AREA:
CLAIM_OR_ASSUMPTION_CHALLENGED:
EVIDENCE:
FAILURE_MODE:
WHY_IT_MATTERS:
AFFECTED_DOCS_PHASES:
PROPOSED_RESOLUTION:
ALTERNATIVES:
DECISION_OWNER:
BLOCKS_IMPLEMENTATION: yes/no
VERIFICATION_REQUIRED:
```

Avoid vague comments such as "security needs more thought."

## 6. Source-challenge requirement

For high-impact source choices, reviewers must compare at least:

```text
keep current candidate
use a smaller/simpler alternative
build SafeEvidence-native
remove/defer the capability
```

"Source is permitted" is not a technical reason to adopt it.

## 7. Reconciliation

After independent reviews:

1. normalize duplicate findings;
2. preserve genuine disagreement;
3. classify each gap P0-P3;
4. amend foundation docs for accepted resolutions;
5. create decision records for contested architecture choices;
6. add each deferred material gap to the exact owning phase;
7. rerun both reviewers against the amended exact commit;
8. do not claim `NO_KNOWN_PLANNING_GAP` until the coverage matrix below is complete.

## 8. Foundation coverage matrix

The final P00 closeout must report each dimension as:

```text
CHALLENGED_AND_RESOLVED
CHALLENGED_AND_DEFERRED_WITH_OWNER
BLOCKED
NOT_APPLICABLE_WITH_REASON
```

Dimensions:

- product;
- clinical safety;
- evidence science;
- retrieval;
- claim/citation verification;
- decision assurance;
- calibration;
- guidelines;
- documents/OCR;
- interoperability/patient context;
- vault/storage;
- privacy;
- security;
- desktop;
- mobile;
- pairing/sync;
- Arabic/i18n;
- accessibility;
- performance/resources;
- provenance/licenses;
- benchmarks/statistics;
- release/update/recovery;
- regulatory/claims;
- cost/zero-cloud assumptions.

`NO_KNOWN_PLANNING_GAP` means only that the defined review coverage found no unresolved unknowns at that revision. It is not evidence that the product is safe, clinically valid, secure, compliant, or release-ready.