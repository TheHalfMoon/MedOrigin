# SafeEvidence P00 — Independent Opus Kill Review — 2026-10-07

Status: `INDEPENDENT_REVIEW_B` (Claude/Opus). Not reconciled. Not implementation authority.

## 0. Review identity and method

| Item | Value |
|---|---|
| Repository | `TheHalfMoon/MedOrigin` (product: SafeEvidence) |
| Requested review base | `136cdffc2cd14133e01018ca56833241dd50bc4e` |
| Live `main` at review start | `136cdffc2cd14133e01018ca56833241dd50bc4e` (verified with `git ls-remote`; match) |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`) |
| Independence | No Codex review existed in the repository or Issue #1 at review time; none was read. |
| Authority read in full | `AGENTS.md`, `README.md`, `THIRD_PARTY_NOTICES.md`, all 12 files under `docs/`, Issue #1 body and all 4 comments. |

### 0.1 Donor heads verified live (2026-10-07)

| Source | Pin recorded in SafeEvidence docs | Live HEAD | Match |
|---|---|---|---|
| TheHalfMoon/MedScale | `1e2b7d94…` | `1e2b7d94e970256b38bda15fa91f62bc397e825a` | yes |
| TheHalfMoon/DAL | `8fcf29f2…` | `8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03` | yes |
| TheHalfMoon/commandMed | `51f73ec0…` | `51f73ec05750137e5bd94ffa0765f6383f475fee` | yes |
| TheHalfMoon/MESC | `f9b75791…` | `f9b7579189b77b06379d1a71d104d4b0267cf500` | yes |
| TheHalfMoon/Morize | `62fc04d0…` | `62fc04d01d398da93b4dacf0ab2f33e3f1440462` | yes |
| TheHalfMoon/ottari | `b7948b5…` (COPY_FIRST) / `fb6ba054…` (REUSE map) | `b7948b541edcd31863991023e18231b8d8d69b82` | docs disagree |
| TheHalfMoon/kernux | `a0c4aaee…` (COPY_FIRST) / `4b5450d4…` (REUSE map) | `2085b6ed1121b1a94c66c076bdd6b578da4dad0d` | no (moved; docs also disagree) |
| TheHalfMoon/Signthos | `f945f12…` | `f945f12fd1a2b600c2c61493162e3654b4d5b50c` | yes |
| AbdulazizShehri/SafeOCR | "empty repository" | `4658ed1ba16d4e6f080f8e2fed164788be6b7a72` (committed 02:43 +0300, before the review base at 03:28 +0300) | **docs stale** |
| maziyarpanahi/openmed | `252806aa…` | `252806aa946c200f3857cc0f6fda37fd83a5cc85` | yes |
| xberg-io/xberg | `42c03edd…` | `42c03edd06964accd6f8b796fba1647da2b8121d` | yes |
| docling-project/docling.rs | `8aea8d54…` | `8aea8d543de832116ebb29436d9281bfe7e82d73` | yes |
| Anush008/fastembed-rs | `29059745…` | `29059745b8c5df6a1adc263b6903609e164ad3c5` | yes |
| ncbi/MedCPT | `11e129be…` | `11e129be74102c98d16a11c310b0b5ce74c1db5e` | yes |
| asreview/asreview | `79d56821…` | `79d568212b2b0a78f9fd7be3c5117dfb890489f9` | yes |
| asreview/synergy-dataset | `dc2dadfd…` | `dc2dadfdbb98eb1b4259604789abd640aa3b693e` | yes |
| mozilla/uniffi-rs | `bc9fb385…` | `bc9fb38556d9efad4cb74a8a61b5c8a7e741fcea` | yes |
| awslabs/tough | `98d8eb8b…` | `98d8eb8b2ce63515d9b4981c938ef6453c5b5771` | yes |
| theupdateframework/rust-tuf | not pinned | `219ca7d05818d5dd44ec4e32ab47c5ce64a7bf44` | n/a |
| cqframework/clinical_quality_language | `c41c21f5…` | `c41c21f5616a0da82d49e32a9cc3a5b3ca299bc2` | yes |
| HL7/ebm | `374b48bb…` | `374b48bb956e26a51dfdece365d98786ccc90e62` | yes |
| allenai/scifact | `68b98a56…` | `68b98a56d93e0f9da0d2aab4e6c3294699a0f72e` | yes |
| dwadden/multivers | `a6ce033f…` | `a6ce033f0e17ae38c1f102eae1ee4ca213fbbe2e` | yes |
| evidence-surveillance/es3 | `fa845217…` | `fa845217690e179d3f8151e97773aabc035d6cfe` | yes |
| ijmarshall/trialstreamer | `a97cb833…` | `a97cb8332c039e228ef42188c9d966440894e354` | yes |
| ijmarshall/robotreviewer | `9a278197…` | `9a2781974c3edc6322b4fb329b1ea0348af7b8a1` | yes |
| bwallace/RRnlp | `e1a26b4e…` | `e1a26b4ed1c8d65f2c2e2558dc9f0918572306d0` | yes |
| jayded/evidence-inference | `a661e8c1…` | `a661e8c14f973398380c8865cf2f27a535aaaf6d` | yes |
| WengLab-InformaticsResearch/PICOX | `f3351c47…` | `f3351c4786bf197efacfcefc1c1e66c36c245842` | yes |
| statsmodels/statsmodels | `8278e2d2…` | `8278e2d218cc85bac2c7af02feb9a19a0e499b04` | yes |
| beir-cellar/beir | `ef83d293…` | `ef83d29307061c65d04b035b4f4e7c18bd8374af` | yes |
| quickwit-oss/tantivy | `1783018f…` | `1783018f9e6c0ffa4a884df3812011d8d13e4b52` | yes |

### 0.2 Source code actually inspected

Shallow clones at the heads above, read directly:

- **MedScale**: `Cargo.toml`, `deny.toml`; `crates/medscale-storage/src/{encrypted_vault,sealed_blob,writer_lock,vault,claim,migrate,lib}.rs`, `sqlite_meta.rs` (open/migrate path), `tests/` listing incl. `encrypted_vault_005.rs`, `migration_recovery_048.rs`; `crates/medscale-keys/src/{aead_wrap,provider,recovery,pack_trust}.rs`; `crates/medscale-network/src/{lib,allowlist,transport}.rs`, `browse.rs` (signatures); `crates/medscale-contracts/src/{evidence/mod.rs,objects/source.rs,network/mod.rs,mobile/mod.rs,os_sandbox/mod.rs}`; `crates/medscale-core/src/authority/{retrieval,knowledge}.rs` (scorers); `crates/medscale-pack/src/{format,store}.rs`; `crates/medscale-fhir/src/{extractors/mod.rs,lexical.rs,units/mod.rs}`.
- **commandMed**: `src/commandmed/spec006/scaffold.py` (decision path), `data/eval/safety_policy.json`, `data/spec006/safety_policy.json` (all 5 rules), test and fixture listings.
- **DAL**: `src/gaxbench/metrics.py` (full), `selective.py` and `p08_stats.py` (signatures), `pyproject.toml`, `README.md` frozen results.
- **ottari**: `crates/himsat-core/Cargo.toml`, `src/vault.rs`, `vault_android_keystore.rs` (header), `vault_backup_creation.rs` and `vault_sqlcipher.rs` (pragmas/WAL), module and test listings.
- **SafeOCR**: `STATE.md`, `pyproject.toml`, `src/safeocr/verification.py` (parsing/normalization/signals), `ocr.py` (signatures), file/test listings.
- **Signthos**: `LICENSES/`, `NOTICE`; contributor list via API.
- **kernux, Morize, MESC**: crate/module listings and sizes only (no material recommendation depends on their internals).
- **Non-public guideline-verification donor named in `COPY_FIRST_SOURCE_PLAN.md` §11**: repository listing only (see OPUS-P00-015).
- **OpenMed**: full tree at the pin via API; `openmed/core/terminology_licenses.py` (read); presence of all paths claimed in `REUSE_FIRST_IMPLEMENTATION_MAP.md` §6 confirmed.
- **xberg**: workspace `Cargo.toml`, `crates/xberg/Cargo.toml` features, `ATTRIBUTIONS.md`, extractor listing (incl. `extractors/jats/`), `telemetry/`, `paddle_ocr/config.rs` (Arabic tier).
- **docling.rs**: workspace members, `README.md` status/provenance, repo creation date via API.
- **fastembed-rs**: `Cargo.toml` features/dependencies, `src/models/bgem3.rs`, user-defined model API.
- **tough**: workspace listing, version, open issue list.
- **statsmodels**: `statsmodels/stats/meta_analysis.py` at the pin (function inventory and options).
- **ASReview**: `pyproject.toml` dependencies, `simulation/cli.py` stoppers, module listing.
- **ES3, PICOX, RRnlp, evidence-inference, trialstreamer, robotreviewer, MedCPT, SciFact, MultiVerS**: license files, top-level layout, RRnlp weight-loading code.
- **HL7/ebm**: full tree listing at the pin (profile/extension inventory).

### 0.3 Not inspected (claims about these are marked VERIFY)

rust-tuf code; TUF conformance suite; cqframework source; Tantivy, BEIR and SYNERGY code/data; UniFFI source (statements rely on its documented architecture); live NLM, PMC, Europe PMC, Crossref and Retraction Watch terms pages; model-weight cards on Hugging Face.

---

## 1. Executive verdict

**`P00_NOT_READY`.**

Two P0 findings remain:

1. **OPUS-P00-001**: the architecture has no split between the *public evidence corpus* and the *private encrypted vault*, and no scoped corpus/size/build/redistribution model. The P02 vault donor cannot hold a literature corpus. Contracts frozen in P02 would have to be reworked.
2. **OPUS-P00-002**: the copy matrix schedules copying of third-party code that the founder cannot authorize: unlicensed `trialstreamer`, GPL-3.0 `robotreviewer`, plus the AGPL-3.0-only `Signthos` sibling, without a donor-rights register. The first transplant PR could put incompatible terms into an Apache-2.0 codebase.

Both are cheap to fix in documentation. Severity reflects lock-in and consequence, not effort.

Separately, the internal `PREBUILD_KILL_REVIEW_2026-10-07.md` readiness matrix marks calibration, decision assurance, study/report identity, rights, and documents/OCR as `RESOLVED`. Live donor code contradicts several of those statements (OPUS-P00-003, -005, -006, -008, -011). That matrix overstates readiness.

### 1.1 Is the "evidence permits an answer" differentiator technically real?

**It is partly real and still under-specified.**

- **Real:** an explicit terminal-state contract, deterministic precedence where a tool or policy applies, claim-to-span verification, and a current-validity overlay are concrete and testable mechanisms. Retrieve-and-summarize products do not need them.
- **Not yet real:**
  - The nine states have no formal semantics, no precedence lattice, and no mapping to commit/abstain metrics (OPUS-P00-005).
  - The sibling evidence for *learned* commit/abstain signals is negative. In its frozen Study-0 results, DAL reports the paper system at target coverage 0.8 with actual coverage 1.0 and unsafe-commit rate 1.0 (`DAL/README.md`, claim `SG23-C004`). Laya confidence was excluded as uncalibrated (`SG23-C003`).
  - The plan's P08 candidate universe repeats that family of approaches and does not acknowledge the result (OPUS-P00-006).
- **Defensible V1 form:** a deterministic sufficiency gate plus a verified claim-support layer, both measured on a SafeEvidence holdout. Learned decision models stay challengers. No percentage is shown until an estimand is validated.
- Calling abstention "calibrated" before that evidence exists would be branding, not a demonstrated property.

---

## 2. Findings

Every finding below uses the GAP_REVIEW format plus the copy-first fields this review requires.

### P0

---

**GAP_ID:** OPUS-P00-001
**SEVERITY:** P0
**AREA:** architecture / storage / corpus / cost / rights
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `ARCHITECTURE.md` §2 and §14 model one "Local Vault" holding canonical sources, evidence snapshots and answers. `COPY_FIRST_SOURCE_PLAN.md` §4 assigns that vault to a MedScale COHERENT_COPY. `RUNTIME_BUDGET.md` §5 targets a CPU-only 16 GB-class desktop. `PRODUCT_THESIS.md` §8 promises an "Open Evidence Pack" at zero founder COGS.
**LIVE_EVIDENCE:**
- MedScale's `EncryptedVault` decrypts the whole `meta.sealed` file into a work database on every open. It re-seals the whole file on every close (`crates/medscale-storage/src/encrypted_vault.rs` `finish_open`, `seal_meta_file` at L205, `unseal_meta_file` at L227). Cost is O(database size) per open/close.
- The MedScale evidence contract inlines full document text in a `Vec<EvidenceCorpusDocument>` inside one manifest (`medscale-contracts/src/evidence/mod.rs`).
- Its only rights value is `EvidenceCorpusRights::SyntheticOwned`.
- PubMed holds tens of millions of citations.
- No SafeEvidence document defines:
  - which subset of the literature ships by default;
  - its size;
  - who builds the lexical and vector projections, and on what hardware;
  - who hosts and pays for distribution;
  - whether abstract text may be redistributed.
**SOURCE_CODE_INSPECTED:** files above; `RUNTIME_BUDGET.md`; `SOURCE_LEDGER.md` §3; `FOUNDATION_GAP_AUDIT` SE-G001/G002.
**FAILURE_MODE:**
- (a) P02 freezes a vault contract that must hold both the public corpus and private data. Either the corpus is forced into a whole-file-sealed store and becomes unusable at scale, or P03 bolts on a second store later and has to rework P02 contracts and snapshot identity.
- (b) The default evidence pack turns out to be either too large for the stated hardware or legally non-redistributable, because abstracts and full text keep publisher or article-level terms. The founder ends up paying to build and host projections, which breaks the zero-COGS thesis.
- (c) Mobile pack scope, P17 sync scope and P22 distribution cannot be designed without a size model.
**WHY_IT_MATTERS:** this is the single largest architecture decision. It is undecided, and the first implementation phase depends on it.
**AFFECTED_PHASES:** P02, P03, P04, P05, P15, P16, P17, P21, P22.
**READY_SOURCE_TO_COPY:**
- SQLite FTS5 or Tantivy for a plain, integrity-protected public corpus store.
- The ottari `himsat-core` vault for the private store (OPUS-P00-003).
- OpenMed `openmed/eval/data_license_gate.py` and `openmed/core/terminology_licenses.py` for rights gating.
**EXACT_CODE_OR_TESTS_TO_REUSE:** see OPUS-P00-003 for the vault. For the corpus store, use FTS5 `bm25()` or Tantivy directly (DEPEND). No custom engine.
**PROPOSED_RESOLUTION:** add a decision record before P02 that defines two data planes.
- **Public Evidence Plane:**
  - non-secret but integrity- and rights-scoped;
  - content-addressed, pack-versioned, rebuildable;
  - not encrypted with the user DEK;
  - signed manifests;
  - item-level rights fields from SE-G002.
- **Private Vault Plane:**
  - encrypted;
  - holds questions, answers, snapshots-as-identities, patient context, user documents, institution-licensed full text, and query logs/caches.

The record must also fix:
- **Snapshot boundary:** a snapshot stores identities and digests into the public plane plus private bytes.
- **Default corpus scope:** for example, a metadata+abstract subset selected by publication type/MeSH/recency. Freeze a size target with measured numbers before P04.
- **Build model:** state who computes embeddings (user device, founder CI on free runners, or institution). Choose an embedding precision/quantization budget that fits the 16 GB target.
- **Redistribution model:** ship metadata/index derived only from redistributable fields, and let users fetch abstracts and full text locally from NLM/PMC bulk files under their own acceptance of terms. Mark VERIFY on NLM and publisher abstract terms before any pack ships.
**ALTERNATIVES:**
- Online-only literature with a local cache: violates offline usefulness.
- Founder-hosted full packs: violates zero COGS and carries rights risk.
- User-built packs from bulk files: compute-heavy but rights-clean. This is the recommended default, with optional prebuilt metadata-only indexes.
**GREENFIELD_REQUIRED:** no for engines. Yes only for the plane-boundary contract.
**BLOCKS_IMPLEMENTATION:** yes (P02 onward).
**VERIFICATION_REQUIRED:**
- A measured pack-size and build-time table for at least two candidate corpus scopes on the 16 GB CPU baseline.
- A rights memo per field (title, abstract, MeSH, full text, embeddings) with the source terms URL and the date checked.

---

**GAP_ID:** OPUS-P00-002
**SEVERITY:** P0
**AREA:** licensing / provenance
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `COPY_FIRST_SOURCE_PLAN.md` §1 says the founder authorized copying "the source code from the source universe discussed for this project". §16 and `SOURCE_LEDGER.md` (evidence-synthesis table) list `ijmarshall/trialstreamer` as `COPY_BOUNDED`. `robotreviewer` is listed as "COPY/WORKER only with exact permission". `Signthos` is listed as COPY/ADAPT for QR pairing.
**LIVE_EVIDENCE:**
- `trialstreamer` has **no license file**; GitHub reports `NONE`. Default copyright applies, so it is not copyable.
- `robotreviewer` is **GPL-3.0** (`LICENSE.txt`).
- `Signthos` ships `LICENSES/AGPL-3.0-only.txt`. API contributors are `TheHalfMoon` and `AbdulazizShehri`.
- MedScale and commandMed list the same two contributors.
- MedScale admits `LicenseRef-Slint-Royalty-free-2.0` in `deny.toml`. Slint's royalty-free license carries attribution obligations.
- Founder authorization can relicense only code whose copyright the founder holds. It cannot change third-party terms.
**SOURCE_CODE_INSPECTED:** license files listed above; `MedScale/deny.toml`; GitHub API contributor lists.
**FAILURE_MODE:**
- An agent follows `AGENTS.md` ("For those authorized sources, permission to copy is not an implementation blocker") and copies trialstreamer or robotreviewer code into the Apache-2.0 tree.
- Or it copies AGPL Signthos code without a written relicensing grant covering every contributor account.
- The SafeEvidence distribution becomes non-compliant, and possibly non-distributable on app stores that conflict with GPL/AGPL obligations.
**WHY_IT_MATTERS:** this is irreversible once published. The copy-first directive makes it likely.
**AFFECTED_PHASES:** every transplant PR; specifically P06, P07, P17, P18, P11 (Slint).
**READY_SOURCE_TO_COPY:** MedScale `third_party/provenance/` and `deny.toml` patterns; Signthos `NOTICE` generator pattern; OpenMed `docs/security/license-inventory.md` pattern.
**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale `deny.toml` as the starting `cargo-deny` policy (DEPEND on cargo-deny).
**PROPOSED_RESOLUTION:**
1. Split the source universe into **FOUNDER_OWNED** (relicensable by written grant) and **THIRD_PARTY** (license-governed). Founder authorization applies only to the first.
2. Record a written relicensing statement for each founder-owned donor, naming all contributor accounts (`TheHalfMoon`, `AbdulazizShehri`) as the same rights holder or as consenting holders.
3. Reclassify:
   - `trialstreamer` → `REFERENCE` (no code copy);
   - `robotreviewer` → `BENCHMARK_ONLY` or an out-of-process `WORKER` that is never distributed inside the Apache artifact, decided by a written license analysis;
   - Slint → record the attribution duty in `THIRD_PARTY_NOTICES.md` planning.
4. Amend the wording in `AGENTS.md` and `COPY_FIRST_SOURCE_PLAN.md` §1.
**ALTERNATIVES:** ask trialstreamer and robotreviewer authors for a permissive grant; independently implement from the papers (clean-room).
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** yes (any transplant).
**VERIFICATION_REQUIRED:** a donor-rights register file with one row per donor: owner class, license SPDX, grant reference, and allowed modes. `cargo-deny` runs in CI from P01.

---

### P1

---

**GAP_ID:** OPUS-P00-003
**SEVERITY:** P1
**AREA:** vault / durability / donor selection
**CLAIM_OR_ASSUMPTION_CHALLENGED:**
- The plan says to COHERENT_COPY the MedScale SQLCipher vault, sealed blobs, writer ownership and migrations (`COPY_FIRST_SOURCE_PLAN.md` §4; `REUSE_FIRST_IMPLEMENTATION_MAP.md` §4.1).
- `DONOR_TRANSPLANT_PROTOCOL.md` §4 says `writer_lock.rs` supersedes the marker-file approach.
**LIVE_EVIDENCE:**
- **Crash loses the session.** `encrypted_vault.rs` L161: "Crash leftovers are not treated as sealed; wipe then restore from meta.sealed." Every commit since the last clean `close()` is discarded after a crash.
- **Whole-vault loss on interrupted close.** `seal_meta_file` writes `meta.sealed` with a plain `fs::write` (L205): no temp file, rename, or fsync. A crash during close can corrupt the only metadata copy.
- **The writer lock is not used.** `EncryptedVault` uses a marker-file lease (`acquire_lease` L231–239: read, compare, write). It never uses `WriterLock`. A stale lease from another `holder_id` locks the user out permanently, and the check-then-write is racy.
- **Backup is stale.** `backup()` (L325) copies `meta.sealed`, which is stale while the vault is open.
- **Crypto-shredding is incomplete.** `destroy_key_material` (L315) deletes the header, but the DEK copy stored by `store_wrapped_dek` in the OS keystore survives.
- **The keystore wrap is cosmetic.** `provider.rs` L219 stores the wrap key in the same payload as the wrapped DEK.
- **Blob filenames leak plaintext digests.** Sealed blob filenames are the plaintext SHA-256 (`sealed_blob.rs` L44). Anyone with disk access can test whether a known document is present.
- **Migrations are entangled.** They are interleaved with unrelated MedScale schemas: v3 `project_graph`, v4 `data_sources`, v5 `collaboration` (`sqlite_meta.rs` `migrate`).
- **Desktop-only key custody.** The `keyring` crate configuration has no Android backend.
- **ottari is a stronger donor.** ottari `crates/himsat-core` (32,319 lines of `vault*.rs`, 297 unit tests) has:
  - WAL-mode SQLCipher;
  - quiesced snapshot backups with verification (`vault_backup_creation.rs`);
  - key rotation, nonce management, a freshness manifest, deletion and recovery modules;
  - platform protectors: Android Keystore, Apple Keychain, Windows DPAPI, Linux Secret Service;
  - integration tests `b005d_journal_kill.rs`, `b205_crypto_adversarial.rs`, `b306_plaintext_spill.rs`, `b405_protector_fail_closed.rs`.
**SOURCE_CODE_INSPECTED:** files cited above.
**FAILURE_MODE:** a transplant faithful to the plan ships a vault that silently drops a clinician's session (screening decisions, saved answers) after a crash or OS kill. That is common on mobile. It can also lose the entire vault on power loss during close.
**WHY_IT_MATTERS:** it violates the P02 closure gate ("survives restart/recovery"). Mobile key custody would need a second implementation later.
**AFFECTED_PHASES:** P02, P15, P21.
**READY_SOURCE_TO_COPY:** ottari `crates/himsat-core/src/vault*.rs` plus `tests/b*`. MedScale `writer_lock.rs`, `claim.rs`, `aead_wrap.rs`, `recovery.rs`.
**EXACT_CODE_OR_TESTS_TO_REUSE:**
- From ottari: `vault_sqlcipher.rs`, `vault_keys.rs`, `vault_protector.rs`, `vault_android_keystore.rs`, `vault_apple_keychain.rs`, `vault_windows_dpapi.rs`, `vault_linux_secret_service.rs`, `vault_backup_*.rs`, `vault_deletion.rs`, `vault_freshness.rs`, `vault_rotation.rs`, `vault_migration.rs`, and `tests/b005d_journal_kill.rs`, `b204_recovery_negative.rs`, `b205_crypto_adversarial.rs`, `b306_plaintext_spill.rs`, `b307_copy_verify_publish.rs`, `b405_protector_fail_closed.rs`.
- From MedScale: `writer_lock.rs` and `claim.rs`.
- Leave behind the ottari `capture_*` modules and the audio dependencies (`cpal`, `cidre`).
**PROPOSED_RESOLUTION:**
- Replace "MedScale vault COHERENT_COPY" with a P02 vault bake-off (ottari himsat-core vault slice vs MedScale), using these acceptance tests: kill-during-write, kill-during-close, power-loss simulation, plaintext-spill scan, second-writer refusal, keystore wipe, and backup-while-open.
- Default hypothesis: ottari vault slice, plus MedScale `writer_lock`/`claim` semantics.
- Never transplant the MedScale whole-file seal/unseal cycle.
- Use HMAC-keyed blob names instead of plaintext digests.
**ALTERNATIVES:** fix MedScale in place (atomic write, WAL without the outer seal, real writer lock). Feasible, but it duplicates work ottari has already done.
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** yes for P02.
**VERIFICATION_REQUIRED:** a bake-off report with the tests above run on Windows, macOS and Linux at an exact head.

---

**GAP_ID:** OPUS-P00-004
**SEVERITY:** P1
**AREA:** pack trust / update security
**CLAIM_OR_ASSUMPTION_CHALLENGED:** "pack admission/signing — MedScale — COHERENT_COPY" (`COPY_FIRST_SOURCE_PLAN.md` §4); TUF semantics (SE-G007).
**LIVE_EVIDENCE:**
- MedScale pack signing derives its only key from a hard-coded seed: `medscale-keys/src/pack_trust.rs` L13 `SYNTHETIC_SIGNING_SEED`, L48 `SigningKey::from_bytes(&SYNTHETIC_SIGNING_SEED)`.
- There is a single trust root, no expiry, no threshold, and no role separation. Anti-rollback compares `pack_epoch`/version only (`medscale-pack/src/store.rs` `is_rollback`).
- `awslabs/tough` open issues include #603 "Datastore: System clocks do step back", #766 "Be less strict in keyid validity check?" and #815 "Required expiry flag and versioning".
- TUF expiry semantics conflict with offline sideloaded packs: an air-gapped user with an expired timestamp role cannot install a USB pack.
- No document says who holds the root and targets keys, or where the repository is hosted at zero cost.
**SOURCE_CODE_INSPECTED:** `pack_trust.rs`, `format.rs`, `store.rs`; tough issue list.
**FAILURE_MODE:** a "coherent copy" ships a signing private key in the public binary, so anyone can mint "admitted" packs. Alternatively, a TUF adoption bricks offline installs on expiry.
**WHY_IT_MATTERS:** pack trust protects model and evidence integrity, which is clinical-content integrity.
**AFFECTED_PHASES:** P03, P10, P17, P22.
**READY_SOURCE_TO_COPY:** MedScale `medscale-pack` admission/store logic (minus the key); `tough` or `rust-tuf` (QUALIFY); the TUF conformance suite (VERIFY availability).
**EXACT_CODE_OR_TESTS_TO_REUSE:** `medscale-pack/src/{format,store}.rs` and their anti-rollback tests, with `pack_trust.rs` replaced.
**PROPOSED_RESOLUTION:**
- Forbid copying `SYNTHETIC_SIGNING_SEED` outside test fixtures.
- Define the TUF role model and the offline policy: a distinct "offline bundle" mode with a long-lived snapshot plus an explicit user-visible staleness state, instead of silent acceptance.
- Define key custody (founder offline root, threshold ≥ 2 for root) and a zero-cost repository host such as static release assets.
**ALTERNATIVES:** Sigstore-only signing (no freeze protection); a custom protocol (rejected).
**GREENFIELD_REQUIRED:** no (policy only).
**BLOCKS_IMPLEMENTATION:** yes for P10/P22 pack distribution; no for P02.
**VERIFICATION_REQUIRED:** a conformance run of the selected client; tests for expired-offline-bundle behavior; key ceremony record.

---

**GAP_ID:** OPUS-P00-005
**SEVERITY:** P1
**AREA:** decision assurance / state machine
**CLAIM_OR_ASSUMPTION_CHALLENGED:**
- The terminal states ANSWER, ANSWER_WITH_CAUTION, ASK_MORE, RETRIEVE_EVIDENCE, USE_TOOL, CONFLICT, ABSTAIN, ESCALATE, EMERGENCY.
- `COPY_FIRST_SOURCE_PLAN.md` §5: "ASK_MORE/ABSTAIN/ESCALATE/EMERGENCY behavior — commandMed — COPY tests".
**LIVE_EVIDENCE:**
- **Vocabulary mismatch.** commandMed defines 7 states, with no ANSWER_WITH_CAUTION and no CONFLICT (`data/eval/safety_policy.json` `behavior_states`; `scaffold.py` constants).
- **Patient-voice lexical rules.** `data/spec006/safety_policy.json` rule `R006-EMERG-LEX-V1` is a substring match on `chest pain|can't breathe|severe bleeding|unconscious|…` plus Arabic equivalents. It has precedence 2, is non-overridable, and has no negation handling (`scaffold.py` `_rule_matches`, `kind == "lexical"` → `any(token in text …)`). A clinician asking "What is the evidence for high-sensitivity troponin in chest pain?" or "patient denies chest pain" deterministically gets EMERGENCY.
- **Patient-dose pattern.** `R006-DOSAGE-INTENT-INCOMPLETE-V1` targets patient phrasing ("how much … take").
- **Role scope.** The commandMed policy is scoped to `PATIENT_CAREGIVER_SAFETY`.
- **Thesis contradiction.** `PRODUCT_THESIS.md` §12 lists "autonomous emergency triage" as a non-goal, yet EMERGENCY is a terminal state, and nothing defines what it means for a clinician user.
- **Control actions mixed with outcomes.** RETRIEVE_EVIDENCE and USE_TOOL are orchestration actions, not user-facing outcomes. The plan never says what the UI shows if they are terminal.
- **Inconsistent vocabularies.** `AGENTS.md` lists `BLOCKED` as a legitimate outcome, but it is not in the state list. `ARCHITECTURE.md` adds `SOURCE_UNAVAILABLE` to support states, but `MASTER_PLAN.md` P06 and SE-G003 omit it.
**SOURCE_CODE_INSPECTED:** commandMed `scaffold.py`, both policy JSON files; SafeEvidence thesis/architecture/plan.
**FAILURE_MODE:**
- Copied rule content produces systematic over-escalation for clinicians. Usability collapses, or users learn to ignore EMERGENCY.
- An undefined state lattice makes gold labels for P08/P20 impossible to write consistently.
- Metrics cannot decide whether ANSWER_WITH_CAUTION or CONFLICT counts as a commit.
**WHY_IT_MATTERS:** this state machine is the claimed differentiator.
**AFFECTED_PHASES:** P02 (AnswerArtifact contract), P08, P09, P11, P20.
**READY_SOURCE_TO_COPY:** commandMed `src/commandmed/spec006/{policy,registry,scaffold,trace}.py` and `specs/006-patient-safety-scaffold/fixtures/`. These cover the mechanics: precedence, fail-closed handling, provenance and hash-chained trace.
**EXACT_CODE_OR_TESTS_TO_REUSE:** mechanics and fixture format as an oracle. **Not** the rule content of `data/spec006/safety_policy.json`.
**PROPOSED_RESOLUTION:** write a state-semantics decision record before P02 freezes `AnswerArtifact`. It should:
- Split `ControlAction {RETRIEVE_EVIDENCE, USE_TOOL, ASK_MORE_INTERNAL}` from `TerminalOutcome {ANSWER, ANSWER_WITH_CAUTION, ASK_MORE, CONFLICT, ABSTAIN, ESCALATE, EMERGENCY_NOTICE, BLOCKED}`.
- Define EMERGENCY for clinician users as a non-triage notice ("time-critical scenario; evidence answer does not replace emergency protocol"), consistent with the non-goal.
- Define a total precedence order.
- Define the commit/abstain mapping and a harm-weighted cost matrix (see OPUS-P00-007).
- Rewrite the policy content for the clinician role, with negation- and context-aware triggers measured on a clinician question set.
**ALTERNATIVES:** keep 9 flat states (rejected: ambiguous); drop EMERGENCY (possible but must be explicit).
**GREENFIELD_REQUIRED:** yes for policy content only; mechanics are copied.
**BLOCKS_IMPLEMENTATION:** yes for P02 contract freeze and P08.
**VERIFICATION_REQUIRED:** a false-escalation rate on a clinician-phrased question set (English and Arabic, including negations); state-label inter-rater agreement.

