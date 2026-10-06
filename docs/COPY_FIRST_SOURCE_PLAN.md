# SafeEvidence Copy-First Source Plan

Status: `P00_BINDING`

## 1. Founder authorization

The founder has explicitly authorized SafeEvidence to copy, modify, combine,
adapt, vendor, and rebrand the source code from the source universe discussed
for this project.

This removes "do we have permission to copy the donor implementation?" as a
planning blocker for those authorized sources.

It does **not** erase obligations attached to embedded third-party code,
datasets, terminology, model weights, fonts, documents, or other separately
licensed material. Those remain tracked independently.

## 2. Engineering rule

SafeEvidence MUST NOT reimplement an already-good capability from scratch when
an authorized source already contains a usable implementation.

Default decision order:

```text
1. COPY coherent product-specific implementation
2. VENDOR a stable generic implementation when independence is desirable
3. DEPEND on a generic library when direct dependency is clearly lower-risk
4. ADAPT copied code behind SafeEvidence contracts
5. PORT only when a trust/platform boundary requires it
6. GREENFIELD only when no suitable ready source exists
```

"Cleaner to rewrite" is not a valid reason.

The objective is maximum reuse of proven implementation while avoiding
unnecessary donor-product coupling.

## 3. Copy styles

### A. COHERENT_COPY

Copy a complete, bounded implementation slice together with tests and fixtures.

Use for sibling-product code that SafeEvidence should own after import.

### B. VENDOR_SNAPSHOT

Import an upstream implementation under `third_party/` or an equivalent
vendored location at an exact revision.

Use when SafeEvidence wants deterministic ownership of the bytes without
rewriting them.

### C. DIRECT_DEPENDENCY

Use upstream as a pinned dependency when maintaining a copy would create more
work than value.

This still satisfies the founder's "do not start from scratch" rule because the
ready implementation is used unchanged.

### D. ORACLE_COPY

Copy reference implementation/tests into benchmark or compatibility tooling,
then implement only the minimal trusted-core adapter necessary.

### E. WORKER_COPY

Vendor/copy a specialist stack as an isolated local worker when porting it
would waste time.

## 4. Copy matrix — foundation

| Capability | Primary source | Observed head | Copy strategy | SafeEvidence destination |
|---|---|---|---|---|
| cryptographic key handling | `TheHalfMoon/MedScale` | `1e2b7d94e970256b38bda15fa91f62bc397e825a` | COHERENT_COPY | `crates/safeevidence-keys/` |
| SQLCipher vault | MedScale | same | COHERENT_COPY + strip unrelated schemas | `crates/safeevidence-vault/` |
| sealed blobs | MedScale | same | COHERENT_COPY | vault/storage modules |
| path claims / local custody | MedScale | same | COHERENT_COPY | vault/core |
| writer ownership | MedScale `writer_lock.rs` | same | COHERENT_COPY incl. cross-process tests | vault |
| migrations/restart integrity | MedScale | same | COPY selected migration framework/tests | vault |
| source identity | MedScale contracts | same | COHERENT_COPY + extend | `safeevidence-contracts` |
| evidence corpus contracts | MedScale | same | COHERENT_COPY + extend | contracts/evidence |
| network broker | MedScale | same | COHERENT_COPY | `safeevidence-network` |
| pack admission/signing | MedScale | same | COHERENT_COPY | `safeevidence-pack` |
| local ONNX specialist runtime | MedScale | same | COPY reusable runtime slice | pack/inference |
| FHIR R4 typed extraction | MedScale | same | COHERENT_COPY | `safeevidence-fhir` |
| lexical evidence baseline | MedScale | same | ORACLE_COPY | retrieval baseline |
| sandbox/privacy test patterns | MedScale + Kernux | `1e2b7d...` / `a0c4aaee...` | COPY tests/policies | security tests |

### Important MedScale rule

Do not copy the entire current MedScale workspace.

Copy the best **behavioral slice** from its qualified evolution. Current
MedScale contains unrelated product modules and schema history.

In particular, SafeEvidence should copy:

