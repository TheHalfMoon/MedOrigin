# SafeEvidence Donor Transplant Protocol

Status: `P00_BINDING`

## 1. Objective

Reuse implementations without inheriting unrelated product architecture.

SafeEvidence follows:

```text
REUSE IMPLEMENTATIONS
OWN SAFE-EVIDENCE SEMANTICS
RE-QUALIFY ALL CLAIMS
```

A donor's passing tests or research claims do not automatically become
SafeEvidence claims.

## 2. Preferred reuse order

```text
stable external dependency
        ↓
bounded coherent code transplant
        ↓
isolated local worker / FFI
        ↓
port to Rust when the trust boundary requires it
        ↓
greenfield only with GREENFIELD_JUSTIFIED
```

Use a dependency for commodity libraries with healthy independent maintenance.
Use a bounded transplant for sibling-project foundation code when direct
dependency would create cross-product coupling. Use a worker for large
Python/Java/native systems whose whole runtime should not enter the trusted
core.

## 3. Required transplant record

Before the first donor-derived line is merged, record:

```text
donor repository
exact commit/tree
source paths
destination paths
reuse disposition
license / special permission basis
embedded/transitive material
required notices
original tests/fixtures
modifications made
trust-zone placement
network privileges
filesystem/key privileges
resource budget
update/backport policy
exit/removal strategy
```

## 4. Coherent-slice rule

Do not copy isolated files when their safety depends on later fixes, companion
modules, or tests.

For sibling projects, inspect history and extract the smallest coherent
qualified behavior, then backport later relevant security/correctness fixes.

### MedScale example

Do **not** copy the current `medscale-storage` crate wholesale. Its present
schema and module set include unrelated Research OS features.

The SafeEvidence vault foundation should instead extract the required behavior
from the qualified evolution around:

- keys / wrapping / recovery;
- SQLCipher working metadata;
- sealed blobs;
- source identity and immutable blobs;
- migrations;
- path-claim validation;
- process-exclusive writer ownership;
- restart/digest invariants;
- privacy probes;
- backup/recovery behavior selected for the SafeEvidence schema.

The newer `writer_lock.rs` behavior and its cross-process tests must take
precedence over older marker-file-only assumptions.

## 5. Tests travel with behavior

A transplant is incomplete when implementation moved but the donor tests that
define its edge cases did not.

Bring, adapt, and preserve useful donor tests for:

- wrong-key and key-loss behavior;
- restart/durability;
- second-writer refusal;
- digest mismatch;
- retraction exclusion;
- source identity/version changes;
- network default deny;
- policy precedence;
- abstention/selective-risk metrics;
- pack digest/signature/rollback checks;
- hostile-input and privacy regressions.

Add SafeEvidence-specific tests on top.

## 6. Upstream update policy

Copied code does not track upstream automatically.

Each transplanted component keeps an `UPSTREAM.md` or machine-readable
provenance record with its source pin. Updates are deliberate:

```text
discover upstream change
 -> inspect diff/security relevance
 -> import selected change
 -> preserve provenance
 -> run donor + SafeEvidence tests
 -> record new source pin
```

No blind synchronization.

## 7. Dependency-vs-copy rule

Prefer direct dependency when:

- the library is generic rather than product-specific;
- API stability and maintenance are acceptable;
- offline packaging is supported;
- its runtime privileges fit SafeEvidence;
- transitive licensing is manageable.

Examples: `fastembed-rs`, selected SQLite/vector crates, parser/OCR libraries
after qualification, and potentially UniFFI.

Prefer bounded transplant when:

- source is sibling-product code;
- SafeEvidence must own the lifecycle;
- the donor crate contains unrelated modules;
- dependency would couple product release cadence.

## 8. Worker rule

Large specialist stacks may run as isolated local workers during development or
product execution only when measured need justifies them.

Default product rules:

- trusted core remains Rust;
- workers get no vault master key;
- workers get no direct canonical DB authority;
- workers get no ambient network;
- input/output contracts are typed and bounded;
- crash/restart cannot corrupt canonical state.

A full OpenMed, CQL/Java, or heavyweight document stack is not imported into the
trusted core merely because its code is useful.

## 9. Empirical-claim firewall

Never transfer donor claims such as:

- clinically safe;
- state of the art;
- calibrated;
- private-data ready;
- release ready;
- superior to another system.

SafeEvidence re-runs matched evaluation on its own exact build.

## 10. Completion gate

A source-admission/transplant PR cannot close until provenance, notices,
transitive review, donor tests, SafeEvidence tests, and exact-head evidence are
bound to the adopted bytes.
