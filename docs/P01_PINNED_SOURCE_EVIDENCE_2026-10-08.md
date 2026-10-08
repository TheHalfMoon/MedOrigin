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
| Kernux | `.github/workflows/ci.yml` | `372e34bf2591d9885d09888c4eb1e291455019b6` |
| Ascout | `.github/workflows/self-verify.yml` | `fffb70fa00b8152063e7ad9b3062988d6b0c04c2` |
| MESC | `src/medscale/provenance.py` | `242aad5871261bdb242977e11bfb4b680209379d` |
| MESC | `tests/test_provenance.py` | `b5da9a4a5d8d2de7dc3d50ff3ff9463611b9dfe3` |

## Byte-level SHA-256 observations (independently computed, not approvals)

Decoded GitHub blob bytes were inspected using `gh api` and SHA-256
computed in the local Windows PowerShell environment on 2026-10-08.
These are content digests, distinct from the Git blob OIDs listed above.

| Candidate | Bytes | Raw SHA-256 |
|---|---:|---|
| MedScale `release_sbom.rs` | 17423 | `62dd80af240c543a03bcc9e37a6cbdc768c5084067facde75d5ff310d1110233` |
| MedScale `release_sbom_054.rs` test | 9131 | `b7ee8328c516a15f86ba9fef0379ba1b9dba2dd4a47e1596bfae70130da804ea` |
| Ascout `self-verify.yml` | 2733 | `0ad849d2a6c94588d6762fa6925916a1fd521a25602b123e74baeb9c03e5817a` |
| MESC `provenance.py` | 2297 | `c156eeac2facc42f1bcb7e89e50ac47ec5a3df3d287575b7a95bd37ca7d65ecf` |

The active `gh` CLI authentication returned HTTP 404 when directly
requesting two ottari blob URLs. **No ottari raw SHA-256 was verified**,
and the empty-byte SHA-256 must never be accepted as evidence for those
files. Git object IDs were separately observed through the connected
GitHub repository reader. Confirm byte digests with access to the exact
repository blobs before choosing any ottari transplant.

Raw file hashing does not establish contributor licensing, imported
third-party rights, NOTICE obligations, or production approval.

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
