# P00 Vault Durability and Key-Custody Contract

Status: P00_BINDING_CONTRACT
Owners: storage/security.
Resolves CODEX-P00-02 and OPUS-P00-003 design gaps. Qualification remains P02.

## Design choice

Use a persistent SQLCipher SQLite authority with WAL and exactly one logical
writer per private vault. Do NOT adopt MedScale whole-file decrypt/edit/reseal
as canonical storage. Ottari himsat-core is a primary copy-first candidate, not
proof that an integrated SafeEvidence vault is ready.

## Acknowledgement and recovery

- Authority writes use explicit transactions. Never acknowledge success until
  a SQLCipher/SQLite COMMIT returns success under a tested durability profile.
- Test the candidate WAL + synchronous=FULL configuration and selected
  filesystem/cipher version. WAL checkpoint is NOT an acknowledgement barrier.
- A timeout/crash before outcome is known yields COMMIT_UNKNOWN pending durable
  recovery, not success or an assumed rollback.
- The writer ownership guard spans open, transaction and close; SQLite
  locking and any companion process lock are qualified together. Lockfile
  existence alone is not ownership.
- There is no encrypt-again-at-exit step on which committed records depend.
  Supported power-loss assumptions must be stated; drive-firmware dishonesty is
  not claimed to be preventable.

## Backups, migration and restore

- Do not copy live .db/WAL files as a backup. Use an encrypted,
  transaction-consistent online backup/snapshot of the admitted SQLCipher DB.
- The backup must be written to staging, validated for cipher/key, schema,
  integrity, source manifests and backup sequence, then published with
  atomic replacement and directory durability where supported.
- Restore into clean staging with the writer quiesced. Verify before switch;
  preserve the prior qualified database until validation succeeds.
- Migrations either commit atomically or have a durable, replayable journal.
  Disk-full, hard kill or partial migration must not erase the only valid
  acknowledged state.
- WAL/checkpoint or backup failures may mark the vault degraded/read-only; do
  not emit false COMMITTED receipts.

## Key and blob custody

Separate KEK/DEK, user-presence/unlock and recovery/rotation policies per
Windows/macOS/Linux/iOS/Android. Native keystore/Keychain integration is
required before that platform is qualified. Use opaque random or keyed private
blob names; never raw public hashes that reveal sensitive file membership.
Restrict decrypted temporary material and exclude private stores from broad OS
indexing or unprotected backups. A compromised unlocked OS is outside the
claimed secrecy guarantee.

## States and acceptance gates

Operational states: LOCKED, OPEN, COMMITTING, COMMIT_UNKNOWN, RECOVERING,
READ_ONLY_RECOVERY, KEY_UNAVAILABLE, BACKUP_INCOMPLETE, CORRUPT_QUARANTINED.

P02 must run exact-donor and integrated tests: separate processes fighting for
the lock; hard kill before/during/after acknowledged commit; restart with WAL;
checkpoint crash; backup during writes; interrupted publish/restore/migration;
wrong/lost key; disk full; private plaintext spill scan; backup/key recovery.
Any acknowledged transaction loss blocks adoption. Device claims additionally
need real native protector and backup-exclusion tests. No results are assumed.