---

**GAP_ID:** OPUS-P00-006
**SEVERITY:** P1
**AREA:** decision models / evidence for the differentiator
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the P08 candidate universe (Decision 2.0, Laya, decider, CLM, Jev, BioClinical encoders); "calibrated abstention" as a competitive property (`PRODUCT_THESIS.md` §9).
**LIVE_EVIDENCE:**
- DAL frozen Study-0 results (`DAL/README.md`):
  - `SG23-C004`: paper system unsafe-commit 1.0 at target coverage 0.8;
  - `SG23-C003`: Laya confidence uncalibrated;
  - `SG23-C002`: no superiority;
  - FHIR-AgentBench blocked;
  - the two compared systems emitted identical action-probability vectors on 500/500 rows.
- DAL states that its Study-0 PubMedQA test has been inspected and will not be reused as a final test.
- SafeEvidence docs do not cite these results.
**SOURCE_CODE_INSPECTED:** DAL README frozen block; `metrics.py`.
**FAILURE_MODE:** SafeEvidence spends P08 re-running a tournament whose sibling evidence is negative. It may also reuse contaminated PubMedQA splits and market "calibrated abstention" without support.
**WHY_IT_MATTERS:** negative results are first-class evidence under AGENTS.md. Ignoring them is planning bias.
**AFFECTED_PHASES:** P08, P09, P20, P23.
**READY_SOURCE_TO_COPY:** DAL `registry/p08_sg000022_final_evaluation/`, `registry/p08_sg000023_paper_evidence/` (as prior evidence); DAL `src/gaxbench/{metrics,selective,p08_stats}.py`.
**EXACT_CODE_OR_TESTS_TO_REUSE:**
- `metrics.py`: `evaluate_abstention`, `expected_calibration_error`, `risk_coverage_curve`, `risk_at_coverage`.
- `p08_stats.py`: `paired_bootstrap_mean_difference`, `reliability_bins`.
- `tests/test_metrics.py`, `tests/test_selective.py`.
**PROPOSED_RESOLUTION:**
- Record DAL Study-0 as binding prior evidence.
- V1 decision assurance = deterministic sufficiency rules + verifier outputs. Learned decision models are `BENCHMARK_ONLY` challengers until they beat the deterministic baseline on a fresh SafeEvidence holdout.
- Exclude the DAL Study-0 PubMedQA test from any SafeEvidence final evaluation (contamination).
**ALTERNATIVES:** proceed with the tournament but preregister the deterministic baseline as the incumbent.
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** yes for P08 promotion; no for P01–P07.
**VERIFICATION_REQUIRED:** a preregistered P08 protocol that cites DAL Study-0 and freezes the incumbent.

