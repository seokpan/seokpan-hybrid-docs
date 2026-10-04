# Isolated synthetic MariaDB partial rehearsal — fixture-20261005-01

## Identity and Scope

- Test T18, partial T17/T18 Data path; full Acceptance NOT RUN.
- App reference `c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3`; fixture DDL is derived from the two approved App revisions, not the operational Migration CLI. No actual project Backup/schema/data was supplied or changed.
- Assigned Data owner 김상희/kshi1313-gif; actual contribution by Codex under tjung03 authorization. C did not execute or review this Run; C Data review pending. A Host and D Image/evidence responsibilities remain unchanged; D index review pending.
- All DBs are newly initialized temporary directories, using `tcp` transport. Unix mode uses `--skip-networking`; TCP mode binds only 127.0.0.1 on separately allocated ephemeral ports and disables the Unix socket. Local disposable fixture root has no password; this is not production TLS/role/account proof. No Docker/registry, project service, AWS/ROSA, S3/VPN, paid environment or Cloud identity used.
- Planned three repeated small samples (52 completed synthetic games/655 moves each), one larger sample (1000 games/13000 moves). Only those two counts match or scale the published precheck; other row composition/bytes are invented, not actual C data. The larger data is a sensitivity case, not forecast production load. No one sample is selected as an operational bound.
- Synthetic identities/rows are invented. The password field is a non-login placeholder: no authentication or App business recovery was tested. The quiescent fixture does not measure concurrent-write consistency or DB load under production traffic.
- Tool versions: `{"age": "1.1.1", "mariadb-dump": "mariadb-dump  Ver 10.19 Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)", "mariadbd": "mariadbd  Ver 10.11.14-MariaDB-0ubuntu0.24.04.1 for debian-linux-gnu on x86_64 (Ubuntu 24.04)", "python": "3.12.14"}`. Package MariaDB version differs from project 11.8.9; no claim of RDS/actual-version parity.

## Results

- Render: NOT RUN; Deployment: NOT RUN; Acceptance: NOT RUN.
- Partial local execution: PASS; completed samples: 4. Completed sample comparisons and negative-case outcomes are recorded below; unfinished steps have no invented success/measurement. Raw metric values are in metrics.csv, not interpreted as RTO/RPO.
- Incident, detection/decision, selected older backup, local OCP/Pod startup, Redis, App Image, client guidance/login/representative business, real S3/network transfer, production workload and cost were not measured. `rto_seconds`, `rpo_seconds`, `incident_at_utc`, `business_resumed_at_utc` remain null.
- UTC/KST wall-clock event timestamps share one host clock. Durations use monotonic perf_counter. No independent clock synchronization uncertainty or real RDS clock was measured.

## Evidence and Recovery

- Five-file Run with four payload checksum entries (checksums.txt does not hash itself); timeline.csv records actual steps, metrics.csv the actual measured durations/bytes. The JSON records below are actual execution comparison results, not source tests. SQL dumps, ciphertext, age identities and private process diagnostics are disposable scratch files and are never published.
- Harness input SHA-256: run.py `1fb3dbacfdc167689d2e3abb0713a6453d05eb4a61db9773368097ae2027ee8c`, schema.sql `5ee2e44becda90fdcf4448f26233647d44dc980f577e7a4c8e973d74e9475f5d`, release_template.json `94e57e4ee29e2b09fa6167fab68fd90261060b1fcac76694c9fc5e65edadc94a`.
- For samples reaching Dump, fixture writes finish and COMMIT first and no writer runs afterward; recorded DB UTC bounds bracket that quiescent snapshot. Only completed equal comparisons below prove the deterministic fixture marker/row hashes were restored. Exact operational Data time is unreviewed, so recovery.data_reference_time_utc/data_reference_level remain null and no confirmed RPO is calculated.
- A local file copy on the same machine replaces the real Data VM→S3→On-Prem path. `fixture_data_reference_lower_bound_to_local_complete_seconds` is a conservative quiescent-fixture bracket only, not actual Cloud backup freshness or a configured interval guarantee.
- Cleanup: all temporary datadirs/processes/keys/backups removed. Cleanup scope is only harness-owned temporary datadirs/processes/keys/backups; output evidence remains.

### fixture-1

