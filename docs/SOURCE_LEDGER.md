# MedOrigin Source Ledger

Status: `FOUNDATION_DRAFT`

This ledger defines the candidate source universe for MedOrigin. Inclusion is not adoption authority. A source becomes adoptable only after the exact revision, exact paths/artifacts, controlling terms/permission, embedded dependencies, notices, modifications, security placement, tests, update strategy, and exit strategy are recorded.

## 1. Adoption modes

```text
COPY_BOUNDED     Copy the minimum useful implementation/test/rule slice with provenance.
ADAPT            Use a donor as a close implementation basis behind MedOrigin-owned contracts.
PORT_TO_RUST     Reimplement bounded behavior/contracts/tests in Rust while preserving provenance.
DEPEND           Use a pinned upstream dependency.
VENDOR           Store an immutable source/runtime snapshot after explicit justification.
FFI              Use a native library behind a narrow Rust-owned ABI/lifetime/error boundary.
WORKER           Run a dependency/model/parser in a constrained local process.
ARTIFACT_IMPORT  Admit immutable model/evidence/terminology artifacts through a verified Pack path.
REFERENCE        Study behavior, architecture, tests, UX, or research; do not inherit runtime authority.
BENCHMARK_ONLY   Use only as a comparator/evaluation input.
REJECT_DEFAULT   Do not adopt as default architecture unless later evidence reverses the decision.
```

Permission expands what is legally/contractually possible; it does not determine the correct architecture.

## 2. Founder-owned / sibling repositories — primary public sources

The following public repositories are the strongest internal sources discovered during the MedOrigin foundation review.

| Source | MedOrigin candidate value | Default mode |
|---|---|---|
| `TheHalfMoon/MedScale` | primary evidence architecture; source identity; rights-aware acquisition; claim-support verification; Packs; local-first privacy; FHIR/interoperability patterns; evidence evaluation protocol | `ADAPT / COPY_BOUNDED / PORT_TO_RUST / REFERENCE` |
| `TheHalfMoon/DAL` | decision assurance; explicit commit-vs-abstain semantics; calibration/selective-risk metrics; MedQAbstain work; typed decision baselines; negative-result discipline | `ADAPT / COPY_BOUNDED / BENCHMARK_ONLY` |
| `TheHalfMoon/commandMed` | deterministic patient-safety state machine; `ANSWER/ASK_MORE/USE_TOOL/RETRIEVE_EVIDENCE/ABSTAIN/ESCALATE/EMERGENCY`; tool-over-generation precedence; medical evaluation discipline | `ADAPT / COPY_BOUNDED / REFERENCE` |
| `TheHalfMoon/MESC` | medical model/evidence research governance; exact model identity; resource-first qualification; abstention/uncertainty contracts; immutable corpus snapshots; evaluation discipline | `REFERENCE / COPY_BOUNDED` |
| `TheHalfMoon/Morize` | temporal truth, contradiction/supersession, evidence graph, explainable recall, rebuildable indexes, typed promotion decisions | `ADAPT / COPY_BOUNDED / REFERENCE` |
| `TheHalfMoon/ottari` | Rust-first local desktop/mobile architecture; document IR; evidence refs; OCR/document boundaries; capture/voice; local model runtime isolation; vault/search/sync patterns; broad donor registry | `ADAPT / COPY_BOUNDED / REFERENCE` |
| `TheHalfMoon/kernux` | capability kernel; permission-before-power; explicit local/remote boundaries; replay/evidence; provider-neutral workers; no silent cloud fallback | `ADAPT / COPY_BOUNDED / REFERENCE` |
| `TheHalfMoon/Signthos` | Tauri/native desktop-mobile boundary; mobile capture; secure local storage; QR pairing/handoff security; offline queue semantics | `ADAPT / COPY_BOUNDED / REFERENCE` |
| `TheHalfMoon/Wispral` | future voice interaction; interruption/steering; command-vs-context semantics; local speech evaluation methodology | `REFERENCE / COPY_BOUNDED` |
| `TheHalfMoon/Inercative` | CLM research; deterministic-vs-decision-vs-generative routing; source-adoption discipline; qualification harness patterns | `REFERENCE / COPY_BOUNDED` |
| `TheHalfMoon/Ecra` | browser/search/agent capability routing and execution-receipt patterns when governed external evidence acquisition is added | `REFERENCE` |
| `TheHalfMoon/Sentrdel` | security evidence/control-plane patterns; stable schemas; evidence adjudication | `REFERENCE / COPY_BOUNDED` |
| `TheHalfMoon/SpecGrain` | recursive bounded planning, explicit readiness, WorkPackets, evidence-first execution | `PROCESS_REFERENCE` |
| `TheHalfMoon/Diffcipline` | proof-before-done change discipline and exact-change verification | `PROCESS_REFERENCE` |
| `TheHalfMoon/Delethos` | bounded delegation and proof-carrying change patterns | `REFERENCE` |