```text
medscale-keys
encrypted vault primitives
sealed blob storage
source/evidence contracts
writer_lock
network broker
pack admission/runtime
FHIR typed extraction
privacy/sandbox tests
selected durability/migration tests
```

and leave behind unrelated analytics, collaboration, audio, huddles, model
fleet, project graph, etc.

## 5. Copy matrix — clinical safety and decision assurance

| Capability | Source | Observed head | Strategy |
|---|---|---|---|
| deterministic safety state machine | `TheHalfMoon/commandMed` | `51f73ec05750137e5bd94ffa0765f6383f475fee` | ORACLE_COPY then bounded Rust adaptation |
| policy precedence | commandMed | same | COPY semantics + fixtures |
| ASK_MORE/ABSTAIN/ESCALATE/EMERGENCY behavior | commandMed | same | COPY tests + port only trusted runtime |
| calibration metrics | `TheHalfMoon/DAL` | `8fcf29f2e0c1b6cf78661acd2f5e1340a578ac03` | COPY Python benchmark code |
| Brier/ECE/NLL/selective risk | DAL | same | COPY unchanged where possible |
| unsafe-commit / over-abstain | DAL | same | COPY unchanged |
| decision-model tournament harness | DAL/Inercative/MESC | current pinned heads | COPY benchmark/eval infrastructure |
| typed decision model source | vLLM Semantic Router Decision family | current qualified pin at adoption | VENDOR/ARTIFACT_IMPORT candidate |

No reason exists to rewrite standard calibration formulas or benchmark harnesses.

## 6. Copy matrix — evidence NLP / grounding

| Capability | Source | Observed head | Strategy |
|---|---|---|---|
| clinical grounding | `maziyarpanahi/openmed` | `252806aa946c200f3857cc0f6fda37fd83a5cc85` | COPY bounded modules/tests |
| terminology candidate/ranking | OpenMed | same | COPY/ADAPT |
| terminology cache/provenance | OpenMed | same | COPY/ADAPT |
| Unicode/span projection | OpenMed | same | COPY tests + implementation |
| FHIR integrity/profile tests | OpenMed | same | COPY tests/adapters where useful |
| de-identification/PII testing | OpenMed | same | COPY selected code/tests |
| document/OCR adapter tests | OpenMed | same | COPY into qualification harness |
| scientific support benchmark | SciFact | exact pin at admission | COPY benchmark code/data subject to dataset terms |
| verifier oracle | MultiVerS | exact pin at admission | VENDOR/WORKER_COPY |

Do not copy OpenMed's entire service/cloud/orchestration dependency universe by
default. Copy the useful clinical algorithms and tests.

## 7. Copy matrix — documents and OCR

### Xberg

Observed head:
`42c03edd06964accd6f8b796fba1647da2b8121d`

Ready source includes native PDF/document extraction, PDFium path, OCR
integrations, FFI, Swift/Dart/JNI support, and broad document parsing.

Default:
`VENDOR_SNAPSHOT / DIRECT_DEPENDENCY`.

### docling.rs

Observed head:
`8aea8d543de832116ebb29436d9281bfe7e82d73`

Ready source includes document IR, converters, PDF pipeline, ONNX layout/OCR,
RAG/chunking, FFI and WASM surfaces.

Default:
`VENDOR_SNAPSHOT / DIRECT_DEPENDENCY`.

### Selection

SafeEvidence MUST NOT build a PDF parser, Office parser, layout engine, table
extractor, or OCR framework from scratch.

Run Xberg vs docling.rs qualification. Copy/vendor the winner as the default
document engine. Preserve the second only as a challenger/fallback if evidence
justifies it.

PaddleOCR can be copied/vendored as an OCR backend where it wins medical/Arabic
fixtures.

## 8. Copy matrix — retrieval

| Capability | Ready source | Strategy |
|---|---|---|
| lexical storage/search | SQLite FTS5 | DEPEND |
| larger lexical engine | Tantivy | DEPEND or VENDOR |
| embeddings/rerank runtime | `fastembed-rs` @ `29059745...` | DEPEND or VENDOR |
| biomedical retriever/reranker | NCBI MedCPT @ `11e129be...` | ARTIFACT/CODE COPY for qualification/runtime subject to model terms |
| vector projection | sqlite-vec / USearch | DEPEND/VENDOR |
| retrieval benchmark | BEIR | COPY benchmark harness/datasets per terms |