---

**GAP_ID:** OPUS-P00-007
**SEVERITY:** P1
**AREA:** calibration / statistics / metrics
**CLAIM_OR_ASSUMPTION_CHALLENGED:**
- SE-G004 estimand: "P(material answer claim is adequately supported by the admitted evidence | pipeline, population, protocol)".
- DAL metrics "COPY unchanged".
**LIVE_EVIDENCE:**
- DAL `evaluate_abstention` is binary. It computes `unsafe_commit_rate = FN/(TP+FN)` and `over_abstain_rate = FP/(FP+TN)`, with no severity weights and no multi-state mapping.
- `expected_calibration_error` is equal-width top-label ECE without intervals (intervals live separately in `p08_stats.py`).
- The estimand's population is the set of claims *generated by the pipeline itself*. Changing the generator, retriever, pack or verifier changes the label distribution.
- No recalibration trigger, minimum calibration sample size, or subgroup (specialty, language, question type) sample plan is defined.
- "Adequately supported" is a human judgment with no rubric.
**SOURCE_CODE_INSPECTED:** `DAL/src/gaxbench/metrics.py`.
**FAILURE_MODE:**
- A displayed percentage silently stops meaning anything after a pack or model update.
- Subgroup miscalibration (Arabic, pediatrics) is hidden by pooled ECE.
- ANSWER_WITH_CAUTION outcomes are miscounted.
**WHY_IT_MATTERS:** this is user-facing probability in a clinical context.
**AFFECTED_PHASES:** P09, P11, P20, P23.
**READY_SOURCE_TO_COPY:** DAL metrics plus `p08_stats.py`; scikit-learn calibration (DEPEND, benchmark-side).
**EXACT_CODE_OR_TESTS_TO_REUSE:** as in OPUS-P00-006.
**PROPOSED_RESOLUTION:**
- **V1 shows no user-facing percentage.** Show categorical support states only.
- If a percentage is ever introduced:
  - (a) calibration identity = hash of {generator, retriever, reranker, verifier, pack set, policy};
  - (b) any component change invalidates the display until recalibrated;
  - (c) per-claim estimand with a written adjudication rubric;
  - (d) minimum per-subgroup counts frozen in advance;
  - (e) reliability reported with bootstrap intervals;
  - (f) temporal holdout: calibrate on questions before date T, test after.
- Extend the DAL metrics with a multi-state cost matrix instead of collapsing to binary.
**ALTERNATIVES:** conformal risk control (MAPIE) as a challenger after its exchangeability assumptions are checked.
**GREENFIELD_REQUIRED:** yes, small: a cost-matrix extension around copied metrics.
**BLOCKS_IMPLEMENTATION:** yes for any percentage UI; no otherwise.
**VERIFICATION_REQUIRED:** a frozen calibration protocol document; invalidation test (component change → display suppressed).

---

**GAP_ID:** OPUS-P00-008
**SEVERITY:** P1
**AREA:** study-level evidence model
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the `Study / StudyReportLink / OutcomeDefinition / EffectEstimate` contracts in `PREBUILD_KILL_REVIEW` PB-G001. The EBMonFHIR "crosswalk later" decision in SE-G011.
**LIVE_EVIDENCE:**
- **No arm entity.** `Study.arms` is a bare list. `EffectEstimate.comparison` does not reference arm identities.
- **No arm-level data.** There are no events/total or mean/SD/N per arm, only `estimate/interval/variance_or_se`.
- **Analysis population in the wrong place.** `analysis_population` sits on `OutcomeDefinition`; it belongs to the analysis/result (ITT vs per-protocol are two analyses of one outcome).
- **No systematic-review linkage.** No Systematic-Review→included-Study link exists.
- **No pooled-report scope.** No representation exists for a report (pooled or IPD analysis) whose estimate spans several studies.
- **No registered-vs-reported pairing.** `OutcomeDefinition` has no pairing needed to detect selective outcome reporting (PB-G006 names the descriptor but no contract carries it).
- **No report versioning.** No version lineage links preprint → published → corrected.
- **EBMonFHIR already models these.** HL7/ebm at the pin contains profiles and extensions:
  - `p-comparator-group.fsh`, `p-exposure-group.fsh`, `p-group-assignment.fsh`;
  - `p-comparative-participant-flow-evidence.fsh`, `p-intervention-only-evidence.fsh`, `p-comparator-only-evidence.fsh`;
  - `p-metaanalysis-study-group.fsh`, `p-metaanalysis-outcome-definition.fsh`;
  - `ext-research-study-included-study.fsh`, `ext-research-study-excluded-study.fsh`, `ext-research-study-search-strategy.fsh`;
  - `ext-research-study-number-of-studies-identified.fsh`, `ext-research-study-number-of-studies-included.fsh`;
  - `p-baseline-measure-evidence.fsh`, `p-certainty-of-evidence.fsh`, `p-outcome-importance.fsh`.
