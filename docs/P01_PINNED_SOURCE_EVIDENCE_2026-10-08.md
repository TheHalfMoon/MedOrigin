# SafeEvidence — P01 Pinned Donor Source Evidence

Observed 2026-10-08. Status: **DISCOVERY_ONLY / NO_ADMISSIONS**.
Rights decision owner: https://github.com/TheHalfMoon/SafeEvidence/issues/5

This is neither a legal opinion nor a reviewed import allowlist. Source root
LICENSE observations do not establish exact file/contributor, transitive,
model, journal, native dependency or asset terms. File identities below are
**Git blob OIDs, not raw file SHA-256 hashes**. An authorized rights signer,
content-digest verification, NOTICE/SBOM, exact feature closure, copy tests,
update owner and exit plan remain mandatory.

| Repository @ inspected commit | Root LICENSE observed | P01 reuse candidate |
|---|---|---|
| [MedScale](https://github.com/TheHalfMoon/MedScale/tree/37f5ae8a965c1e49d961010c3135a5b5dde12d67) | Apache-2.0; Rust 2024 workspace | CycloneDX SBOM, Rust CI |
| [ottari](https://github.com/TheHalfMoon/ottari/tree/73706029849bcbe51243624e37f03a1969dc74ca) | Apache-2.0; Rust 1.98.1 workspace | Provenance/native component checks, CI |
| [Kernux](https://github.com/TheHalfMoon/kernux/tree/2085b6ed1121b1a94c66c076bdd6b578da4dad0d) | Apache-2.0 | Rust CI/quality contracts |
| [Ascout](https://github.com/TheHalfMoon/Ascout/tree/ca6b6f514e5a8881e2cfa2789b5e5ea43e3aaaad) | Apache-2.0 | Exact-head clean-tree verification |
| [MESC](https://github.com/TheHalfMoon/MESC/tree/f9b7579189b77b06379d1a71d104d4b0267cf500) | Apache-2.0 | Typed source provenance and tests |

## Candidate exact file identities (Git blob OIDs)

| Source | Path | Blob OID |
|---|---|---|
| MedScale | `crates/medscale-core/src/release_sbom.rs` | `97f5165b20db16f1bd3212e594ba8fa672e8300f` |
| MedScale | `crates/medscale-core/tests/release_sbom_054.rs` | `79bb1bfbfc99bc470227d5deef96e72b73501f06` |
| MedScale | `scripts/generate-release-sbom.ps1` | `5c0db999609c89bcca583099a2f36fd6bd80848e` |
| MedScale | `.github/workflows/ci.yml` | `0e13351067c2070045a2b816ebf0c3a8c7fe9f82` |
| ottari | `tools/provenance.py` | `a36568be1b789a34222de76fd25e88f13a768332` |
| ottari | `tools/provenance_gate.py` | `8dffa32146529bbdd3e3026a0fceff4bce58c24e` |
| ottari | `.github/workflows/ci.yml` | `9224672e49022c85d217cb06de7a40ba54274a13` |
| kernux | `.github/workflows/ci.yml` | `372e34bf2591d9885d09888c4eb1e291455019b6` |
| Ascout | `.github/workflows/self-verify.yml` | `fffb70fa00b8152063e7ad9b3062988d6b0c04c2` |
| MESC | `src/medscale/provenance.py` | `242aad5871261bdb242977e11bfb4b680209379d` |
| MESC | `tests/test_provenance.py` | `b5da9a4a5d8d2de7dc3d50ff3ff9463611b9dfe3` |

## Byte-level SHA-256 observations (independently computed, not approvals)

Decoded GitHub blob bytes were inspected using `gh api` and SHA-256
computed in the local Windows PowerShell environment on 2026-10-08.
These are content digests, distinct from the Git blob OIDs listed above. The two ottari entries immediately below were obtained through a separately authorized owner-account read.

| Candidate | Bytes | Raw SHA-256 |
|---|---:|---|
| MedScale `release_sbom.rs` | 17423 | `62dd80af240c543a03bcc9e37a6cbdc768c5084067facde75d5ff310d1110233` |
| MedScale `release_sbom_054.rs` test | 9131 | `b7ee8328c516a15f86ba9fef0379ba1b9dba2dd4a47e1596bfae70130da804ea` |
| Ascout `self-verify.yml` | 2733 | `0ad849d2a6c94588d6762fa6925916a1fd521a25602b123e74baeb9c03e5817a` |
| MESC `provenance.py` | 2297 | `c156eeac2facc42f1bcb7e89e50ac47ec5a3df3d287575b7a95bd37ca7d65ecf` |

The initial active `gh` account returned HTTP 404 for two ottari blob
URLs. On 2026-10-08, a separately authenticated repository-owner account
was used for a **single scoped read** of each immutable Git blob; neither
the active account nor GitHub permissions were modified. Both returned
the expected blob OIDs and Base64 content. Raw byte digests:

| Candidate | Bytes | Raw SHA-256 |
|---|---:|---|
| ottari `tools/provenance_gate.py` | 18516 | `988b084a3d90ca002661ea88c134f15c082513f7ffb2a4d90c4d8d66f7f7b409` |
| ottari `tools/provenance.py` | 23492 | `b4644897846a41043c3d5f7bee8a37db606e4ce7beae1c4b49ad56ec8b080cb4` |

This resolves **byte access and identity only**. No contributor-level
rights, dependency terms, signed admission, copied code, security
qualification or release authorization follows from either hash.

Raw file hashing does not establish contributor licensing, imported
third-party rights, NOTICE obligations, or production approval.


## Additional immutable byte observations — 2026-10-09

The remaining five reference-only candidates were checked against their pinned
Git blob OIDs. Three blobs (MedScale and MESC) were read through `gh api`
on the authorized Windows host, with SHA-256 and Git blob identities independently
recomputed from their decoded bytes. The `ottari` and `kernux` workflow blobs
were read through the connected GitHub repository interface and hashed from
their complete UTF-8 byte sequences. Both computed Git blob OIDs matched
their existing frozen object identities. These findings do not admit source
bytes or certify rights, security, test behavior, or release readiness.

| Candidate | Bytes | Raw SHA-256 |
|---|---:|---|
| MedScale `generate-release-sbom.ps1` | 9262 | `a8068de158d9b673a2c9b33e31cef93856cf3d41749a3b6f20c7909e0d61e6ce` |
| MedScale `.github/workflows/ci.yml` | 5122 | `aaeaed50d0a651d716bbe5d449c279bcb20fca6b7ab95409ffa529bbd1f85863` |
| ottari `.github/workflows/ci.yml` | 22171 | `067c97d65043bfd7653141eef423c6b61bf3e6670401802586cefb7ce13e28bc` |
| kernux `.github/workflows/ci.yml` | 5846 | `bcda6ccffe0beb88cac793287235d69c13797f7d0b88c41c4f6217426fa50a2b` |
| MESC `test_provenance.py` | 1583 | `27f38a69fa9366171bce611f244298a8d297b76188dee3439d607bc273df32a3` |

## Bounded copy-first preference after qualified authorization

Prefer the MedScale `release_sbom.rs` implementation and negative fixtures for
a minimal source/lock/dependency/native SBOM, without adopting its desktop,
model, or SQLCipher stack. MedScale says its current SBOM is READY_BASE:
it does **not** prove a reproducible build or release signing.

For provenance admission, study ottari `provenance_gate.py` and
`provenance.py`; do not copy its full program. Reuse the existing
SafeEvidence exact-head GitHub workflow design for baseline CI.

Before changing to VERIFIED_ALLOWED, the **actual** rights owner must
approve exact source revision, paths, raw SHA-256, contributor/third-party
licenses, model/data/font exclusions, notices, test evidence, modifications,
distribution obligations and maintenance owner. Until then, all entries are
**REFERENCE_ONLY_PENDING_EXACT_SLICE_ADMISSION**; no source bytes are copied.
