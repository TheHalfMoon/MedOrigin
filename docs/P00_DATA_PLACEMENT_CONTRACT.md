# P00 Data Placement and Corpus Contract

Status: P00_BINDING_CONTRACT
Owners: architecture, privacy/security and evidence-rights.
Resolves planning detail for CODEX-P00-01 and OPUS-P00-001.

## Invariants

Separate a public, rights-admitted, rebuildable and integrity-verified evidence
store from the encrypted private authority. Public visibility is NOT permission
to redistribute. Private query-derived indexes inherit private classification.
Historical proofs store source identities/digests and cannot silently substitute
a newer document or a missing licensed byte.

## Per-object placement

| Object | Store | Backup/export/sync | Deletion and references |
|---|---|---|---|
| Public citation metadata | Public versioned corpus | Export per metadata terms; rebuildable | Tombstone versions; reference immutable IDs |
| Public abstracts/full text | Item-rights-admitted public cache/pack | Export only if item rights explicitly allow | Purge bytes/index on rights change; keep permitted digest |
| Institution-licensed content | Encrypted rights-scoped private content store | Only while institution/user grants permit | Revoke bytes and derived caches; preserve minimal lawful tombstone |
| User PDF and OCR intermediate | Encrypted private document store | Encrypted backup; explicit private export | Delete source/derived data; best-effort OS limits disclosed |
| Patient and question/history | Encrypted private authority | Encrypted authorized export only | Scoped retention/deletion; never in public packs |
| Private query embeddings/rank caches | Encrypted private projection | Excluded from normal backup; recompute | Delete with originating query/source |
| Global FTS/vector index | Rights-admitted public rebuildable projection | Rebuild or transfer if redistribution allowed | Remove restricted/retracted bytes from active search |
| Signed model/evidence/terminology pack | Immutable verified pack store | Share only if every bundled component permits | Tombstone or revoke pack; digest retained |
| EvidenceSnapshot | Encrypted private manifest | Rights-aware, encrypted export | Original bytes optional; missing/revoked -> PARTIAL_REPRODUCTION |
| AnswerArtifact and AnswerProofManifest | One encrypted private transaction | Encrypted, explicitly authorized only | Historical proof immutable; overlay warns current invalidity |
| Retraction/correction overlay | Public verified metadata store | Rebuildable | Monotonic validity epoch; re-check on view/export |

## Cross-store lifecycle

No unsupported claim of an atomic distributed transaction across public and
private stores. Public packs are immutable by digest/version. Private proof
references SourceId, content_digest, rights_version and validity_epoch.

An ingest/change crossing stores uses an idempotent durable intent/outbox with
PREPARED/ADMITTED/FAILED and restart replay. Proof admission rechecks immutable
source identity, rights and current-validity watermark before its private commit.
A racing update fails or invalidates current assurance. Historical answers do
not silently change; unavailable content yields PARTIAL_REPRODUCTION.

Rights admission is checked at ingestion, indexing, pack-build, export, backup,
sync send and sync receive. Unknown, expired or denied grants fail closed.
Deletion/GC honors scope/retention and tracks permitted tombstone metadata.

## Default evidence corpus gate

V1 starts from a bounded, rights-admitted curated scope for population-level
clinician evidence questions, NOT entire PubMed. P01 product owner must select
the supported specialties/question classes and corpus admission rule; P03 must
measure count, bytes, update cost, local index/model size, builder ownership and
distribution economics BEFORE promoting the first pack. No invented size
target is certified in this planning document. Shipped offline evidence search
must not cause hidden model/corpus download.

## Acceptance fixtures

Trace a public record, institutional article, user PDF, PHI context, query
embedding and saved proof through ingest/index/backup/export/sync/revocation.
Assert no private/restricted byte enters public packs, no non-admitted export,
correct durable outbox replay, and partial reproduction if licensed bytes vanish.