**SOURCE_CODE_INSPECTED:** HL7/ebm tree at `374b48bb`; PB-G001–G012.
**FAILURE_MODE:**
- (1) Fast-answer double counting: a meta-analysis and its own constituent RCTs are retrieved and presented as consistent independent evidence. This is the most common real double count, and nothing links an SR to its included studies.
- (2) Multi-arm trials: the shared control is counted twice in pairwise estimates, because arms are not identities.
- (3) Zero events and rare events cannot be re-derived without arm counts.
- (4) A pooled analysis of trials A+B is treated as a third study.
- (5) A preprint and its published version are linked as two reports of a study but are not version-aware, so the outdated preprint result can be cited.
**WHY_IT_MATTERS:** P02 freezes these contracts. Adding arms and arm data later is a schema migration across stored evidence.
**AFFECTED_PHASES:** P02, P03, P06, P07, P18, P20.
**READY_SOURCE_TO_COPY:**
- EBMonFHIR profiles above (concept model; COPY concepts and value sets, not storage).
- ES3/Trial2rev for SR↔trial links (data and `ecitmatch_tools.py`).
- ClinicalTrials.gov API v2 results sections and the CTTI AACT database for structured arm-level registry results (data sources; VERIFY terms).
**EXACT_CODE_OR_TESTS_TO_REUSE:** EBMonFHIR examples under `input/` as golden fixtures for the internal model and its export.
**PROPOSED_RESOLUTION:** before the P02 contract freeze, add the following.
- `Arm` (`arm_id`, role, intervention, n randomized/analyzed).
- `ArmOutcomeData` (events/total or mean/SD/N per arm, timepoint, analysis_id, `source_span_refs`).
- `Analysis` (population ITT/mITT/PP, adjustment set, model).
- `EffectEstimate.scope` ∈ {SINGLE_STUDY, POOLED_STUDY_SET(study_ids), REVIEW_SYNTHESIS(review_id)}.
- `ReviewInclusionLink` (review report → study, with source).
- `ReportVersionLink` (preprint/published/corrected/retracted).
- `RegisteredOutcome` paired to `ReportedOutcome`.
- A rule that fast-answer evidence profiles deduplicate across ReviewInclusionLink.

Derive field names from EBMonFHIR so export becomes mechanical.
**ALTERNATIVES:** store EBMonFHIR JSON natively (rejected: FHIR must remain interchange).
**GREENFIELD_REQUIRED:** no (concepts copied); a thin internal schema is SafeEvidence-specific.
**BLOCKS_IMPLEMENTATION:** yes for P02 evidence contracts.
**VERIFICATION_REQUIRED:** adversarial fixtures:
- SR + constituent RCT double count;
- three-arm shared control;
- pooled-analysis report;
- preprint→published with changed result;
- registry primary outcome ≠ published primary outcome;
- ITT vs PP of the same outcome.

---

**GAP_ID:** OPUS-P00-009
**SEVERITY:** P1
**AREA:** quantitative synthesis / statistical safety
**CLAIM_OR_ASSUMPTION_CHALLENGED:** PB-G005 says "statsmodels.stats.meta_analysis for basic fixed/random effects, effect-size utilities, heterogeneity, and HKSJ" and "multi-arm correlation handled explicitly"; "SafeEvidence does not reimplement meta-analysis formulas".
**LIVE_EVIDENCE:** `statsmodels/stats/meta_analysis.py` at `8278e2d2` provides:
- `combine_effects` with `method_re ∈ {"iterated","pm","chi2","dl"}` (no REML);
- HKSJ variance;
- a homogeneity Q test;
- `effectsize_smd`;
- `effectsize_2proportions` with `zero_correction ∈ {None, float, "tac", "clip"}`.

It has no:
- multivariate/multilevel model, so multi-arm correlation cannot be handled;
- Mantel-Haenszel or Peto pooling in this module;
- prediction interval;
- tau² confidence interval;
- small-study or Egger test;
- trim-and-fill;
- rare-event GLMM.

statsmodels is a Python/NumPy/SciPy stack, which does not run on mobile and adds a large desktop worker. Cochrane unit-of-analysis rules (cluster ICC design effect, crossover handling, multi-arm combine/split) are decision rules, not library functions.
**SOURCE_CODE_INSPECTED:** `meta_analysis.py` function and option inventory.
**FAILURE_MODE:**
- The plan believes multi-arm, rare-event and publication-bias cases are covered by a dependency that does not implement them. Agents then improvise formulas without oracles.
- Or pooling runs with a continuity correction that biases rare-event results without disclosure.
**WHY_IT_MATTERS:** statistical errors in pooled estimates are high-consequence and look authoritative.
**AFFECTED_PHASES:** P18, P20, P22 (packaging).
**READY_SOURCE_TO_COPY:**
- statsmodels (DEPEND in a desktop Python worker, or ORACLE for a port).
- R `metafor` as `BENCHMARK_ONLY` oracle, never shipped (license believed GPL; VERIFY).
- PyMARE (permissive license believed; VERIFY) as a candidate for REML and multiple tau² estimators.
**EXACT_CODE_OR_TESTS_TO_REUSE:** statsmodels `statsmodels/stats/tests/test_meta.py` (VERIFY path) and metafor published examples as golden fixtures.
**PROPOSED_RESOLUTION:**
- Restrict V1 quantitative synthesis to desktop Deep Review.
- Methods supported: pairwise inverse-variance FE, RE with DL/PM + HKSJ, I² and prediction interval derived from copied outputs.
- Any multi-arm, cluster, crossover, rare-event (any arm 0 events in ≥1 study), or <3-study case → refuse pooling and fall back to narrative synthesis with an explicit `POOLING_NOT_SUPPORTED_FOR_REASON`.
- Implement unit-of-analysis *decision rules* (`GREENFIELD_JUSTIFIED`: no library implements them) from the Cochrane Handbook with fixtures.
- Decide by measurement whether to ship a Python worker or port the few formulas to Rust with statsmodels/metafor as test oracles. A port is justified by a platform boundary (mobile, no Python runtime).
**ALTERNATIVES:** ship R (rejected: runtime budget and GPL).
**GREENFIELD_REQUIRED:** yes, bounded: unit-of-analysis rules and refusal logic.
**BLOCKS_IMPLEMENTATION:** yes for P18 quantitative lane.
**VERIFICATION_REQUIRED:** golden fixtures agreeing with metafor to a stated tolerance; refusal tests for every unsupported design.

---

**GAP_ID:** OPUS-P00-010
**SEVERITY:** P1
**AREA:** evidence acquisition formats / network
**CLAIM_OR_ASSUMPTION_CHALLENGED:**
- P03 "PubMed/NCBI metadata adapter … PMC open-full-text adapter".
- `REUSE_FIRST_IMPLEMENTATION_MAP.md` §4.3 calls the MedScale network broker reusable for evidence acquisition.
- P12 concentrates document effort on PDF/OCR.
**LIVE_EVIDENCE:**
- **No live transport.** MedScale `UreqTransport::send` always returns `TransportError::ExternalGateRequired` (`medscale-network/src/transport.rs`). The broker has no live egress path for evidence. Only `browse.rs` has a public-only GET (no redirects, `PublicOnlyResolver`).
- **Path matching is not normalized.** The allowlist matches `destination_path.starts_with(&entry.path_prefix)` with no normalization (`allowlist.rs` L30).
- **Formats never mentioned.** No SafeEvidence document mentions JATS, MEDLINE/PubMed XML, `DeleteCitation`, `CommentsCorrections` (RetractionIn / ErratumIn / ExpressionOfConcernIn), or PMC `<license>` elements. These are the actual carriers of the lifecycle and rights signals that SE-G001/G002 require.
- **Ready parsers exist.** xberg has `crates/xberg/src/extractors/jats/{parser,metadata,elements}.rs`; docling.rs lists JATS among supported formats.
- **E-utilities identity linkage.** NCBI E-utilities usage normally carries `tool`/`email`/`api_key` parameters, which link query history to an identity.
**SOURCE_CODE_INSPECTED:** MedScale network crate; xberg extractor tree; docling.rs README.
**FAILURE_MODE:**
- P03 builds lifecycle overlays from Crossref/Retraction Watch only and misses PubMed-native retraction and erratum links and deletions.
- P03 writes a new JATS parser.
- The broker's real transport, bulk resumable download, rate limiting and secret handling are all greenfield while marked "copy".
- Users' online queries become linkable to their e-mail or API key.
**WHY_IT_MATTERS:** this is the core evidence lifecycle, and the "reuse broker" claim overstates reality.
**AFFECTED_PHASES:** P03, P12, P21.
**READY_SOURCE_TO_COPY:**
- xberg `extractors/jats/` or docling.rs JATS backend (single choice per OPUS-P00-013).
- MedScale `browse.rs` (`validate_url`, `is_forbidden_ip`, `PublicOnlyResolver`, no-redirect agent).
- ES3 `ecitmatch_tools.py` (citation matching).
**EXACT_CODE_OR_TESTS_TO_REUSE:** `browse.rs` tests `validate_url_accepts_only_https_dns_hosts_on_443`, `forbidden_addresses_cover_private_and_special_ranges`, `redirects_resolve_only_absolute_https_and_paths`.
**PROPOSED_RESOLUTION:**
- Add to P03: a PubMed XML parser and ingest tests covering DeleteCitation, CommentsCorrections, PublicationType "Retracted Publication", and citation versioning; PMC JATS `<license>` → item-level rights mapping; a bulk resumable HTTPS downloader with checksum verification.
- State that the broker transport is greenfield glue on a vetted HTTP client.
- Online discovery mode sends no user e-mail and uses an installation-random or no `tool` identity (VERIFY NCBI policy). API keys are stored as vault secrets and never placed in logs.
**ALTERNATIVES:** Europe PMC REST as the primary online source (single endpoint, OA flags).
**GREENFIELD_REQUIRED:** yes for PubMed XML lifecycle mapping and the downloader; no for JATS.
**BLOCKS_IMPLEMENTATION:** yes for P03.
**VERIFICATION_REQUIRED:** fixture tests on real baseline and update XML samples with deletions and retraction links; a rights-mapping test on PMC articles with different licenses.

---

**GAP_ID:** OPUS-P00-011
**SEVERITY:** P1
**AREA:** documents/OCR / copy-first
**CLAIM_OR_ASSUMPTION_CHALLENGED:**
- SE-G008, `SOURCE_LEDGER.md` "SafeOCR status", and `MASTER_PLAN.md` P00A: "SafeOCR is currently empty… not an implementation donor".
- P12 lists "critical numeric verifier" as SafeEvidence-owned work.
**LIVE_EVIDENCE:**
- At `4658ed1` (committed before the review base), SafeOCR contains:
  - `src/safeocr/verification.py` (682 lines): independent-engine agreement, perturbation stability, visual grounding, structural association, unit validation, patient linkage;
  - `ocr.py` (PaddleOCR normalization, Tesseract crop reads);
  - `labgold.py`, `evaluation.py` (frozen split, Wilson bounds), `fhir.py`, `fhir_validator.py`;
  - 19 test files.
- `STATE.md` reports a frozen synthetic final evaluation (48 documents / 288 fields).
- License: Apache-2.0.
- Limits observed:
  - `parse_critical_value` normalizes only NFC and matches an ASCII-digit regex. Arabic-Indic digits, the Arabic decimal separator, and comma decimals return `None` (fail closed, zero coverage).
  - It is Python and lab-report specific.
**SOURCE_CODE_INSPECTED:** `verification.py`, `ocr.py`, `STATE.md`, `pyproject.toml`.
**FAILURE_MODE:** P12 rebuilds an existing critical-field verifier from scratch, in violation of the copy-first rule.
**WHY_IT_MATTERS:** this is a direct copy-first violation in the plan's own terms.
**AFFECTED_PHASES:** P12, P16, P20.
**READY_SOURCE_TO_COPY:** SafeOCR.
**EXACT_CODE_OR_TESTS_TO_REUSE:**
- `src/safeocr/{verification,ocr,contracts,labgold,evaluation}.py`;
- `tests/test_verification.py`, `test_ocr_adapters.py`, `test_evaluation*.py`, `test_labgold.py`.
**PROPOSED_RESOLUTION:**
- Correct the stale statements.
- Classify SafeOCR as an ORACLE_COPY/WORKER donor for the critical-number verifier.
- Port its signal logic into the primary document-engine integration only where the Rust trust boundary requires it.
- Add Arabic-Indic digit and separator support as SafeEvidence-specific work with fixtures.
**ALTERNATIVES:** keep SafeOCR as a Python worker during P12 qualification.
**GREENFIELD_REQUIRED:** no (Arabic numerals: small extension).
**BLOCKS_IMPLEMENTATION:** yes for P12.
**VERIFICATION_REQUIRED:** re-run SafeOCR's own suite at the pinned head inside the SafeEvidence harness; Arabic numeric fixtures.

