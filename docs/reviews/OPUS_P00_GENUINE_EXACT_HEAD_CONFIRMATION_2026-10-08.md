# SafeEvidence P00: final independent Opus review

**Verdict: `P00_READY_TO_CLOSE`**

This review covers documentation only. It does not say the code was tested, that any contract has been built, or that the product is clinically safe, compliant, secure or ready to release.

## 0. Identity and scope

| Item | Value |
|---|---|
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), working on its own as Claude/Opus |
| SHA under review | `9368e09e3e31df3176404e7b2b86b54a6a5aac08` (`reconcile/p00-opus-minor-repair-2026-10-08`), detached worktree |
| Previous Opus recheck | `d2280cae49fe37c4b3621400788e61f113d83b46`: `P00_RECONCILIATION_NEEDS_MINOR_REPAIR` (R1 and R2 required, R3 recommended) |
| Inputs | `_independent_review_inputs/OPUS_ORIGINAL.md`, `_independent_review_inputs/OPUS_PREVIOUS_RECHECK.md` |
| Method | Read-only file reads and searches. No git, network or writes. |

**What I read at this SHA:**
- **The six repaired files:**
  - `docs/PRODUCT_THESIS.md`
  - `docs/COPY_FIRST_SOURCE_PLAN.md`
  - `docs/MASTER_PLAN.md`
  - `docs/SOURCE_LEDGER.md`
  - `docs/FOUNDATION_GAP_AUDIT_2026-10-07.md`
  - `docs/PREBUILD_KILL_REVIEW_2026-10-07.md`
- **Checks against the documents the earlier dispositions rely on:**
  - `docs/P00_DECISION_ASSURANCE_CONTRACT.md`
  - `docs/DONOR_RIGHTS_REGISTER.md` (read in full)
  - `docs/P00_OPUS_P1_ACCEPTANCE_REGISTER.md`
  - `docs/P00_REPAIR_CLOSEOUT_PLAN_2026-10-08.md`
  - `AGENTS.md`
- **Searches across the whole repo** for:
  - the withheld donor's identity;
  - old guideline copy directives;
  - old state words such as a bare `EMERGENCY`.

## 1. Required repairs

| Repair | Result | Evidence |
|---|---|---|
| **R1**: `PRODUCT_THESIS.md` §5 | **SATISFIED** | `docs/PRODUCT_THESIS.md:102-126` now separates `ControlAction` (RETRIEVE_EVIDENCE, USE_TOOL, REQUEST_CONTEXT) from `TerminalOutcome` (ANSWER … BLOCKED, EMERGENCY_NOTICE). It says a ControlAction is never an answer commitment, `EMERGENCY_NOTICE` is disabled in V1 and is not autonomous emergency triage, and points to `P00_DECISION_ASSURANCE_CONTRACT.md` for precedence, limits, reason codes and metrics. This matches the contract (`:9-21`, `:45-47`) and `MASTER_PLAN.md:341-349`. |
| **R2**: guideline donor that is not public | **SATISFIED** | **`COPY_FIRST_SOURCE_PLAN.md:226`**: the source is "non-public, unqualified research reference (identity withheld)", marked `REFERENCE_ONLY`, with no copying, adaptation or claim that it is ready to implement.<br>**`MASTER_PLAN.md:901-907`**: P13 is limited to guideline documents provided by users or institutions plus metadata-only links, with per-item rights and checks on issuer, jurisdiction and version. Semantic verification stays research-only, and source code that is not public is not an admitted donor.<br>**`SOURCE_LEDGER.md:353-356`**: identity withheld, research-only, no assumed admission.<br>**`FOUNDATION_GAP_AUDIT_2026-10-07.md:256-259`**: SE-G012 is now REFERENCE_ONLY with no reuse of code and no clinical claim.<br>A repo-wide search outside the input folder finds no remaining identity string and no "COPY/ADAPT" or "P13 uses … semantics" directive. The earlier recheck allowed either a founder decision on disclosure or a neutral label; the neutral label was used, which fits `AGENTS.md:111`. |
| **R3**: old readiness matrix | **SATISFIED** | `PREBUILD_KILL_REVIEW_2026-10-07.md:387-391` now has the marker `SUPERSEDED_BY_P00_REPAIR_2026_10_08` directly above the matrix. It states the `RESOLVED` rows do not close findings, do not authorise copying and do not show tested capability. The existing notice at `:435-442` agrees. |