### Private sibling sources

Authorized private repositories were inspected during founder review. Because MedOrigin is public, this public ledger intentionally does **not** disclose private repository names or private file paths without separate explicit authorization for public disclosure. If a private source is selected for implementation, its exact identity and permission basis must be recorded in a non-public founder-controlled provenance record or disclosed here only after explicit authorization.

## 3. Primary evidence/discovery sources

These are candidate source adapters, not bundled content rights.

| Source | Candidate role | Default mode |
|---|---|---|
| PubMed / NCBI | biomedical bibliographic discovery, PMID identity, metadata | `DEPEND/API_ADAPTER` |
| PubMed Central | open/full-text evidence where article-level rights permit | `DEPEND/API_ADAPTER` |
| Crossref | DOI metadata, citation identity, correction/retraction metadata | `DEPEND/API_ADAPTER` |
| OpenAlex | optional discovery/graph metadata; not clinical authority | `DEPEND/API_ADAPTER / REFERENCE` |
| ClinicalTrials.gov | structured trial discovery and candidate matching | `DEPEND/API_ADAPTER` |
| publisher/guideline metadata | authoritative version/correction/jurisdiction metadata where terms permit | `ADAPTER` |
| user-provided local documents | local evidence ingestion subject to user rights and policy | `CORE_INPUT` |
| institution-owned guidelines/protocols | institution-scoped local evidence packs | `CORE_INPUT` |

Source access and content redistribution are separate decisions. A public URL is not a redistribution license.

## 4. Medical standards and terminology

| Source | Candidate role | Rule |
|---|---|---|
| HL7 FHIR R4 4.0.1 | primary interchange reference | `REFERENCE`; MedOrigin keeps its own canonical authority model |
| SMART on FHIR | future read-only connector/auth reference | separately qualified adapter |
| CQL / CPG-on-FHIR | computable guideline/evidence logic reference | verification-first; no compilation-equals-correctness assumption |
| NPHIES | Saudi interoperability reference where applicable | exact profile/version and deployment authority required |
| SNOMED CT | terminology pack | rights/version/checksum controlled; never assumed redistributable |
| LOINC | terminology/lab identity pack | rights/version/checksum controlled |
| UCUM | units and numeric normalization | versioned deterministic tooling |
| ICD | coding/interchange reference | edition/rights controlled |
| ATC | medication classification reference | version/rights controlled |
| UMLS / Athena vocabularies | optional terminology mapping | user/institution license boundary |

## 5. Evidence/retrieval architecture candidates

MedOrigin owns retrieval contracts. Heavy RAG systems are references or optional workers, not default product authority.

| Source | Candidate value | Default mode |
|---|---|---|
| SQLite / FTS5 | canonical local metadata + lexical retrieval foundation | `DEPEND` |
| `Anush008/fastembed-rs` | local embeddings/reranking | `DEPEND` candidate; model rights separately |
| `asg017/sqlite-vec` | small local vector projection | `DEPEND` behind abstraction; maturity gate |
| Tantivy | higher-scale lexical index | `DEPEND` only after measured need |
| USearch | vector projection candidate | `DEPEND/FFI` only after benchmark |
| `langflow-ai/openrag` | ingestion/RAG architecture reference or isolated worker | `REFERENCE/WORKER`; not trusted core |
| Onyx | enterprise retrieval/search reference | `REFERENCE` |
| AnythingLLM | local knowledge/LLM UX reference | `REFERENCE` |
| Graphify | graph/context patterns | `REFERENCE` |
| code-graph-rag | graph retrieval patterns | `REFERENCE` |
| OpenSearch / Meilisearch | scale candidates | `REJECT_DEFAULT`; adopt only if local measurements justify server complexity |
| Qdrant / LanceDB | vector-service/storage candidates | `REJECT_DEFAULT`; no load-bearing server dependency without evidence |