---

**GAP_ID:** OPUS-P00-012
**SEVERITY:** P1
**AREA:** Arabic / cross-language retrieval
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `ARCHITECTURE.md` §22 calls for "Arabic query → English literature retrieval". SE-G009 promotes MedCPT.
**LIVE_EVIDENCE:**
- MedCPT encoders are initialized from PubMedBERT (`MedCPT/README.md`), an English biomedical vocabulary. It cannot embed Arabic queries meaningfully.
- fastembed-rs ships a multilingual BGE-M3 path (`src/models/bgem3.rs`, `gpahal/bge-m3-onnx-int8`).
- No SafeEvidence document names:
  - the mechanism for Arabic→English retrieval (translation vs multilingual encoder);
  - the verification of a translated query;
  - an Arabic medical terminology source.
**SOURCE_CODE_INSPECTED:** MedCPT README/LICENSE; fastembed-rs models.
**FAILURE_MODE:**
- Arabic questions silently retrieve poorly.
- Or a local LLM translates the query unverified, so a generative step becomes an unseen retrieval authority (e.g., negation or dose lost in translation).
**WHY_IT_MATTERS:** Arabic is declared an architectural requirement.
**AFFECTED_PHASES:** P04, P05, P10, P11, P20.
**READY_SOURCE_TO_COPY:**
- fastembed-rs BGE-M3 (DEPEND; model rights VERIFY).
- MedCPT (English lane).
- OpenMed multilingual grounding fixtures.
- WHO EMRO Unified Medical Dictionary as a candidate Arabic terminology source (VERIFY existence of a machine-readable form and its rights).
**EXACT_CODE_OR_TESTS_TO_REUSE:** fastembed-rs `UserDefinedEmbeddingModel` and reranking APIs for the MedCPT ONNX export.
**PROPOSED_RESOLUTION:**
- Add an explicit cross-language lane to P05: the multilingual encoder vs translate-then-MedCPT tournament.
- Any translated query is shown to the user and preserved in the snapshot.
- Negation, number and unit preservation checks on translation.
- Arabic normalization rules (alef/ya/ta-marbuta, diacritics, tatweel, Arabic-Indic digits) as a deterministic, tested module.
**ALTERNATIVES:** English-only V1 retrieval with Arabic UI, declared as a limitation.
**GREENFIELD_REQUIRED:** yes, small: the normalization module (no suitable Rust donor identified).
**BLOCKS_IMPLEMENTATION:** yes for P05 promotion.
**VERIFICATION_REQUIRED:** Arabic→English retrieval benchmark with recall@k vs the English-query baseline; translation-fidelity sentinel set.

---

**GAP_ID:** OPUS-P00-013
**SEVERITY:** P1
**AREA:** runtime anti-sprawl
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `RUNTIME_BUDGET.md` §2 "one primary engine per capability". The table has no row for inference runtimes.
**LIVE_EVIDENCE:** the planned donors bring:
- `tract-onnx` (MedScale `medscale-pack` workspace dependency);
- ONNX Runtime via `ort` (fastembed-rs; xberg PaddleOCR via ONNX Runtime per `ATTRIBUTIONS.md`; docling.rs `docling-onnx`);
- Candle (fastembed-rs `qwen3` feature; xberg `xberg-candle-ocr`);
- llama.cpp or mistral.rs (P10);
- Python (statsmodels, ASReview, SafeOCR, OpenMed, MultiVerS);
- Java (CQL).

fastembed-rs default features are `ort-download-binaries-native-tls`, `hf-hub-native-tls` and `image-models`. That means a build-time binary download plus runtime model download. RRnlp downloads weights from Zenodo and SciBERT from Hugging Face at import (`rrnlp/models/__init__.py`, `encoder.py`).
**SOURCE_CODE_INSPECTED:** cited Cargo.toml and Python files.
**FAILURE_MODE:** three ONNX-capable runtimes and two tensor stacks ship in the desktop app. Mobile binary size explodes. Hidden downloads violate "no hidden download on first clinical question".
**WHY_IT_MATTERS:** resource budget, supply chain and offline guarantees.
**AFFECTED_PHASES:** P05, P10, P12, P15, P16, P22.
**READY_SOURCE_TO_COPY:** n/a (policy).
**EXACT_CODE_OR_TESTS_TO_REUSE:** `cargo-deny` bans (MedScale `deny.toml` pattern) to forbid `hf-hub` and `ort/download-binaries` in product builds.
**PROPOSED_RESOLUTION:**
- Add "tensor/ONNX inference runtime" and "LLM runtime" rows to `RUNTIME_BUDGET.md`.
- Choose `ort` (it covers fastembed-rs, xberg and docling ONNX paths) as primary unless measured otherwise. Demote `tract` to the fallback the MedScale pack runtime is adapted away from.
- Build all Rust donors with `default-features = false`.
- Treat every model as an admitted ModelPack. No import-time downloads in any worker.
**ALTERNATIVES:** tract-only (pure Rust, smaller; operator coverage must be measured on MedCPT/BGE-M3/PP-OCR exports).
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** yes for P05/P10/P12 dependency admission.
**VERIFICATION_REQUIRED:** dependency tree check in CI showing exactly one ONNX runtime in the product build; a network-namespace test that model loading performs no egress.

---

**GAP_ID:** OPUS-P00-014
**SEVERITY:** P1
**AREA:** patient applicability / medication safety / FHIR
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `ARCHITECTURE.md` §4 PatientContext includes medications and allergies. Applicability covers "interacting medications". P14 "starts from MedScale's existing FHIR R4 crate".
**LIVE_EVIDENCE:**
- MedScale `medscale-fhir` extracts only `Patient`, `Observation` and `Condition` (`extractors/mod.rs` L373–375). Its own test asserts `MedicationRequest` is unsupported (L478). There is no AllergyIntolerance or MedicationStatement.
- The commandMed policy requires a `REQUIRED_AUTHORITATIVE` source for `MEDICATION_INTERACTION_OR_CONTRAINDICATION_LOOKUP` with generative substitution `PROHIBITED` (`data/eval/safety_policy.json`).
- No SafeEvidence source ledger entry names a redistributable, authoritative drug-interaction or contraindication source. NLM's public interaction API is understood to have been discontinued (VERIFY).
**SOURCE_CODE_INSPECTED:** MedScale FHIR extractors; commandMed policy.
**FAILURE_MODE:** interaction or contraindication questions get answered from literature retrieval plus LLM synthesis, exactly what the copied policy prohibits. Applicability is also asserted while medications and allergies are invisible to the FHIR adapter.
**WHY_IT_MATTERS:** medication errors are high-consequence.
**AFFECTED_PHASES:** P07, P08, P14, P20.
**READY_SOURCE_TO_COPY:** OpenMed `openmed/interop/fhir/` (tests/adapters; inventory confirmed); OpenMed `linkers/rxnorm.py` and `loaders/rxnorm_loader.py` for RxNorm normalization (rights-gated).
**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale `medscale-fhir` gate and extractors plus tests; OpenMed RxNorm loader/linker tests.
**PROPOSED_RESOLUTION:**
- Extend the FHIR subset to MedicationRequest, MedicationStatement and AllergyIntolerance, with unsupported/loss reporting.
- Add a binding rule: with no admitted authoritative interaction source, interaction or contraindication questions resolve to ABSTAIN or ESCALATE with an explicit reason. Allow an institution-provided adapter only.
**ALTERNATIVES:** a licensed commercial DDI database via an institution adapter (allowed, optional).
**GREENFIELD_REQUIRED:** small FHIR extractor extensions only.
**BLOCKS_IMPLEMENTATION:** yes for P07/P14 applicability claims.
**VERIFICATION_REQUIRED:** sentinel tests where an interaction question with no admitted source must not produce ANSWER.

---

**GAP_ID:** OPUS-P00-015
**SEVERITY:** P1
**AREA:** guidelines / provenance governance
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `COPY_FIRST_SOURCE_PLAN.md` §11 "guideline verification semantics | ProtocolWISE | COPY/ADAPT"; SE-G012 "ProtocolWISE remains the SafeEvidence-specific verification research source"; GuidelinePack as a pack class.
**LIVE_EVIDENCE:**
- The named donor is not a publicly accessible repository. `AGENTS.md` requires that non-public source identities not be disclosed in this public repository without explicit authorization.
- Inspected under founder access, its default branch contains no implementation code (a research README only).
- No SafeEvidence document identifies any guideline corpus whose redistribution rights permit a GuidelinePack. Most society and national guidelines are copyrighted. Saudi/NPHIES-specific guideline sources are unnamed.
- CQL tooling (`cqframework`) is Java.
**SOURCE_CODE_INSPECTED:** repository listing of the named donor; SafeEvidence ledger.
**FAILURE_MODE:**
- P13 assumes a COPY donor that has no code.
- The public docs keep disclosing a non-public source.
- GuidelinePacks cannot legally ship content.
**WHY_IT_MATTERS:** guideline applicability is one of the six primary jobs.
**AFFECTED_PHASES:** P13, P07, P20.
**READY_SOURCE_TO_COPY:** `cqframework/clinical_quality_language` CQL-to-ELM (WORKER, desktop/dev only); EBMonFHIR recommendation and certainty profiles (concepts).
**EXACT_CODE_OR_TESTS_TO_REUSE:** CQL-to-ELM translator test suite (VERIFY paths).
**PROPOSED_RESOLUTION:**
- Reclassify the named donor to `REFERENCE` (research thesis only). Have the founder decide whether its name may remain public.
- Make the V1 guideline scope "user/institution-provided guideline documents" (rights carried by the provider) plus metadata-only links to public guidelines.
- Treat semantic guideline verification as a `GREENFIELD_JUSTIFIED` research lane with no product claim.
**ALTERNATIVES:** defer P13 entirely beyond V1.
**GREENFIELD_REQUIRED:** yes (research).
**BLOCKS_IMPLEMENTATION:** yes for P13.
**VERIFICATION_REQUIRED:** founder disclosure decision recorded; rights memo for any bundled guideline.

---

**GAP_ID:** OPUS-P00-016
**SEVERITY:** P1
**AREA:** snapshots vs deletion / revocation / license expiry
**CLAIM_OR_ASSUMPTION_CHALLENGED:** "Saved answers bind immutable evidence snapshots" (`PRODUCT_THESIS.md` §7). Deletion/tombstone propagation and institution-licensed packs.
**LIVE_EVIDENCE:**
- No document reconciles three things:
  - immutable historical snapshots;
  - (a) user deletion of patient context;
  - (b) expiry or revocation of institution-licensed full text, which must be purged from historical snapshots.
- MedScale `SealedBlobStore` names files by plaintext digest, and `destroy_key_material` leaves keystore copies (OPUS-P00-003).
**SOURCE_CODE_INSPECTED:** `sealed_blob.rs`, `encrypted_vault.rs`.
**FAILURE_MODE:** either immutability is violated silently, or deletion and license obligations are violated.
**WHY_IT_MATTERS:** privacy and licensing compliance vs reproducibility.
**AFFECTED_PHASES:** P02, P03, P17, P21.
**READY_SOURCE_TO_COPY:** ottari `vault_deletion.rs` (deletion semantics and tests).
**EXACT_CODE_OR_TESTS_TO_REUSE:** ottari deletion tests; ottari `b306_plaintext_spill.rs`.
**PROPOSED_RESOLUTION:**
- A snapshot stores identities, digests and span coordinates. Bytes are referenced, not owned.
- Deleted or revoked bytes leave a tombstone that keeps the digest and the reason (`REDACTED_BY_USER`, `LICENSE_EXPIRED`).
- Reproduction reports `PARTIAL_REPRODUCTION`.
**ALTERNATIVES:** per-snapshot encryption keys for crypto-shredding.
**GREENFIELD_REQUIRED:** small (contract).
**BLOCKS_IMPLEMENTATION:** yes for the P02 snapshot contract.
**VERIFICATION_REQUIRED:** tests where deleting context or expiring a license removes bytes from vault, indexes, caches and backups, while snapshot identity remains verifiable.

---

