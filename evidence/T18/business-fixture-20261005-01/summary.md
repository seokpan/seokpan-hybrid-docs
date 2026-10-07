# Synthetic Backend business continuation — business-fixture-20261005-01

## Scope

- Partial T18 only. App source c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3; source verified without modifying App. No approved Image/Release, OCP/Pod, Harbor/PVC, actual RDS/S3/VPN, operator detection/decision, Host guidance, browser/FE/WSS or service RTO/RPO achievement.
- Data owner C/김상희, App B/정태훈, Image/evidence D/최유준, real Host A/이유빈 remain responsible. Execution environment: isolated local loopback TCP/TLS synthetic fixture. None of those teammates performed/reviewed this Run unless their separate review is recorded.
- All source/restore datadirs and Redis are new temporary owned processes, loopback only. Redis plaintext port is 0; TLS/AUTH is required. Python verifies explicit CA and localhost hostname to DB/Redis/HTTPS Backend. Fixture root access is local administrative plumbing, not proof of production account/host isolation.
- Dedicated synthetic identity_svc/game_svc accounts require SSL; Passwords, age identities, SQL dumps, ciphertext, sessions and process logs remain private temporary material intended for removal. Actual cleanup status is recorded below; removal is not claimed when cleanup is incomplete. Operational C credentials, storage policy, supported tool/version and Host capacity are unverified.
- A quiescent fictional dataset uses the approved eight-table DDL. Its invented draws/moves are row-comparison fixtures, not proof of semantically valid historical games. Existing completed row counts/hashes and rating values are checked without rebuilding old Redis rooms.
- Prepared Backup exists before scripted continuation begins. Timings use monotonic clock, UTC/KST use one host wall clock. The scripted continuation starts at decrypt/preparation and excludes human detection/decision/wait/guidance. Its elapsed time must not be labeled service RTO.
- Versions: {"age": "1.1.1", "mariadbd": "mariadbd  Ver 10.11.14-MariaDB-0ubuntu0.24.04.1 for debian-linux-gnu on x86_64 (Ubuntu 24.04)", "openssl": "OpenSSL 3.0.13 30 Jan 2024 (Library: OpenSSL 3.0.13 30 Jan 2024)", "python": "Python 3.13.15", "redis-server": "Redis server v=7.0.15 sha=00000000:0 malloc=jemalloc-5.3.0 bits=64 build=e53ff17674aa6190"}. MariaDB and Redis versions are fixture package versions and may differ from actual project versions.
- Tool hashes: run.py 6a0fdf182b75e004fbdfd2ab669f7729b4f046792797f44f5cbd17b620d6f728; business_probe.py 0c62946c10155e2c162b0fc149247fff23463359f1df7c905d7bfdf15b5d4f75; Data helper 1fb3dbacfdc167689d2e3abb0713a6453d05eb4a61db9773368097ae2027ee8c; derived schema 5ee2e44becda90fdcf4448f26233647d44dc980f577e7a4c8e973d74e9475f5d.
- Cleanup: verified: all owned temporary material removed.

## Results

Partial execution: PASS. Deployment/Release/full T18 Acceptance: NOT RUN.
rto_seconds/rpo_seconds/data_reference_time_utc/incident_at_utc/business_resumed_at_utc remain null.

```json
{
  "app_owned_inherited_loopback_socket_verified": true,
  "business_probe": {
    "checks": [
      "production_provider_and_runner_readiness",
      "two_restored_members_login_with_fresh_secure_sessions",
      "persistent_ranking_and_rating_read",
      "fresh_room_join_teams_ready_and_new_game_read",
      "fresh_game_explicit_leave_forfeit_result_and_rating_read"
    ],
    "excluded": [
      "FE/browser/WSS",
      "Harbor/Image/PVC/OCP",
      "incident_detection",
      "manual_user_guidance",
      "real_RDS/S3/VPN",
      "historical_result_HTTP"
    ],
    "new_completed_game_id": "dbe7d2b5-91b3-4497-926a-3794b0a8548a",
    "probe_elapsed_seconds": 1.76253,
    "release_acceptance": false,
    "scope": "synthetic_loopback_https_backend_business",
    "service_rto": null
  },
  "encrypted_backup_sha256": "b675b6cb464901df10dd9a39705989ed215088b2bd50b301e7b98aca06d4dbce",
  "historical_result_http": "NOT VERIFIED: new Redis has no old Room participation",
  "new_completion_sql_and_rating_verified": true,
  "new_redis_tls_auth_empty": true,
  "restored_row_counts": {
    "alembic_version": 1,
    "game": 52,
    "game_participant": 104,
    "game_result": 52,
    "member": 2,
    "member_stats": 2,
    "move": 655,
    "rating_history": 104
  },
  "rpo_seconds": null,
  "rto_seconds": null,
  "source_restore_equal": true
}
```

## Functional limit and follow-up

The current GET /api/v1/games/{old-id}/result first requires Redis participation, current Room and current/last Game. A fresh empty Redis does not provide that old Room association, although completed DB rows survive. Thus SQL/hash/ranking checks do not prove historical individual-result access for the specified client. The minimum design clarification distinguishes preserved historical records/relations checked by operator SQL, restored member ranking/rating visible to a fresh client, and new-game completion/result visible in the new Runtime. B and the design review must explicitly confirm this scope. This fixture does not add a History feature, invent old Redis state, or present SQL as historical-result client access.

C reviews dataset/snapshot/accounts/TLS/restore conclusions; B reviews historical read and transient-state policy; A confirms actual isolated Host/storage; D reviews Image and new Run/index. Current architecture choice may use these partial measurements, but retained service targets must be supported by an adequately scoped combined rehearsal, user impact/cost/schedule decision and adopted design artifacts.
