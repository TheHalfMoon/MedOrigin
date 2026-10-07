# SafeEvidence: Independent P00 Kill Review

Review date: 2026-10-07. Verdict: **P00_NOT_READY**.

Frozen product SHA: `136cdffc2cd14133e01018ca56833241dd50bc4e`. Live main observed during this audit: `136cdffc2cd14133e01018ca56833241dd50bc4e`. Review branch: `review/codex-p00-kill-review-2026-10-07`. This is a proposed independent review, not an authority amendment, reconciliation, product implementation, safety certification or release approval.

## Independence and method

The exact commit was fetched directly and checked out before reviewing authority. No newer product commit, review branch, review PR, post-base review artifact, other reviewer's conclusions or later reconciliation was read. The pre-existing FOUNDATION_GAP_AUDIT and PREBUILD_KILL_REVIEW at the exact base were mandatory inputs and were challenged rather than accepted as truth. No independent-review contamination was encountered.

The complete mandatory authority set was read: AGENTS.md, README.md, THIRD_PARTY_NOTICES.md, PRODUCT_THESIS.md, ARCHITECTURE.md, SOURCE_LEDGER.md, COPY_FIRST_SOURCE_PLAN.md, REUSE_FIRST_IMPLEMENTATION_MAP.md, DONOR_TRANSPLANT_PROTOCOL.md, RUNTIME_BUDGET.md, FOUNDATION_GAP_AUDIT_2026-10-07.md, PREBUILD_KILL_REVIEW_2026-10-07.md, MASTER_PLAN.md and GAP_REVIEW.md, plus Issue #1 foundation body/comments. Issue filtering used the base commit time `2026-10-07T00:28:49Z`; body lastEditedAt was null. Included foundation comments: [6019210092](https://github.com/TheHalfMoon/MedOrigin/issues/1#issuecomment-6019210092), [6027280967](https://github.com/TheHalfMoon/MedOrigin/issues/1#issuecomment-6027280967), [6027361439](https://github.com/TheHalfMoon/MedOrigin/issues/1#issuecomment-6027361439), all created and updated before the cutoff. Later comment bodies were excluded before display/inspection.

Donor live default-branch heads were inventoried separately from the frozen product and pinned for source inspection. Selective code, manifests, tests, fixtures and actual license files were inspected; fetched files alone were not counted as inspected. Links below resolve to exact inspected revisions. This was not a full contributor-title, transitive-license, CVE, dependency-execution or medical-validation audit. ProtocolWISE was inaccessible at attempted public locations; no inspected revision or readiness is claimed. Official Europe PMC terms returned HTTP 403; rights there remain unverified.

Executed evidence: an AST-extracted commandMed rule probe, an AST-extracted statsmodels function probe with numpy and limited harness substitutions, and resource/sample-size arithmetic. No full donor test suite, clinical benchmark, native-device suite, parser bakeoff, TUF conformance run or app privacy test ran. Jev was attempted for review-scope classification using public path/action metadata only; it returned `Not logged in; run jev login` (exit 1), so no judgment was obtained. The installed native CLI differed from the skill's Python CLI. No Alibaba Open Code Review callable was available; the available code-review tool reads PR CI diagnostics and was inapplicable because no PR was opened. Tool absence did not substitute for direct inspection. No paid mandatory gate was introduced.

## Executive assessment

The product thesis is implementable as a bounded clinician evidence workstation, but the frozen foundation is not ready to start implementation. Six unresolved P0 decisions affect canonical contracts, storage authority, donor import rights or final answer commitment. Naming Study and assurance states is insufficient to establish participant independence or a measurable justified-answer contract. The chosen MedScale vault slice also contains source-visible recovery/backup hazards that the demand to copy newer writer_lock does not itself resolve.

The roadmap already rejects greenfield search, parsing, updates, bindings and statistics. The major issue is treating a candidate or research oracle as a qualified coherent implementation. The review proposes eight bounded SafeEvidence-specific integration subsystems, not new databases, parser frameworks, vector servers, cryptography, screening algorithms or standard statistical formulas. No evidence here establishes differentiation/superiority over OpenEvidence or clinical safety. A defensible differentiator would be explicit, reproducible justified-commit behavior at useful coverage under a declared clinical task, demonstrated on a human-adjudicated holdout.

P0 closes only after the named foundational decisions and reviewable contracts are bound. P1 findings block the affected phase until resolved or precisely phase-bound; P2/P3 do not independently invalidate the foundation. Proposed owners are roles to assign, not invented appointments. Later-phase qualification tests need not all run in P00.

## Findings

### CODEX-P00-01: Data-plane boundaries are not defined before selecting the vault

**GAP_ID:** CODEX-P00-01

**SEVERITY:** P0

**AREA:** Storage and scale

**CLAIM_OR_ASSUMPTION_CHALLENGED:** A single local-vault foundation can safely serve public corpus, private context, licensed documents, projections and packs.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L433) lists the vault without a concrete placement/custody matrix; [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L57) distinguishes authority from projections but not their independent rights, encryption and retention domains. The preferred vault reads and reseals the entire metadata database.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-storage/src/encrypted_vault.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/encrypted_vault.rs#L155); [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1); [TheHalfMoon/MedScale: crates/medscale-contracts/src/evidence/mod.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-contracts/src/evidence/mod.rs#L1)

**FAILURE_MODE:** A PubMed-sized rebuildable index inherits private-data backup/key/migration costs, or private and licensed derived data leak into a supposedly public corpus pack.

**WHY_IT_MATTERS:** P02 commits schema, key scope and backup semantics used by every later phase. This is a foundational choice, not a request to complete large-corpus benchmarks in P00.

**AFFECTED_PHASES:** P01-P05, P12, P14-P18, P21-P22

**READY_SOURCE_TO_COPY:** SQLite/SQLCipher and existing index libraries; MESC immutable corpus snapshot pattern. No new database or vector engine.

**EXACT_CODE_OR_TESTS_TO_REUSE:** MESC corpus.py snapshot identity; MedScale evidence contracts as a restricted seed; ottari vault_sqlcipher.rs for private storage qualification.

**PROPOSED_RESOLUTION:** Bind a placement table before P01: public/rebuildable corpus store; encrypted private authority; rights-scoped licensed/user document stores; separate rebuildable indexes; read-only verified packs. Include cross-store transactional references, grants, cache scoping, garbage collection and backup inclusion. Private query-derived indexes remain private.

**ALTERNATIVES:** One physical database is possible only with measured bounds and explicit logical domains; a small curated corpus is a simpler first wedge.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Walk one public report, uploaded clinical PDF, institutional article, patient context and saved answer through ingest, indexes, backup, export, sync and deletion. Prove no private item enters distributable pack build.

**DECISION_OWNER:** Principal architect + security/rights owner

### CODEX-P00-02: The selected vault slice has no coherent crash/backup authority

**GAP_ID:** CODEX-P00-02

**SEVERITY:** P0

**AREA:** Durability

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Copying MedScale primitives plus writer_lock yields a ready durable private vault.

**LIVE_EVIDENCE:** [docs/COPY_FIRST_SOURCE_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/COPY_FIRST_SOURCE_PLAN.md#L92) and [docs/DONOR_TRANSPLANT_PROTOCOL.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/DONOR_TRANSPLANT_PROTOCOL.md#L77) correctly demand newer writer ownership but do not bind a coherent revision/slice. In live inspected encrypted_vault.rs:155-169 restart wipes work/sidecars before unsealing the older sealed file; 193-210 whole-file sealing writes the destination directly; 231-240 marker acquisition is check-then-write; 326-342 backup copies sealed state without a current working-DB checkpoint. The separate writer_lock is not held by this EncryptedVault path.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-storage/src/encrypted_vault.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/encrypted_vault.rs#L155); [TheHalfMoon/MedScale: crates/medscale-storage/src/writer_lock.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/writer_lock.rs#L1); [TheHalfMoon/ottari: crates/himsat-core/src/vault_sqlcipher.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_sqlcipher.rs#L539)

**FAILURE_MODE:** Acknowledged working-DB commits can disappear after crash before clean close; interrupted reseal can damage the only sealed copy; backup can omit recent rows. Combining files without a defined lifecycle leaves a second-writer race.

**WHY_IT_MATTERS:** The canonical authority cannot be selected on the basis of independent synthetic primitives. SQLCipher working pages are encrypted; this finding does not falsely claim they are plaintext.

**AFFECTED_PHASES:** P01-P02, P17, P21-P22

**READY_SOURCE_TO_COPY:** ottari has a materially stronger focused snapshot primitive; SQLite/SQLCipher transactions and process-exclusive ownership remain commodity implementations.

**EXACT_CODE_OR_TESTS_TO_REUSE:** ottari vault_sqlcipher.rs:539-665 snapshot_quiesced_sqlcipher_database and embedded tests around 1178 (committed WAL row restored), 1410 (encrypted working files). MedScale writer_lock.rs and cross-process fixtures, only integrated with the chosen authority lifecycle.

**PROPOSED_RESOLUTION:** Choose and document a coherent encrypted database lifecycle before P01. Define acknowledgement durability, persistent SQLCipher DB vs sealed checkpoint roles, journal recovery, atomic replacement/fsync ordering, lock lifetime and backup barrier. Reuse the stronger snapshot slice with its guard, companion modules and tests; do not paste a standalone function.

**ALTERNATIVES:** A persistent SQLCipher database with separately sealed blobs avoids whole-database reseal; a bounded snapshot vault can remain only with explicit transactional checkpoint/recovery.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Real subprocess kill/power-loss fault injection at every acknowledgement/seal/rename/checkpoint step; restore backup while writes occur; two independent processes; wrong key, partial backup and interrupted migration. Static flow inspected, donor crash suite not run here.

**DECISION_OWNER:** Storage architect + security owner

### CODEX-P00-03: Study identity alone does not prevent participant/result double counting

**GAP_ID:** CODEX-P00-03

**SEVERITY:** P0

**AREA:** Evidence ontology

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Study, StudyReportLink, OutcomeDefinition and EffectEstimate are enough canonical additions.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L195) preserves population/comparison/timepoint fields but defines no canonical identities or overlap semantics for arms, result populations, repeated participants, pooled analyses or included-study membership. HL7 profiles explicitly separate group assignment and endpoint statistical model; they are trial-use, not a ready local application schema.

**SOURCE_CODE_INSPECTED:** [HL7/ebm: input/fsh/evidence/p-single-study-evidence.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-single-study-evidence.fsh#L1); [HL7/ebm: input/fsh/evidence-variable/p-group-assignment.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence-variable/p-group-assignment.fsh#L1); [HL7/ebm: input/fsh/evidence/p-endpoint-analysis-plan.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-endpoint-analysis-plan.fsh#L1); [ijmarshall/trialstreamer: trialstreamer/dbutil.py](https://github.com/ijmarshall/trialstreamer/blob/a97cb8332c039e228ef42188c9d966440894e354/trialstreamer/dbutil.py#L5)

**FAILURE_MODE:** A primary report and follow-up are linked to one Study yet two timepoints are pooled as independent; a pooled IPD analysis and its constituent trials are counted twice; subgroup totals are added to whole-trial totals; overlapping reviews masquerade as independent support.

**WHY_IT_MATTERS:** Later extraction/synthesis cannot repair lost population and result identity without migrating canonical contracts and evidence history.

**AFFECTED_PHASES:** P01-P03, P06-P07, P18, P20

**READY_SOURCE_TO_COPY:** EBMonFHIR profiles as semantic crosswalk/reference; ES3 trial-publication linkage patterns. Neither is a full ready local evidence schema.

**EXACT_CODE_OR_TESTS_TO_REUSE:** HL7 GroupAssignment, ParticipantFlowEvidenceVariable, EndpointAnalysisPlan, SingleStudyEvidence and EvidenceSynthesisEvidence profiles; ES3 check_trialpubs_nctids and test/test_bot.py patterns subject to bounded network adaptation.

**PROPOSED_RESOLUTION:** Bind explicit StudyArm, AnalysisPopulation, ArmObservation, Comparison, Result/OutcomeReport, ReportVersionLink and SystematicReviewIncludedStudy semantics (names may differ). Preserve analysis-set and overlap-group IDs, enrollment denominators, adjusted estimand, uncertainty/covariance, registry-to-reported outcome pairing and human linkage state. Never infer independence from distinct report IDs.

**ALTERNATIVES:** A deliberately narrow V1 can store qualified single-study results and prohibit pooling; still preserve overlap/version links for later migration.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Fixtures for protocol/registry/conference/preprint/primary/follow-up/subgroup/secondary analysis, correction/EoC/retraction, IPD and pooled studies, overlapping reviews and reused participants. Assert every synthesis input maps to a declared independent contribution or supplied covariance.

**DECISION_OWNER:** Evidence-science architect + statistician

### CODEX-P00-04: The assurance state vocabulary is not a decision contract

**GAP_ID:** CODEX-P00-04

**SEVERITY:** P0

**AREA:** Decision semantics

**CLAIM_OR_ASSUMPTION_CHALLENGED:** The nine named states define clinically coherent, measurable assurance.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L266) and [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L329) mix orchestration and terminal results. commandMed policy has seven actions, with no direct CONFLICT/ANSWER_WITH_CAUTION semantics. Exact extracted _rule_matches plus the real frozen safety_policy fired for population chest-pain evidence, a patient denying chest pain, an exclusion criterion, and equivalent Arabic evidence/negation cases.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/commandMed: src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py#L1); [TheHalfMoon/commandMed: src/commandmed/spec006/scaffold.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/scaffold.py#L83); [TheHalfMoon/commandMed: data/spec006/safety_policy.json](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/data/spec006/safety_policy.json#L1)

**FAILURE_MODE:** Lexical EMERGENCY suppresses an ordinary clinician question; ASK_MORE loops; USE_TOOL is counted as a clinical commit; CONFLICT is used for irrelevant differences; caution permits unsupported facts.

**WHY_IT_MATTERS:** Commit denominators, thresholds, UI and final answer authority all depend on these definitions. A tournament cannot select an architecture when candidates count different outcomes.

**AFFECTED_PHASES:** P01-P02, P06-P10, P11, P16, P20

**READY_SOURCE_TO_COPY:** commandMed deterministic precedence/trace fixtures, retained as an oracle rather than unchanged clinical policy.

**EXACT_CODE_OR_TESTS_TO_REUSE:** src/commandmed/spec006/policy.py, scaffold.py and tests/spec006/fixtures/{edge-conflicts,us1-tool-routing,us2-context-safety,us3-injection-spoof}.json; adapt the frozen policy with explicit question-intent and negation fixtures.

**PROPOSED_RESOLUTION:** Before P01 separate bounded actions (retrieve/tool/ask) from terminal assurance and per-claim publication. Freeze precedence, reason codes, maximum clarification/retrieval rounds, worker-failure behavior and the precise definition of commit/abstention/false escalation. Population evidence may be answered while patient applicability is explicitly unresolved. EMERGENCY needs clinician-facing semantics and supported current patient evidence, not symptom substrings.

**ALTERNATIVES:** Start with a smaller terminal vocabulary plus orthogonal conflict, missing-context and urgency flags; omit automated emergency classification until qualified.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Property/model checks of termination and precedence; clinician-adjudicated intent/negation/urgency cases in both languages; report risk versus coverage, false escalation and useful coverage separately. Probe tested the lexical function only, not a clinical system.

**DECISION_OWNER:** Clinical safety owner + decision architect

### CODEX-P00-05: Blanket source-code authorization exceeds the founder rights boundary

**GAP_ID:** CODEX-P00-05

**SEVERITY:** P0

**AREA:** Legal source admission

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Permission to copy every discussed implementation is no longer a blocker; remaining rights are only embedded material.