## 2. Original P0 dispositions

| ID | Disposition | Basis |
|---|---|---|
| OPUS-P00-001 (data planes and corpus scope) | **CLOSED_BY_RECONCILIATION** | Carried over from the previous recheck. The repaired files do not touch the data-placement contract or the runtime budget. `AGENTS.md:227` still says the data planes are separate. |
| OPUS-P00-002 (third-party rights contamination) | **CLOSED_BY_RECONCILIATION** | I checked this again at this SHA. The import ledger is still `NO_ADMISSIONS`, an asserted grant is still treated as "deny-for-copy", and the copyleft corrections for trialstreamer, robotreviewer, Signthos and Slint are unchanged (`DONOR_RIGHTS_REGISTER.md:59-117`). R2 also removes the last copy directive that went around these rules. |

## 3. Original P1 dispositions (OPUS-P00-003 to -019)

| ID | Topic | Disposition |
|---|---|---|
| 003 | Vault durability | PRECISELY_PHASE_BOUND (P02) |
| 004 | Pack trust / TUF | PRECISELY_PHASE_BOUND (P01 ADR, before P10) |
| 005 | State semantics | **RESOLVED** (design). The remaining vocabulary problem in the thesis was fixed by R1; tests come at P02/P08. |
| 006 | DAL negative prior | RESOLVED |
| 007 | Calibration estimand | RESOLVED (no clinical percentage in V1) |
| 008 | Study model | RESOLVED (design); fixtures at P02/P18 |
| 009 | Statistical synthesis | PRECISELY_PHASE_BOUND (P18 statistician gate) |
| 010 | PubMed XML / JATS ingest | PRECISELY_PHASE_BOUND (P03) |
| 011 | SafeOCR status | RESOLVED (planning); qualification at P12 |
| 012 | Arabic across languages | PRECISELY_PHASE_BOUND (P05) |
| 013 | Too many runtimes | PRECISELY_PHASE_BOUND |
| 014 | Medication / FHIR | PRECISELY_PHASE_BOUND (P14) |
| 015 | Guidelines and the non-public donor | **RESOLVED** (governance) and **PRECISELY_PHASE_BOUND** (P13 semantics, rights and regression testing in register row `P00_OPUS_P1_ACCEPTANCE_REGISTER.md:25`). Previously INSUFFICIENTLY_BOUND; R2 closes it. |
| 016 | Snapshots vs deletion / revocation | RESOLVED (design) |
| 017 | Support labels / facets | PRECISELY_PHASE_BOUND (P06) |
| 018 | Desktop shell conflict | PRECISELY_PHASE_BOUND (open tournament) |
| 019 | Adjudication resourcing | PRECISELY_PHASE_BOUND (P01 charter, otherwise BLOCKED) |

**Totals:** RESOLVED 6 (plus 015 as resolved and phase-bound), PRECISELY_PHASE_BOUND 10 (counting 015), INSUFFICIENTLY_BOUND 0, REGRESSED 0. All rows except 005 and 015 are carried over from the previous recheck; the edits did not change the documents those rows rely on.

## 4. New P0, regressions and contradictions

- **New P0:** none.
- **Regressions:** none.
- **Material contradictions:** none.
- **Minor wording left over (P2, not blocking):** two places still use the commandMed donor's own state words, including a bare `EMERGENCY`:
  - `COPY_FIRST_SOURCE_PLAN.md:124` (strategy "COPY tests");
  - `SOURCE_LEDGER.md:33`.

  Both describe the donor, not SafeEvidence's own states. Each is already overridden by:
  - `COPY_FIRST_SOURCE_PLAN.md:330-331`: commandMed's lexical policy content for patients is not copied unchanged;
  - `SOURCE_LEDGER.md:345-346`: commandMed is used for its mechanics and as an oracle only;
  - the precedence and stop-on-conflict rule in `AGENTS.md:240-242`;
  - the empty import ledger.

  An optional later fix is to relabel both as "donor vocabulary; mapped per decision contract".
- **Optional, not required:** `DONOR_RIGHTS_REGISTER.md` has no row for the withheld reference. It does not need one: it has no admission, and the ledger defaults to denying copies.