```json
{
  "data_reference_lower_bound_utc": "2026-10-04T16:21:52.804679Z",
  "data_reference_upper_bound_utc": "2026-10-04T16:21:52.852326Z",
  "dump_finished_at_utc": "2026-10-04T16:21:52.838694Z",
  "dump_started_at_utc": "2026-10-04T16:21:52.805254Z",
  "encrypted_backup_sha256": "9d6e91aaf203f049427fac1834d0584999b7909b9942900ef24c61c39b929d0e",
  "import_finished_at_utc": "2026-10-04T16:21:53.942611Z",
  "import_started_at_utc": "2026-10-04T16:21:53.843042Z",
  "reused_target_rejected": true,
  "sample_id": "fixture-1",
  "source_restore_comparison_equal": true,
  "synthetic_games": 52,
  "truncated_ciphertext_rejected": true,
  "verification": {
    "revision": "20260902_0002",
    "row_counts_by_table": {
      "alembic_version": 1,
      "game": 52,
      "game_participant": 104,
      "game_result": 52,
      "member": 2,
      "member_stats": 2,
      "move": 655,
      "rating_history": 104
    },
    "rows_sha256_by_table": {
      "alembic_version": "1fc125bb0a8c70d2d827f702be23fc428782f8c32de61dddcacde1ebf73887fc",
      "game": "40807ee918ab569b2a41b94cfd4219041c6754ff974616718eee7bec45d735a3",
      "game_participant": "efb428b1380a4c36e75c45149f90ff827c36de5df065bd19772f768b0f14dd1d",
      "game_result": "002f7006d923db04fd12b08faf8c26c909f8afa04ecc7f19ca0a7e27e09d13ff",
      "member": "acecc531c25c00aab71630f536eca2bc2b60bec4521420c321d230733d6f387f",
      "member_stats": "523c6390e20d2e856dbc3c808bf991234c0e9502c900395ef6bdc3e834be513e",
      "move": "420f6412bae41a7c2037c14505865f167b07908a4cf3aa47788a55d2a7d24bc9",
      "rating_history": "9f13a98ca8298b12ca01939d8e5da62a7a94176e5774878d9eb2b7096e37e4ba"
    },
    "schema_sha256_by_table": {
      "alembic_version": "b2675f480152747b74f45377fc7a68e7e2fcd8c2e6b25b188365699c9c56594e",
      "game": "1bfa100540b59ceecfa8194606d2ae89a554c50f55062a252966038055b21620",
      "game_participant": "c6def8e495d7b81735729483b5ca9676239e726caad59c2dd2d5678f9d126cca",
      "game_result": "d6bffa75400603573c2d29fdb5a9e6dd493925d97e7d8e032d9fa6a0d217565e",
      "member": "da7f4f1083df09d935a7d5ccee0000fff62b4e853bcfe0ff2470b3baa3d13993",
      "member_stats": "96e0f0e865ff69619ba06ec99af2f37db8b226ea9b699fcc1ca816d08fe7d2b9",
      "move": "8400015dde41cfe0da0205edadd90b3b08b232ac13516e68e3d9f02226f6c476",
      "rating_history": "aae55ccaece540010f627e9f9f29d31b11e6654923440acdd9d5a160372bbac0"
    }
  },
  "wrong_key_rejected": true
}
```

### fixture-2