**LIVE_EVIDENCE:** [docs/COPY_FIRST_SOURCE_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/COPY_FIRST_SOURCE_PLAN.md#L5) removes source-code permission as a blocker for the entire discussed universe; [docs/DONOR_TRANSPLANT_PROTOCOL.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/DONOR_TRANSPLANT_PROTOCOL.md#L195) says limiting questions are technical. This cannot grant independent upstream copyrights. Trialstreamer tree has no detected license grant; RobotReviewer is GPL-3.0; Signthos contains AGPL-3.0-only; Slint has custom royalty-free/GPL/commercial options. Repository Apache status does not relicense them.

**SOURCE_CODE_INSPECTED:** [ijmarshall/robotreviewer: docker-compose.yml](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/docker-compose.yml#L1); [slint-ui/slint: LICENSE.md](https://github.com/slint-ui/slint/blob/a199b6bddde18d939886f2a0de0700999fe32851/LICENSE.md#L1); [allenai/scifact: LICENSE.md](https://github.com/allenai/scifact/blob/68b98a56d93e0f9da0d2aab4e6c3294699a0f72e/LICENSE.md#L1)

**FAILURE_MODE:** Unlicensed code is copied or GPL/AGPL/custom licensed code is silently relicensed/rebranded as Apache without satisfying source, attribution or commercial terms.

**WHY_IT_MATTERS:** P01 source imports must have a defensible permission basis before the first transplant. Easy document correction does not reduce this foundational gate.

**AFFECTED_PHASES:** P01 and all donor-derived phases

**READY_SOURCE_TO_COPY:** Permissive sibling slices and permissive generic libraries after file/transitive review. Trialstreamer remains reference-only pending a valid rightsholder grant.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Use MIT ES3 linkage patterns instead of unlicensed Trialstreamer source where suitable; keep RobotReviewer/metafor as separately licensed research/optional workers only after distribution review. Preserve actual LICENSE/NOTICE/REUSE files per copied slice.

**PROPOSED_RESOLUTION:** Before P01 scope founder authorization to rights the founder actually controls or documentary sublicensing permission. Create code/model/data/assets/terminology/publication permission columns, with file-level license and provenance. Copyleft is a conditional distribution choice, not automatically forbidden; worker isolation alone does not waive obligations. Public history/contributor ownership was not exhaustively audited.

**ALTERNATIVES:** Obtain explicit rightsholder permission for a required unlicensed slice; retain public source as behavioral reference and use an independently licensed implementation.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Rights owner signs the exact first-import allowlist, notices and combined-distribution obligations; inspect contributors and embedded code for admitted slices. Unknown rights deny copy, pack, sync and export until resolved.

**DECISION_OWNER:** Founder as rights owner + distribution counsel/maintainer

### CODEX-P00-06: A final answer has no atomic proof-admission boundary

**GAP_ID:** CODEX-P00-06

**SEVERITY:** P0

**AREA:** Evidence before publication

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Evidence sufficiency followed by synthesis and post-answer verification guarantees EVIDENCE BEFORE ANSWERS.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L191) binds many identities, and [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L391) requires post-answer verification, but neither binds a transactional publish authority, dependency-validity watermark or what user-visible partial streaming may expose before verification.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1); [TheHalfMoon/commandMed: src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py#L1); [maziyarpanahi/openmed: openmed/clinical/grounding/snapshot_cache.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/snapshot_cache.py#L1)

**FAILURE_MODE:** A verified candidate is changed by the generator; a correction or revoked source grant arrives during synthesis; partially streamed text reaches the clinician before verification fails. Historical immutable text is mistaken for presently valid evidence.

**WHY_IT_MATTERS:** The first canonical AnswerArtifact and UI event contract must make unverified text uncommitted and distinguish as-of proof from current validity. Bolting this on after P10 would alter every downstream consumer.

**AFFECTED_PHASES:** P01-P02, P03, P06-P10, P11, P16-P18

**READY_SOURCE_TO_COPY:** MESC immutable snapshot and commandMed trace/precedence patterns; existing transaction primitives. No donor supplies the complete SafeEvidence publication contract.

**EXACT_CODE_OR_TESTS_TO_REUSE:** MESC corpus snapshot metadata; commandMed typed traces; OpenMed snapshot_cache/provenance patterns after rights/scope adaptation.

**PROPOSED_RESOLUTION:** Before P01 bind candidate claims, verification results and final text to a proof manifest: source version/span, rights scope, validity watermark, extractor/model/tool/policy identities and decision. Admit final publication atomically after post-verification, or label segregated drafts explicitly. A dependency change invalidates current status without rewriting historical text; offline uncertainty must remain visible.

**ALTERNATIVES:** A deterministic evidence card with no generated assertions is a simpler first committed result; bounded synthesis can follow.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Race correction/retraction/grant revocation against synthesis/publication; worker crash after token generation; stale mobile answer and cache replay. Assert no unsupported claim reaches a committed answer and invalidated results cannot appear currently assured.

**DECISION_OWNER:** Core architect + clinical safety owner

### CODEX-P00-07: Key custody and blob privacy do not follow from encryption

**GAP_ID:** CODEX-P00-07

**SEVERITY:** P1

**AREA:** Keys and storage confidentiality

**CLAIM_OR_ASSUMPTION_CHALLENGED:** MedScale wrapping is sufficient mobile/desktop custody and destroy implies revocation.

**LIVE_EVIDENCE:** provider.rs stores the wrapping-key bytes alongside the wrapped DEK in the same OS credential entry; this is protection by that credential store, not an independently nonexportable KEK. sealed_blob path uses plaintext content SHA. Deleting a vault header does not prove deletion of OS entries or backed-up wraps. ottari provides actual native bridge code, but Android .setUserAuthenticationRequired(false) needs an explicit product policy.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-keys/src/provider.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-keys/src/provider.rs#L211); [TheHalfMoon/MedScale: crates/medscale-storage/src/sealed_blob.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/sealed_blob.rs#L42); [TheHalfMoon/ottari: crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java#L86); [TheHalfMoon/ottari: crates/himsat-core/src/vault_apple_keychain.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_apple_keychain.rs#L1)

**FAILURE_MODE:** Known-document membership is exposed through filenames; memory/backup copies survive key loss; native protector policy differs by device; a boolean mobile policy is mistaken for implemented secure custody.

**WHY_IT_MATTERS:** Threat model must distinguish locked device, compromised account/process, exportable credentials, plaintext in RAM and stolen unlocked device.

**AFFECTED_PHASES:** P02, P15-P17, P21

**READY_SOURCE_TO_COPY:** ottari native protector and backup-exclusion slices are materially better starting points for mobile than desktop-generic key wrappers.

**EXACT_CODE_OR_TESTS_TO_REUSE:** vault_android_keystore.rs with HimsatAndroidKeystoreBridge.java; vault_apple_keychain.rs; companion protector/rotation/lease modules and embedded tests. Adopt native platform code rather than recreate crypto.

**PROPOSED_RESOLUTION:** Bind KEK/DEK ownership and recovery policy per platform before P02. Use opaque or keyed private blob identifiers and scoped deduplication; define zeroization limitations, unlock/user-presence, logout/rotation, backup exclusion and best-effort revocation of future access.

**ALTERNATIVES:** Passphrase-only vault with documented usability/recovery tradeoff; platform credential storage as an explicit weaker supported profile.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Real iOS/Android/desktop tests for reinstall, backup restore, protector invalidation, device lock, stolen unlocked device and copied old backup; audit exposed filenames and support bundles. No native device tests ran in this review.

**DECISION_OWNER:** Platform security owner

### CODEX-P00-08: Synthetic pack signing cannot be promoted as production trust

**GAP_ID:** CODEX-P00-08

**SEVERITY:** P1

**AREA:** Pack/update trust

**CLAIM_OR_ASSUMPTION_CHALLENGED:** MedScale pack admission can precede TUF decisions deferred to P21/P22.

**LIVE_EVIDENCE:** pack_trust.rs exposes deterministic synthetic signing material and format.rs imports SYNTHETIC_PACK_TRUST_ROOT_ID/verify_pack_signature. This is explicitly synthetic, not a covert backdoor. Yet P03/P05/P10 consume packs before the late update phases.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-keys/src/pack_trust.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-keys/src/pack_trust.rs#L1); [TheHalfMoon/MedScale: crates/medscale-pack/src/format.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-pack/src/format.rs#L1); [awslabs/tough: tough/src/lib.rs](https://github.com/awslabs/tough/blob/98d8eb8b2ce63515d9b4981c938ef6453c5b5771/tough/src/lib.rs#L1); [theupdateframework/rust-tuf: tuf/src/client.rs](https://github.com/theupdateframework/rust-tuf/blob/219ca7d05818d5dd44ec4e32ab47c5ce64a7bf44/tuf/src/client.rs#L1); [theupdateframework/tuf-conformance: tuf_conformance/test_rollback.py](https://github.com/theupdateframework/tuf-conformance/blob/8729aa18b7811503556c8aa602eebde11471ea2a/tuf_conformance/test_rollback.py#L1)

**FAILURE_MODE:** Test trust is accidentally a release root, or valid old packs pass local epoch checks despite expiry, key compromise or revoked evidence.

**WHY_IT_MATTERS:** Trust bootstrap, persisted versions and clock/offline policy must exist when the first pack is admitted, not only at release.

**AFFECTED_PHASES:** P02-P03, P05, P10, P12-P13, P21-P22

**READY_SOURCE_TO_COPY:** tough or rust-tuf, qualified against python-tuf/reference conformance. Do not build a custom updater.

**EXACT_CODE_OR_TESTS_TO_REUSE:** tough RepositoryLoader and expiration enforcement; rust-tuf tuf/src/client.rs trusted-root constructors (TOFU must not substitute for pinned root); tuf-conformance/test_rollback.py and reference expired/freeze/root-rotation cases.

**PROPOSED_RESOLUTION:** Bind trust-root custody/thresholds, offline root provision, rollback/freeze/expiry handling, trusted clock uncertainty, targets-key compromise and pack revocation before pack-consuming phases. Compile synthetic keys only in test scope. App authenticity and evidence/model validity remain separate.

**ALTERNATIVES:** Verified manual offline imports with pinned trusted root and fail-closed metadata expiration; defer automatic updater but preserve the same trust protocol.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Cross-implementation fixtures for expired timestamp/snapshot, version rollback, sequential root rotation, thresholds, compromised targets, stale model and evidence revocation. Current donor conformance suites were inspected selectively, not run.

**DECISION_OWNER:** Security/update owner

### CODEX-P00-09: The broker donor is a fixture and host validation is not confinement

**GAP_ID:** CODEX-P00-09

**SEVERITY:** P1

**AREA:** Network and sensitive queries

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Copied broker/policy code supplies the only egress path.

**LIVE_EVIDENCE:** MedScale UreqTransport.send always returns ExternalGateRequired; fixture transport opens no sockets. Kernux EgressHost states explicitly that parsing is not DNS/endpoint enforcement. Xberg and parser/runtime libraries own HTTP clients if activated.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-network/src/transport.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-network/src/transport.rs#L58); [TheHalfMoon/kernux: crates/kernux-policy/src/egress.rs](https://github.com/TheHalfMoon/kernux/blob/2085b6ed1121b1a94c66c076bdd6b578da4dad0d/crates/kernux-policy/src/egress.rs#L101); [xberg-io/xberg: crates/xberg/src/model_download.rs](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/src/model_download.rs#L250); [docling-project/docling.rs: crates/docling/Cargo.toml](https://github.com/docling-project/docling.rs/blob/2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86/crates/docling/Cargo.toml#L18)

**FAILURE_MODE:** A worker bypasses broker; redirect or DNS rebinding reaches private addresses; outbound PubMed question text, URLs, DNS/SNI and logs disclose patient or clinician interests despite no inference API.

**WHY_IT_MATTERS:** Explicit online mode does not make all query-derived data nonsensitive. A syntactic allowlist is not SSRF or socket enforcement.

**AFFECTED_PHASES:** P03, P05, P12-P13, P17, P21

**READY_SOURCE_TO_COPY:** Existing policy/fixture contracts and hardened transport libraries; platform sandbox/network-denial mechanisms need actual integration.

**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale transport.rs/allowlist and fixture tests; Kernux egress host-policy tests; upstream parser download guards as inputs, not permission to bypass broker.

**PROPOSED_RESOLUTION:** Before P03 specify exact outbound request schema, user-visible disclosure, patient-redacted search construction, redirect policy, DNS resolution and connection-bound IP checks, private/link-local/loopback denial, byte/time limits and worker OS denial. Model/parser workers cannot open sockets in offline mode.

**ALTERNATIVES:** Bulk corpus updates followed by local search avoid routine question disclosure; optional user/institution adapters retain separate consent and cost.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Packet/socket probes under offline mode and worker compromise; redirect chains, IDNs, alternate IP encodings, IPv6, proxy env vars, DNS rebinding and model auto-download. Assert no PHI/query in logs or default URLs.

**DECISION_OWNER:** Network/security owner

### CODEX-P00-10: Lifecycle state lacks completeness and freshness semantics

**GAP_ID:** CODEX-P00-10

**SEVERITY:** P1

**AREA:** Corpus updates/current validity

**CLAIM_OR_ASSUMPTION_CHALLENGED:** PubMed/PMC/Crossref/Retraction Watch coverage can establish source validity.

**LIVE_EVIDENCE:** [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L154) names revisions/deletes; official PubMed download instructions require an annual replaced baseline followed by daily files in numeric order. NLM abstracts are not all public domain. Crossref says Retraction Watch corrections/EoCs are incomplete; absence of an alert is not proof of validity. Europe PMC terms request returned HTTP 403 in this review.

**SOURCE_CODE_INSPECTED:** [ijmarshall/trialstreamer: trialstreamer/dbutil.py](https://github.com/ijmarshall/trialstreamer/blob/a97cb8332c039e228ef42188c9d966440894e354/trialstreamer/dbutil.py#L5); [evidence-surveillance/es3: bot.py](https://github.com/evidence-surveillance/es3/blob/fa845217690e179d3f8151e97773aabc035d6cfe/bot.py#L34); [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1)

**FAILURE_MODE:** Missing daily file silently yields a current-looking corpus; a new report version has old spans; a deleted PMID is treated as scientific retraction; incomplete retraction feed is taken as clean status; stale offline answers appear current.

**WHY_IT_MATTERS:** Different source events require different legal/scientific responses; cached freshness cannot be asserted solely from last successful query.

**AFFECTED_PHASES:** P03-P06, P10, P17-P18, P20

**READY_SOURCE_TO_COPY:** ES3 linkage and update patterns as bounded reference/adaptation; immutable snapshots and replayable ingestion.

**EXACT_CODE_OR_TESTS_TO_REUSE:** ES3 bot.py check_trialpubs_nctids and test/test_bot.py; MESC corpus snapshot schema. Do not transplant Trialstreamer PostgreSQL/service stack without rights or pretend it is a local updater.

**PROPOSED_RESOLUTION:** Bind per-feed watermark, sequence completeness, replay/idempotency, gaps, baseline rollover, delete/revision reason, publication-state confidence and local/offline freshness policy before P03. Validity is multi-source and can be unknown. Preserve historical artifact and current overlay; propagate dependency invalidation.

**ALTERNATIVES:** Small manually refreshed curated packs with explicit as-of date and limited scope rather than implied comprehensive surveillance.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Out-of-order/missing/duplicate daily files, baseline rebuild interrupted, PMID deletion, DOI/version changes, correction changing a table result, retraction versus EoC, feed unavailable and concurrent saved-answer use.

**DECISION_OWNER:** Corpus/lifecycle owner

### CODEX-P00-11: Retrieval promotion needs clinical/study and language boundaries

**GAP_ID:** CODEX-P00-11

**SEVERITY:** P1

**AREA:** Retrieval

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Existing lexical donor plus MedCPT tournament is sufficient source admission.

**LIVE_EVIDENCE:** MedScale evidence contract is restricted (SyntheticOnly/Active/Retracted and relevance-based hits). MedCPT source loads query/article encoders separately and uses dot products; it is not one interchangeable embedding pack. BEIR evaluator scores document qrels, not automatically study recall, rights access or answer sufficiency.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-contracts/src/evidence/mod.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-contracts/src/evidence/mod.rs#L1); [ncbi/MedCPT: retriever/models.py](https://github.com/ncbi/MedCPT/blob/11e129be74102c98d16a11c310b0b5ce74c1db5e/retriever/models.py#L13); [beir-cellar/beir: beir/retrieval/evaluation.py](https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/beir/retrieval/evaluation.py#L1); [quickwit-oss/tantivy: src/query/bm25.rs](https://github.com/quickwit-oss/tantivy/blob/e988ecb7a11109d89f9f4582b386089fc3a2fec0/src/query/bm25.rs#L1); [anush008/fastembed-rs: Cargo.toml](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/Cargo.toml#L1)

**FAILURE_MODE:** Multiple reports inflate recall; filtered-out inaccessible or retracted studies are invisible in evaluation; English biomedical retrieval fails Arabic query concepts; wrong query/document encoder pairing silently ranks badly.

**WHY_IT_MATTERS:** Retrieval is necessary but cannot be the assurance estimand. No production quality or model superiority was measured here.

**AFFECTED_PHASES:** P03-P06, P08, P20

**READY_SOURCE_TO_COPY:** FTS5 first baseline, Tantivy if measured scale requires it; fastembed local runtime; MedCPT and BEIR as benchmark/runtime candidates.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Tantivy src/query/bm25.rs and index writer APIs; BEIR retrieval/evaluation.py; MedCPT retriever/models.py and evals; fastembed user-defined text/reranker constructors. Do not create a new vector DB.

**PROPOSED_RESOLUTION:** Before P04 freeze report and study qrels, source-family strata, eligibility/rights filters, lifecycle visibility, temporal/study-grouped split and clinical error review. P05 compare MedCPT paired encoders/reranker with newer multilingual BGE-M3/Qwen3-style candidates after exact model-card/runtime/license admission, plus lexical-only and fusion. Those challengers are candidates, not winners inspected here.

**ALTERNATIVES:** Keep lexical-only if semantic components fail accuracy, RAM, disk, latency or Arabic concept recall gates; curated corpus first.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Measured study-level recall and report recall, rights-filtered failure cases, alias/identifier/numeric queries, cross-language recall and source-family coverage; cache/model mismatches; no silent remote downloads. Biomedical/PubMedQA tasks are useful subsets, not full clinical gold.

**DECISION_OWNER:** Retrieval owner + bilingual clinical evaluator

### CODEX-P00-12: Support is multidimensional, and unavailable is not neutral

**GAP_ID:** CODEX-P00-12

**SEVERITY:** P1

**AREA:** Claim verification

**CLAIM_OR_ASSUMPTION_CHALLENGED:** SUPPORTS/PARTIALLY_SUPPORTS/CONTRADICTS/DOES_NOT_ESTABLISH/UNRESOLVED safely summarize a claim.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L140) defines structured claims, while SciFact and MultiVerS are rationale/closed-label research donors. Their label spaces do not establish causal efficacy, patient applicability, exact numerical agreement or currently available source authority.

**SOURCE_CODE_INSPECTED:** [dwadden/multivers: multivers/model.py](https://github.com/dwadden/multivers/blob/a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e/multivers/model.py#L1); [allenai/scifact: LICENSE.md](https://github.com/allenai/scifact/blob/68b98a56d93e0f9da0d2aab4e6c3294699a0f72e/LICENSE.md#L1); [jayded/evidence-inference: evidence_inference/preprocess/preprocessor.py](https://github.com/jayded/evidence-inference/blob/a661e8c14f973398380c8865cf2f27a535aaaf6d/evidence_inference/preprocess/preprocessor.py#L25); [maziyarpanahi/openmed: openmed/clinical/grounding/types.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/types.py#L1); [maziyarpanahi/openmed: openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py#L1)

**FAILURE_MODE:** A correct abstract citation supports the wrong subgroup/timepoint/dose; source-unavailable becomes weak support; a corrected result keeps old label; opposing estimates with different populations are called contradiction.

**WHY_IT_MATTERS:** Entailment of a sentence is different from justified clinical assertion. One label must not erase rights, availability, numeric or causal failures.

**AFFECTED_PHASES:** P02, P06-P08, P10, P20

**READY_SOURCE_TO_COPY:** SciFact rationale scoring, MultiVerS local research oracle, Evidence Inference intervention/comparator direction tasks, OpenMed offset/grounding contracts.

**EXACT_CODE_OR_TESTS_TO_REUSE:** SciFact verisci/evaluate/lib/metrics.py; MultiVerS multivers/model.py; Evidence Inference prompt/annotation schema; OpenMed structured/offset_properties.py and tests/unit/structured/test_offset_properties.py.

**PROPOSED_RESOLUTION:** Bind orthogonal source availability/validity, exact-span relation, structured PICO/timepoint/numeric compatibility and clinical applicability; retain UNVERIFIABLE_SOURCE (or explicit unavailable reason under UNRESOLVED), not another probability. For every admitted claim require matched result identity and separate evidence-design/causality judgment. Full-text/abstract conflict remains visible.

**ALTERNATIVES:** Conservative deterministic structured checks and human confirmation with model rationale proposal; refrain from claiming automated causal verification.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Wrong paper/population/subgroup/timepoint; primary vs secondary endpoint; adjusted/unadjusted; absolute/relative risk; direction swap; dose/unit/decimal/negation; table row/column; abstract/fulltext conflict; source unavailable/retracted/corrected; mutually conflicting passages. Failure must suppress or qualify the exact affected claim.

**DECISION_OWNER:** Verification owner + evidence scientist

### CODEX-P00-13: Research extraction donors do not supply quantitative result extraction

**GAP_ID:** CODEX-P00-13

**SEVERITY:** P1

**AREA:** Clinical extraction

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Evidence Inference/PICOX/RRnlp/RobotReviewer/Trialstreamer can be copied as structured effect extraction.

**LIVE_EVIDENCE:** PICOX consists of training/evaluation notebooks using Hugging Face/torch boundary and span classifiers. Evidence Inference preprocessor requires annotation/XML directories at import. RRnlp sample-size code has a fixed magic threshold and old model/runtime coupling. Trialstreamer schema has scalar num_randomized/effect and global PostgreSQL connection; RobotReviewer composes web/API/Celery/RabbitMQ/BERT/GROBID.

**SOURCE_CODE_INSPECTED:** [WengLab-InformaticsResearch/PICOX: step_1_2_boundary_prediction.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_1_2_boundary_prediction.ipynb#L1); [jayded/evidence-inference: evidence_inference/preprocess/preprocessor.py](https://github.com/jayded/evidence-inference/blob/a661e8c14f973398380c8865cf2f27a535aaaf6d/evidence_inference/preprocess/preprocessor.py#L25); [bwallace/RRnlp: rrnlp/models/sample_size_extractor.py](https://github.com/bwallace/RRnlp/blob/e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0/rrnlp/models/sample_size_extractor.py#L1); [ijmarshall/trialstreamer: trialstreamer/dbutil.py](https://github.com/ijmarshall/trialstreamer/blob/a97cb8332c039e228ef42188c9d966440894e354/trialstreamer/dbutil.py#L5); [ijmarshall/robotreviewer: docker-compose.yml](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/docker-compose.yml#L1)

**FAILURE_MODE:** PICO span or inferred direction is treated as events/total, SD, HR/CI or arm denominator; notebook/runtime downloads or pickle weights enter trusted production; a number extracted from abstract has no analysis population.

**WHY_IT_MATTERS:** Ready research code is useful but not an admitted full-result engine, and wholesale service stacks violate the default local budget.

**AFFECTED_PHASES:** P06, P12, P18, P20

**READY_SOURCE_TO_COPY:** Use these as bounded oracles/workers, not ready clinical extractors; OpenMed offset provenance and document table IR are stronger integration primitives.

**EXACT_CODE_OR_TESTS_TO_REUSE:** PICOX step_1_2_boundary_prediction.ipynb, step_2_2_span_clf.ipynb, step_3_evaluate.ipynb; Evidence Inference preprocessing and direction evaluation; RRnlp sample_size_extractor.py fixtures; preserve exact source-region lineage.

**PROPOSED_RESOLUTION:** Before P06 define auto-proposed versus human-confirmed Result records and the typed result grammar from gap 03. Qualify small local extraction workers for supported designs; enforce missing-value/ambiguous-denominator abstention. Reuse NLP code without claiming it implements all numeric extraction. Reject untrusted pickle/code execution.

**ALTERNATIVES:** Human-led extraction first; auto-proposed PICO/direction only; delay quantitative automation until qualified.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Events/total, means/SD, RR/OR/RD/HR and CI, log transforms, adjusted models, ITT/per-protocol, subgroup/timepoint, tables, repeated participant totals and uncertain OCR. Audit weights/datasets and reproduce oracle tasks separately from clinical extraction.

**DECISION_OWNER:** Extraction owner + statistician

### CODEX-P00-14: statsmodels meta_analysis is a limited, experimental source

**GAP_ID:** CODEX-P00-14

**SEVERITY:** P1

**AREA:** Statistical safety

**CLAIM_OR_ASSUMPTION_CHALLENGED:** The named module provides the required synthesis methods without a stronger oracle.

**LIVE_EVIDENCE:** combine_effects supports PM/iterated and DL/chi2, not REML, takes variances rather than full covariance and defaults use_t=False. DL tau2 is not clamped. An exact-function probe with effects=[0,0,0], variances=[0.1,0.1,0.1] yielded tau2=-0.1 and nonfinite pooled result; PM yielded tau2=0 and HKSJ scale=0. The convergence flag from iterative tau fitting is discarded. This is a limited extracted-function probe, not the upstream suite.

**SOURCE_CODE_INSPECTED:** [statsmodels/statsmodels: statsmodels/stats/meta_analysis.py](https://github.com/statsmodels/statsmodels/blob/8278e2d218cc85bac2c7af02feb9a19a0e499b04/statsmodels/stats/meta_analysis.py#L1); [wviechtb/metafor: R/rma.mv.r](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/R/rma.mv.r#L1)

**FAILURE_MODE:** Invalid random-effects variance or degenerate interval is presented as precision; correlated arms/repeated participants treated independently; a REML/HKSJ label is attached to another computation.

**WHY_IT_MATTERS:** A ready standard statistics engine should fill gaps. SafeEvidence must not reinvent formulas to compensate for an inadequate selected module.

**AFFECTED_PHASES:** P18, P20 (input identities bound in P02)

**READY_SOURCE_TO_COPY:** metafor is materially stronger for method coverage and reference qualification; GPL >=2 distribution obligations and R runtime are explicit. statsmodels remains a restricted BSD oracle/worker.

**EXACT_CODE_OR_TESTS_TO_REUSE:** statsmodels/stats/meta_analysis.py and statsmodels/stats/tests/test_meta.py; metafor R/rma.uni.r, rma.mv.r, rma.glmm.r, escalc.r, regtest.r, ranktest.r and upstream testthat cases for selected methods.

**PROPOSED_RESOLUTION:** Before P18 bind supported designs/estimands and method defaults. Prefer pinned metafor as development oracle or optional licensed local R worker for REML/correlated/rare-event designs if budget permits. Restrict initial statsmodels slice to independently verified cases; reject nonfinite/negative variances and nonconvergence. Do not blindly clamp tau without declaring estimator policy.

**ALTERNATIVES:** No pooling when design or covariance is unsupported; export a qualified extraction dataset for external analysis; no mandatory R on mobile.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Compare fixed/random REML/PM/DL, declared HKSJ modification, multi-arm covariance, cluster design effects, crossover correlation, zero/rare events, continuous/SMD, adjusted estimates, participant overlap, subgroups/timepoints/multiplicity, heterogeneity and sensitivity against a mature oracle. Egger/funnel diagnostics are conditional, not evidence of absent publication bias.

**DECISION_OWNER:** Statistician

### CODEX-P00-15: Screening prioritization does not establish review completeness

**GAP_ID:** CODEX-P00-15

**SEVERITY:** P1

**AREA:** Deep Review

**CLAIM_OR_ASSUMPTION_CHALLENGED:** ASReview stopping can support a complete systematic/living review.

**LIVE_EVIDENCE:** ASReview stoppers.py labels its stoppers experimental. LastRelevant has a fully-labeled oracle requirement; NConsecutiveIrrelevant/Quantile/NLabeled are heuristics/budget gates. [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L630) lists required review artifacts but does not operationalize the review completion estimand or revision counters.

**SOURCE_CODE_INSPECTED:** [asreview/asreview: asreview/models/stoppers.py](https://github.com/asreview/asreview/blob/79d568212b2b0a78f9fd7be3c5117dfb890489f9/asreview/models/stoppers.py#L1); [evidence-surveillance/es3: bot.py](https://github.com/evidence-surveillance/es3/blob/fa845217690e179d3f8151e97773aabc035d6cfe/bot.py#L34); [HL7/ebm: input/fsh/evidence/p-single-study-evidence.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-single-study-evidence.fsh#L1)

**FAILURE_MODE:** A run stops after an irrelevant streak and reports a complete review; restart/reprioritization changes exclusions without audit; study/report dedup and PRISMA counts disagree.

**WHY_IT_MATTERS:** The frozen plan already says stopping is independent; the missing binding is an executable completion protocol rather than a new generic screening engine.

**AFFECTED_PHASES:** P18, P20

**READY_SOURCE_TO_COPY:** ASReview prioritization/state and SYNERGY datasets subject to item rights; ES3 linkage reference.

**EXACT_CODE_OR_TESTS_TO_REUSE:** asreview/models/stoppers.py, simulation/state and query models as a coherent pinned worker; benchmark on fully labeled SYNERGY reviews only under authorized abstract rights.

**PROPOSED_RESOLUTION:** Before P18 bind ReviewProtocol/search source/date/exact strategy, coverage gaps, report vs study counts, dedup states, dual-screening disagreement, exclusions, extraction/appraisal signoff, deviations, living-update delta and stopping audit. Budget stop != exhaustive completion; sampled residual recall needs a declared design and human signoff.

**ALTERNATIVES:** Manual screening with model ordering and transparent incomplete-review state; a rapid evidence scan must be named as such.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Missed relevant tail, change in query after protocol freeze, unresolved reviewer disagreement, overlapping reports, excluded study re-entering on update, residual sampling, reproducible PRISMA-compatible counts.

**DECISION_OWNER:** Review-methods owner

### CODEX-P00-16: Appraisal state must be result/design and rubric specific

**GAP_ID:** CODEX-P00-16

**SEVERITY:** P1

**AREA:** Risk of bias and certainty

**CLAIM_OR_ASSUMPTION_CHALLENGED:** AUTO_EXTRACTED/AUTO_PROPOSED/HUMAN_CONFIRMED/HUMAN_OVERRIDDEN/UNRESOLVED plus design profiles suffice.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L328) separates dimensions, but workflow states alone do not bind reviewer identity, rubric version, result/estimand scope, conflicts and reappraisal when corrected extraction changes a judgment. RobotReviewer is a proposal source, not the current authoritative instrument.

**SOURCE_CODE_INSPECTED:** [ijmarshall/robotreviewer: docker-compose.yml](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/docker-compose.yml#L1); [HL7/ebm: input/fsh/evidence/p-single-study-evidence.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-single-study-evidence.fsh#L1)

**FAILURE_MODE:** One generic score overrides RoB 2 result-level questions, ROBINS-I/E design concerns, QUADAS diagnostic pathways or AMSTAR 2 review appraisal; human confirmation becomes a perpetual badge despite changed evidence.

**WHY_IT_MATTERS:** Risk of bias, precision, inconsistency, indirectness, publication bias and overall certainty have different units and cannot be averaged into evidence quality.

**AFFECTED_PHASES:** P07, P18, P20

**READY_SOURCE_TO_COPY:** RobotReviewer research proposals under GPL; HL7 artifact-assessment profiles as interchange reference; actual official rubric rights/version must be admitted separately.

**EXACT_CODE_OR_TESTS_TO_REUSE:** RobotReviewer robots/bias_robot.py as isolated oracle only; HL7 input/fsh/artifact-assessment/p-evidence-assessment.fsh and p-certainty-of-evidence.fsh crosswalk.

**PROPOSED_RESOLUTION:** Before P07 bind instrument applicability, official version/license, result/design unit, domain questions, supporting spans, independent reviewers and adjudication/override reason. Confirmed judgment is invalidated or flagged for rereview when input/result versions change. No generic quality score.

**ALTERNATIVES:** Human-only design-specific appraisal first; automated extraction can populate evidence without issuing final judgment.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** RoB2 versus observational/diagnostic/review designs; two outcomes in one trial with different bias; changed missing-data result; conflicting raters; rubric update; certainty based on multiple studies with incomplete publication-bias evidence.

**DECISION_OWNER:** Clinical evidence-methods owner

### CODEX-P00-17: V1 should show no clinical confidence percentage

**GAP_ID:** CODEX-P00-17

**SEVERITY:** P1

**AREA:** Calibration and donor negative evidence

**CLAIM_OR_ASSUMPTION_CHALLENGED:** DAL calibration/selective code can become SafeEvidence assurance confidence.

**LIVE_EVIDENCE:** DAL main results record identical paper/control correctness with action accuracy 0.552 and no primary accuracy gain. selective_results explicitly preserves unsafe_commit_rate=1.0 at frozen target coverages 0.8/0.9 for the paper system (actual coverage 1.0); one ranking comparison improves risk_at_80 by 0.0125, not clinical safety. Grounding Candidate.score is not probability of medical truth.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/DAL: src/gaxbench/metrics.py](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/src/gaxbench/metrics.py#L1); [TheHalfMoon/DAL: registry/p08_sg000023_paper_evidence/selective_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/selective_results.json#L1); [TheHalfMoon/DAL: registry/p08_sg000023_paper_evidence/main_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/main_results.json#L1); [maziyarpanahi/openmed: openmed/clinical/grounding/types.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/types.py#L1)

**FAILURE_MODE:** Good Brier/ECE or slightly improved ranking on PubMedQA is promoted as safe clinical commitment; copied features rerun a failed donor approach under a new name; percentages outlive evidence/model/retriever/generator changes.

**WHY_IT_MATTERS:** Donor empirical claims are not transferable, and selective risk can look better by abstaining from all useful cases.

**AFFECTED_PHASES:** P08-P09, P11, P16, P20, P23

**READY_SOURCE_TO_COPY:** DAL metric implementations/tests remain valuable; reuse measurements, not the failed medical claim. OpenMed grounding calibration is task-specific.

**EXACT_CODE_OR_TESTS_TO_REUSE:** gaxbench/metrics.py, selective.py, tests/test_metrics.py, tests/test_selective.py; preserve registry/p08_sg000023_paper_evidence negative evidence.

**PROPOSED_RESOLUTION:** Default V1 to reasons, evidence dimensions and applicability state with no percent. Before any later percent bind claim/answer estimand, clinician rubric, disjoint temporal/study/patient splits, minimum useful coverage, calibration/final separation and subgroup CIs. A complete pipeline manifest includes packs, rights/validity policy, terminology, retrieval/reranker, verifier, generator, tools and thresholds; changes invalidate the old qualification.

**ALTERNATIVES:** A task-specific experimentally calibrated research score can remain hidden in benchmark output; it must not imply patient outcome probability.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Locked final holdout; false commitments/over-abstention/escalation; Arabic/specialty/setting shifts; pack/model/policy updates and generator changes; grouped bootstrap or suitable clustered uncertainty. No clinical calibration was run here.

**DECISION_OWNER:** Evaluation/statistics owner

### CODEX-P00-18: Patient context is temporal and tools need an admission catalog

**GAP_ID:** CODEX-P00-18

**SEVERITY:** P1

**AREA:** Applicability and deterministic tools

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Missing fields plus generic patient context and donor tool routing safely enable calculators.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L168) names clinical fields; commandMed scaffold executes simulation output, not qualified renal/dose/risk tools. SafeOCR delegates UCUM syntax to ucumvert; syntax-valid units alone do not prove dimension, formula eligibility or clinical applicability.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/commandMed: src/commandmed/spec006/scaffold.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/scaffold.py#L83); [TheHalfMoon/commandMed: data/spec006/safety_policy.json](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/data/spec006/safety_policy.json#L1); [AbdulazizShehri/SafeOCR: src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py#L463); [cqframework/clinical_quality_language: cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt](https://github.com/cqframework/clinical_quality_language/blob/c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2/cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt#L23)

**FAILURE_MODE:** Old creatinine is treated as current renal function, eGFR and creatinine clearance interchangeable, pediatric/adult formula used outside domain, weight type or mg/dL versus micromol/L confused; absent pregnancy/hepatic/interaction information inferred.

**WHY_IT_MATTERS:** Patient-specific action eligibility depends on observation time, method and missingness, not simply a filled JSON slot.

**AFFECTED_PHASES:** P02, P07-P08, P13-P14, P16, P20

**READY_SOURCE_TO_COPY:** Existing CQL/UCUM quantity semantics and admitted institutional calculator implementations; no ready complete clinical calculator catalog was established among inspected donors.

**EXACT_CODE_OR_TESTS_TO_REUSE:** CQL translator/reference quantity semantics; SafeOCR validate_ucum_unit adapter and tests; commandMed tool eligibility/trace fixtures, not its simulated output as a formula.

**PROPOSED_RESOLUTION:** Before P07 bind observation timestamp/source/reference interval, clinically relevant sex/age, pregnancy/pediatrics, renal/hepatic status, weight convention, interacting medicines, severity, prior therapy, contraindications, setting/jurisdiction and uncertainty. Admit each calculator with authoritative formula/version, eligibility, units, rounding and reference cases. Depend on a qualified existing library if available; a tiny pure deterministic adapter is GREENFIELD_JUSTIFIED only after source/license search fails and clinician-approved reference tests exist. Do not let an LLM compute formulas.

**ALTERNATIVES:** V1 provides population evidence without patient-specific calculation; defer unqualified eGFR/CrCl/QTc/risk scores rather than invent a generic calculator framework.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Missing/stale labs, AKI versus steady-state creatinine, pediatrics/pregnancy, obesity/weight type, renal dose and interacting drugs, units/rounding/boundaries, denominator zero and contraindications. Small tool adapters are part of GF04, not a new platform.

**DECISION_OWNER:** Clinical tools owner

### CODEX-P00-19: CQL compilation does not validate a guideline recommendation

**GAP_ID:** CODEX-P00-19

**SEVERITY:** P1

**AREA:** Guidelines

**CLAIM_OR_ASSUMPTION_CHALLENGED:** CQL/CQF and ProtocolWISE semantics are ready guideline execution authority.

**LIVE_EVIDENCE:** CqlTranslator exposes compiler output/errors, not evidence/jurisdiction/recommendation validation. ProtocolWISE source was inaccessible at the public locations attempted; it cannot be recorded as inspected/admitted. HL7 recommendation action is a crosswalk, not rights to publisher guideline content.

**SOURCE_CODE_INSPECTED:** [cqframework/clinical_quality_language: cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt](https://github.com/cqframework/clinical_quality_language/blob/c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2/cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt#L23); [HL7/ebm: input/fsh/evidence/p-endpoint-analysis-plan.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-endpoint-analysis-plan.fsh#L1)

**FAILURE_MODE:** Valid CQL executes superseded or wrong-jurisdiction recommendation; missing terminology maps alter behavior; competing guideline recommendations get collapsed; narrative prose is mistranslated into executable authority.

**WHY_IT_MATTERS:** The product must preserve source authority, recommendation strength and applicability independently from executable syntax.

**AFFECTED_PHASES:** P13, P07, P14, P20

**READY_SOURCE_TO_COPY:** Pinned CQL compiler/engine reference tooling; a bounded worker rather than a new CQL parser or broad Rust rewrite.

**EXACT_CODE_OR_TESTS_TO_REUSE:** cql-to-elm CqlTranslator.kt/CqlCompiler.kt and engine reference tests; HL7 recommendation-action profile. Bind a runtime separately from compiler and handle terminology packages explicitly.

**PROPOSED_RESOLUTION:** Before P13 admit narrative guideline cards first with publisher/issuer, jurisdiction, version, supersession, target population, strength, conflicts and institution override scope. Executable recommendations require semantic review and clinical regression fixtures, explicit source/term rights and deterministic missing-data behavior. ProtocolWISE stays unavailable/unqualified until exact source can be inspected.

**ALTERNATIVES:** Narrative verified recommendation navigation with no execution; institution-provided licensed rules as explicit optional adapter.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Syntax-valid wrong comparator/units, version change, expired institution protocol, conflicting guidelines, unknown value set, excluded patient population and executable/narrative divergence.

**DECISION_OWNER:** Guidelines owner + clinician

### CODEX-P00-20: Parser default features violate the offline worker budget

**GAP_ID:** CODEX-P00-20

**SEVERITY:** P1

**AREA:** Document processing and sandbox

**CLAIM_OR_ASSUMPTION_CHALLENGED:** A parser dependency can be admitted by engine choice and a host allowlist.

**LIVE_EVIDENCE:** docling default features include pdf, asr, fetch-images and vlm; remote image fetching and OpenAI-compatible VLM paths exist. Xberg default is narrower tokio-runtime/simd-utf8, but OCR/model/LLM features introduce HTTP/download behavior; model_download client-build failure falls back to default client. fastembed defaults enable ORT binary/HF downloads. PDF timeout checks between stages/pages do not kill a hung native parser.

**SOURCE_CODE_INSPECTED:** [xberg-io/xberg: crates/xberg/Cargo.toml](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/Cargo.toml#L1); [xberg-io/xberg: crates/xberg/src/model_download.rs](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/src/model_download.rs#L250); [docling-project/docling.rs: crates/docling/Cargo.toml](https://github.com/docling-project/docling.rs/blob/2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86/crates/docling/Cargo.toml#L18); [anush008/fastembed-rs: Cargo.toml](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/Cargo.toml#L1)

**FAILURE_MODE:** First open of a document downloads weights, fetches external resources, opens a service or hangs beyond budget; path checks inside a library are mistaken for process confinement; hostile file exhausts trusted app.

**WHY_IT_MATTERS:** These are actual opt-in/default runtime paths, not evidence of observed telemetry leakage. Feature flags and sandbox authority are separate gates.

**AFFECTED_PHASES:** P05, P10, P12, P15-P16, P21-P22

**READY_SOURCE_TO_COPY:** Xberg is the better primary hypothesis for a narrow offline build based on inspected feature boundaries; docling.rs is the challenger, not rejected on accuracy. No medical parsing winner measured.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Xberg crates/xberg/Cargo.toml with default-features=false and only required pdf/selected local OCR features; docling Cargo.toml default-features=false with explicit local path; fastembed user-defined local model/session constructors. Reuse engines rather than author a framework.

**PROPOSED_RESOLUTION:** Before P12 freeze feature/dependency closure and shipped weights. Disable Xberg liter-llm/bedrock/otel and downloader paths; disable docling fetch-images/asr/vlm unless independently admitted local implementation. Block worker sockets at OS layer, deny arbitrary file paths, cap nesting/decompression/pages/pixels/output bytes/threads/time and kill/restart on deadline. Retain source-region IR and trust/no-key/no-DB boundary.

**ALTERNATIVES:** Born-digital PDF/text-only V1; optional desktop OCR worker with preinstalled validated weights; no parser fallback to network.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Hostile PDFs/archives, zip bombs, symlinks/path traversal, embedded URLs, parser crashes/hangs, cancellation, low disk/RAM, cold empty model cache offline, network proxy variables and feature closure. Compare both engines on medical tables/columns, not generic text score alone.

**DECISION_OWNER:** Document/security owner

### CODEX-P00-21: SafeOCR is a real critical-value donor, not an empty source

**GAP_ID:** CODEX-P00-21

**SEVERITY:** P1

**AREA:** OCR medical verification

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Critical OCR safety must be invented because SafeOCR is empty.

**LIVE_EVIDENCE:** Live SafeOCR at 7b892c7 contains contracts, OCR adapters, Decimal critical-value parsing, source-region hashes, perturbed-read checks, patient HMAC linkage, UCUM validator boundary and tests. The frozen source ledger classification is now stale; code availability is not proof of Arabic/clinical performance.

**SOURCE_CODE_INSPECTED:** [AbdulazizShehri/SafeOCR: src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py#L463); [AbdulazizShehri/SafeOCR: tests/test_verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/tests/test_verification.py#L1); [maziyarpanahi/openmed: openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py#L1)

**FAILURE_MODE:** SafeEvidence duplicates a critical-number gate or admits dose/unit/decimal output based only on character error rate. Agreement of correlated OCR reads is treated as independent clinical truth.

**WHY_IT_MATTERS:** This is a better ready implementation for safety qualification glue than a generic parser alone and narrows necessary greenfield work.

**AFFECTED_PHASES:** P12, P16, P20

**READY_SOURCE_TO_COPY:** SafeOCR Apache-2.0 bounded verification/contract slice with OpenMed offset properties.

**EXACT_CODE_OR_TESTS_TO_REUSE:** src/safeocr/{contracts,verification,ocr}.py, tests/test_verification.py, test_foundation_contracts.py, test_ocr_adapters.py and runtime_smoke tests. Admit Python dependencies/weights/ucumvert separately and preserve patient-binding secret boundary.

**PROPOSED_RESOLUTION:** Before P12 inspect/admit the coherent slice rather than recreate it. Require source crop/page coordinates, extraction provenance, exact unit text, critical comparison and explicit unverified state. Human confirmation where critical values remain uncertain; identical perturbation readings alone cannot certify fidelity.

**ALTERNATIVES:** Born-digital only or human-confirmed scans first; no numeric patient-context promotion from unchecked OCR.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Decimals, inequality signs, mg/mcg, case-sensitive UCUM, Arabic digits/separators, mixed-script drug/dose text, negation, tables/row association, source crop mismatch, wrong patient and unhealthy OCR runtime. No full SafeOCR runtime suite ran here.

**DECISION_OWNER:** OCR safety owner

### CODEX-P00-22: Desktop preference needs license and exposure evidence

**GAP_ID:** CODEX-P00-22

**SEVERITY:** P1

**AREA:** Desktop shell

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Slint is a lower-risk default shell than Tauri.

**LIVE_EVIDENCE:** Slint LICENSE.md has royalty-free 2.0 custom attribution and redistribution/API conditions, GPL-3.0 or commercial alternatives; it is not interchangeable with MIT. Tauri is Apache/MIT. Frozen plan makes shell choice a tournament but licenses, screen-reader Arabic and OS data exposure remain prerequisites, not preference.

**SOURCE_CODE_INSPECTED:** [slint-ui/slint: LICENSE.md](https://github.com/slint-ui/slint/blob/a199b6bddde18d939886f2a0de0700999fe32851/LICENSE.md#L1)

**FAILURE_MODE:** Shell is selected before rights/packaging/accessibility review; PHI enters WebView cache, devtools, crash report, clipboard history or OS index; native toolkit is assumed inherently private.

**WHY_IT_MATTERS:** Privacy depends on configured app/platform behavior, while inaccessible evidence review undermines actual clinician use.

**AFFECTED_PHASES:** P11, P21-P22

**READY_SOURCE_TO_COPY:** Slint and Tauri as qualified dependencies; sibling desktop modules only if exact relevant code is present. Signthos current source is not a ready SafeEvidence desktop shell.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Slint per-file REUSE/LICENSE and native widgets; Tauri crates/tauri-runtime-wry plus cache/protocol controls. The review does not report shell benchmark or screen-reader/device tests.

**PROPOSED_RESOLUTION:** Before P11 freeze distribution license/attribution, app data placement and measured shell qualification: cold startup/RAM, keyboard-only workflow, screen-reader citation/reading order, Arabic shaping/bidi, crash/temp/cache cleanup, packaging and updates. Keep Slint as hypothesis only until those gates pass.

**ALTERNATIVES:** Tauri with private offline profile/no remote content and tested exposure controls; choose by evidence, not native-vs-WebView slogan.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Windows/macOS screen readers, RTL/mixed scripts, clipboard/copy warning policy, OS indexing exclusion, dumps/WER/crash reporter, pagefile/hibernation residuals and cache/temp/support scans after realistic PHI flows.

**DECISION_OWNER:** Desktop/platform owner + accessibility evaluator

### CODEX-P00-23: FFI parity tests are not native mobile custody or memory proof

**GAP_ID:** CODEX-P00-23

**SEVERITY:** P1

**AREA:** Mobile

**CLAIM_OR_ASSUMPTION_CHALLENGED:** UniFFI plus OpenMed bridge tests establish production mobile readiness.

**LIVE_EVIDENCE:** UniFFI RustBuffer serializes/owns Vec memory with manual destruction; large payloads require explicit API policy. OpenMed Flutter tests are environment-gated and a test-session path; RN bridge checks depend on Node/npm and do not establish native secure storage. Native ottari protector code exists but Android no-user-auth default is a policy decision.

**SOURCE_CODE_INSPECTED:** [mozilla/uniffi-rs: uniffi_core/src/ffi/rustbuffer.rs](https://github.com/mozilla/uniffi-rs/blob/bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea/uniffi_core/src/ffi/rustbuffer.rs#L1); [maziyarpanahi/openmed: tests/mobile/test_flutter_ffi.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/tests/mobile/test_flutter_ffi.py#L1); [maziyarpanahi/openmed: tests/mobile/test_rn_bridge_parity.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/tests/mobile/test_rn_bridge_parity.py#L1); [TheHalfMoon/ottari: crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java#L86); [TheHalfMoon/ottari: crates/himsat-core/src/vault_apple_keychain.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_apple_keychain.rs#L1)

**FAILURE_MODE:** PDF/model/evidence corpus crosses FFI as multiple large buffers; mobile runs out of RAM, keeps secret buffers, or leaves pack/session state inconsistent after suspension; mocked bridge parity is mistaken for real device security.

**WHY_IT_MATTERS:** Mobile supports narrower profiles; engine desktop capability cannot be copied blindly onto low-memory thermally constrained devices.

**AFFECTED_PHASES:** P15-P17, P20-P22

**READY_SOURCE_TO_COPY:** UniFFI generated Swift/Kotlin bindings; ottari platform key bridge; OpenMed parity tests as harness patterns.

**EXACT_CODE_OR_TESTS_TO_REUSE:** uniffi_core/src/ffi/rustbuffer.rs and generated binding tests; OpenMed tests/mobile/test_flutter_ffi.py, test_rn_bridge_parity.py as bounded oracles; native protector code from gap 07.

**PROPOSED_RESOLUTION:** Before P15 define paged queries/opaque object handles/file-backed bounded input, cancellation/lifetimes, no master-key FFI exposure and maximum payloads. Bind minimum iOS/Android device/storage/model profiles, backup exclusion, app-switcher/screenshot/notification policies and suspension/restart behavior. Require native tests, not only Python/Node parity.

**ALTERNATIVES:** Mobile evidence reader with small verified packs and no full generation/OCR first; optional local specialized models promoted by measurement.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Physical low-memory devices, memory pressure/thermal throttling/battery, interrupted OCR/sync, OS backup/reinstall, stolen device, previews/screenshots/notifications, stale handles, cancellation and secret-buffer lifetime.

**DECISION_OWNER:** Mobile platform owner

### CODEX-P00-24: Transport authentication is not pairing or rights-aware sync

**GAP_ID:** CODEX-P00-24

**SEVERITY:** P1

**AREA:** Pairing/sync

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Existing sibling sync and authenticated transport solve selective sync.

**LIVE_EVIDENCE:** Signthos inspected tree is now a document-signing product with sync/mobile ideas rather than a ready QR implementation. Iroh endpoint explicitly exposes relay/default/staging/custom modes; network configuration must be chosen. Neither transport auth nor possession of a QR is authority for all evidence or patient data.

**SOURCE_CODE_INSPECTED:** [n0-computer/iroh: iroh/src/endpoint.rs](https://github.com/n0-computer/iroh/blob/41e782a8f0c858bcd1f74bfc703758244d5a6538/iroh/src/endpoint.rs#L155); [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1); [TheHalfMoon/commandMed: src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py#L1)

**FAILURE_MODE:** Replay/racing QR enrolls wrong peer; stale grant sends institutional PDF or PHI; offline revocation is falsely immediate; a tombstone loses conflict resolution and deleted item resurrects; relay contact contradicts local-only UX.

**WHY_IT_MATTERS:** Revocation cannot erase bytes already exported or guarantee deletion on an offline/untrusted peer. Rights and authorization must be carried to projections and resume logs.

**AFFECTED_PHASES:** P17, P02-P03, P21

**READY_SOURCE_TO_COPY:** Existing cryptographic transport (Iroh or LAN TLS/QUIC) as dependency; native/SQLite sync primitives. No verified ready sibling pairing engine was found.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Iroh Endpoint builder/RelayMode plus transport tests; reuse vetted QR/TLS primitives, not a custom cryptographic handshake. Signthos is reference only pending exact qualified slice and AGPL permission handling.

**PROPOSED_RESOLUTION:** Before P17 bind single-use expiring enrollment challenge, authenticated out-of-band peer confirmation, replay/race storage, least scope capabilities, key rotation, explicit relay policy, cursor/checkpoint recovery, rights checks at send and receive, merge/tombstone semantics and retained offline status. QR contains no raw PHI or long-lived secret.

**ALTERNATIVES:** Explicit encrypted file export/import or LAN-only transfer first; remote relay optional user-provided service with metadata disclosure and cost.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Concurrent bootstrap, replay, altered peer identity, stale device/grant, revoked license, interrupted resume, conflicting edits/deletes, key loss/rotation, offline revocation and denial of relay sockets when LAN-only.

**DECISION_OWNER:** Sync/security owner

### CODEX-P00-25: Private-data qualification needs an early platform exposure contract

**GAP_ID:** CODEX-P00-25

**SEVERITY:** P1

**AREA:** Privacy

**CLAIM_OR_ASSUMPTION_CHALLENGED:** No cloud/telemetry plus encrypted vault makes local use sufficiently private until P21.

**LIVE_EVIDENCE:** [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L765) requires campaigns and cross-cutting security intent, but [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L114) has no exact per-platform retention/exposure boundary for query text, derived embeddings, workers, pagefile/dumps/OS backups. Encryption at rest does not protect unlocked app memory or OS copies.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-storage/src/encrypted_vault.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/encrypted_vault.rs#L155); [TheHalfMoon/MedScale: crates/medscale-storage/src/sealed_blob.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/sealed_blob.rs#L42); [TheHalfMoon/MedScale: crates/medscale-keys/src/provider.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-keys/src/provider.rs#L211); [TheHalfMoon/ottari: crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java#L86)

**FAILURE_MODE:** Query caches/vector projections/logs/temp files or crash bundles reveal PHI; model/OCR worker sees more context than needed; screenshots and previews persist after logout.

**WHY_IT_MATTERS:** P21 qualification cannot retrofit a threat model after real data paths and packaging are implemented. This is not a claim of impossible perfect endpoint secrecy.

**AFFECTED_PHASES:** P02-P03, P10-P12, P14-P17, P21-P22

**READY_SOURCE_TO_COPY:** Existing platform protections and sibling privacy fixtures; no novel privacy engine.

**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale encrypted working-file/probe fixtures; ottari no-backup native protector path; copied privacy tests adapted to SafeEvidence resource names.

**PROPOSED_RESOLUTION:** Before each private-data phase bind minimum supported OS/device posture, process/key/access boundaries, permitted residuals and retention. Keep queries/embeddings private, redact logs/support exports, avoid PHI command arguments/paths/notifications, deny indexing, and test cache/temp/backup cleanup. Document platform limits for swap/hibernation/screenshots instead of promising complete erasure.

**ALTERNATIVES:** Synthetic data-only development until device qualification; explicit institution-managed stronger profile later.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Known PHI canaries across logs, temp, WAL/journal, pagefile/hibernation, dumps/WER/macOS reports, clipboard history, Windows Search/Spotlight, backups, model caches and support bundles; minimum context worker exposure.

**DECISION_OWNER:** Privacy/security owner

### CODEX-P00-26: Arabic fidelity requires semantic and coordinate contracts

**GAP_ID:** CODEX-P00-26

**SEVERITY:** P1

**AREA:** Arabic and clinical meaning

**CLAIM_OR_ASSUMPTION_CHALLENGED:** RTL localization and cross-language models cover Arabic safety.

**LIVE_EVIDENCE:** OpenMed offset contract uses half-open Unicode codepoint indices; Rust bytes, JavaScript UTF-16, document coordinates and normalized text are different spaces. commandMed Arabic symptom substrings show the same emergency misfire as English. SafeOCR unit checks preserve case-sensitive source text.

**SOURCE_CODE_INSPECTED:** [maziyarpanahi/openmed: openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py#L1); [TheHalfMoon/commandMed: src/commandmed/spec006/scaffold.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/scaffold.py#L83); [TheHalfMoon/commandMed: data/spec006/safety_policy.json](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/data/spec006/safety_policy.json#L1); [AbdulazizShehri/SafeOCR: src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py#L463)

**FAILURE_MODE:** A highlight points to wrong evidence after normalization; bidi displays a medication/dose in misleading order; Arabic query translation flips negation/comparator; decimal punctuation changes a dose; a citation opens the wrong region.

**WHY_IT_MATTERS:** Preserving clinical meaning and exact evidence provenance is a core contract, not translated button text.

**AFFECTED_PHASES:** P02, P04-P08, P11-P12, P16, P19-P20

**READY_SOURCE_TO_COPY:** OpenMed offset/property and cross-language tests; native shaping/bidi libraries; SafeOCR numeric/unit gates.

**EXACT_CODE_OR_TESTS_TO_REUSE:** structured/offset_properties.py, tests/unit/core/test_offset_contract_parity.py, tests/unit/structured/test_offset_properties.py, grounding crosslingual/provenance fixtures; do not copy translation augmentation as a validated medical translator.

**PROPOSED_RESOLUTION:** Before P02 bind source bytes/version, codepoint offsets, normalized-text mapping and rendered-region mapping; never overwrite original. Before affected phases define Arabic/Latin drug/dose/UCUM/identifier isolation, transliteration policy, bidirectional citation navigation and concept-preserving query translation with unresolved state.

**ALTERNATIVES:** Arabic input with explicit English evidence cards and verified bilingual presentation first; constrain unsupported languages/translation rather than imply full parity.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Mixed bidi identifiers/drugs, Arabic digits/decimal separators, negation, dose/units, diacritics/normalization, OCR region mapping, long strings/screen readers and Arabic-to-English study recall. Bilingual adjudication required; no Arabic clinical benchmark ran.

**DECISION_OWNER:** Bilingual clinical + localization owner

### CODEX-P00-27: Human gold and phase gates have no executable resourcing plan

**GAP_ID:** CODEX-P00-27

**SEVERITY:** P1

**AREA:** Evaluation governance

**CLAIM_OR_ASSUMPTION_CHALLENGED:** A later SafeEvidenceBench can cheaply qualify earlier clinical gates.

**LIVE_EVIDENCE:** [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L679) lists human review but does not bind intended-use cohort, recruited expertise, double review/adjudication, label budget or uncertainty design before P04/P06/P08/P09 choices. For independent Bernoulli cases, zero failures requires at least 299 cases for one-sided 95% upper bound below 1%; clustered/subgroup clinical tasks require a different design.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/DAL: src/gaxbench/metrics.py](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/src/gaxbench/metrics.py#L1); [beir-cellar/beir: beir/retrieval/evaluation.py](https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/beir/retrieval/evaluation.py#L1); [TheHalfMoon/DAL: registry/p08_sg000023_paper_evidence/main_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/main_results.json#L1)

**FAILURE_MODE:** Model-generated labels become gold; small convenience sample supports a strong unsafe-commit bound; test data tunes thresholds; Arabic/specialty subgroups are unpowered; unavailable adjudication makes promotion gates ceremonial.

**WHY_IT_MATTERS:** Zero inference COGS does not pay clinicians or create valid gold. Delayed measurement can lock in unsuitable representations.

**AFFECTED_PHASES:** P01, P04-P09, P12-P13, P18, P20, P23

**READY_SOURCE_TO_COPY:** DAL/BEIR scoring and grouped statistical tooling; task-specific research datasets as supplements, not clinical gold.

**EXACT_CODE_OR_TESTS_TO_REUSE:** DAL metrics.py and test_metrics.py; BEIR evaluation.py; SciFact rationale metrics; reuse mechanics with blinded human labels and stage-specific targets.

**PROPOSED_RESOLUTION:** Before affected tournaments bind protocol owner, recruiting/compensation, clinician/bilingual expertise, two-review sampling/adjudication, conflicts, data rights, ethics/IRB if applicable, agreement measure, study/patient/temporal split, subgroup sample sizes and missing-label rule. Move benchmark design/holdout custody prerequisites earlier while retaining P20 as integrated qualification.

**ALTERNATIVES:** Narrow research-only scope and qualitative evaluation until funded adjudication exists; no unsupported probability/safety claim.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Budget and actual label packet, blinded double-review sample, disagreement resolution, annotation version history, leakage checks and uncertainty calculation. The 299 calculation is arithmetic, not a SafeEvidence sample-size recommendation.

**DECISION_OWNER:** Clinical evaluation lead + founder

### CODEX-P00-28: The first intended-use wedge must precede model and UX admission

**GAP_ID:** CODEX-P00-28

**SEVERITY:** P1

**AREA:** Scope and claims

**CLAIM_OR_ASSUMPTION_CHALLENGED:** One V1 can qualify broad evidence answering, patient applicability, guidelines, OCR, mobile and review workflows.

**LIVE_EVIDENCE:** [docs/PRODUCT_THESIS.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/PRODUCT_THESIS.md#L1) describes a broad clinical evidence/assurance product; [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L816) defers claims/comparative protocol. The benchmark population and tolerable false escalation cannot be fixed without first user/task/setting exclusions.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/commandMed: src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py#L1); [TheHalfMoon/DAL: registry/p08_sg000023_paper_evidence/main_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/main_results.json#L1)

**FAILURE_MODE:** A clinician research-support workflow becomes patient-specific treatment advice through wording or tools; evaluation covers one specialty while launch implies another; broad roadmap costs obscure a viable local product.

**WHY_IT_MATTERS:** Supported intended use is an admission boundary for safety, evidence coverage, performance and legal/regulatory assessment. No medical-device or compliance determination is made here.

**AFFECTED_PHASES:** P01 and all qualification phases, P23

**READY_SOURCE_TO_COPY:** Existing retrieval/evidence-card components; no new platform. Product-specific task semantics remain integration work.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Use deterministic policy/trace and evidence card contracts already described; no donor supplies an intended-use decision for SafeEvidence.

**PROPOSED_RESOLUTION:** Before P01 bind initial clinician audience, specialty/question classes, geography/care setting, supported evidence/documents/devices, patient-specific actions excluded or explicitly supported, and acceptable failure/coverage profiles. Bind claim register now; P23 can evaluate claims later against exact supported use.

**ALTERNATIVES:** Small desktop population-evidence workstation first; advanced guidelines/calculators, broad patient context, voice and quantitative reviews as separate promotions.

**GREENFIELD_REQUIRED:** yes

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Task walkthroughs with representative clinicians, explicit out-of-scope cases, launch-copy versus evaluation-scope traceability and comparative protocol without superiority assumptions.

**DECISION_OWNER:** Founder/product + clinical safety owner

### CODEX-P00-29: Near-zero runtime COGS is not a distribution/pack-build plan

**GAP_ID:** CODEX-P00-29

**SEVERITY:** P1

**AREA:** Resource economics

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Local-first corpus/models are compatible with near-zero founder cost without a bound distribution profile.

**LIVE_EVIDENCE:** [docs/RUNTIME_BUDGET.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/RUNTIME_BUDGET.md#L1) defers measured limits and [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L576) gives profile intent. Planning scenario: 40M reports x 768 dimensions requires 122.88GB float32 or 61.44GB float16 vectors alone, excluding ANN, metadata, blobs and build workspace. This is not a measured PubMed corpus or resident RAM requirement.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-storage/src/encrypted_vault.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/encrypted_vault.rs#L155); [anush008/fastembed-rs: Cargo.toml](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/Cargo.toml#L1); [ncbi/MedCPT: retriever/models.py](https://github.com/ncbi/MedCPT/blob/11e129be74102c98d16a11c310b0b5ce74c1db5e/retriever/models.py#L13); [xberg-io/xberg: crates/xberg/Cargo.toml](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/Cargo.toml#L1)

**FAILURE_MODE:** Users cannot install/update the default corpus; founder pays repeated builds/CDN/relay bandwidth or hidden APIs; mobile cold startup hits model downloads; background threads exhaust thermal/battery budget.

**WHY_IT_MATTERS:** The data-plane choice and default corpus size determine feasibility before expensive benchmarking. Local user RAM and founder distribution cost are separate budgets.

**AFFECTED_PHASES:** P02-P05, P10-P12, P15-P18, P22

**READY_SOURCE_TO_COPY:** Existing indexes, model runtimes, compression/delta transfer and verified offline import; no custom vector/index distribution engine.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Tantivy/FTS5 and local model pack primitives; narrow features/session construction; source streaming and immutable snapshot patterns.

**PROPOSED_RESOLUTION:** Before P03 bind default corpus/wedge, install/update/build workspace bytes, embedding dimensions/quantization, index distribution rights, builder ownership/cost, quotas and user-provided optional downloads. Before runtime phases bind minimum device, startup/latency/peak RAM/disk/CPU/threads/cancellation/thermal budgets with measured promotion. Separate development, pack-generation, bandwidth and per-query costs; no mandatory founder CDN/auth/inference.

**ALTERNATIVES:** User-built indexes, small curated downloadable packs, institution-built licensed indexes or explicit removable packs. Large population corpus optional.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Cold offline install; low disk; peak memory including FFI/worker copies; interrupted pack update; representative desktop/mobile device; budgeted build and distribution scenario including egress/relay costs and rights.

**DECISION_OWNER:** Runtime/performance + distribution owner

### CODEX-P00-30: First imports need a transitive executable/asset admission boundary

**GAP_ID:** CODEX-P00-30

**SEVERITY:** P1

**AREA:** Supply chain and model execution

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Pinned repository source plus rights_uri is enough to admit models/tool workers.

**LIVE_EVIDENCE:** MedScale pack format rejects Pickle/CodeBin/custom ONNX ops by default, a good boundary. Research donors include pickled terminology/weights and service runtimes; parser/model defaults can download additional bytes. A repository code license does not authorize associated model/data packages.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MedScale: crates/medscale-pack/src/format.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-pack/src/format.rs#L1); [ijmarshall/robotreviewer: docker-compose.yml](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/docker-compose.yml#L1); [bwallace/RRnlp: rrnlp/models/sample_size_extractor.py](https://github.com/bwallace/RRnlp/blob/e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0/rrnlp/models/sample_size_extractor.py#L1); [WengLab-InformaticsResearch/PICOX: step_1_2_boundary_prediction.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_1_2_boundary_prediction.ipynb#L1); [anush008/fastembed-rs: Cargo.toml](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/Cargo.toml#L1)

**FAILURE_MODE:** An import brings executable deserialization, plugin/custom-op authority, incompatible embedded UMLS/DrugBank material, font/assets obligations or network-fetched unsigned dependencies.

**WHY_IT_MATTERS:** This is a provenance and trust boundary at first import, not a request for a speculative compliance checklist.

**AFFECTED_PHASES:** P01, P03, P05-P06, P10, P12-P13, P18, P22

**READY_SOURCE_TO_COPY:** Existing SBOM/license tools, pinned package resolution and TUF/pack format; no new dependency scanner.

**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale pack format forbidden_kind/read_bounded_artifact/path guards and tests; pinned dependency lockfiles and per-file upstream LICENSE/NOTICE/REUSE records.

**PROPOSED_RESOLUTION:** Before imports record source/weights/tokenizers/data/font/terminology digests and permission basis separately; dependencies/features/network privileges, shipped executable formats and patch/update owner. Workers have typed bounded messages and no model-authorized tools, DB writes or vault key. Prompt injection in literature must remain data. Reject unreviewed pickle/plugins/ONNX custom ops and run unsupported research formats only in isolated development environments.

**ALTERNATIVES:** Use verified inert model formats and admitted runtime ops only; human/manual workflow for unsupported models.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** yes

**VERIFICATION_REQUIRED:** Cold artifact digest substitution, transitive download, malicious custom op/pickle, prompt/tool injection, unauthorized tool request, hostile citation URL, supply-chain update and exact offline SBOM/notice closure.

**DECISION_OWNER:** Source-admission/security owner

### CODEX-P00-31: FHIR validity and reference integrity need an explicit loss ledger

**GAP_ID:** CODEX-P00-31

**SEVERITY:** P2

**AREA:** FHIR interoperability

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Typed FHIR R4 import adequately preserves patient semantics.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L417) names reference/loss concerns, but no per-supported-resource mapping is frozen. OpenMed reference/profile code is reusable yet syntax/reference validity is not clinical completeness.

**SOURCE_CODE_INSPECTED:** [maziyarpanahi/openmed: openmed/clinical/grounding/types.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/types.py#L1); [AbdulazizShehri/SafeOCR: src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py#L463)

**FAILURE_MODE:** Missing/ambiguous units, references, extensions or timestamps are dropped and the normalized patient context appears complete.

**WHY_IT_MATTERS:** The principle is already phase-bound; freeze exact mappings during P14 rather than infer completeness from schema success.

**AFFECTED_PHASES:** P14, P07, P16

**READY_SOURCE_TO_COPY:** MedScale typed FHIR slice and OpenMed interoperability boundary.

**EXACT_CODE_OR_TESTS_TO_REUSE:** OpenMed openmed/interop/fhir/reference_integrity.py and profiles.py; MedScale FHIR R4 crate tests; SafeOCR FHIR export fixtures with critical-value status.

**PROPOSED_RESOLUTION:** Keep per-field source/reference/version and loss/unsupported-extension records; external validation remains separate from patient applicability. Unknown fields cannot authorize tools.

**ALTERNATIVES:** Support a small documented FHIR subset with explicit rejected resources.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** Dangling/cyclic references, unsupported extensions, absent units, stale observations, multiple conflicting versions and round-trip loss reports.

**DECISION_OWNER:** FHIR owner

### CODEX-P00-32: Diagnostic reproducibility needs a private safe evidence receipt

**GAP_ID:** CODEX-P00-32

**SEVERITY:** P2

**AREA:** Observability

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Local-only diagnostics can capture enough detail without privacy leakage.

**LIVE_EVIDENCE:** [docs/ARCHITECTURE.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/ARCHITECTURE.md#L564) states privacy-first diagnostics but does not distinguish safe public receipt from sensitive reproduction bundle.

**SOURCE_CODE_INSPECTED:** [maziyarpanahi/openmed: openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py#L1); [TheHalfMoon/DAL: src/gaxbench/metrics.py](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/src/gaxbench/metrics.py#L1)

**FAILURE_MODE:** A reproducibility export contains query/PHI, source excerpts, grants or filesystem locations; aggressively redacted logs cannot explain a safety decision.

**WHY_IT_MATTERS:** A small dual receipt design improves qualification and maintenance without changing overall architecture.

**AFFECTED_PHASES:** P01, P20-P22

**READY_SOURCE_TO_COPY:** OpenMed hashed offset/property reporting and DAL measurement manifests.

**EXACT_CODE_OR_TESTS_TO_REUSE:** OpenMed structured/offset_properties.py safe summaries; DAL run/metric identity and trace patterns.

**PROPOSED_RESOLUTION:** Define a default receipt of versions/digests/reason codes/resource/error classes; explicit encrypted user-controlled sensitive bundle with source rights and redaction review. Never upload automatically.

**ALTERNATIVES:** Manual local review of private traces with no support export.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** PHI canaries in receipts, error strings, paths and tracebacks; validate reproducibility from safe metadata and authorized local input.

**DECISION_OWNER:** Diagnostics/privacy owner

### CODEX-P00-33: Voice is an input proposal, not clinical context authority

**GAP_ID:** CODEX-P00-33

**SEVERITY:** P2

**AREA:** Voice

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Optional local voice can share ordinary text assurance.

**LIVE_EVIDENCE:** [docs/MASTER_PLAN.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/MASTER_PLAN.md#L660) is optional and correctly promotion-gated. Drug/dose/negation transcription requires an explicit confirmation boundary; model language support alone is insufficient.

**SOURCE_CODE_INSPECTED:** [AbdulazizShehri/SafeOCR: src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py#L463); [TheHalfMoon/commandMed: src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py#L1)

**FAILURE_MODE:** ASR flips dose/negation, speaker or patient identity; a transient voice question is saved or synced unexpectedly.

**WHY_IT_MATTERS:** Keep optional voice downstream of core semantics and do not incur a new always-on service.

**AFFECTED_PHASES:** P19, P16, P20

**READY_SOURCE_TO_COPY:** Existing qualified local ASR runtime; document critical-value verification patterns, no new speech engine.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Reuse local model pack/runtime admission and critical-token confirmation patterns; no specific ASR model was qualified in this review.

**PROPOSED_RESOLUTION:** Bind push-to-talk/recording retention, speaker/patient context confirmation and critical-token review before submission; voice-derived values stay proposed until confirmed.

**ALTERNATIVES:** Omit voice V1.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** Arabic/English code switching, numbers/drugs/negation, background speakers, offline model missing and cancellation; privacy tests on recordings.

**DECISION_OWNER:** Voice/mobile owner

### CODEX-P00-34: Source readiness needs typed levels rather than status propagation

**GAP_ID:** CODEX-P00-34

**SEVERITY:** P2

**AREA:** Donor qualification

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Resolved foundation dimensions or observed heads imply an admitted implementation slice.

**LIVE_EVIDENCE:** [docs/PREBUILD_KILL_REVIEW_2026-10-07.md](https://github.com/TheHalfMoon/MedOrigin/blob/136cdffc2cd14133e01018ca56833241dd50bc4e/docs/PREBUILD_KILL_REVIEW_2026-10-07.md#L1) explicitly distinguishes planning from clinical validation yet its RESOLVED/NO_KNOWN_P0 presentation can conceal missing slice bindings. SafeOCR, Signthos and research extraction illustrate availability, fit and qualification being different.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1); [TheHalfMoon/Morize: crates/morize-core/src/relation.rs](https://github.com/TheHalfMoon/Morize/blob/62fc04d01d398da93b4dacf0ab2f33e3f1440462/crates/morize-core/src/relation.rs#L1); [TheHalfMoon/MedScale: crates/medscale-network/src/transport.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-network/src/transport.rs#L58); [WengLab-InformaticsResearch/PICOX: step_1_2_boundary_prediction.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_1_2_boundary_prediction.ipynb#L1)

**FAILURE_MODE:** Agent sees COPY and skips dependency/license/correctness qualification; a filename snapshot becomes alleged production proof.

**WHY_IT_MATTERS:** Existing transplant protocol is useful; its admission evidence must be local and enforceable rather than inherited status.

**AFFECTED_PHASES:** P01-P23

**READY_SOURCE_TO_COPY:** Existing provenance records, tests and package tools.

**EXACT_CODE_OR_TESTS_TO_REUSE:** DONOR_TRANSPLANT_PROTOCOL required record and tests-travel rule; exact pinned manifests/test paths in this review. Do not reproduce a full donor workspace.

**PROPOSED_RESOLUTION:** Use AVAILABLE/INSPECTED/COMPONENT_QUALIFIED/PRODUCT_QUALIFIED distinctions, exact acceptance packet and reject/default disposition. Record which source lines/tests were inspected versus executed. Retain upstream updates deliberately.

**ALTERNATIVES:** A simple admission ledger with manual signoff rather than new infrastructure.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** First transplant record traces source bytes to tests, notices, runtime privileges, measured limits and upstream backport/exit owner.

**DECISION_OWNER:** Engineering/source-admission owner

### CODEX-P00-35: Projection relations must not become causal or truth authority

**GAP_ID:** CODEX-P00-35

**SEVERITY:** P2

**AREA:** Graph and historical answers

**CLAIM_OR_ASSUMPTION_CHALLENGED:** Morize relation vocabulary can act as evidence contradiction graph.

**LIVE_EVIDENCE:** Morize relation.rs explicitly supplies vocabulary only, not endpoints, evidence sufficiency, mutations or persistence. Architecture correctly calls graphs projections; preserve that boundary when evolving saved-answer linkage.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/Morize: crates/morize-core/src/relation.rs](https://github.com/TheHalfMoon/Morize/blob/62fc04d01d398da93b4dacf0ab2f33e3f1440462/crates/morize-core/src/relation.rs#L1); [TheHalfMoon/MESC: apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py#L1)

**FAILURE_MODE:** A SUPPORTS/CONTRADICTS edge loses source span/result scope and is counted as independent truth; graph recomputation rewrites historical proof.

**WHY_IT_MATTERS:** The plan already limits projection authority; typed relation semantics and versioned derivation are a refinement, not a new graph platform.

**AFFECTED_PHASES:** P02, P06, P10, P18

**READY_SOURCE_TO_COPY:** Morize vocabulary seed and SQLite indexes.

**EXACT_CODE_OR_TESTS_TO_REUSE:** morize-core relation.rs as REFERENCE only; MESC snapshot identities; existing database projection operations.

**PROPOSED_RESOLUTION:** Retain canonical proof/result references and derivation version in graph edges; rebuild without mutating historical AnswerArtifact. Conflicts require matched estimands before presentation.

**ALTERNATIVES:** No graph database; ordinary typed joins/indexes suffice until a measured need appears.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** Projection rebuild, correction/retraction, duplicated report edge and historical answer traceability.

**DECISION_OWNER:** Core/evidence owner

### CODEX-P00-36: Pin and path drift makes the copy ledger ambiguous

**GAP_ID:** CODEX-P00-36

**SEVERITY:** P3

**AREA:** Documentation maintenance

**CLAIM_OR_ASSUMPTION_CHALLENGED:** The source plan names reproducible source targets.

**LIVE_EVIDENCE:** MedScale, OpenMed, Xberg, docling.rs, Tantivy and kernux documented heads differ from live inspected heads. ottari has an older REUSE pin and newer COPY pin. commandMed actual safety policy is data/spec006/safety_policy.json; fixture location is tests/spec006/fixtures, not the quoted evaluation/spec fixture paths.

**SOURCE_CODE_INSPECTED:** [TheHalfMoon/commandMed: data/spec006/safety_policy.json](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/data/spec006/safety_policy.json#L1); [TheHalfMoon/commandMed: src/commandmed/spec006/scaffold.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/scaffold.py#L83); [maziyarpanahi/openmed: openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py#L1)

**FAILURE_MODE:** A later import cannot tell which revision/path was intended; agent substitutes current source without recording changed bytes.

**WHY_IT_MATTERS:** Drift alone does not prove an old pin unsafe. Behavior/legal gates above carry the implementation severity; the ledger correction itself is process cleanup.

**AFFECTED_PHASES:** P01 and each transplant

**READY_SOURCE_TO_COPY:** Pinned repository snapshots and existing provenance tooling.

**EXACT_CODE_OR_TESTS_TO_REUSE:** Use exact inventory SHAs in Appendix A; validate file existence on the adopted pin and preserve byte digests. No automatic upstream merge.

**PROPOSED_RESOLUTION:** Update ledgers only during authorized reconciliation, with old/new/inspected distinction; do not silently repair authority in this review.

**ALTERNATIVES:** Keep older qualified source only if behavioral history/security fixes are reviewed and target paths exist.

**GREENFIELD_REQUIRED:** no

**BLOCKS_IMPLEMENTATION:** no

**VERIFICATION_REQUIRED:** Machine-check full SHA, target files, license, tests and divergence reason for each admitted source.

**DECISION_OWNER:** Source-ledger owner


## Copy-first decisions for every phase

Ready source means reusable machinery exists, not clinical or product qualification. COPY is a coherent bounded slice with tests/fixtures; DEPEND is a pinned generic library; WORKER is an isolated local specialist stack. REFERENCE is not an executable admission. GF identifiers refer only to the eight bounded integration subsystems below. Blocker numbers refer to CODEX-P00 findings. No phase is implemented by this review.

| Phase | Major capability | Ready source? | Best source | COPY/VENDOR/DEPEND/WORKER/GREENFIELD | Exact reusable target | Remaining SafeEvidence-specific work | Blocker? |
|---|---|---|---|---|---|---|---|
| P01 | Governance/reproducibility/source admission | Partial | Existing repository/transplant protocol; donor manifests | COPY / DEPEND | DONOR_TRANSPLANT_PROTOCOL record; pinned LICENSE/NOTICE/manifests/lockfiles and donor tests | Freeze P0 contracts, first-import rights allowlist and intended use; ordinary CI/SBOM tools | Yes: 01-06, 27-30 |
| P02 | Canonical contracts/private vault/keys | Partial; preferred vault not ready | ottari private vault/protectors; MedScale selected contracts | COPY / DEPEND; GF01/GF02/GF05 | himsat-core/src/vault_sqlcipher.rs, vault_android_keystore.rs, vault_apple_keychain.rs; native bridge; MedScale writer_lock.rs and evidence contracts | Placement/authority/overlap identities, coherent durability/key policy and proof admission; no new DB/crypto | Yes: 01-08, 25-26 |
| P03 | Rights-scoped corpus acquisition/update | Partial | MESC immutable snapshots; ES3 linkage; official NLM feeds | COPY / DEPEND; GF02/GF05 | MESC corpus.py; ES3 bot.py check_trialpubs_nctids, test/test_bot.py; MedScale pack format guards | Feed replay/watermarks/gaps/deletes and SafeEvidence item-level grants; no copied Trialstreamer service | Yes: 01, 05, 08-10, 29-30 |
| P04 | Local lexical retrieval | Yes, generic engine; not clinical qualification | SQLite FTS5; Tantivy if measured need | DEPEND / COPY oracle | Tantivy src/query/bm25.rs and index writer; MedScale synthetic evidence contract as correctness seed; BEIR evaluation.py | Study/report qrels, eligibility/rights filters, clinical scope and lifecycle visibility | Yes: 03, 10-11, 26-27 |
| P05 | Embeddings/reranking tournament | Yes runtime; model choice conditional | fastembed local user-defined sessions; MedCPT baseline | DEPEND / WORKER | fastembed text_embedding/reranking user-defined constructors; MedCPT retriever/models.py; BEIR metrics | Paired encoders/digests, licensed offline artifacts, Arabic/English/study recall and newer challenger tournament; no vector DB | Yes: 08, 11, 20, 29-30 |
| P06 | Identity/span/claim/result verification | Partial research oracles | OpenMed offsets/provenance; SciFact/MultiVerS/Evidence Inference | COPY / WORKER; GF01/GF07 | openmed/structured/offset_properties.py + property tests; SciFact rationale metrics; multivers/model.py; Evidence Inference annotations/preprocessor; PICOX notebooks | Typed clinical result grammar and claim compatibility/admission; human-confirmed numeric extraction | Yes: 03, 06, 12-13, 26-27 |
| P07 | Appraisal/patient applicability | Partial | Official design rubrics; HL7 crosswalk; RobotReviewer proposal oracle | WORKER / REFERENCE; GF04 | HL7 p-evidence-assessment/p-certainty-of-evidence; RobotReviewer robots/bias_robot.py under GPL | Versioned design/result rubric, reviewer state, context freshness/eligibility and domain-specific certainty | Yes: 03, 12, 16, 18, 27-28 |
| P08 | Decision assurance | Partial; no qualified clinical policy | commandMed policy/trace; DAL measurement | COPY / WORKER; GF03 | commandmed/spec006/policy.py, scaffold.py, tests/spec006/fixtures; DAL metrics.py/test_metrics.py | Terminal/action separation, clinician intent, negation, precedence, commit definition and bounded loops | Yes: 04, 06, 12, 17-18, 27 |
| P09 | Calibration | Yes metric machinery; no clinical qualification | DAL | COPY; defer visible percent | gaxbench/metrics.py/selective.py, test_metrics.py/test_selective.py; preserve negative registry evidence | No-percent V1; later estimand, temporal/grouped holdout, subgroup power and full pipeline invalidation | Yes before any percent: 17, 27 |
| P10 | Local synthesis/post-verification | Partial | MedScale ONNX pack/runtime; existing local model runtime | COPY / DEPEND; GF01/GF07 | medscale-pack/src/{format,runtime,onnx_runtime}.rs, onnx_runtime_069 tests; existing admitted inference runtime | Bounded candidate/final proof and no unverified publication; model license/resource qualification | Yes: 06, 08, 12, 17, 20, 30 |
| P11 | Doctor Workstation desktop | Yes shell; choice unqualified | Slint/Tauri qualified tournament | DEPEND; GF06 | Slint native widgets + per-file REUSE terms; Tauri tauri-runtime-wry controls | Clinical evidence UX, keyboard/screen-reader/Arabic fidelity and safe caching/packaging | Yes: 04, 06, 22, 25-28 |
| P12 | PDF/document/OCR | Yes engines; critical safety partial | Narrow Xberg primary hypothesis; docling challenger; SafeOCR | DEPEND / COPY / WORKER | Xberg Cargo feature closure/local PDF path; docling default-features=false; SafeOCR verification.py/contracts.py/tests; OpenMed offsets | Common bounded document/result IR, hostile worker confinement and critical-value admission; no parser framework | Yes: 12-13, 20-21, 25-27, 30 |
| P13 | Guidelines/CQL conformance | Partial; ProtocolWISE unavailable | CQL compiler/engine reference + HL7 crosswalk | DEPEND / WORKER; GF04 | cql-to-elm CqlTranslator.kt/CqlCompiler.kt; reference tests; HL7 recommendation-action profile | Authority/jurisdiction/version/supersession/semantic review; narrative-first; no CQL rewrite | Yes: 18-19, 27-28, 30 |
| P14 | FHIR patient boundary | Yes typed/reference primitives | MedScale FHIR R4; OpenMed reference integrity | COPY / DEPEND | MedScale FHIR crate; openmed/interop/fhir/reference_integrity.py/profiles.py | Supported resource subset, provenance/loss ledger, temporal patient applicability and explicit missingness | Yes: 03, 18, 25; 31 refinement |
| P15 | Native mobile foundation | Yes binding/native key primitives | UniFFI + ottari native protector slices | DEPEND / COPY | uniffi_core/src/ffi/rustbuffer.rs; native Swift/Kotlin bindings; ottari Android/Apple modules | Bounded handle/paging/cancel APIs and supported device/privacy profile; no custom FFI platform | Yes: 07, 23, 25, 29 |
| P16 | Mobile Ask/Scan/Saved/Patient | Partial integration | Shared Rust core; native Compose/SwiftUI; SafeOCR | DEPEND / COPY; GF06 | Same qualified contracts/runtime as desktop; SafeOCR tests; OpenMed mobile parity harness as oracle only | Scoped mobile UX and evidence proof; critical scan confirmation, interruption/low-memory handling | Yes: 04, 06, 18, 21, 23, 25-29 |
| P17 | Pairing/selective sync | Partial transport only | Iroh or LAN TLS/QUIC; SQLite journals | DEPEND; GF02/GF05 | Iroh Endpoint builder/RelayMode with explicit LAN/relay config; native key/capability primitives | Single-use QR enrollment, peer scope, replay/revocation/tombstones, item rights and resumable state | Yes: 01-03, 06-07, 24-25, 29 |
| P18 | Deep Review/synthesis | Partial | ASReview screening; ES3 linking; metafor stronger stats oracle | WORKER / COPY; GF01/GF04 | ASReview stoppers/state/query models; ES3 linkage; metafor rma.uni/rma.mv/rma.glmm/escalc/regtest/ranktest + tests; statsmodels restricted oracle | ReviewProtocol/audit, human decisions, result independence, valid pooling, deviations and living updates | Yes: 03, 10, 13-16, 27; R/GPL/resource admission |
| P19 | Optional voice | Partial; no model qualified here | Existing local ASR + admitted model runtime | DEPEND / WORKER; GF06 | Reused pack/local runtime and critical-token confirmation pattern; no new ASR engine | Supported language/task profile, recording retention and confirmed critical transcript before assurance | Optional; 25-27, 30; 33 refinement |
| P20 | SafeEvidenceBench | Yes scoring; clinical gold new | DAL/BEIR/SciFact/SafeOCR tests | COPY; GF08 | DAL metrics/selective tests; BEIR retrieval/evaluation.py; SciFact rationale metrics; SafeOCR verification tests | Human-adjudicated clinical/bilingual held-out cases and exact pipeline/resource/security qualification | Yes: 11-18, 21, 26-27; protocol starts earlier |
| P21 | Privacy/security/real data | Yes primitives; integration unqualified | MedScale/Kernux/ottari tests; platform controls | COPY / DEPEND | Writer/default-deny/pack/protector test slices; native backup exclusion; TUF conformance fixtures | Actual OS worker/socket/data exposure qualification and real-data permission; threat contract starts before P02 | Yes: 07-09, 20, 23-27, 30 |
| P22 | Release/distribution | Yes generic packaging/update tooling | TUF tough/rust-tuf; native packaging + notices | DEPEND / COPY | RepositoryLoader/trusted-root clients; rollback/expiry/root conformance; upstream LICENSE/NOTICE/REUSE | Exact reproducible artifact, signatures/rights/quotas/offline install and recovery; no custom updater | Yes: 05, 08, 20, 22-25, 29-30 |
| P23 | Claims/comparison/publication | No ready evidence of clinical superiority | Existing reporting/analysis tools only | DEPEND; GF08 | DAL trace/statistical reporting methods, not transplanted empirical claims | Claim register, matched comparative protocol and qualified intended-use evidence; no automatic approval | Yes: 17, 27-28; no safety/compliance/superiority claim |

## Bounded greenfield justification register

These are integration semantics, not eight independent platforms. The greenfield-required fields in findings refer to these shared units and must not be summed as separate engines. Tiny rule/catalog/crosswalk additions belong to the unit below; additional new frameworks require a fresh source search and justification. Standard formulas, Unicode algorithms, parser engines, embedding runtimes, databases, transport cryptography, TUF, FFI and screening algorithms remain reused.

| ID | Explicit classification | New bounded work | Why no ready inspected source supplies it | Reused foundation / phases |
|---|---|---|---|---|
| GF01 | GREENFIELD_JUSTIFIED | SafeEvidence evidence/result/proof integration contracts | No inspected donor represents all report/study/participant/result overlap plus atomic justified-answer publication; HL7 profiles are interchange references, MESC/MedScale are narrower | HL7, MESC, MedScale, commandMed; P02/P06/P10/P18 |
| GF02 | GREENFIELD_JUSTIFIED | Item rights and scoped evidence/patient authority adapters | Existing libraries do not encode publisher/institution/user combinations across SafeEvidence ingest/index/export/sync; no new ACL or crypto engine | Existing capability/policy/storage primitives; P02/P03/P17 |
| GF03 | GREENFIELD_JUSTIFIED | Clinical assurance policy and liveness semantics | commandMed lexical/synthetic policy cannot supply clinician intent, per-claim commitment, conflict meaning or calibrated coverage; adapt its precedence/trace machinery | commandMed/DAL; P08 |
| GF04 | GREENFIELD_JUSTIFIED | Clinical applicability, rubric and guideline/tool admission profiles | CQL syntax and research appraisal do not establish intended-use eligibility, temporal context or licensed authoritative rubric; tiny qualified tool adapters only after ready-source search | CQL/HL7/UCUM/rubric sources; P07/P13/P14/P18 |
| GF05 | GREENFIELD_JUSTIFIED | Evidence lifecycle/current-validity and sync integration transactions | Existing snapshots/feeds/transports do not coordinate corrections, grants, publication proofs and offline/tombstone policies for SafeEvidence | MESC/ES3/SQLCipher/TUF/transport; P03/P10/P17 |
| GF06 | GREENFIELD_JUSTIFIED | Clinician desktop/mobile/Arabic semantic UX | Generic shells/components cannot provide the product's evidence-reading, unresolved-state, safe critical-input and bilingual presentation behavior | Slint/Tauri/native UI, existing shaping/offset libraries; P11/P16/P19 |
| GF07 | GREENFIELD_JUSTIFIED | Clinical structured-claim/extraction verification adapter | Research rationale/direction/PICO models do not enforce complete numeric, population, timepoint, source version and final text compatibility | SciFact/MultiVerS/Evidence Inference/OpenMed/SafeOCR; P06/P10/P12 |
| GF08 | GREENFIELD_JUSTIFIED | Human-adjudicated SafeEvidence holdout and qualification protocol | Donor gold targets/scopes and negative results cannot establish SafeEvidence clinical assurance or Arabic fidelity | DAL/BEIR/SciFact/SafeOCR metric/test machinery; earlier protocols, P20/P23 |

Total justified greenfield subsystems: **8**. This count includes semantic profiles and benchmark governance; it does not authorize eight bespoke runtimes. No fresh standard statistics, search/vector DB, PDF/OCR, crypto/updater, CQL parser, mobile binding framework or speech engine is justified.

## Where better ready code replaces or narrows planned work

Count: **5 distinct planned capabilities with a stronger starting implementation than the preferred slice or an unnecessarily broad new integration**. This is a scoped source recommendation, not a claim that five complete production systems passed qualification. Other ready sources already present in the plan are not misreported as newly discovered duplication.

1. Private-vault backup/checkpoint: ottari quiesced SQLCipher snapshot plus WAL/restore tests is stronger than copying MedScale's sealed-directory backup path.
2. Native mobile key protection/backup exclusion: ottari real Android/Apple bridge slices are stronger than MedScale generic desktop credential wrapping or a boolean mobile policy.
3. Critical medical OCR verification: SafeOCR verification/contracts/tests are available; treating the source as empty would duplicate those gates.
4. Statistical synthesis methods/oracle: metafor fills important REML/correlation/rare-event and diagnostic gaps beyond statsmodels.meta_analysis. Use an appropriately licensed oracle/optional worker, not a broad rewrite.
5. Production update/pack trust: an existing TUF client/reference suite supplies production metadata/root/expiry/rollback machinery beyond MedScale's synthetic signer. TUF is already mentioned in the roadmap; move its trust contract to first pack admission rather than rebuilding or promoting the test signer.

The plan already correctly prefers OpenMed offsets/grounding, commandMed policy scaffolding, DAL metrics, FTS5/Tantivy, fastembed, Xberg/docling, ASReview, UniFFI and CQL over generic greenfield. The audit narrows their actual admitted role. There is no evidence that a new vector database or generic parser is needed. A complete ready licensed quantitative clinical extractor, clinical decision policy, pairing engine or calculator catalog was not established by the inspected sources; do not invent one.

## Rights and corpus lifecycle admission table

Source discoverability, technical access and code permission are distinct from local storage, index/projection use, synchronization, export and redistribution. Every operation is item/grant/version scoped; an unknown permission is not a distribution permission. Embedding/index distribution must receive a separate rights determination rather than assuming transformation removes restrictions. The following are admission requirements, not legal certification.

| Material | Observed evidence / terms | Admission consequences |
|---|---|---|
| PubMed metadata/abstracts | [PubMed download](https://pubmed.ncbi.nlm.nih.gov/download/) specifies annual baseline plus numbered daily new/revised/deleted records; [NLM download terms](https://www.nlm.nih.gov/databases/download.html) warn abstracts may be copyrighted and require acknowledgment/no endorsement/staleness notice | Baseline/delta identity and sequence completeness; distinguish deletion from retraction. Metadata availability does not authorize blanket abstract pack/export/sync; index/storage/redistribution decisions need a recorded basis |
| PMC / OA | [PMC text mining](https://pmc.ncbi.nlm.nih.gov/tools/textmining/) and [OA subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/) identify approved automated retrieval methods and article-specific terms; not every PMC article is OA | Use approved routes (cloud/OAI/E-utilities/BioC as applicable); bind article license/version. CC BY, NC and ND conditions differ, as do manuscripts and publisher content. Fetchable text is not blanket redistributable |
| Europe PMC | Official terms retrieval returned HTTP 403 during this audit | Discovery/adapters remain candidate; no permission to copy/redistribute content was inferred. Recheck official terms and each originating article/grant before admission |
| Crossref / Retraction Watch | [Official feed documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/) says updated every working day and corrections/EoCs incomplete | Record feed rights and retrieval watermark; absence of alert != active/valid. Multiple feeds/conflicting metadata need unknown/proposed states; full-text rights do not follow DOI metadata |
| MeSH / RxNorm / other terminology | [MeSH download](https://www.nlm.nih.gov/databases/download/mesh.html); [RxNorm terms](https://www.nlm.nih.gov/research/umls/rxnorm/docs/termsofservice.html) distinguish normalized public-domain names from proprietary source vocabularies/full UMLS-licensed releases | Pin package and release, license/acceptance/attribution, clinical staleness notice and source-provider terms. Do not copy bundled UMLS/DrugBank assets merely because the surrounding Python code is licensed |
| Institutional literature / user documents | Permission must be obtained from the controlling publisher/institution/user grant and supported operation | Private store and rights-scoped derived indexes; user upload does not prove cross-device, onward export or public-pack rights. Revoked future access does not erase already distributed copies |
| Model weights/tokenizers | Code LICENSE is separate; MedCPT repo has a US-government-work notice, other model cards may differ | Bind exact model artifact/card/license/digest, transitive base weights, tokenizers, local conversion/quantization rights, data/attribution and runtime privileges. No model winner or weights rights certification was inferred here |
| Research corpora | SciFact code Apache-2.0, claims CC BY 4.0, abstracts ODC-By 1.0 in its LICENSE; SYNERGY root CC0 does not automatically clear third-party abstracts; BEIR datasets have separate terms | Code scoring machinery can be reused under its license; each copied dataset/item gets its own rights/attribution and split provenance. Research permission is not production evidence-pack permission |

Official terms were fetched on 2026-10-07, with source pages sometimes updated during 2026. They are live donor/corpus evidence, not newer SafeEvidence product authority. Routes and terms must be revalidated on actual admission. This review did not query a patient's data or distribute literature/model weights.

## Source/legal classification corrections

- Trialstreamer: no detected root license in inspected tree. Public source availability plus founder direction does not supply upstream permission. REFERENCE pending rightsholder grant; PostgreSQL/services are not default local product fit.
- RobotReviewer: GPL-3.0 plus separately sourced terminology/model material and service architecture. Research oracle/optional worker only after rights/distribution review; isolation does not erase copyleft.
- Signthos: AGPL-3.0-only material is present; GitHub top-level license metadata returned null. Do not infer permissive rights or a ready QR/mobile donor. The inspected product is document signing, and planned sync is not source implementation.
- Slint: custom royalty-free 2.0, GPL-3.0 or commercial alternatives and per-file REUSE assets. Attribution/About/redistribution conditions must be decided before shell admission; it is not a generic permissive classification.
- metafor: GPL >=2 and R/dependency runtime; materially broader stats coverage, but not Apache Rust paste-in. TUF rust client actual license files are Apache/MIT, despite limited metadata labels.
- SciFact/SYNERGY/BEIR/OpenMed/model repositories: code, datasets, publication content and weights have separate grants. Correct existing legal warnings are retained; the error is blanket admission, not a claim that every ledger license entry is wrong.
- HL7/ebm: inspected profiles are trial-use and root API license metadata was null; interchange reference does not license guideline/publisher/rubric content. Verify the applicable HL7 content/package terms before redistribution.

## Appendix A: documented, live and inspected donor pins

Default-branch live head is also the inspected revision below. No source recommendation assumes old and new revisions are equivalent. Documented pins are literal frozen plan values; abbreviated pins remain abbreviated rather than invented. Root license labels are orientation only; actual copied file/dependency/asset obligations control. `NOASSERTION`/null API metadata is not permission.

| Source | Documented frozen pin | Live head = inspected revision | License orientation |
|---|---|---|---|
| [AbdulazizShehri/SafeOCR](https://github.com/AbdulazizShehri/SafeOCR/tree/7b892c7d78132e5f1990e2a9409cd398d5436da0) | EMPTY/unqualified; no exact implementation pin | `7b892c7d78132e5f1990e2a9409cd398d5436da0` | Apache-2.0 |
| [allenai/scifact](https://github.com/allenai/scifact/tree/68b98a56d93e0f9da0d2aab4e6c3294699a0f72e) | 68b98a56d93e0f9da0d2aab4e6c3294699a0f72e | `68b98a56d93e0f9da0d2aab4e6c3294699a0f72e` | Apache-2.0 code; CC-BY-4.0 claims; ODC-By-1.0 corpus |
| [anush008/fastembed-rs](https://github.com/anush008/fastembed-rs/tree/29059745b8c5df6a1adc263b6903609e164ad3c5) | 29059745b8c5df6a1adc263b6903609e164ad3c5 | `29059745b8c5df6a1adc263b6903609e164ad3c5` | Apache-2.0 |
| [asreview/asreview](https://github.com/asreview/asreview/tree/79d568212b2b0a78f9fd7be3c5117dfb890489f9) | 79d568212b2b0a78f9fd7be3c5117dfb890489f9 | `79d568212b2b0a78f9fd7be3c5117dfb890489f9` | Apache-2.0 |
| [asreview/synergy-dataset](https://github.com/asreview/synergy-dataset/tree/dc2dadfdbb98eb1b4259604789abd640aa3b693e) | dc2dadfdbb98eb1b4259604789abd640aa3b693e | `dc2dadfdbb98eb1b4259604789abd640aa3b693e` | CC0-1.0 |
| [awslabs/tough](https://github.com/awslabs/tough/tree/98d8eb8b2ce63515d9b4981c938ef6453c5b5771) | 98d8eb8b2ce63515d9b4981c938ef6453c5b5771 | `98d8eb8b2ce63515d9b4981c938ef6453c5b5771` | Apache-2.0 / MIT files |
| [beir-cellar/beir](https://github.com/beir-cellar/beir/tree/ef83d29307061c65d04b035b4f4e7c18bd8374af) | ef83d29307061c65d04b035b4f4e7c18bd8374af | `ef83d29307061c65d04b035b4f4e7c18bd8374af` | Apache-2.0 |
| [bwallace/RRnlp](https://github.com/bwallace/RRnlp/tree/e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0) | e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0 | `e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0` | MIT |
| [cqframework/clinical_quality_language](https://github.com/cqframework/clinical_quality_language/tree/c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2) | c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2 | `c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2` | Apache-2.0 |
| [docling-project/docling.rs](https://github.com/docling-project/docling.rs/tree/2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86) | 8aea8d543de832116ebb29436d9281bfe7e82d73 | `2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86` | MIT |
| [dwadden/multivers](https://github.com/dwadden/multivers/tree/a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e) | a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e | `a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e` | MIT |
| [evidence-surveillance/es3](https://github.com/evidence-surveillance/es3/tree/fa845217690e179d3f8151e97773aabc035d6cfe) | fa845217690e179d3f8151e97773aabc035d6cfe | `fa845217690e179d3f8151e97773aabc035d6cfe` | MIT |
| [HL7/ebm](https://github.com/HL7/ebm/tree/374b48bb956e26a51dfdece365d98786ccc90e62) | 374b48bb956e26a51dfdece365d98786ccc90e62 | `374b48bb956e26a51dfdece365d98786ccc90e62` | Package/content terms require verification; API null |
| [ijmarshall/robotreviewer](https://github.com/ijmarshall/robotreviewer/tree/9a2781974c3edc6322b4fb329b1ea0348af7b8a1) | 9a2781974c3edc6322b4fb329b1ea0348af7b8a1 | `9a2781974c3edc6322b4fb329b1ea0348af7b8a1` | GPL-3.0 |
| [ijmarshall/trialstreamer](https://github.com/ijmarshall/trialstreamer/tree/a97cb8332c039e228ef42188c9d966440894e354) | a97cb8332c039e228ef42188c9d966440894e354 | `a97cb8332c039e228ef42188c9d966440894e354` | No detected license grant |
| [jayded/evidence-inference](https://github.com/jayded/evidence-inference/tree/a661e8c14f973398380c8865cf2f27a535aaaf6d) | a661e8c14f973398380c8865cf2f27a535aaaf6d | `a661e8c14f973398380c8865cf2f27a535aaaf6d` | MIT |
| [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed/tree/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b) | SOURCE: 59d9cb0a2e0ccbba8fa3d891a66d83ffaf45e837 (v2.2); COPY: 252806aa946c200f3857cc0f6fda37fd83a5cc85 | `79ddb2b1ab08146432add4fe9ae6da3d393f9e2b` | Apache-2.0 |
| [mozilla/uniffi-rs](https://github.com/mozilla/uniffi-rs/tree/bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea) | bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea | `bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea` | MPL-2.0 |
| [n0-computer/iroh](https://github.com/n0-computer/iroh/tree/41e782a8f0c858bcd1f74bfc703758244d5a6538) | No exact frozen pin; live challenger/reference inspected | `41e782a8f0c858bcd1f74bfc703758244d5a6538` | Apache-2.0 |
| [ncbi/MedCPT](https://github.com/ncbi/MedCPT/tree/11e129be74102c98d16a11c310b0b5ce74c1db5e) | 11e129be74102c98d16a11c310b0b5ce74c1db5e | `11e129be74102c98d16a11c310b0b5ce74c1db5e` | US Government Work/public-domain notice; weights separate |
| [quickwit-oss/tantivy](https://github.com/quickwit-oss/tantivy/tree/e988ecb7a11109d89f9f4582b386089fc3a2fec0) | 1783018f9e6c0ffa4a884df3812011d8d13e4b52 | `e988ecb7a11109d89f9f4582b386089fc3a2fec0` | MIT |
| [slint-ui/slint](https://github.com/slint-ui/slint/tree/a199b6bddde18d939886f2a0de0700999fe32851) | No exact frozen pin; live challenger/reference inspected | `a199b6bddde18d939886f2a0de0700999fe32851` | Royalty-free-2.0 / GPL-3.0 / commercial, per-file REUSE |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels/tree/8278e2d218cc85bac2c7af02feb9a19a0e499b04) | 8278e2d218cc85bac2c7af02feb9a19a0e499b04 | `8278e2d218cc85bac2c7af02feb9a19a0e499b04` | BSD-3-Clause |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri/tree/a916205db2c21a2475502452efa9b70132ae52f3) | No exact frozen pin; live challenger/reference inspected | `a916205db2c21a2475502452efa9b70132ae52f3` | Apache-2.0 |
| [TheHalfMoon/commandMed](https://github.com/TheHalfMoon/commandMed/tree/51f73ec05750137e5bd94ffa0765f6383f475fee) | 51f73ec05750137e5bd94ffa0765f6383f475fee | `51f73ec05750137e5bd94ffa0765f6383f475fee` | Apache-2.0 |
| [TheHalfMoon/DAL](https://github.com/TheHalfMoon/DAL/tree/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03) | 8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03 | `8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03` | Apache-2.0 |
| [TheHalfMoon/kernux](https://github.com/TheHalfMoon/kernux/tree/2085b6ed1121b1a94c66c076bdd6b578da4dad0d) | REUSE: 4b5450d40f89de7541bbd5fc4f85e7a63c173f8d; COPY: a0c4aaee... | `2085b6ed1121b1a94c66c076bdd6b578da4dad0d` | Apache-2.0 |
| [TheHalfMoon/MedScale](https://github.com/TheHalfMoon/MedScale/tree/98c26aa3a0f919f4dfbb0c2adc27265a767631e4) | 1e2b7d94e970256b38bda15fa91f62bc397e825a | `98c26aa3a0f919f4dfbb0c2adc27265a767631e4` | Apache-2.0 |
| [TheHalfMoon/MESC](https://github.com/TheHalfMoon/MESC/tree/f9b7579189b77b06379d1a71d104d4b0267cf500) | f9b7579189b77b06379d1a71d104d4b0267cf500 | `f9b7579189b77b06379d1a71d104d4b0267cf500` | Apache-2.0 |
| [TheHalfMoon/Morize](https://github.com/TheHalfMoon/Morize/tree/62fc04d01d398da93b4dacf0ab2f33e3f1440462) | 62fc04d01d398da93b4dacf0ab2f33e3f1440462 | `62fc04d01d398da93b4dacf0ab2f33e3f1440462` | Apache-2.0 |
| [TheHalfMoon/ottari](https://github.com/TheHalfMoon/ottari/tree/b7948b541edcd31863991023e18231b8d8d69b82) | REUSE: fb6ba054435931e0fc1d18d18c2bf21ca74c41c5; COPY: b7948b541edcd31863991023e18231b8d8d69b82 | `b7948b541edcd31863991023e18231b8d8d69b82` | Apache-2.0 |
| [TheHalfMoon/Signthos](https://github.com/TheHalfMoon/Signthos/tree/f945f12fd1a2b600c2c61493162e3654b4d5b50c) | f945f12fd1a2b600c2c61493162e3654b4d5b50c | `f945f12fd1a2b600c2c61493162e3654b4d5b50c` | AGPL-3.0-only material; root API null |
| [theupdateframework/python-tuf](https://github.com/theupdateframework/python-tuf/tree/ff0ff7897454d1dedc07a6d2cce53361d07f8828) | No exact frozen pin; live challenger/reference inspected | `ff0ff7897454d1dedc07a6d2cce53361d07f8828` | Apache-2.0 |
| [theupdateframework/rust-tuf](https://github.com/theupdateframework/rust-tuf/tree/219ca7d05818d5dd44ec4e32ab47c5ce64a7bf44) | No exact frozen pin; live challenger/reference inspected | `219ca7d05818d5dd44ec4e32ab47c5ce64a7bf44` | Apache-2.0 / MIT files |
| [theupdateframework/tuf-conformance](https://github.com/theupdateframework/tuf-conformance/tree/8729aa18b7811503556c8aa602eebde11471ea2a) | No exact frozen pin; live challenger/reference inspected | `8729aa18b7811503556c8aa602eebde11471ea2a` | MIT |
| [WengLab-InformaticsResearch/PICOX](https://github.com/WengLab-InformaticsResearch/PICOX/tree/f3351c4786bf197efacfcefc1c1e66c36c245842) | f3351c4786bf197efacfcefc1c1e66c36c245842 | `f3351c4786bf197efacfcefc1c1e66c36c245842` | MIT |
| [wviechtb/metafor](https://github.com/wviechtb/metafor/tree/a17aa2e9f0ef3bf1136c2bc8431b05370d974821) | No exact frozen pin; live challenger/reference inspected | `a17aa2e9f0ef3bf1136c2bc8431b05370d974821` | GPL >=2 in DESCRIPTION |
| [xberg-io/xberg](https://github.com/xberg-io/xberg/tree/de48b6160efe01aff3c849fd054c465f5057390f) | 42c03edd06964accd6f8b796fba1647da2b8121d | `de48b6160efe01aff3c849fd054c465f5057390f` | MIT |

Important stale/divergent records: MedScale, OpenMed (both recorded pins), Xberg, docling.rs, Tantivy and kernux; ottari's older REUSE record conflicts with its newer COPY record. SafeOCR's empty/unqualified status is materially stale relative to its live implementation. An old pin may be intentional; this review does not automatically promote any live head or assert a historical regression without inspecting that historical slice.

## Appendix B: implementation inspection targets and limits

The list below identifies actual source-oriented targets reviewed, not just README claims. Files were inspected selectively; the audit did not execute or fully read every file fetched from each repository. Paths in reusable-target fields identify code/tests to qualify or carry with a transplant, even when their full suite was not executed. No hidden production readiness is inferred from test existence.

- **TheHalfMoon/MedScale**: [crates/medscale-storage/src/encrypted_vault.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/encrypted_vault.rs); [crates/medscale-storage/src/writer_lock.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/writer_lock.rs); [crates/medscale-storage/src/sealed_blob.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/sealed_blob.rs); [crates/medscale-storage/src/sqlite_meta.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/sqlite_meta.rs); [crates/medscale-storage/src/backup.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-storage/src/backup.rs); [crates/medscale-keys/src/provider.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-keys/src/provider.rs); [crates/medscale-keys/src/pack_trust.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-keys/src/pack_trust.rs); [crates/medscale-pack/src/format.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-pack/src/format.rs); [crates/medscale-pack/src/runtime.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-pack/src/runtime.rs); [crates/medscale-network/src/transport.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-network/src/transport.rs); [crates/medscale-contracts/src/evidence/mod.rs](https://github.com/TheHalfMoon/MedScale/blob/98c26aa3a0f919f4dfbb0c2adc27265a767631e4/crates/medscale-contracts/src/evidence/mod.rs).
- **TheHalfMoon/DAL**: [src/gaxbench/metrics.py](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/src/gaxbench/metrics.py); [src/gaxbench/selective.py](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/src/gaxbench/selective.py); [registry/p08_sg000023_paper_evidence/main_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/main_results.json); [registry/p08_sg000023_paper_evidence/selective_results.json](https://github.com/TheHalfMoon/DAL/blob/8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03/registry/p08_sg000023_paper_evidence/selective_results.json).
- **TheHalfMoon/commandMed**: [src/commandmed/spec006/scaffold.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/scaffold.py); [src/commandmed/spec006/policy.py](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/src/commandmed/spec006/policy.py); [data/spec006/safety_policy.json](https://github.com/TheHalfMoon/commandMed/blob/51f73ec05750137e5bd94ffa0765f6383f475fee/data/spec006/safety_policy.json).
- **TheHalfMoon/MESC**: [apps/workspace/src/medscale_workspace/corpus.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/corpus.py); [apps/workspace/src/medscale_workspace/evidence_strength.py](https://github.com/TheHalfMoon/MESC/blob/f9b7579189b77b06379d1a71d104d4b0267cf500/apps/workspace/src/medscale_workspace/evidence_strength.py).
- **TheHalfMoon/Morize**: [crates/morize-core/src/relation.rs](https://github.com/TheHalfMoon/Morize/blob/62fc04d01d398da93b4dacf0ab2f33e3f1440462/crates/morize-core/src/relation.rs).
- **TheHalfMoon/ottari**: [crates/himsat-core/src/vault_sqlcipher.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_sqlcipher.rs); [crates/himsat-core/src/vault_android_keystore.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_android_keystore.rs); [crates/himsat-core/src/vault_apple_keychain.rs](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/src/vault_apple_keychain.rs); [crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java](https://github.com/TheHalfMoon/ottari/blob/b7948b541edcd31863991023e18231b8d8d69b82/crates/himsat-core/android/com/thehalfmoon/himsat/crypto/HimsatAndroidKeystoreBridge.java).
- **TheHalfMoon/kernux**: [crates/kernux-policy/src/egress.rs](https://github.com/TheHalfMoon/kernux/blob/2085b6ed1121b1a94c66c076bdd6b578da4dad0d/crates/kernux-policy/src/egress.rs).
- **AbdulazizShehri/SafeOCR**: [src/safeocr/verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/verification.py); [src/safeocr/ocr.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/src/safeocr/ocr.py); [tests/test_verification.py](https://github.com/AbdulazizShehri/SafeOCR/blob/7b892c7d78132e5f1990e2a9409cd398d5436da0/tests/test_verification.py).
- **maziyarpanahi/openmed**: [openmed/structured/offset_properties.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/structured/offset_properties.py); [openmed/training/synthetic/offset_projection.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/training/synthetic/offset_projection.py); [openmed/clinical/grounding/types.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/types.py); [openmed/clinical/grounding/snapshot_cache.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/openmed/clinical/grounding/snapshot_cache.py); [tests/mobile/test_flutter_ffi.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/tests/mobile/test_flutter_ffi.py); [tests/mobile/test_rn_bridge_parity.py](https://github.com/maziyarpanahi/openmed/blob/79ddb2b1ab08146432add4fe9ae6da3d393f9e2b/tests/mobile/test_rn_bridge_parity.py).
- **xberg-io/xberg**: [crates/xberg/Cargo.toml](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/Cargo.toml); [crates/xberg/src/model_download.rs](https://github.com/xberg-io/xberg/blob/de48b6160efe01aff3c849fd054c465f5057390f/crates/xberg/src/model_download.rs).
- **docling-project/docling.rs**: [crates/docling/Cargo.toml](https://github.com/docling-project/docling.rs/blob/2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86/crates/docling/Cargo.toml); [crates/docling-pdf/src/lib.rs](https://github.com/docling-project/docling.rs/blob/2d8f98b3b0cb3c2b1712b46cbc81ce623499fb86/crates/docling-pdf/src/lib.rs).
- **anush008/fastembed-rs**: [Cargo.toml](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/Cargo.toml); [src/text_embedding/impl.rs](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/src/text_embedding/impl.rs); [src/reranking/impl.rs](https://github.com/anush008/fastembed-rs/blob/29059745b8c5df6a1adc263b6903609e164ad3c5/src/reranking/impl.rs).
- **ncbi/MedCPT**: [retriever/models.py](https://github.com/ncbi/MedCPT/blob/11e129be74102c98d16a11c310b0b5ce74c1db5e/retriever/models.py); [LICENSE](https://github.com/ncbi/MedCPT/blob/11e129be74102c98d16a11c310b0b5ce74c1db5e/LICENSE).
- **asreview/asreview**: [asreview/models/stoppers.py](https://github.com/asreview/asreview/blob/79d568212b2b0a78f9fd7be3c5117dfb890489f9/asreview/models/stoppers.py).
- **mozilla/uniffi-rs**: [uniffi_core/src/ffi/rustbuffer.rs](https://github.com/mozilla/uniffi-rs/blob/bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea/uniffi_core/src/ffi/rustbuffer.rs).
- **awslabs/tough**: [tough/src/lib.rs](https://github.com/awslabs/tough/blob/98d8eb8b2ce63515d9b4981c938ef6453c5b5771/tough/src/lib.rs).
- **theupdateframework/rust-tuf**: [tuf/src/client.rs](https://github.com/theupdateframework/rust-tuf/blob/219ca7d05818d5dd44ec4e32ab47c5ce64a7bf44/tuf/src/client.rs).
- **cqframework/clinical_quality_language**: [cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt](https://github.com/cqframework/clinical_quality_language/blob/c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2/cql-to-elm/src/commonMain/kotlin/org/cqframework/cql/cql2elm/CqlTranslator.kt).
- **HL7/ebm**: [input/fsh/evidence/p-single-study-evidence.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-single-study-evidence.fsh); [input/fsh/evidence-variable/p-group-assignment.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence-variable/p-group-assignment.fsh); [input/fsh/evidence/p-endpoint-analysis-plan.fsh](https://github.com/HL7/ebm/blob/374b48bb956e26a51dfdece365d98786ccc90e62/input/fsh/evidence/p-endpoint-analysis-plan.fsh).
- **allenai/scifact**: [LICENSE.md](https://github.com/allenai/scifact/blob/68b98a56d93e0f9da0d2aab4e6c3294699a0f72e/LICENSE.md); [verisci/evaluate/lib/metrics.py](https://github.com/allenai/scifact/blob/68b98a56d93e0f9da0d2aab4e6c3294699a0f72e/verisci/evaluate/lib/metrics.py).
- **dwadden/multivers**: [multivers/model.py](https://github.com/dwadden/multivers/blob/a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e/multivers/model.py); [requirements.txt](https://github.com/dwadden/multivers/blob/a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e/requirements.txt).
- **evidence-surveillance/es3**: [bot.py](https://github.com/evidence-surveillance/es3/blob/fa845217690e179d3f8151e97773aabc035d6cfe/bot.py); [crud.py](https://github.com/evidence-surveillance/es3/blob/fa845217690e179d3f8151e97773aabc035d6cfe/crud.py); [test/test_bot.py](https://github.com/evidence-surveillance/es3/blob/fa845217690e179d3f8151e97773aabc035d6cfe/test/test_bot.py).
- **ijmarshall/trialstreamer**: [trialstreamer/dbutil.py](https://github.com/ijmarshall/trialstreamer/blob/a97cb8332c039e228ef42188c9d966440894e354/trialstreamer/dbutil.py); [docker-compose.yml](https://github.com/ijmarshall/trialstreamer/blob/a97cb8332c039e228ef42188c9d966440894e354/docker-compose.yml).
- **ijmarshall/robotreviewer**: [docker-compose.yml](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/docker-compose.yml); [robotreviewer/robots/bias_robot.py](https://github.com/ijmarshall/robotreviewer/blob/9a2781974c3edc6322b4fb329b1ea0348af7b8a1/robotreviewer/robots/bias_robot.py).
- **bwallace/RRnlp**: [rrnlp/models/sample_size_extractor.py](https://github.com/bwallace/RRnlp/blob/e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0/rrnlp/models/sample_size_extractor.py).
- **jayded/evidence-inference**: [evidence_inference/preprocess/preprocessor.py](https://github.com/jayded/evidence-inference/blob/a661e8c14f973398380c8865cf2f27a535aaaf6d/evidence_inference/preprocess/preprocessor.py); [evidence_inference/models/pipeline.py](https://github.com/jayded/evidence-inference/blob/a661e8c14f973398380c8865cf2f27a535aaaf6d/evidence_inference/models/pipeline.py).
- **WengLab-InformaticsResearch/PICOX**: [step_1_2_boundary_prediction.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_1_2_boundary_prediction.ipynb); [step_2_2_span_clf.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_2_2_span_clf.ipynb); [step_3_evaluate.ipynb](https://github.com/WengLab-InformaticsResearch/PICOX/blob/f3351c4786bf197efacfcefc1c1e66c36c245842/step_3_evaluate.ipynb).
- **statsmodels/statsmodels**: [statsmodels/stats/meta_analysis.py](https://github.com/statsmodels/statsmodels/blob/8278e2d218cc85bac2c7af02feb9a19a0e499b04/statsmodels/stats/meta_analysis.py).
- **wviechtb/metafor**: [R/rma.uni.r](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/R/rma.uni.r); [R/rma.mv.r](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/R/rma.mv.r); [R/rma.glmm.r](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/R/rma.glmm.r); [R/regtest.r](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/R/regtest.r); [DESCRIPTION](https://github.com/wviechtb/metafor/blob/a17aa2e9f0ef3bf1136c2bc8431b05370d974821/DESCRIPTION).
- **beir-cellar/beir**: [beir/retrieval/evaluation.py](https://github.com/beir-cellar/beir/blob/ef83d29307061c65d04b035b4f4e7c18bd8374af/beir/retrieval/evaluation.py).
- **quickwit-oss/tantivy**: [src/query/bm25.rs](https://github.com/quickwit-oss/tantivy/blob/e988ecb7a11109d89f9f4582b386089fc3a2fec0/src/query/bm25.rs).
- **slint-ui/slint**: [LICENSE.md](https://github.com/slint-ui/slint/blob/a199b6bddde18d939886f2a0de0700999fe32851/LICENSE.md).
- **n0-computer/iroh**: [iroh/src/endpoint.rs](https://github.com/n0-computer/iroh/blob/41e782a8f0c858bcd1f74bfc703758244d5a6538/iroh/src/endpoint.rs).

Signthos was inspected for license/source-tree fit (AGPL material and current document-signing modules), plus actual `packages/providers/src/pdf/browser/pdf-extract-runtime.js`, `pdfium-structural-evidence.js` and `packages/providers/test/pdf-extract-runtime.test.js` at the pinned head. These contain a digest-pinned local PDFium WASM boundary, bounded input/output and structural observation checks; the test surface uses synthetic/fake runtimes and PDF fixtures. They are useful document-boundary references after AGPL/transitive PDFium rights review, not a ready QR implementation. SYNERGY license/data organization, TUF reference updater/trusted_metadata_set and conformance rollback code, Tauri license/runtime configuration and manifests were also inspected selectively; no device/transport/protocol test was claimed. Tauri `tauri-runtime-wry/src/lib.rs:4712-4745` wires data directory/incognito/clipboard controls and `4820-4825` the navigation callback; their presence is configuration machinery, not a privacy guarantee. Modern multilingual model challengers were named for a later admission/tournament, not represented as source-inspected or benchmarked winners.

## Appendix C: focused probe receipts

### commandMed lexical rule

Revision: `51f73ec05750137e5bd94ffa0765f6383f475fee`. The probe parsed `src/commandmed/spec006/scaffold.py`, compiled only the exact `_rule_matches` AST with `re` and typing substitutions, and passed the actual EMERGENCY rule from `data/spec006/safety_policy.json`. It asserted a match for each case below. This proves the rule matching behavior, not the full scaffold's ultimate action or a population false-escalation rate.

| Input scenario | Actual lexical emergency match |
|---|---|
| What evidence supports evaluation of chest pain in adults? | true |
| The patient denies chest pain and has no dyspnea. | true |
| A review protocol excludes participants with chest pain. | true |
| Arabic population-level evidence question containing the same symptom phrase | true |
| Arabic patient-negation statement containing the same symptom phrase | true |

Arabic inputs were evaluated as Unicode strings; descriptions here are English to preserve repository language. The observed match arises from substring/pattern matching without intent/negation interpretation, not from a multilingual model benchmark.

### statsmodels extracted functions

Revision: `8278e2d218cc85bac2c7af02feb9a19a0e499b04`. Parsed `statsmodels/stats/meta_analysis.py`; compiled exact `combine_effects` and `_fit_tau_iterative`; used numpy with small array/string validators, standard-library NormalDist critical value and result container supplied by the harness because scipy was unavailable. No source formula was edited. Inputs: effects = [0, 0, 0]; variances = [0.1, 0.1, 0.1]. Harness substitutions mean this is a focused algorithm probe, not a full package test or proof of every output field.

| Method | tau2 | Pooled random-effects mean finite? | HKSJ random-effects scale | default use_t |
|---|---:|---|---|---|
| dl | -0.1 | false | nonfinite | false |
| pm | 0.0 | true | 0.0 | false |

`reml` was rejected by the exact supported-method branch. DL emitted divide-by-zero/invalid division warnings. The source itself explains why: `tau2=(q-df)/c` without a nonnegative bound and weights `1/(variance+tau2)`. The PM zero scale also requires a declared interval policy; it is not automatically an upstream bug under every inferential convention. Statistical acceptance must be compared against reference behavior for the chosen estimand/defaults.

### Planning arithmetic and source integrity

40,000,000 hypothetical reports x 768 dimensions x 4 bytes = 122,880,000,000 bytes (~114.44 GiB); float16 = 61,440,000,000 bytes (~57.22 GiB). This excludes index, metadata, source bytes and build workspace, and does not require all vectors in RAM. A JSON array of random ciphertext bytes can approach four bytes per encoded byte; whole-file reseal can therefore allocate several database-sized buffers. For independent zero-failure Bernoulli observations, `(1 - 0.01)^299 < 0.05`; clustered/study/patient/subgroup qualification needs its own design.

- Source SHA-256 `824f7fcf01137507f13d9694b2c49f652fd7700c0cca296ec0c691cce4789736`: `TheHalfMoon/commandMed:src/commandmed/spec006/scaffold.py` at `51f73ec05750137e5bd94ffa0765f6383f475fee`.
- Source SHA-256 `8e39192faf3e646c96d64c38426181d067709be5458abcb9b8bbcb3230c46a60`: `TheHalfMoon/commandMed:data/spec006/safety_policy.json` at `51f73ec05750137e5bd94ffa0765f6383f475fee`.
- Source SHA-256 `d1ca84dd296d56221fcce9954bb2ab1556266c4857341ecd292af427213f2250`: `statsmodels/statsmodels:statsmodels/stats/meta_analysis.py` at `8278e2d218cc85bac2c7af02feb9a19a0e499b04`.
- Source SHA-256 `60c5a766759ee1154579b54546ee951d1dccaee4829e5669d4ac18b188e0151c`: `TheHalfMoon/MedScale:crates/medscale-storage/src/encrypted_vault.rs` at `98c26aa3a0f919f4dfbb0c2adc27265a767631e4`.

## Appendix D: paper failure campaigns and method coverage

These are deliberately constructed architecture counterexamples and required acceptance cases, not product tests reported as executed. A frozen contract that merely says "must not double-count" does not determine the correct handling below. Gap 03 is the missing identity/independence contract; gap 14 is the statistical method admission gate.

| Report or evidence scenario | Required identity/interpretation | Failure if only report or Study ID is used |
|---|---|---|
| Protocol plus registry record | Study + planned outcome/timepoint/analysis population; registry version | Planned outcomes are counted as observed effects or selective reporting is invisible |
| Conference abstract then preprint then primary paper | Proposed/confirmed report links; source versions and status retained | Three documents become three independent trials; early estimate overrides corrected full publication |
| Primary paper plus long follow-up | Same underlying participants; distinct timepoint/result and retention denominator | Repeated participants are added as new independent evidence |
| Subgroup paper and secondary analysis | Parent study/population overlap; interaction versus within-subgroup contrast | Subgroup significance becomes whole-population effect; subgroup and parent are pooled twice |
| Corrected paper | Immutable old report plus explicit correction/version link and changed Result | Old table spans remain authoritative; current answer misses changed effect |
| Expression of concern | Explicit concern/unknown status with reason and effective date | Not retracted is equated with clean validity |
| Retraction | Separate publication state and dependency invalidation; historical visibility | Source is silently removed from search so the old answer cannot be explained |
| IPD meta-analysis plus component trials | Synthesis-to-included-study/participant contribution relation | Patient data appear twice when pooled summary and component results are combined |
| Pooled analysis of related cohorts | Partial overlap group and population/comparison identity | Distinct report IDs imply independence despite shared participants |
| Systematic review plus constituent primary reports | Review source and included-study membership are distinct | Review-level estimate and underlying trials become independent corroboration |
| Two overlapping systematic reviews | Membership/coverage intersection and protocol/time horizon | Two reviews of the same trials masquerade as independent evidence sets |
| Multi-arm trial | Shared comparator and covariance or prespecified arm combination | Comparator participants counted twice; CI falsely narrows |
| Cluster randomized trial | Cluster design, unit of analysis and ICC/effective sample policy | Individual count enters ordinary inverse-variance analysis without design adjustment |
| Crossover trial | Within-person pairing/correlation, period/carryover assumptions | Same person treated as two independent arms |
| Multiple outcomes/timepoints | Prespecified target estimand and multiplicity/selection policy | Most favorable endpoint/timepoint is selected post hoc |
| Adjusted versus unadjusted observational estimates | Analysis model/covariates/estimand identity | Different causal interpretations are merged under one effect measure |

Claim adversaries must preserve separate mismatch reasons: genuine citation/wrong claim; correct paper/wrong population, subgroup, timepoint or endpoint; adjusted/unadjusted and absolute/relative measures; direction/comparator reversal; dose/unit/decimal; negation; table row/column; unavailable source; abstract/full-text disagreement; retracted/corrected source and conflicting passages. A classifier's SUPPORTS label cannot erase any deterministic result/availability/validity mismatch.

| Requested synthesis capability | Precisely observed statsmodels.meta_analysis support | Reuse/safety disposition |
|---|---|---|
| Fixed effects | Inverse-variance fixed result in combine_effects | Reuse for declared independent input effects with validated positive variances |
| Random effects | PM/iterated and DL/chi2; no REML branch | Restricted methods; reject invalid output/nonconvergence; stronger metafor oracle |
| REML | Not in this module | Use existing metafor implementation; do not rewrite REML formulas |
| HKSJ | WLS residual scale and scaled FE/RE variance/interval paths; default use_t=False | Explicit t/normal and modified/unmodified interval policy; zero scale edge must be declared |
| Continuous/SMD | effectsize_smd accepts means/SD/sample sizes and bias-corrected standardized effect/variance | Reuse with matched outcome/population/SD interpretation; raw mean difference can be admitted through qualified standard tooling |
| Binary effects | effectsize_2proportions for RD, log-RR, log-OR, arcsine | Preserve log versus original scale and direction; correct source denominator |
| Zero events | None, numeric continuity, treatment-arm correction (`tac`), or proportion clipping; source calls zero options experimental/incomplete | Prespecify estimator; no automatic dropping/double-zero pooling or arbitrary correction; reference GLMM/rare-event alternatives |
| HR / adjusted estimate | Can combine a supplied effect and variance, not extract/reconstruct clinical estimand | Qualified extraction/log transform and compatible design required |
| Multi-arm / repeated / cluster / crossover | combine_effects takes variance vector, not full sampling covariance or trial-design model | Supply a qualified independence transformation or use metafor rma.mv/full model; abstain if needed covariance unknown |
| Heterogeneity | Q and derived heterogeneity quantities in result | Do not equate non-significance with homogeneity; predeclare estimator/CI/diagnostic interpretation |
| Subgroups/multiple timepoints/multiplicity | No protocol selecting independent contributions built into this module | SafeEvidence protocol selects inputs; mature meta-regression/multilevel engine handles admitted analysis |
| Sensitivity | Repeated qualified runs can form sensitivity analysis; no clinical protocol provided | Freeze alternative eligibility/transformation/method plans and report all prespecified variants |
| Publication bias/funnel/Egger | No complete bias-diagnostic workflow in this module | Reuse metafor diagnostics conditionally with sample-size/design caveats; absence of signal != absence of bias |

The comparison is limited to the named module, not an assertion that the entire statsmodels library lacks all related statistics. metafor's method scope is broader, but does not solve missing covariance, invalid extracted data or review bias automatically. Appropriate source license/runtime/distribution qualification remains necessary.

## Closure disposition and counts

Verdict: **P00_NOT_READY**.

| Severity | Count | Binding |
|---|---:|---|
| P0 | 6 | Resolve foundational contract/storage/rights decisions before P01 begins |
| P1 | 24 | Resolve or precisely phase-bind before the affected implementation starts |
| P2 | 5 | Refine in the owning phase; does not independently invalidate foundation |
| P3 | 1 | Ledger/path cleanup at reconciliation/admission |

Greenfield subsystems still justified: **8**, scoped in GF01-GF08. Planned capabilities with stronger ready implementation starting points: **5**, scoped above. Counts are findings/integration units, not claims of exploitable running-product vulnerabilities.

Next authorized product-governance step is later reconciliation after independent reviews exist. This review makes no repairs, changes no authority documents, starts no implementation phase, posts no issue comment, opens no PR and merges nothing. Its normal isolated review commit adds only this artifact. Implementation is not approved by the act of committing the review.