## 5. External gate still open (separate from this verdict)

Closing P00 still depends on outside checks I could not do here:
1. **Exact-head CI:** CI must pass on exactly `9368e09e…` and the head must not move. I ran no CI, git or network commands, so I have not seen a CI result or the live head.
2. **Diff scope:** the change from `d2280ca` to `9368e09` should be confirmed to touch only the six documentation files listed in §0.
3. **Codex:** the matching Codex recheck of the same exact head must agree, as `P00_REPAIR_CLOSEOUT_PLAN_2026-10-08.md:77-78` requires.

## 6. Limitations

- I took the SHA and branch from the worktree context and your brief. I did not confirm them with git.
- I did not list the changed files myself. Instead I checked that all R1, R2 and R3 fixes are present in the six target files, searched the whole repo for regressions, and spot-checked the documents the carried-over dispositions rely on. Item 2 in §5 is the outside check that would confirm the diff scope.
- I did not re-inspect any donor source code. Donor facts come from the original Opus review.
- These contracts are documented design decisions and gates. None is implemented or tested, and nothing here shows medical validity, clinical safety, regulatory compliance, security or release readiness.

I made no changes to files, the repo, PRs or GitHub.

---

## Final Opus disposition clarification (second read-only Opus invocation)

**Reviewer decision on SafeEvidence P00 (Claude Opus, read-only)**

**Reviewed SHA:** `9368e09e3e31df3176404e7b2b86b54a6a5aac08`

**What I checked:** I read the parts of the four named docs that the closing questions depend on. I didn't redo the full targeted review. I made no edits to files, git, the repo or the network.

- **`docs/P00_OPUS_P1_ACCEPTANCE_REGISTER.md`**
  - The status is `OPEN_PHASE_GATES`. The register says plainly that it does not claim the tests were run or the repair accepted.
  - Row OPUS-P00-015 (line 25) ties the finding to the P13 guideline gate and names a responsible owner (guideline and rights owner).
  - The decision that must come first is to limit early guidelines to documents the user or institution provides, plus metadata links, with no unqualified disclosure of private donors.
  - Acceptance evidence is listed: jurisdiction, version, issuer and scope; source rights; and semantics checked against a CQL regression.
- **`docs/COPY_FIRST_SOURCE_PLAN.md:226`** The private guideline donor now appears only as a "Non-public, unqualified research reference (identity withheld from public documentation)", marked `REFERENCE_ONLY` with no copying, adaptation or readiness claimed. This fixes the original disclosure problem.
- **`docs/PRODUCT_THESIS.md:250-281`** and **`docs/PREBUILD_KILL_REVIEW_2026-10-07.md`** Their wording on the qualified first target and out-of-scope items matches the register and the copy plan. I found no contradictions.

**Single disposition for OPUS-P00-015: PRECISELY_PHASE_BOUND.** The private-donor disclosure problem is fixed in the docs. But the finding's acceptance evidence is the P13 guideline qualification gate, which hasn't been met yet. Of the two labels, only PRECISELY_PHASE_BOUND fits the finding as a whole, and that settles the earlier report's double disposition.

**Totals**
- **P0:** 2 closed. OPUS-P00-001 and 002 are CLOSED_BY_RECONCILIATION.
- **P1:** 17 dispositioned:
  - 6 RESOLVED: 005, 006, 007, 008, 011, 016.
  - 11 PRECISELY_PHASE_BOUND: 003, 004, 009, 010, 012, 013, 014, 015, 017, 018, 019.
- **New P0:** 0
- **Regressions:** 0
- **Material contradictions:** none

**Not covered by this review:** product code, clinical tests and CI on the exact PR head are not part of the reviewed source. This decision doesn't vouch for any of them.

**FINAL VERDICT: P00_READY_TO_CLOSE**

— Reviewer: Claude Opus

---

*Artifact preservation note (not authored by Opus): the two blocks above reproduce the outputs of the two read-only Claude Opus CLI invocations on 2026-10-08 against the detached checkout at SHA `9368e09e3e31df3176404e7b2b86b54a6a5aac08`. The reviewer did not modify GitHub and did not execute clinical/product tests. The second block resolves the original classification ambiguity for OPUS-P00-015; do not double-count it.*