**GAP_ID:** OPUS-P00-017
**SEVERITY:** P1
**AREA:** claim-support verification
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the five-label support set {SUPPORTS, PARTIALLY_SUPPORTS, CONTRADICTS, DOES_NOT_ESTABLISH, UNRESOLVED} is "sufficient".
**LIVE_EVIDENCE:**
- Labels alone cannot express *why* support is partial.
- The required hard cases differ along independent facets: population/subgroup, intervention/dose/unit, comparator, outcome, timepoint, effect measure (absolute vs relative), adjustment (adjusted vs unadjusted), endpoint hierarchy (primary vs secondary), direction, numeric value, negation, hedging/certainty, and source validity (retracted).
- SciFact labels are abstract-level SUPPORT/CONTRADICT/NEI on scientific claims, not clinical-answer claims.
- `SOURCE_UNAVAILABLE` appears in `ARCHITECTURE.md` but not in P06 or SE-G003.
**SOURCE_CODE_INSPECTED:** SciFact `LICENSE.md` (claims CC BY 4.0, abstracts ODC-By 1.0, code Apache-2.0); MultiVerS `LICENSE` (MIT).
**FAILURE_MODE:**
- "Correct paper, wrong subgroup" and "relative risk stated as absolute risk" both collapse into PARTIALLY_SUPPORTS. The UI cannot warn specifically, and the downgrade policy cannot differentiate high-consequence mismatches.
- A retracted source's span shows as SUPPORTS.
**WHY_IT_MATTERS:** claim support is the core verification product.
**AFFECTED_PHASES:** P02, P06, P10, P20.
**READY_SOURCE_TO_COPY:**
- SciFact evaluation code (Apache-2.0) and data (CC BY 4.0 / ODC-By) as BENCHMARK.
- Evidence-Inference annotations (direction labels) as BENCHMARK; data rights derive from PMC OA articles (VERIFY per article).
- SafeOCR `parse_critical_value` pattern for numeric comparison.
**EXACT_CODE_OR_TESTS_TO_REUSE:** SciFact evaluation scripts; Evidence-Inference `annotations/` splits.
**PROPOSED_RESOLUTION:**
- Keep the 5 labels plus `SOURCE_UNAVAILABLE`.
- Add a required `mismatch_facets[]` set and a separate `source_validity` axis that comes from the overlay, not the verifier.
- Numeric, unit and dose facets are checked deterministically before any model verifier.
- The P06 holdout must include ≥1 adversarial case per facet listed in this review's 13 test-case classes.
**ALTERNATIVES:** more labels (rejected: facets compose better).
**GREENFIELD_REQUIRED:** yes: facet policy and deterministic numeric checker (SafeEvidence-specific).
**BLOCKS_IMPLEMENTATION:** yes for P02 Claim contract and P06.
**VERIFICATION_REQUIRED:** per-facet confusion matrices on the SafeEvidence holdout.

---

**GAP_ID:** OPUS-P00-018
**SEVERITY:** P1
**AREA:** desktop shell decision conflict
**CLAIM_OR_ASSUMPTION_CHALLENGED:** `ARCHITECTURE.md` §2/§15, `SOURCE_LEDGER.md` §9 and `MASTER_PLAN.md` P11 name Tauri/React as the candidate. SE-G014 says "Slint is the stronger default hypothesis". `PREBUILD_KILL_REVIEW` marks desktop `RESOLVED_WITH_TOURNAMENT`.
**LIVE_EVIDENCE:**
- MedScale desktop uses `slint = "=1.16.1"` with `backend-winit`, `renderer-femtovg` and `accessibility`, under `LicenseRef-Slint-Royalty-free-2.0`.
- The MedScale desktop crate has only one file referencing Arabic/RTL (`utility_surfaces.rs`). There is no evidence in the donor of Arabic shaping or bidi quality.
**SOURCE_CODE_INSPECTED:** MedScale `Cargo.toml`, `deny.toml`, desktop crate listing.
**FAILURE_MODE:** agents pick a shell by whichever document they read last. Arabic RTL and screen-reader parity is assumed, not measured.
**WHY_IT_MATTERS:** `AGENTS.md` says conflicts must be recorded explicitly, not treated as resolved.
**AFFECTED_PHASES:** P11.
**READY_SOURCE_TO_COPY:** MedScale `crates/medscale-desktop` (Slint patterns); Tauri (DEPEND) if it wins.
**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale desktop accessibility setup.
**PROPOSED_RESOLUTION:**
- Mark the shell as `OPEN_CONFLICT` in all four documents until the spike runs.
- The spike measures Arabic shaping/bidi in mixed Arabic-Latin dose strings, the screen reader on Windows/macOS, WebView cache and crash-dump surfaces (Tauri), and license attribution (Slint).
**ALTERNATIVES:** native per-OS UI (rejected: cost).
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** yes for P11.
**VERIFICATION_REQUIRED:** spike report at exact heads.

---

**GAP_ID:** OPUS-P00-019
**SEVERITY:** P1
**AREA:** human adjudication / hidden development cost
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the zero-founder-COGS principle and AGENTS "do not introduce paid … as mandatory development gates", alongside mandatory clinician-adjudicated holdouts (SE-G003, P06, P09, P20).
**LIVE_EVIDENCE:**
- P06/P09/P20 closure depends on clinician adjudication, inter-rater agreement and Arabic clinician review.
- No document states:
  - who the clinicians are;
  - how many labels are needed;
  - cost or volunteer basis;
  - conflict-of-interest handling;
  - any ethics/IRB need for using real questions.
**SOURCE_CODE_INSPECTED:** n/a (plan analysis).
**FAILURE_MODE:** the most important gates silently stall, or get satisfied by model-generated "gold".
**WHY_IT_MATTERS:** it determines whether any verification claim can ever be made.
**AFFECTED_PHASES:** P06, P08, P09, P20, P23.
**READY_SOURCE_TO_COPY:** DAL and SafeOCR frozen-split/claim-ledger tooling for adjudication bookkeeping.
**EXACT_CODE_OR_TESTS_TO_REUSE:** DAL `tools/build_sg000023_paper_evidence.py` (claim-ledger pattern); SafeOCR `evaluation.py` split freezing.
**PROPOSED_RESOLUTION:** a P20 resourcing decision record covering:
- minimum label counts derived from target CI widths;
- the adjudicator pool and qualifications;
- funding or volunteer basis (founder decision);
- a rule that model-generated labels are never gold.
**ALTERNATIVES:** narrow V1 claims to public benchmarks only, with no clinical-support claims.
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no for P01–P05; yes for the P06/P09 closure gates.
**VERIFICATION_REQUIRED:** recorded founder decision.

---

### P2

---

**GAP_ID:** OPUS-P00-020 · **SEVERITY:** P2 · **AREA:** online query privacy
**CLAIM_OR_ASSUMPTION_CHALLENGED:** SE-G015/PB-G016 two-mode rule suffices.
**LIVE_EVIDENCE:**
- The query text itself is sensitive. Stripping "patient identifiers" from a free-text clinical question is not a solved deterministic task.
- Remote queries are also exposed through DNS and SNI metadata and through any persistent `api_key`/`email`.
- Remote results cached locally must inherit private-plane scope.
**SOURCE_CODE_INSPECTED:** MedScale `browse.rs` (resolver).
**FAILURE_MODE:** "minimized" queries still carry rare-disease plus age plus location combinations.
**WHY_IT_MATTERS:** this is the clinical question confidentiality promise.
**AFFECTED_PHASES:** P03, P11, P21.
**READY_SOURCE_TO_COPY:** OpenMed PII/de-identification evaluation (`android/openmedkit/.../PiiValidators.kt`, Python deid modules) as BENCHMARK/WORKER.
**EXACT_CODE_OR_TESTS_TO_REUSE:** OpenMed PII validator tests.
**PROPOSED_RESOLUTION:**
- Online discovery never auto-sends. The user sees and edits the exact outbound string.
- The default outbound query is built from structured PICO terms (MeSH/keywords), not the raw narrative.
- Remote results are cached only in the private plane.
**ALTERNATIVES:** Europe PMC only.
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no (P03 bound).
**VERIFICATION_REQUIRED:** an egress-capture test showing only the confirmed string leaves.

---

**GAP_ID:** OPUS-P00-021 · **SEVERITY:** P2 · **AREA:** mobile
**CLAIM_OR_ASSUMPTION_CHALLENGED:** "MedScale mobile security contracts and tests" are a COPY source (`COPY_FIRST_SOURCE_PLAN.md` §10).
**LIVE_EVIDENCE:**
- MedScale `medscale-contracts/src/mobile/mod.rs` is a `READY_BASE` stub: `apps_shipped: false`, `ffi_boundary: "contracts_stub_no_uniffi"`, iOS FFI admission "TBD".
- MedScale's `keyring` configuration covers Windows, Apple and Linux only.
- UniFFI generates Kotlin bindings over JNA (documented architecture; VERIFY overhead): large byte payloads (images, PDFs) should cross as file handles, not buffers.
- OpenMed ships `swift/OpenMedKit` and `android/openmedkit` with `UnicodeOffsetContract.kt`, `OffsetMap.kt`, `OcrOffsetMapTest.kt` and `OffsetContractParityTest.kt`. These are directly relevant to Swift/Kotlin span parity.
- The `keyring` Linux `linux-native` backend is believed to use kernel keyutils, which do not persist across reboot (VERIFY).
**SOURCE_CODE_INSPECTED:** MedScale mobile contract; OpenMed tree.
**FAILURE_MODE:** mobile key custody and span parity get built twice.
**WHY_IT_MATTERS:** this is the Swift/Kotlin divergence risk.
**AFFECTED_PHASES:** P15, P16.
**READY_SOURCE_TO_COPY:** ottari Android/Apple protectors; OpenMed offset parity tests; UniFFI (DEPEND).
**EXACT_CODE_OR_TESTS_TO_REUSE:** `android/openmedkit/src/test/kotlin/com/openmed/openmedkit/parity/OffsetContractParityTest.kt`, `ocr/OcrOffsetMapTest.kt`; ottari `vault_android_keystore.rs`, `vault_apple_keychain.rs`.
**PROPOSED_RESOLUTION:**
- Re-point mobile donors.
- Add mobile backup exclusion (iOS `isExcludedFromBackup`, Android `allowBackup=false` / data-extraction rules), `FLAG_SECURE`, app-switcher snapshot blur, and notification-content redaction as P15 acceptance tests.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no (P15 bound).
**VERIFICATION_REQUIRED:** device tests per item.

---

**GAP_ID:** OPUS-P00-022 · **SEVERITY:** P2 · **AREA:** lexical baseline
**CLAIM_OR_ASSUMPTION_CHALLENGED:** "MedScale lexical baseline + SQLite FTS5" (P04 reuse default).
**LIVE_EVIDENCE:**
- The MedScale `retrieval.rs` `score` is the fraction of query tokens present, over an in-memory synthetic corpus. `knowledge.rs` `lexical-v1` is a capped-tf idf variant.
- `LexicalRetrieveRequest.include_retracted` defaults to false (`evidence/mod.rs` L131): retracted documents are *excluded from ranking*. That contradicts `ARCHITECTURE.md` §6 "retracted … sources remain visible with explicit state", and prevents "your cited paper was retracted" detection.
**SOURCE_CODE_INSPECTED:** files cited.
**FAILURE_MODE:** a copied default hides retracted evidence instead of flagging it.
**WHY_IT_MATTERS:** retraction behavior is a declared competitive property.
**AFFECTED_PHASES:** P04.
**READY_SOURCE_TO_COPY:** SQLite FTS5 `bm25()` or Tantivy (DEPEND).
**EXACT_CODE_OR_TESTS_TO_REUSE:** MedScale `tests/retrieval_011.rs`, `evidence_corpus_025.rs` as *inverted* fixtures (retracted must be returned and flagged).
**PROPOSED_RESOLUTION:** use FTS5/Tantivy directly. Retracted documents are ranked and flagged. The MedScale scorer is not a baseline.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** a retraction-visibility test.

---

**GAP_ID:** OPUS-P00-023 · **SEVERITY:** P2 · **AREA:** evidence-synthesis donor maturity
**CLAIM_OR_ASSUMPTION_CHALLENGED:** ES3, PICOX, RRnlp and Trialstreamer are `COPY_BOUNDED` donors.
**LIVE_EVIDENCE:**
- ES3 is a Flask/PostgreSQL/RabbitMQ web app, "not intended for use in production" (README), last pushed 2023.
- PICOX has only Jupyter notebooks plus a zip corpus; no library code and no weights.
- RRnlp fetches weights from Zenodo and SciBERT from Hugging Face at import.
- MultiVerS is a Longformer research model (GPU-oriented).
- ASReview core pulls Flask, flask-mail, requests, datahugger and `synergy_dataset` as hard dependencies. Its stoppers are `LastRelevant` and `NLabeled` only (`simulation/cli.py`); there is no statistical stopping rule.
**SOURCE_CODE_INSPECTED:** listed.
**FAILURE_MODE:** agents "copy" stacks that violate the runtime budget, or believe stopping is solved.
**WHY_IT_MATTERS:** realistic donor classification.
**AFFECTED_PHASES:** P06, P07, P18.
**READY_SOURCE_TO_COPY:**
- ES3 data and `ecitmatch_tools.py`.
- Evidence-Inference data.
- RRnlp models as ModelPacks (weights rights VERIFY).
- ASReview `asreview/models/` + `learner.py` as a headless worker slice.
- A statistical stopping method such as the buscar approach (VERIFY source and license).
**EXACT_CODE_OR_TESTS_TO_REUSE:** ASReview `asreview/models`, `asreview/learner.py`, `asreview/metrics.py`; SYNERGY datasets (CC0).
**PROPOSED_RESOLUTION:**
- Reclassify: ES3 → DATA/REFERENCE; PICOX → BENCHMARK/REFERENCE; RRnlp → MODEL_ARTIFACT_IMPORT; MultiVerS → BENCHMARK_ONLY.
- A Deep Review stop decision requires a statistical criterion plus human confirmation.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no (P18 bound).
**VERIFICATION_REQUIRED:** SYNERGY recall@stop and workload saved.