```json
{
  "data_reference_lower_bound_utc": "2026-10-04T16:21:57.447982Z",
  "data_reference_upper_bound_utc": "2026-10-04T16:21:57.532502Z",
  "dump_finished_at_utc": "2026-10-04T16:21:57.511483Z",
  "dump_started_at_utc": "2026-10-04T16:21:57.449602Z",
  "encrypted_backup_sha256": "6529951d6eb18076a92d2d273434cdcefc749d0c649c6c8f85ddd7554d8df798",
  "import_finished_at_utc": "2026-10-04T16:21:58.806142Z",
  "import_started_at_utc": "2026-10-04T16:21:58.727122Z",
  "reused_target_rejected": true,
  "sample_id": "fixture-2",
  "source_restore_comparison_equal": true,
  "synthetic_games": 52,
  "truncated_ciphertext_rejected": true,
  "verification": {
    "revision": "20260902_0002",
    "row_counts_by_table": {
      "alembic_version": 1,
      "game": 52,
      "game_participant": 104,
      "game_result": 52,
      "member": 2,
      "member_stats": 2,
      "move": 655,
      "rating_history": 104
    },
    "rows_sha256_by_table": {
      "alembic_version": "1fc125bb0a8c70d2d827f702be23fc428782f8c32de61dddcacde1ebf73887fc",
      "game": "40807ee918ab569b2a41b94cfd4219041c6754ff974616718eee7bec45d735a3",
      "game_participant": "efb428b1380a4c36e75c45149f90ff827c36de5df065bd19772f768b0f14dd1d",
      "game_result": "002f7006d923db04fd12b08faf8c26c909f8afa04ecc7f19ca0a7e27e09d13ff",
      "member": "acecc531c25c00aab71630f536eca2bc2b60bec4521420c321d230733d6f387f",
      "member_stats": "523c6390e20d2e856dbc3c808bf991234c0e9502c900395ef6bdc3e834be513e",
      "move": "420f6412bae41a7c2037c14505865f167b07908a4cf3aa47788a55d2a7d24bc9",
      "rating_history": "9f13a98ca8298b12ca01939d8e5da62a7a94176e5774878d9eb2b7096e37e4ba"
    },
    "schema_sha256_by_table": {
      "alembic_version": "b2675f480152747b74f45377fc7a68e7e2fcd8c2e6b25b188365699c9c56594e",
      "game": "1bfa100540b59ceecfa8194606d2ae89a554c50f55062a252966038055b21620",
      "game_participant": "c6def8e495d7b81735729483b5ca9676239e726caad59c2dd2d5678f9d126cca",
      "game_result": "d6bffa75400603573c2d29fdb5a9e6dd493925d97e7d8e032d9fa6a0d217565e",
      "member": "da7f4f1083df09d935a7d5ccee0000fff62b4e853bcfe0ff2470b3baa3d13993",
      "member_stats": "96e0f0e865ff69619ba06ec99af2f37db8b226ea9b699fcc1ca816d08fe7d2b9",
      "move": "8400015dde41cfe0da0205edadd90b3b08b232ac13516e68e3d9f02226f6c476",
      "rating_history": "aae55ccaece540010f627e9f9f29d31b11e6654923440acdd9d5a160372bbac0"
    }
  },
  "wrong_key_rejected": true
}
```

### fixture-3

```json
{
  "data_reference_lower_bound_utc": "2026-10-04T16:22:02.794343Z",
  "data_reference_upper_bound_utc": "2026-10-04T16:22:02.871173Z",
  "dump_finished_at_utc": "2026-10-04T16:22:02.845578Z",
  "dump_started_at_utc": "2026-10-04T16:22:02.795274Z",
  "encrypted_backup_sha256": "37741d4946406ba0d6ab348240a7e210f71782376cd0ab24a76f846bbb20ecf5",
  "import_finished_at_utc": "2026-10-04T16:22:04.136565Z",
  "import_started_at_utc": "2026-10-04T16:22:04.014859Z",
  "reused_target_rejected": true,
  "sample_id": "fixture-3",
  "source_restore_comparison_equal": true,
  "synthetic_games": 52,
  "truncated_ciphertext_rejected": true,
  "verification": {
    "revision": "20260902_0002",
    "row_counts_by_table": {
      "alembic_version": 1,
      "game": 52,
      "game_participant": 104,
      "game_result": 52,
      "member": 2,
      "member_stats": 2,
      "move": 655,
      "rating_history": 104
    },
    "rows_sha256_by_table": {
      "alembic_version": "1fc125bb0a8c70d2d827f702be23fc428782f8c32de61dddcacde1ebf73887fc",
      "game": "40807ee918ab569b2a41b94cfd4219041c6754ff974616718eee7bec45d735a3",
      "game_participant": "efb428b1380a4c36e75c45149f90ff827c36de5df065bd19772f768b0f14dd1d",
      "game_result": "002f7006d923db04fd12b08faf8c26c909f8afa04ecc7f19ca0a7e27e09d13ff",
      "member": "acecc531c25c00aab71630f536eca2bc2b60bec4521420c321d230733d6f387f",
      "member_stats": "523c6390e20d2e856dbc3c808bf991234c0e9502c900395ef6bdc3e834be513e",
      "move": "420f6412bae41a7c2037c14505865f167b07908a4cf3aa47788a55d2a7d24bc9",
      "rating_history": "9f13a98ca8298b12ca01939d8e5da62a7a94176e5774878d9eb2b7096e37e4ba"
    },
    "schema_sha256_by_table": {
      "alembic_version": "b2675f480152747b74f45377fc7a68e7e2fcd8c2e6b25b188365699c9c56594e",
      "game": "1bfa100540b59ceecfa8194606d2ae89a554c50f55062a252966038055b21620",
      "game_participant": "c6def8e495d7b81735729483b5ca9676239e726caad59c2dd2d5678f9d126cca",
      "game_result": "d6bffa75400603573c2d29fdb5a9e6dd493925d97e7d8e032d9fa6a0d217565e",
      "member": "da7f4f1083df09d935a7d5ccee0000fff62b4e853bcfe0ff2470b3baa3d13993",
      "member_stats": "96e0f0e865ff69619ba06ec99af2f37db8b226ea9b699fcc1ca816d08fe7d2b9",
      "move": "8400015dde41cfe0da0205edadd90b3b08b232ac13516e68e3d9f02226f6c476",
      "rating_history": "aae55ccaece540010f627e9f9f29d31b11e6654923440acdd9d5a160372bbac0"
    }
  },
  "wrong_key_rejected": true
}
```

