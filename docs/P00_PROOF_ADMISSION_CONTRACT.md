# P00 Atomic Answer Proof Admission Contract

Status: P00_BINDING_CONTRACT
Owners: trusted-core architect and clinical safety.
Blocking lineage: CODEX-P00-06.

## Immutable input and states

Candidate->Verified->Committed is NOT a rendering status shortcut.
State machine:

DRAFT_PRIVATE -> CANDIDATE_FROZEN -> VERIFYING ->
 VERIFIED_UNCOMMITTED -> COMMITTED
or VERIFYING/VERIFIED_UNCOMMITTED -> REJECTED.
A previously committed answer can subsequently be
CURRENTLY_INVALIDATED or CURRENTNESS_UNKNOWN while its historical bytes and
audit manifest remain unchanged.

DRAFT_PRIVATE and failed verification are never persisted/displayed in the
same user-visible "assured answer" surface as COMMITTED. If streamed, drafts
must be clearly segregated as UNVERIFIED and cannot trigger clinical-copy/
export/share actions; safest V1 default is to withhold draft clinical claims.

## Proof manifest requirements

AnswerProofManifest binds a stable question/context snapshot, ordered
material claim IDs and **final rendered text digest**, exact source bytes
and versions, evidence spans and coordinates, study/result identities,
rights-grant version, last known local current-validity epoch, retriever/
reranker/translator/OCR/verifier/generator/tool versions, prompts/policy/
threshold identity, applicability, contradiction, decision reason/outcome,
post-answer verification result, and verification time.

Proof does not claim to know changes to an offline external repository beyond
its last downloaded watermark. Display SOURCE_FRESHNESS_UNKNOWN when that
watermark is out of qualified scope.

## Atomic commit

1. Freeze candidate claims/text and source identity digests.
2. Verify **final** displayed claims against admitted exact spans and
   deterministic numeric/unit/negation facets. Invalid claims are rejected
   or cause a new candidate and full verification; no silent repair.
3. Read the local rights/validity authority watermark and verify every
   admitted source/rights grant at that watermark.
4. Enter one private authority transaction; compare verified watermark and
   source/rights references with the latest locally admitted epoch.
5. Atomically store final answer bytes, AnswerProofManifest, per-claim outcomes
   and an immutable audit event in the SAME transaction. Return COMMITTED only
   after the durable commit boundary.
6. Expose the answer on an assured UI surface only after durable acknowledgement.
   A failed/unknown transaction remains non-committed until recovery confirms.

The public store and private DB are different planes; this protocol does NOT
claim global 2PC. New public validity updates use a monotonic, durable local
epoch transition. If the epoch races the private commit, either fail admission
before commit or immediately mark the resulting proof currently invalidated
before any **current assured** display; recheck on view/export/sync/resume.
The historic commit is always scoped to its local captured epoch.

## Crash, revocation and replay

A worker crash or verifier timeout before COMMITTED leaves only private
rejected/staging records, never an assured answer. Incomplete proof intents
have idempotency keys; restart reconciles with durable authority.

If rights expire, source is corrected/retracted/deleted, model/pack is revoked,
or content is no longer accessible, keep historical hash/claim lineage as
permitted but show CURRENTLY_INVALIDATED, SOURCE_UNAVAILABLE or
PARTIAL_REPRODUCTION. Never silently replay cached answer as currently
supported. Mobile replicas carry source epoch and must requalify freshness.

## Required adversarial proof tests

- Retraction/revision arrives between retrieval, verification and commit.
- License grant revoked just before/after commit.
- Worker crashes while rendering and after DB commit before UI notification.
- Source content version changes after candidate freeze.
- One supported and one unsupported material claim.
- Offline stale pack, cached replay, sync to revoked mobile device.
- Failed encrypted transaction/disk full -> no COMMITTED UI state.
- Idempotent recovery never commits two differing texts under one proof ID.

This is a contract for implementation/testing, not a claim of existing
production atomicity.