Default V1 direction: scoped lexical retrieval + optional local embeddings + reranking, with indexes treated as sensitive rebuildable projections.

## 6. Decision assurance and calibration candidates

No candidate is trusted because it emits a probability. Every model is benchmarked under MedOrigin's own protocol.

| Source | Candidate role | Default mode |
|---|---|---|
| Decision 2.0 family | compact typed-choice/yes-no/score decision models; phone/desktop tournament candidate | `ARTIFACT_IMPORT / BENCHMARK_ONLY` until qualified |
| Laya | compact typed-decision baseline | `ADAPT / ARTIFACT_IMPORT / BENCHMARK_ONLY` |
| `Mapika/decider` | one-pass typed boolean/choice/score decision surface | `ADAPT / BENCHMARK_ONLY` |
| `Contrastive-LM/CLM` | contrastive state/action baseline | `BENCHMARK_ONLY / REFERENCE` |
| `ikermoel/open-alternative-jev` | restricted-logit/no-task-training control | `BENCHMARK_ONLY / REFERENCE` |
| TypeSafe Jev | optional black-box comparison when reproducible access/terms permit | `BENCHMARK_ONLY` |
| BioClinical ModernBERT family | clinical encoder control / specialized classifier candidate | `ARTIFACT_IMPORT / BENCHMARK_ONLY` |
| Qwen structured-output models | generative structured-output control | `ARTIFACT_IMPORT / BENCHMARK_ONLY` |
| `TheoLeeCJ/SemIf` | option-logit scoring/calibration patterns | `REFERENCE / COPY_BOUNDED` |

Required evaluation includes calibration, Brier/ECE/NLL where meaningful, risk-coverage, unsafe-commit rate, over-abstention, abstention precision/recall, distribution shift, and missing-information behavior.

## 7. Local generation and model runtimes

| Source | Candidate role | Default mode |
|---|---|---|
| ONNX Runtime | specialist/encoder/OCR runtime | `DEPEND/FFI` |
| `ggml-org/llama.cpp` | broad GGUF local inference | `DEPEND/VENDOR/FFI` candidate |
| `EricLBuehler/mistral.rs` | Rust-native local LLM inference | `DEPEND` candidate |
| Hugging Face Candle | Rust-native specialist runtime | `DEPEND` candidate |
| Burn | Rust-native inference/training comparator | `DEPEND` candidate |
| MLX / mlx-lm | Apple accelerator path | platform adapter only |

Model weights, tokenizer files, processors, and code libraries have separate identities and rights.

## 8. Documents, PDF, OCR and extraction

| Source | Candidate role | Default mode |
|---|---|---|
| `xberg-io/xberg` | Rust-first document extraction/IR/parser candidate | `DEPEND/ADAPT/COPY_BOUNDED` after security/maturity tests |
| historical Kreuzberg/Kreuzberg-LTS | historical document extraction implementation/research | exact-revision `REFERENCE/COPY_BOUNDED` only |
| `docling-project/docling.rs` | Rust document parsing candidate | `DEPEND` candidate |
| Docling / docling-core | layout/table/formula/document-IR quality | `WORKER/REFERENCE/COPY_BOUNDED` |
| PaddleOCR | scanned-document and multilingual OCR candidate | `WORKER/VENDOR` after Arabic medical benchmark |
| MinerU | document parsing quality/IR candidate | `REFERENCE/COPY_BOUNDED` subject to exact rights |
| MarkItDown | conversion UX/normalization/security reference | `REFERENCE/COPY_BOUNDED` |
| tokimo file parser | pure-Rust PDF/Office extraction candidate | `EXPERIMENT/DEPEND` |
| Magika | MIME/file classification candidate | `DEPEND` only if benchmarked |
| Presidio | PII/de-identification taxonomy/rules reference | `REFERENCE/COPY_BOUNDED` |
| medSpaCy | clinical NLP patterns/tests | `REFERENCE` |

The document boundary must quarantine hostile inputs and preserve source page/region/table coordinates. OCR output is advisory until admitted through validation. Critical numbers, decimal points, units, doses, negation, and laboratory values require dedicated verification tests.

## 9. Desktop, mobile, storage and local sync

