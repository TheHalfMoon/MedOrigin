# SafeEvidence G01a — Synthetic Engineering Bootstrap

Status: **G01A_SYNTHETIC_QUALIFIED / INDEPENDENT_REVIEW_PENDING / NOT_A_PRODUCT_RELEASE**.

Founder scope: https://github.com/TheHalfMoon/SafeEvidence/issues/17
Signed governance merge: https://github.com/TheHalfMoon/SafeEvidence/pull/19

## Boundaries

This workspace exists solely to establish reproducibility for later governed work.
There are no medical decisions, inference engines, patient records, literature
imports, signed evidence packs, trial data, models, terminology assets, secrets,
network calls from the crate, source transplants, or runtime cloud services.

The single crate uses Rust's standard library only. It is marked
`publish = false`. Its immutable synthetic fixture has SHA-256:

`6d7d7070cb270e830b5d232f1aa127c0d5fa0eac1fdf1677c3de2898a417c3dd`

That identity is repeated in `docs/evidence/g01a_synthetic_manifest.json` and
the stdlib-only fail-closed verifier, **not** a signed supply-chain guarantee.
The `.gitattributes` policy forces this fixture to LF on both Windows and Linux;
otherwise checkout-level CRLF conversion can silently invalidate its digest.

The single reviewed Rust source `crates/g01a-synthetic/src/lib.rs` is also
LF-pinned with SHA-256
`35356b0c9d5bcd70231fd6c038574ebc5951530f03c50235d4a0447049761860`.
The JSON source identity and Python fail-closed guard must agree. Extra repository
Cargo configuration directories are disallowed. CI runs the source/config
admission guard **before** installing Rust tooling or executing Rust compilation.
This mitigates accidental unreviewed execution paths; it is not a substitute
for signed source review, trusted workflow governance or a real security audit.

## Reproduce on a clean Windows or Linux checkout

Development setup may explicitly install Rust 1.97.1 and rustfmt/clippy.
The project has no third-party crate dependencies. After toolchain setup,
run offline from the repository root:

```text
python tools/governance/g01a_synthetic_check.py --root . --json
python -m unittest discover -s tools/governance/tests -q
cargo fmt --all -- --check
cargo test --offline --locked --workspace --all-targets
cargo clippy --offline --locked --workspace --all-targets -- -D warnings
```

GitHub's `G01a Synthetic Reproducibility` matrix runs the same commands on
Windows and Ubuntu. It checks out the exact pull-request SHA. Rustup toolchain
acquisition at CI setup requires network, whereas crate compilation, lint and
tests run in Cargo offline mode. No cold-egress measurement is claimed.

The fixture, manifest and negative tests are all **synthetic**. A passing
check returns `classification=SYNTHETIC_ONLY`,
`clinical_validation=NOT_PERFORMED`, `copy_authorized=false` and
`source_imports=BLOCKED`; it can never upgrade those statuses.

## Completion boundary

Successful G01a build/CI would qualify only the bounded synthetic engineering
substrate at the tested revision. P01 full entry, P02, donor imports, clinical
evaluation, product claims and release remain blocked by their own authorities,
including #3 (owners), #4 (qualified clinical/evaluation) and #5 (rights/trust).
The original 41 P1 findings remain open until actual accepted evidence exists.
