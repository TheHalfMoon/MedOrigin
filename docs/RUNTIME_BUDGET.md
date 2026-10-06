# SafeEvidence Runtime Budget and Anti-Sprawl Policy

Status: `P00_BINDING`

## 1. Purpose

SafeEvidence is a local clinical evidence product, not a fleet of overlapping
frameworks. The default release must remain understandable, installable,
auditable, and usable on ordinary clinician hardware.

## 2. One-primary-engine rule

For each production capability, SafeEvidence admits at most one primary engine
in the default build:

| Capability | Default shape |
|---|---|
| lexical search | one local index engine |
| vector projection | one local vector backend |
| embeddings | one admitted default model/runtime |
| reranking | one admitted default model/runtime |
| document parsing | one primary document engine |
| OCR | one primary OCR route plus a justified fallback only |
| decision assurance | one promoted decision model plus deterministic baseline |
| synthesis | one promoted local generator per hardware class |
| mobile FFI | one binding strategy |
| device sync transport | one transport if P17 is promoted |

Challengers live in qualification tooling until they win a defined benchmark.

## 3. No service-fleet default

The supported local installation must not require:

- Docker;
- Kubernetes;
- Postgres;
- Qdrant;
- Neo4j;
- Redis;
- a Python daemon fleet;
- a Java server;
- cloud auth;
- cloud vector storage;
- remote inference.

A specialist worker may be admitted only when a measured requirement cannot be
met more simply.

## 4. Sequential model loading

CPU/RAM-limited devices should load specialist models sequentially where
possible. The design must not require generator + reranker + OCR + multiple
decision models resident simultaneously.

## 5. Desktop baseline

The desktop architecture is optimized first for a CPU-only 16 GB-class machine.
Exact latency/RAM/disk targets are frozen after measurement, not invented in
planning.

Hard planning constraints:

- useful offline path;
- no GPU requirement;
- bounded cancellation;
- disk-full/OOM fail safely;
- model and evidence packs are optional/selective;
- no hidden download on first clinical question.

## 6. Mobile baseline

Mobile carries a selected evidence/model subset, not the complete desktop
corpus. Native shells remain SwiftUI and Kotlin/Compose candidates over one
shared Rust semantic core.

A large desktop model is never assumed to fit mobile.

## 7. Python and Java

Python remains acceptable for benchmarks, research or isolated workers.
Java remains acceptable for standards conformance/validation workers such as
CQL tooling.

Neither is a mandatory always-running runtime in the default application
without a separately qualified need.

## 8. Candidate promotion

Every competing engine must report at least:

```text
correctness/task metric
latency
peak RSS
disk/artifact size
startup cost
platform support
license/redistribution
failure behavior
offline behavior
security/trust placement
```

Winner selection is workload-specific.

## 9. Removal is a feature

Every optional engine or worker must have an exit strategy. SafeEvidence must be
able to remove a donor/runtime without rewriting canonical evidence records.