No vector database is built from scratch.

## 9. Copy matrix — Deep Review

| Capability | Source | Strategy |
|---|---|---|
| active-learning screening | ASReview @ `79d568...` | COPY/WORKER_COPY |
| screening benchmark | SYNERGY | COPY benchmark data per terms |
| dedup/screening workflow ideas | ASReview | COPY/ADAPT |
| systematic review audit trail | SafeEvidence-specific | build only missing integration semantics |

SafeEvidence should not rebuild generic active-learning screening.

## 10. Copy matrix — mobile

| Capability | Source | Strategy |
|---|---|---|
| Rust↔Swift/Kotlin bindings | UniFFI @ `bc9fb385...` | DEPEND or VENDOR |
| mobile security contracts | MedScale | COPY |
| QR pairing threat model/patterns | Signthos @ `f945f12...` | COPY/ADAPT |
| platform architecture patterns | ottari @ `b7948b5...` | COPY/ADAPT |
| iOS/Android document bridge ideas | Xberg | COPY/REFERENCE |

Do not hand-write two complete FFI layers if UniFFI qualifies.

## 11. Copy matrix — guidelines and evidence standards

| Capability | Source | Strategy |
|---|---|---|
| guideline verification semantics | ProtocolWISE | COPY/ADAPT |
| CQL translation/conformance | `cqframework/clinical_quality_language` @ `c41c21...` | VENDOR/WORKER_COPY |
| evidence interoperability | HL7/EBMonFHIR | COPY schemas/examples as reference/export mappings |
| FHIR patient context | MedScale + OpenMed tests | COPY |

SafeEvidence owns the simplified internal model; it does not reimplement CQL
tooling.

## 12. Copy matrix — updates/security

| Capability | Source | Strategy |
|---|---|---|
| TUF update semantics | TUF spec/conformance suite | COPY tests/spec fixtures |
| Rust implementation candidate | awslabs/tough @ `98d8eb...` | VENDOR/DEPEND after qualification |
| capability/no-silent-egress patterns | Kernux @ `a0c4aa...` | COPY bounded policy/tests |
| release/SBOM patterns | MedScale/sibling repos | COPY workflows/scripts |

Do not implement a custom secure updater protocol.

## 13. What SafeEvidence still has to build

Copy-first does **not** mean there is no original engineering.

SafeEvidence-specific integration remains:

- the canonical Evidence/Claim/Answer semantic model;
- item-level evidence rights policy;
- PubMed/PMC/Crossref/Europe PMC update lifecycle;
- query decomposition and PICO/PICOTS orchestration;
- exact clinical claim↔evidence support policy;
- contradiction resolution/presentation;
- evidence quality vs patient applicability separation;
- calibrated commit/abstain semantics;
- current-validity overlay over immutable historical answers;
- clinician workstation UX;
- Arabic/English medical benchmark suite;
- SafeEvidenceBench;
- product-level integration, packaging and qualification.

These are the areas where new code is justified.

## 14. Mandatory agent behavior

Before an agent writes more than trivial glue code, it must answer:

```text
WHAT READY SOURCE ALREADY IMPLEMENTS THIS?
WHAT EXACT FILES/CRATES CAN BE COPIED?
WHY ARE WE NOT COPYING THEM?
```

If the first two answers identify a good implementation, copying/adapting it is
the default action.

## 15. P00 closure condition

P00 cannot close until Codex and Opus independently verify that:

- every P01-P15 major capability has a copy/vendor/dependency source where one
  exists;
- there is no generic subsystem scheduled for greenfield work while an
  authorized good implementation exists;
- copy boundaries avoid importing unrelated donor-product architecture;
- donor tests/fixtures are included in the copy plan;
- third-party nested terms are tracked separately;
- every truly greenfield component is SafeEvidence-specific.