### fixture-4

```json
{
  "data_reference_lower_bound_utc": "2026-10-04T16:22:12.082276Z",
  "data_reference_upper_bound_utc": "2026-10-04T16:22:12.150422Z",
  "dump_finished_at_utc": "2026-10-04T16:22:12.137085Z",
  "dump_started_at_utc": "2026-10-04T16:22:12.083590Z",
  "encrypted_backup_sha256": "b2b5831271f91bb561851150298cade8efb5cb76a42fa138eee60de1e4f010cb",
  "import_finished_at_utc": "2026-10-04T16:22:13.414340Z",
  "import_started_at_utc": "2026-10-04T16:22:13.120115Z",
  "reused_target_rejected": true,
  "sample_id": "fixture-4",
  "source_restore_comparison_equal": true,
  "synthetic_games": 1000,
  "truncated_ciphertext_rejected": true,
  "verification": {
    "revision": "20260902_0002",
    "row_counts_by_table": {
      "alembic_version": 1,
      "game": 1000,
      "game_participant": 2000,
      "game_result": 1000,
      "member": 2,
      "member_stats": 2,
      "move": 13000,
      "rating_history": 2000
    },
    "rows_sha256_by_table": {
      "alembic_version": "1fc125bb0a8c70d2d827f702be23fc428782f8c32de61dddcacde1ebf73887fc",
      "game": "3f6ff796264b463ecf0d514159eb6732666505effc9aaf2fcbd2a390b4dbbae7",
      "game_participant": "02dfdcb2b57fa264de51b132669732f91f9d43e41b915f9248569af13454551b",
      "game_result": "47894575e1571a92037910541340ab40701e2acc2a895762c21af6203819e739",
      "member": "acecc531c25c00aab71630f536eca2bc2b60bec4521420c321d230733d6f387f",
      "member_stats": "28c59c2b7651b2f828cc653fb1dfd5f2e7ce090d4daf0b300acb73fea77ca285",
      "move": "765278ecfd1fb50372ebfd4468708aaf702428d147a4cc18127001de85202e79",
      "rating_history": "7b9ed523d74dc5392a7329e283d25008036b62923182d07e52b79562b8d7abbe"
    },
    "schema_sha256_by_table": {
      "alembic_version": "b2675f480152747b74f45377fc7a68e7e2fcd8c2e6b25b188365699c9c56594e",
      "game": "1bfa100540b59ceecfa8194606d2ae89a554c50f55062a252966038055b21620",
      "game_participant": "6ac2ba981a5b76bbcbff53acd61b4568f2f3909d04c1f7c88debfbaec7790eb0",
      "game_result": "d6bffa75400603573c2d29fdb5a9e6dd493925d97e7d8e032d9fa6a0d217565e",
      "member": "da7f4f1083df09d935a7d5ccee0000fff62b4e853bcfe0ff2470b3baa3d13993",
      "member_stats": "96e0f0e865ff69619ba06ec99af2f37db8b226ea9b699fcc1ca816d08fe7d2b9",
      "move": "8400015dde41cfe0da0205edadd90b3b08b232ac13516e68e3d9f02226f6c476",
      "rating_history": "d0ec360a6bbe865d3ce1e2282cf5faae372974192a82b37c46bfcdde9d740886"
    }
  },
  "wrong_key_rejected": true
}
```

## Follow-up

- C reviews derived schema, snapshot assumptions, restore comparisons and operational tools/accounts; those reviews are pending and must not be attributed to C before received.
- A confirms actual isolated Host/capacity; B/D prepare preserved current Image/new Redis/client path and combine the full business timeline; no full T18 or deployed Release acceptance follows from this partial Run.
- This evidence may inform implementation burden/bottlenecks in the current restore structure. Real backup transfer/availability, user interruption/loss acceptance, full-business rehearsal, costs/team schedule and adopted design choice remain separate before new targets are finalized.
