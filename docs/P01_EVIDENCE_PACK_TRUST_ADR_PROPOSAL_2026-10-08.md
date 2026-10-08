# SafeEvidence — Proposed Evidence-Pack Trust Design (NOT APPROVED)

Date: 2026-10-08. State: **P01_ADR_PROPOSAL_ONLY**.
Approval issue: https://github.com/TheHalfMoon/SafeEvidence/issues/5
Original gates: CODEX-P00-08, OPUS-P00-004. First use: P10.

Normative reference under consideration:
https://theupdateframework.github.io/specification/v1.0.36/
This is a *reference*, not an imported codebase or deployed protocol.

## Proposed direction — requires release/security owner signature

Use an existing, pinned and qualified TUF implementation (candidate
`tough` or `rust-tuf`) through a bounded SafeEvidence adapter, NOT a
homemade cryptographic update protocol. Exact code, maintenance, conformance
and third-party rights must be evaluated before dependency admission.

Top-level Root, Timestamp, Snapshot and Targets metadata each have defined
keys, thresholds, expiry and monotonic versions. Keep signed app releases and
evidence-pack trust domains **separately versioned**, with a human-invoked
offline import channel, an immutable shipped first-install root, no silent
network retrieval, and independent source-content rights admission.

| Unapproved decision | Proposed safe default | Mandatory failure case |
|---|---|---|
| Root key custody | Offline multi-key threshold; named operator | Wrong root, duplicate signature, insufficient old/new rotation threshold |
| Targets | Hash, size, version and rights/provenance link for each artifact | Missing/wrong target, malicious digest, identity swap |
| Snapshot and Timestamp | Monotonic versions, consistent snapshots and expiry | Rollback, freeze, mix-and-match, stale timestamp |
| Offline time | Record clock provenance, distrust rollback and fail closed on unknown freshness | Clock rollback, absent trusted time, expired offline metadata |
| First installation | Bundled trusted root, no automatic network bootstrap | Substituted root, unsigned local package |
| Application and pack split | Separate trust metadata and rights validity | Signature-valid but revoked data rights: deny use |
| Import transaction | Verify full target before atomic durable activation | Interrupted copy, disk-full and crash leave old pack intact |
| Compromise and removal | Explicit key/target revocation and local tombstones | Compromised signer or removed evidence not marked current |
| Diagnostics | No patient data, source article text or file paths in logs | Synthetic canary leakage |
| Distribution | No mandatory paid services, accounts or cloud dependencies | Cold offline launch performs zero egress |

Authenticated bytes are **not** evidence of source availability, permitted
text rights, clinical truth, applicability, or answer commitment.
A signature must never imply `SAFE_TO_COMMIT`. Answers still require
the separate atomic proof admission and clinical policy gates.

## Required before approval

1. Appoint a release/security owner and actual root-key custodians.
2. Pin, read and license-audit selected TUF client code/dependencies,
   compare offline API behavior, negative fixtures and maintenance.
3. Approve root/targets/timestamp/snapshot thresholds and expiry policy.
4. Test expired/rollback/mix-match/freeze/replay, compromised key, missing
   clock, partial import and known rights revocation (Windows and Linux).
5. Keep any developer/synthetic keys out of release artifacts.
6. Record exact approver, signed decision revision, credential custody,
   trust failure reason codes, update/remove owner and incident runbook.

**No signature keys have been created, no pack verifier implemented,
no source rights admitted, no TUF library adopted and no product release
authorized by this proposal.** P01-G01 remains PREPARED_NOT_ACTIVATED
until the original named approval/clinical-resource gates are satisfied.