---

**GAP_ID:** OPUS-P00-024 · **SEVERITY:** P2 · **AREA:** document-engine selection
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the Xberg vs docling.rs tournament is symmetric.
**LIVE_EVIDENCE:**
- docling.rs was created 2026-06-27 (API). Its README says it was "Developed with Claude Code". It carries RAG, vector-store and HTTP-server crates.
- xberg is a broad polyglot workspace (16 crates plus bindings) with optional OpenTelemetry telemetry (feature-gated), model download, LLM, MCP and service modules. It has an Arabic PaddleOCR tier (`paddle_ocr/config.rs`), a JATS extractor, and an `extractors/security` test module.
- Both carry overlapping chunking/embedding/RAG features that duplicate SafeEvidence retrieval.
**SOURCE_CODE_INSPECTED:** listed.
**FAILURE_MODE:** a dependency with default features re-introduces a second embedding or vector stack and telemetry code paths.
**WHY_IT_MATTERS:** anti-sprawl and privacy.
**AFFECTED_PHASES:** P12.
**READY_SOURCE_TO_COPY:** xberg (primary hypothesis: maturity, Arabic OCR tier, JATS, security tests) or docling.rs.
**EXACT_CODE_OR_TESTS_TO_REUSE:** xberg `crates/xberg/src/extractors/security_tests.rs`, `extractors/security/tests.rs`.
**PROPOSED_RESOLUTION:**
- Tournament with `default-features = false`.
- Forbid `otel`, model-download, `llm`, `mcp`, `service`, chunking and embedding features via `cargo-deny`/feature audit.
- Run parsing in an out-of-process worker under the MedScale `os_sandbox` compositions.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** feature audit in CI; hostile-file corpus results.

---