| Source / technology | Candidate role | Default mode |
|---|---|---|
| Tauri 2 | desktop shell candidate | `DEPEND`, conditional on PHI/cache/crash/accessibility qualification |
| React/TypeScript | shared desktop UI where appropriate | product UI only; never authority |
| Swift / SwiftUI | iOS/iPadOS native surface and platform integrations | native client |
| Kotlin / Jetpack Compose | Android native surface and platform integrations | native client |
| SQLCipher | encrypted SQLite candidate | `DEPEND/FFI`; durability/key tests mandatory |
| OS Keychain/Keystore/secure credential APIs | key-wrapping/custody candidate | platform-specific qualification |
| `n0-computer/iroh` | optional authenticated local/P2P sync transport | `DEPEND` candidate; no silent public relay |
| QR bootstrap pattern from sibling work | short-lived authenticated local desktop-mobile pairing | `ADAPT`; QR never carries raw patient data or long-lived secrets |

Mobile must remain a native, scoped product rather than an identical desktop WebView.

## 10. Audio/voice — deferred but pre-registered candidate universe

Voice is not required for the initial evidence wedge. When promoted, candidates include:

- `k2-fsa/sherpa-onnx`;
- `ggml-org/whisper.cpp`;
- NVIDIA NeMo-Speech.cpp;
- Moonshine;
- OpenWhispr / OpenSuperWhisper;
- Meetily;
- Silero VAD / TEN VAD;
- WebRTC AudioProcessing / Sonora;
- DeepFilterNet / RNNoise;
- pyannote-audio;
- multilingual/Arabic and medical-specialized ASR challengers.

Speech model/runtime rights and device-specific performance must be qualified independently.

## 11. FHIR, imaging and scientific ecosystem references

- Medplum / HAPI FHIR — FHIR integration/reference comparators;
- Synthea — synthetic healthcare fixture generation;
- OHIF / Orthanc / dcm4che / dicom-rs — future imaging/DICOM path;
- OMOP tooling — research export/mapping candidate, not a second canonical clinical DB;
- DuckDB / Polars / Arrow / DataFusion — later research/data-workbench candidates, not evidence-core prerequisites.

## 12. Security, supply chain and sandbox candidates

- Extism / Wasmtime — optional bounded plugin/worker host only if a plugin need is proven;
- TUF/tough — offline-verifiable pack/update trust;
- sigstore-rs — optional attestation/signature path;
- cargo-deny / RustSec / OSV / cargo-vet / cargo-auditable — supply-chain evidence;
- Syft / Trivy — SBOM/artifact scanning where applicable;
- platform sandbox primitives — exact OS confinement must be demonstrated, not declared.

## 13. Competitive / behavioral references

These may guide product or evaluation but are not automatically code donors or evidence-content sources:

- OpenEvidence;
- Abridge;
- OpenMed;
- commercial clinical evidence products;
- commercial medical-scribe products;
- first-party OS health/document/mobile features.

Competitor behavior must not be reverse-engineered into unsupported clinical claims. Comparative evaluation requires matched dated conditions and explicit source-access differences.

## 14. Sources explicitly not chosen as default architecture

The following are not banned, but they must earn adoption through measured need:

```text
mandatory Qdrant/LanceDB server
mandatory Neo4j/GraphRAG server
mandatory PostgreSQL service
mandatory Docker/Kubernetes for end users
mandatory Python service fleet
mandatory OpenRAG/Onyx/AnythingLLM runtime
mandatory hosted inference
mandatory hosted auth
mandatory hosted telemetry
mandatory cloud synchronization
```

## 15. Source-admission record

Before copied/adapted/vendored/runtime material becomes canonical, create a record containing at least:

```text
source_name
source_repository_or_artifact_uri
exact_revision_or_digest
source_path_or_artifact_files
public_license
separate_permission_basis_if_used
permission_scope_if_used
embedded_or_transitive_material
model_dataset_asset_rights
copyright_notice_requirements
MedOrigin_target
adoption_mode
why_reuse_beats_native
security_trust_placement
network/filesystem/key capabilities
tests_and_benchmarks
modifications
update_strategy
rollback_or_exit_strategy
review_evidence
```

No "all source is permitted" statement overrides third-party/model/data/asset provenance or the requirement to bind the adopted bytes to an exact identity.