**GAP_ID:** OPUS-P00-025 · **SEVERITY:** P2 · **AREA:** model, data and fixture rights
**CLAIM_OR_ASSUMPTION_CHALLENGED:** donor tests and fixtures "travel with the code".
**LIVE_EVIDENCE:**
- OpenMed `openmed/clinical/grounding/data/` contains `chpo_hpo.json`, `icd10cn_icd10.json` and `indic_hpo_aliases.json`.
- `openmed/eval/golden/grounding/loinc.jsonl` contains LOINC content, which carries the LOINC license. `rxnorm.jsonl` is RxNorm-derived.
- Evidence-Inference ships PMC-derived article text.
- MedCPT code is a US Government Work (public domain). Weight-card terms are separate (VERIFY).
- Model weights for docling layout/TableFormer, PP-OCR, GLiNER, BGE-M3 and generator candidates are unrecorded.
**SOURCE_CODE_INSPECTED:** OpenMed tree; MedCPT LICENSE; SciFact LICENSE.
**FAILURE_MODE:** fixtures copied with code carry restricted terminology or article text into a public Apache repository.
**WHY_IT_MATTERS:** provenance.
**AFFECTED_PHASES:** all transplant PRs.
**READY_SOURCE_TO_COPY:** OpenMed `openmed/core/terminology_licenses.py`, `openmed/eval/data_license_gate.py`, `openmed/eval/datasets/licenses.py` (copy as the SafeEvidence rights gate).
**EXACT_CODE_OR_TESTS_TO_REUSE:** those three modules and their tests.
**PROPOSED_RESOLUTION:** every fixture file needs a rights row. Restricted terminology stays outside the repository (OpenMed's own rule).
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** fixture-rights CI check.

---

**GAP_ID:** OPUS-P00-026 · **SEVERITY:** P2 · **AREA:** applicability calculators
**CLAIM_OR_ASSUMPTION_CHALLENGED:** "deterministic tools outrank generative text", with no tool inventory.
**LIVE_EVIDENCE:**
- Renal and hepatic applicability requires identified equations: CKD-EPI 2021 vs 2009, Cockcroft–Gault for drug dosing, Child–Pugh. Pediatric weight-based checks need identified formulas.
- No calculator source is named.
- commandMed requires `mechanism_id/revision/result_digest` for calculators.
**SOURCE_CODE_INSPECTED:** commandMed truth boundaries.
**FAILURE_MODE:** an LLM computes eGFR, or an unidentified equation is used.
**WHY_IT_MATTERS:** numeric clinical safety.
**AFFECTED_PHASES:** P07, P08.
**READY_SOURCE_TO_COPY:** commandMed tool registry/provenance (`registry.py`); no vetted calculator code donor identified.
**EXACT_CODE_OR_TESTS_TO_REUSE:** commandMed `registry.py` and `test_registry.py`.
**PROPOSED_RESOLUTION:** `GREENFIELD_JUSTIFIED` for a small calculator set, using published equations and published test vectors, with unit handling through UCUM (MedScale `units/` subset).
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** yes (small).
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** published-vector tests.

---

**GAP_ID:** OPUS-P00-027 · **SEVERITY:** P2 · **AREA:** retrieved-content prompt injection
**CLAIM_OR_ASSUMPTION_CHALLENGED:** injection is handled by "source text is data".
**LIVE_EVIDENCE:** commandMed detection is an 8-entry lexical marker list (`INJECTION_MARKERS`), signal-only.
**SOURCE_CODE_INSPECTED:** `scaffold.py`.
**FAILURE_MODE:** adversarial text in a preprint or user document steers synthesis wording.
**WHY_IT_MATTERS:** synthesis integrity.
**AFFECTED_PHASES:** P10, P12.
**READY_SOURCE_TO_COPY:** commandMed trace/injection fixtures (as regression tests).
**EXACT_CODE_OR_TESTS_TO_REUSE:** commandMed `tests/spec006/test_scaffold.py` injection cases.
**PROPOSED_RESOLUTION:**
- The generator has no tools and no egress.
- Output is constrained to claims citing span IDs.
- Every material claim passes the verifier.
- Spans are delimited and escaped in the context compiler.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** an injected-span adversarial set.

---

**GAP_ID:** OPUS-P00-028 · **SEVERITY:** P2 · **AREA:** OS residual surfaces
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the P21 campaign list is sufficient.
**LIVE_EVIDENCE:** none of the following are named:
- Windows Error Reporting / macOS ReportCrash full-memory dumps;
- pagefile and hibernation files;
- the clipboard history service;
- Spotlight/Windows Search indexing of vault paths.

MedScale `privacy_probes.rs` exists and is reusable; MedScale `assert_claim_path` refuses sync roots by substring only.
**SOURCE_CODE_INSPECTED:** `claim.rs`; storage `lib.rs` exports.
**FAILURE_MODE:** PHI in crash dumps or OS indexes.
**WHY_IT_MATTERS:** privacy.
**AFFECTED_PHASES:** P11, P21.
**READY_SOURCE_TO_COPY:** MedScale `privacy_probes.rs` (`probe_os_privacy_surfaces`, `scan_vault_work_leftovers`); ottari `b306_plaintext_spill.rs`.
**EXACT_CODE_OR_TESTS_TO_REUSE:** those.
**PROPOSED_RESOLUTION:** add these surfaces to P21, with documented residual risk where they cannot be controlled.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** probe report.

---

**GAP_ID:** OPUS-P00-029 · **SEVERITY:** P2 · **AREA:** publication lifecycle details
**CLAIM_OR_ASSUMPTION_CHALLENGED:** SE-G001/PB-G009 lifecycle coverage.
**LIVE_EVIDENCE:** the plan does not mention:
- preprint → published version linking (Crossref relation metadata; Europe PMC preprint links, VERIFY);
- conference abstracts that are usually absent from PubMed;
- expressions of concern as a state distinct from retraction (PB-G009 lists CORRECTION and RETRACTION_NOTICE but no EXPRESSION_OF_CONCERN state);
- registry result postings as evidence with arm-level data (OPUS-P00-008).
**SOURCE_CODE_INSPECTED:** plan documents.
**FAILURE_MODE:** expressions of concern are invisible, and preprint results get cited after publication changed them.
**WHY_IT_MATTERS:** current-validity overlay accuracy.
**AFFECTED_PHASES:** P03, P06.
**READY_SOURCE_TO_COPY:** PubMed XML CommentsCorrections; Crossref relations; CT.gov API v2 (data).
**EXACT_CODE_OR_TESTS_TO_REUSE:** n/a.
**PROPOSED_RESOLUTION:** add `EXPRESSION_OF_CONCERN` and `ReportVersionLink`.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** overlay fixtures.

---

**GAP_ID:** OPUS-P00-030 · **SEVERITY:** P2 · **AREA:** readiness overclaim
**CLAIM_OR_ASSUMPTION_CHALLENGED:** the `PREBUILD_KILL_REVIEW_2026-10-07.md` readiness matrix: "calibration RESOLVED", "decision assurance RESOLVED", "rights/licensing RESOLVED", "documents/OCR RESOLVED", "quantitative synthesis RESOLVED".
**LIVE_EVIDENCE:** OPUS-P00-002, -005, -006, -007, -009 and -011 contradict those statuses with donor code.
**SOURCE_CODE_INSPECTED:** as cited.
**FAILURE_MODE:** downstream agents treat open gates as closed.
**WHY_IT_MATTERS:** AGENTS.md evidence discipline.
**AFFECTED_PHASES:** P00.
**READY_SOURCE_TO_COPY:** n/a.
**EXACT_CODE_OR_TESTS_TO_REUSE:** n/a.
**PROPOSED_RESOLUTION:** in reconciliation, change those rows to `OPEN_WITH_OWNER` and reference this review.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** reconciled matrix.

---

**GAP_ID:** OPUS-P00-031 · **SEVERITY:** P2 · **AREA:** ASK_MORE / over-abstention UX
**CLAIM_OR_ASSUMPTION_CHALLENGED:** abstention is always a success.
**LIVE_EVIDENCE:** no maximum ASK_MORE turns, no minimum useful-coverage target, and no "answer the population-level question while flagging missing patient context" mode is defined.
**SOURCE_CODE_INSPECTED:** plan documents.
**FAILURE_MODE:** the product abstains on most real questions, or loops on ASK_MORE.
**WHY_IT_MATTERS:** clinician adoption.
**AFFECTED_PHASES:** P08, P11, P20.
**READY_SOURCE_TO_COPY:** DAL `risk_coverage_curve` for coverage reporting.
**EXACT_CODE_OR_TESTS_TO_REUSE:** DAL metrics.
**PROPOSED_RESOLUTION:**
- Define a population-level answer with explicit applicability gaps as ANSWER_WITH_CAUTION.
- Cap ASK_MORE turns.
- Report coverage alongside unsafe-commit.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** coverage at fixed unsafe-commit on the holdout.

---

### P3

---

**GAP_ID:** OPUS-P00-032 · **SEVERITY:** P3 · **AREA:** document consistency
**CLAIM_OR_ASSUMPTION_CHALLENGED:** pins and closure scope are consistent.
**LIVE_EVIDENCE:**
- ottari and kernux pins differ between `COPY_FIRST_SOURCE_PLAN.md` and `REUSE_FIRST_IMPLEMENTATION_MAP.md`, and kernux has moved.
- P00 closure scope reads "P01–P15" (`COPY_FIRST_SOURCE_PLAN.md` §15) vs "P01–P10" (`MASTER_PLAN.md`, REUSE map §13).
- The `GAP_REVIEW.md` gap format lacks the READY_SOURCE fields that the founder's copy-first directive requires.
**SOURCE_CODE_INSPECTED:** docs.
**FAILURE_MODE:** ambiguous closure criteria.
**WHY_IT_MATTERS:** process hygiene.
**AFFECTED_PHASES:** P00.
**READY_SOURCE_TO_COPY:** n/a.
**EXACT_CODE_OR_TESTS_TO_REUSE:** n/a.
**PROPOSED_RESOLUTION:** single pin table; single closure scope; amend the gap format.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** doc diff.

---

**GAP_ID:** OPUS-P00-033 · **SEVERITY:** P3 · **AREA:** accessibility of evidence visuals
**CLAIM_OR_ASSUMPTION_CHALLENGED:** accessibility is covered generically.
**LIVE_EVIDENCE:** forest plots, risk-of-bias matrices and PRISMA diagrams have no non-visual representation requirement.
**SOURCE_CODE_INSPECTED:** n/a.
**FAILURE_MODE:** screen-reader users cannot read synthesis results.
**WHY_IT_MATTERS:** accessibility.
**AFFECTED_PHASES:** P11, P18.
**READY_SOURCE_TO_COPY:** statsmodels `summary_frame` (tabular output).
**EXACT_CODE_OR_TESTS_TO_REUSE:** —
**PROPOSED_RESOLUTION:** every chart has an equivalent table.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** a11y review.

---

**GAP_ID:** OPUS-P00-034 · **SEVERITY:** P3 · **AREA:** sibling roles
**CLAIM_OR_ASSUMPTION_CHALLENGED:** Morize/MESC/kernux are material donors.
**LIVE_EVIDENCE:**
- Morize `morize-core` is about 2,058 lines of Rust (identity/decision/relation/scope primitives).
- kernux is about 19,294 lines (policy/egress/identity/secret/store, `kernuxd` auth/transport).
- MESC is a Python research workspace.
- No recommendation in this review depends on their internals.
**SOURCE_CODE_INSPECTED:** listings only.
**FAILURE_MODE:** none material.
**WHY_IT_MATTERS:** scope.
**AFFECTED_PHASES:** P02, P21.
**READY_SOURCE_TO_COPY:** kernux `kernux-policy/src/egress.rs` and `kernuxd/src/auth.rs` may serve UI↔core authentication (VERIFY in P02/P21).
**EXACT_CODE_OR_TESTS_TO_REUSE:** VERIFY.
**PROPOSED_RESOLUTION:** inspect kernux `kernuxd` auth before designing UI↔core authentication.
**ALTERNATIVES:** —
**GREENFIELD_REQUIRED:** no.
**BLOCKS_IMPLEMENTATION:** no.
**VERIFICATION_REQUIRED:** donor decision at P02.

---

## 3. Required test-case coverage for claim verification (OPUS-P00-017)

| Hard case | Facet | Deterministic first? |
|---|---|---|
| correct citation, wrong claim | outcome/direction | no |
| correct paper, wrong subgroup | population/subgroup | partial (subgroup terms) |
| correct result, wrong timepoint | timepoint | yes (time expressions) |
| directionality reversal | direction | no |
| absolute vs relative risk | effect measure | yes (measure tokens) |
| adjusted vs unadjusted | adjustment | partial |
| secondary vs primary endpoint | endpoint hierarchy | partial (registry link) |
| numeric mismatch | numeric | yes |
| dose/unit mismatch | dose/unit | yes (UCUM) |
| negation | negation | partial |
| retracted evidence | source validity (overlay) | yes |
| inaccessible full text | SOURCE_UNAVAILABLE | yes |
| multiple conflicting spans | CONTRADICTS + CONFLICT state | no |

## 4. Phase reuse table P01–P23

| PHASE | MAJOR_CAPABILITY | READY_SOURCE_EXISTS? | BEST_SOURCE | MODE | EXACT REUSE TARGET | REMAINING SAFEEVIDENCE-SPECIFIC WORK | BLOCKER? |
|---|---|---|---|---|---|---|---|
| P01 | repo, CI, provenance, supply chain | yes | MedScale | COPY | `deny.toml`, `supply-chain/`, `third_party/provenance/`, `rust-toolchain.toml`; cargo-deny/cargo-vet DEPEND | donor-rights register (OPUS-002) | yes: OPUS-002 |
| P02 | contracts, vault, keys | yes | ottari himsat-core vault + MedScale writer_lock/claim + EBMonFHIR concepts | COPY / VENDOR | `himsat-core/src/vault*.rs` + `tests/b*`; MedScale `writer_lock.rs`, `claim.rs`, `aead_wrap.rs`; HL7/ebm profiles | data-plane split, Study/Arm model, state contract, snapshot tombstones | yes: OPUS-001/003/005/008/016/017 |
| P03 | acquisition, lifecycle, rights | partial | xberg JATS extractor; MedScale `browse.rs`; ES3 `ecitmatch_tools.py`; OpenMed license gates | DEPEND / COPY | `extractors/jats/*`; `validate_url`/`PublicOnlyResolver`; `data_license_gate.py` | PubMed XML lifecycle mapping, bulk downloader, overlay | yes: OPUS-001/010 |
| P04 | lexical retrieval | yes | SQLite FTS5 / Tantivy | DEPEND | FTS5 `bm25()` | medical/Arabic tokenization, MeSH expansion | no |
| P05 | embeddings, rerank, cross-language | yes | fastembed-rs (no default features); MedCPT; BGE-M3; BEIR | DEPEND / ARTIFACT_IMPORT / BENCHMARK | `UserDefinedEmbeddingModel`, reranking API; BEIR harness | Arabic lane, quantization budget | yes: OPUS-012/013 |
| P06 | claim support, effect extraction | partial | SciFact eval; Evidence-Inference data; MultiVerS oracle; SafeOCR numeric pattern | BENCHMARK / ORACLE_COPY | SciFact eval scripts; EI annotations | facet policy, deterministic numeric checker, holdout | yes: OPUS-017/019 |
| P07 | appraisal, applicability | partial | EBMonFHIR RoB/certainty concepts; RRnlp models; RobotReviewer (GPL, benchmark only) | REFERENCE / ARTIFACT_IMPORT / BENCHMARK | `p-certainty-of-evidence.fsh` etc. | design-specific profiles, calculators, DDI rule | yes: OPUS-014 |
| P08 | decision assurance | yes (mechanics) | commandMed spec006 + DAL | ORACLE_COPY / COPY | `spec006/{policy,registry,scaffold,trace}.py` + fixtures; DAL `metrics.py`, `p08_stats.py` | clinician policy content, state semantics | yes: OPUS-005/006 |
| P09 | calibration | yes (metrics) | DAL | COPY | `metrics.py`, `selective.py`, `p08_stats.py` + tests | estimand, invalidation, cost matrix | yes for any % UI: OPUS-007 |
| P10 | synthesis runtime, packs | yes | llama.cpp / mistral.rs; MedScale pack admission (minus key) | DEPEND / COPY | `medscale-pack/src/{format,store}.rs` | context compiler, post-verifier, TUF policy | yes: OPUS-004/013 |
| P11 | desktop | yes | Slint (MedScale) or Tauri | DEPEND | `medscale-desktop` patterns | clinician UX, Arabic/RTL measurement | yes: OPUS-018 |
| P12 | documents, OCR, critical numbers | yes | xberg (primary hypothesis) / docling.rs; SafeOCR | DEPEND / WORKER / ORACLE_COPY | `extractors/*`, `paddle_ocr`; `safeocr/verification.py` + tests | hostile-input composition, span normalization, Arabic numerals | yes: OPUS-011/013 |
| P13 | guidelines | partial | cqframework CQL-to-ELM; EBMonFHIR recommendation concepts | WORKER / REFERENCE | CQL translator | rights-feasible corpus, semantic verification research | yes: OPUS-015 |
| P14 | FHIR patient context | yes | MedScale `medscale-fhir` + OpenMed `interop/fhir` tests | COPY | `extractors/`, `lexical.rs`, `units/` | Medication*/Allergy extractors | no (OPUS-014 bound) |
| P15 | mobile foundation | yes | UniFFI; ottari protectors; OpenMed OpenMedKit parity tests | DEPEND / COPY | `vault_android_keystore.rs`, `vault_apple_keychain.rs`; `OffsetContractParityTest.kt` | backup/screenshot/notification policies | no |
| P16 | mobile Ask/Scan | yes | xberg Swift/JNI bridges; SafeOCR; P05 models | DEPEND / COPY | `packages/swift/rust`, `crates/xberg-jni` | device-qualified packs | no |
| P17 | pairing/sync | partial | Signthos (AGPL, relicense needed); iroh | COPY (after grant) / DEPEND | Signthos QR bootstrap code (VERIFY paths) | selective scope, revocation | yes: OPUS-002 |
| P18 | Deep Review | partial | ASReview models; SYNERGY; statsmodels; ES3 data; EBMonFHIR search/inclusion extensions | WORKER / DEPEND / BENCHMARK | `asreview/models`, `learner.py`; `meta_analysis.py` | unit-of-analysis rules, refusal logic, stopping, PRISMA accounting | yes: OPUS-009 |
| P19 | voice | yes | sherpa-onnx / whisper.cpp; ottari `capture_*` | DEPEND / COPY | ottari `himsat-core/src/capture_*.rs` | medical ASR evaluation | no (deferred) |
| P20 | SafeEvidenceBench | partial | DAL harness; BEIR; SciFact; SYNERGY; SafeOCR LabGold pattern | COPY / BENCHMARK | DAL `gaxbench`, SafeOCR `labgold.py`, `evaluation.py` | clinician holdouts, Arabic sets | yes: OPUS-019 |
| P21 | privacy/security qualification | yes | MedScale `privacy_probes.rs`, `os_sandbox/*`; ottari spill tests; kernux policy | COPY | `privacy_probes.rs`; Landlock/seccomp/AppContainer compositions; `b306_plaintext_spill.rs` | residual surfaces (OPUS-028) | no |
| P22 | release/update | partial | tough or rust-tuf (QUALIFY); MedScale `release_sbom.rs` | DEPEND / COPY | `medscale-core/src/release_sbom.rs` | offline TUF policy, key ceremony | yes: OPUS-004 |
| P23 | claims/publication | yes | DAL claim ledger | COPY | DAL `tools/build_sg000023_paper_evidence.py` pattern | product claims registry | no |

### 4.1 Phases that still say "build X" where ready authorized code exists

1. **P02** "encrypted metadata/blob prototype; key provider; backup/restore" → ottari `himsat-core` vault is stronger than the designated MedScale donor (OPUS-003).
2. **P03** "PubMed/NCBI metadata adapter; PMC adapter; source deduplication" → xberg/docling.rs JATS extractors; ES3 `ecitmatch_tools.py`; ASReview record dedup utilities (OPUS-010, -023).
3. **P04** "medical terminology normalization" → OpenMed `clinical/grounding/` (rights-gated).
4. **P06** "verifier benchmark" → SciFact evaluation code; Evidence-Inference splits.
5. **P12** "critical numeric verifier" → SafeOCR `verification.py` (plan wrongly says the repository is empty) (OPUS-011).
6. **P15** "Keychain/Keystore; encrypted local subset vault" → ottari platform protectors (OPUS-021).
7. **P18** "source inclusion/exclusion, search record" → EBMonFHIR `ext-research-study-{search-strategy,included-study,excluded-study,number-of-studies-*}` concept model; ASReview models (OPUS-008, -023).
8. **P20/P23** "claims registry, frozen evaluation" → DAL claim-ledger and SafeOCR frozen-split tooling (OPUS-019).
9. **P02/P03 rights** "item-level rights" → OpenMed `terminology_licenses.py` / `data_license_gate.py` (OPUS-025).

## 5. Greenfield judgment

Subsystems where this review finds `GREENFIELD_JUSTIFIED` defensible (no suitable ready implementation found):

1. Public-plane / private-vault boundary contract and snapshot-as-identities (OPUS-001, -016)
2. Thin internal Study/Arm/Analysis/EffectEstimate schema (concepts copied from EBMonFHIR) (OPUS-008)
3. Clinician-role decision policy content and state lattice (mechanics copied) (OPUS-005)
4. Claim-support facet policy and deterministic numeric/unit checker integration (OPUS-017)
5. Unit-of-analysis and pooling-refusal rules (OPUS-009)
6. PubMed XML lifecycle → current-validity overlay mapping and bulk downloader glue (OPUS-010)
7. Arabic normalization module and cross-language retrieval verification (OPUS-012)
8. Small deterministic clinical calculator set (OPUS-026)
9. Guideline semantic-verification research lane (OPUS-015)
10. Clinician workstation UX and SafeEvidenceBench content (already declared SafeEvidence-specific)

## 6. Requested reconciliation actions (not applied here)

This review deliberately does **not** edit authority documents. Reconciliation with the independent Codex review must happen first (`GAP_REVIEW.md` §7). Minimum edits proposed for reconciliation:

1. Data-plane decision record (OPUS-001).
2. Donor-rights register; reclassify trialstreamer, robotreviewer and Signthos; amend `AGENTS.md` and `COPY_FIRST_SOURCE_PLAN.md` §1 (OPUS-002).
3. Vault bake-off replacing "MedScale vault COHERENT_COPY" (OPUS-003).
4. Correct SafeOCR status in `SOURCE_LEDGER.md`, `FOUNDATION_GAP_AUDIT` SE-G008 and `MASTER_PLAN.md` P00A (OPUS-011).
5. State-semantics decision record (OPUS-005); record DAL Study-0 as prior evidence (OPUS-006); "no percentage in V1" rule (OPUS-007).
6. Study/Arm/Analysis contract additions before P02 (OPUS-008).
7. Runtime budget rows for inference runtimes (OPUS-013).
8. Mark the desktop shell as `OPEN_CONFLICT` (OPUS-018).
9. Downgrade `PREBUILD_KILL_REVIEW` readiness rows (OPUS-030).
10. Founder decision on disclosure of the non-public guideline donor's name (OPUS-015).

## 7. Summary

| Item | Value |
|---|---|
| Reviewed SHA | `136cdffc2cd14133e01018ca56833241dd50bc4e` |
| Artifact | `docs/reviews/OPUS_P00_INDEPENDENT_KILL_REVIEW_2026-10-07.md` |
| P0 | 2 |
| P1 | 17 |
| P2 | 12 |
| P3 | 3 |
| Greenfield subsystems judged justified | 10 |
| Planned subsystems where better ready code was found | 8 (vault → ottari; critical OCR verifier → SafeOCR; JATS/PubMed parsing → xberg/docling.rs; rights gates → OpenMed; Study/evidence concepts → EBMonFHIR; mobile key custody → ottari protectors; mobile span parity → OpenMed OpenMedKit; multilingual retrieval → fastembed-rs BGE-M3) |
| Final verdict | **`P00_NOT_READY`** |

This review makes no claim that SafeEvidence is clinically safe, validated, compliant, release-ready, or superior to any other product.
