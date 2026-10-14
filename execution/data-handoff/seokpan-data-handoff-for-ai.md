---
title: 석판(Seokpan) 2차 프로젝트 — Data 영역 인수인계 (AI 학습용)
snapshot: 2026-10-13 22:00 KST (하차 정리 반영)
previous_owner: 김상희 (GitHub kshi1313-gif, controller 리눅스 계정 ksh) — 2026-10-13 하차
next_owner: 미정 (이유빈 전담 또는 이유빈 · 정태훈 · 최유준 분담)
language: ko
secrets_included: none (비밀번호 · Token · 개인키 · AWS 계정 번호 · 공인 IP 없음)
---

# 석판 2차 프로젝트 — Data 영역 인수인계 (AI 학습용)

## 2026-10-14 보완 — Data 인계 형식과 수신 확인

이 절은 아래 2026-10-13 기록 중 인계 파일 형식과 수신 상태를 갱신합니다.
Data 후속 작업은 이유빈이 이어서 진행하며, 실제 실행 조건은 기존 Runbook을 따릅니다.

- 기존 `c-data-outputs.json`과 `handoff-manifest.json`을 유지합니다.
- `jth` 계정의 Data 인계 파일 읽기 가능·쓰기 불가를 확인했습니다.
- 정태훈은 Data 인계 파일·manifest 결속과 연결 값 네 개의 해시 대조가
  모두 통과했다고 회신했습니다.
- 10/13 기록의 Data 인계 읽기·Endpoint 해시 대조 대기는 해소됐습니다.
- 실제 DB·Valkey 접속, TLS·평문 거부 시험은 이 수신 확인과 별도입니다.
- PR #68의 검토 Plan JSON 접근·Apply 승인은 이 인계 확인과 구분합니다.
- 실제 주소·ID·ARN은 공개 문서나 Git에 추가하지 않습니다.

### 인계 파일을 읽는 형식

`c-data-outputs.json`은 각 항목에 값을 직접 담습니다.

| 항목 | 인계 파일 조회 표현 |
| --- | --- |
| RDS 주소 | `.rds_address` |
| RDS 포트 | `.rds_port` |
| Valkey Primary Endpoint | `.redis_primary_endpoint` |
| Valkey 포트 | `.redis_port` |
| RDS 보안 그룹 | `.rds_security_group_id` |
| Valkey 보안 그룹 | `.redis_security_group_id` |

이 인계 파일에는 `.rds_address.value` 같은 중첩 조회 표현을 사용하지 않습니다.
`terraform output -json` 원본 출력의 `.value` 구조와 구분합니다.
AWS 응답 처리와 두 형식을 지원하는 기존 검사 코드의 `.value`는 삭제하지 않습니다.

Data 계약의 관련 대기 상태 정정과 결과 기록은 기존 Infra #19·#23에서 이어갑니다.
- [Data 계약 기준본](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6143942560)
- [Data 인계 접근 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6159843548)

## 0. AI에게 — 이 문서를 읽는 방법

너는 석판 2차 프로젝트에서 **Data · Storage · Recovery 영역**(1차 데이터 이관, 15분 백업, 온프렘 복원)을 이어받은 팀원을 돕는다. 이전 담당자 김상희는 2026-10-13에 하차했다. 이 문서는 그 시점의 전체 상태를 담은 스냅샷이다.

**반드시 지킬 것**

1. **이 문서는 스냅샷이다.** 실행 절차의 최신본은 GitHub Issue 본문(Runbook)이다. 실행 명령을 안내하기 전에 사용자에게 해당 Issue 본문의 현재 버전 줄(맨 위 `v…`)을 확인하게 하거나, GitHub 도구가 있으면 직접 읽어라. 이 문서의 버전보다 높으면 Issue를 따른다.
2. **비밀값을 요구하거나 출력하지 마라.** Token · 비밀번호 · 개인키 · AWS 계정 번호 · ARN · 실제 Endpoint 주소를 화면에 출력하거나 Issue · PR 문안에 넣는 명령을 만들지 마라. 비교가 필요하면 SHA-256 앞 12자리 해시로 비교한다.
3. **1차 DB(MariaDB · MaxScale)는 읽기 전용이다.** 1차 DB에 쓰기 · 계정 추가 · 설정 변경 명령을 만들지 마라.
4. **Apply는 지정 실행자만 한다.** foundation = 이유빈, rosa = 정태훈. 다른 사람에게는 Plan 확인까지만 안내하고 "plan만"으로 기록하게 한다.
5. **팀에 공개하는 글(Issue · PR · 코멘트)** 은 역할 기호(A · B · C · D) 대신 이름(이유빈 · 정태훈 · 김상희 · 최유준)을 쓰고, 작업용 약어는 풀어 쓴다. 다른 저장소 번호는 전체 URL로 쓴다(`#44`만 쓰면 현재 저장소의 44번으로 링크된다).
6. **모르면 추측하지 말고** "확인 필요"로 표시하고 어디서 확인할지(Issue 번호 · 파일 경로)를 말하라.
7. 명령을 줄 때는 **어디서(호스트 · 계정) 실행하는지** 반드시 함께 적어라. 특히 controller에서는 `ksh`(온프렘 Data 작업, AWS 불가)와 사용자 본인 계정(AWS · GitHub)을 구분하라(6-2절). 이 프로젝트는 controller · 백업 작업 VM · 복구 DB VM · 1차 VM이 섞여 있어 실행 위치 실수가 잦았다.

---

## 1. 프로젝트 요약

| 항목 | 값 |
|---|---|
| 프로젝트 | 석판 2차 — 실시간 투표형 오목 서비스의 하이브리드 클라우드 확장 (코오롱베니트 하이브리드 클라우드 컨테이너 플랫폼 과정) |
| 기간 | 2026-09-28 ~ 2026-10-26 |
| 일정 | Technical Freeze 10/16 · 본 검증 창 10/19 ~ 21 · Demo Freeze 10/22 · Presentation Ready 10/23 · 발표 10/26 |
| 필수 기술 | Hybrid 환경, OpenShift(ROSA Classic Multi-AZ), Terraform |
| AWS 예산 | 500달러 한도(계획선 450 + 여유 50). 교육기관이 일일 요금 보고. 결제 알림 설정 불가 |
| 리전 | ap-northeast-2 (서울) |
| GitHub org | `seokpan`, 저장소 `seokpan-hybrid-{app, gitops, infra, docs}` (모두 Public, 팀원 전원 admin) |
| 아키텍처 | **B1: Cloud Primary + On-Prem Restore-based Recovery** — 정상 서비스는 AWS(ROSA · RDS · Valkey · ECR · S3), 온프렘은 복구 · CI(Jenkins · Harbor). 정상 사용자 경로에 VPN · 온프렘 없음 |
| 프로젝트 PC | 평일 상시 가동, **주말 종료**(주말 백업 · VPN · 작업 불가) |

### 1-1. 팀

| 이름 | GitHub | 담당 | 실행 책임 | 서버 |
|---|---|---|---|---|
| 이유빈 | ggbun2 | Network · Ansible · External Infra | bootstrap · foundation Terraform 실행 | Server-04 |
| 정태훈 | tjung03 | Kubernetes · 서비스 플랫폼 · Application (팀장) | rosa Terraform 실행, App 배포 | Server-01 |
| 김상희 (하차) | kshi1313-gif | DB · Storage · Backup/DR | Data 이관 · Restore | Server-02 |
| 최유준 | cyj200115-prog | Observability · CI/CD · Test · 비용 · Evidence Index | 시험 · 비용 조율 | Server-03 |

### 1-2. Data 영역 범위

- RDS for MariaDB Multi-AZ — 정상 서비스 주 DB
- ElastiCache **Valkey 7.2** — Runtime State(진행 중 게임 상태). **백업 대상 아님**. (10/6 Redis OSS에서 변경. Redis 프로토콜 호환, App 환경변수 `SEOKPAN_REDIS_*` · Secret 이름 `backend-redis-*` · Terraform 이름 `seokpan-fnd-redis`는 그대로)
- 1차 데이터 이관: 1차 온프렘 MariaDB → RDS, 논리 덤프 1회, 실사용자 데이터 그대로(가명화 안 함)
- 15분 백업: RDS → 백업 작업 VM(덤프 · gzip · age 암호화) → S3 `periodic/` → 복구 DB VM 사본
- Offline Recovery: AWS 없이 복구 DB VM에 복원 → 새 Recovery Redis → 복구 App. 목표 **RTO 10분 · DB RPO 30분**
- 종료 시 실데이터 삭제

---

## 2. 확정 설계값

### 2-1. 네트워크 (03 상세설계, foundation으로 생성)

- VPC `192.168.64.0/20` (`seokpan-fnd-vpc`), 3 AZ × (Public · ROSA Private · Data Private) /24
  - Data Private: `192.168.70.0/24` · `.71.0/24` · `.72.0/24`
- AZ 매핑: az_a = 2a(apne2-az1), az_b = 2b(az2), az_c = 2c(az3)
- VPN: EC2 WireGuard 1대 + EIP ↔ 온프렘 전용 VPN Gateway VM, 터널 `10.200.0.0/30`. **아직 미구성**(이유빈, Infra #16)
- NAT Gateway: 10/13 Apply 입력에서 제외됨
- 온프렘 → RDS 허용: 백업 작업 VM `192.168.52.50/32` 하나만 (`onprem_job_host_cidrs`, IPv4 `/32`만 허용하는 검사 있음)

### 2-2. Data 자원

| 자원 | 설정 |
|---|---|
| RDS | `seokpan-fnd-mariadb`, MariaDB 11.8.9, db.t4g.small, Multi-AZ, gp3 20GiB(자동 확장 끔), 자동 백업 7일, 마이너 자동 업그레이드 끔, 삭제 보호 켜짐, 파라미터 그룹(mariadb11.8): `time_zone = Asia/Seoul`, 1차와 같은 `sql_mode`, `require_secure_transport = 1`(코드에 `apply_method = "pending-reboot"`), utf8mb4_unicode_ci. 백업 창 17:00-17:30 UTC, 유지보수 일 18:00-19:00 UTC. `max_connections` 기본식으로 85 미만 |
| RDS 마스터 | `manage_master_user_password = true` → Secrets Manager(RDS 관리). **7일 자동 회전**. 다음 회전 창 **2026-10-20 09:00 ~ 10-21 08:59 KST**(UTC 하루 창). 회전 설정은 바꾸지 않기로 함 |
| RDS CA | `rds-ca-rsa2048-g1`, 서울 번들 `ap-northeast-2-bundle.pem` SHA-256 `913fb5b814f17af79d4c1622584a8d0ceddf5b0d76fe353d0c7d1186cdd6b229` |
| Valkey | `seokpan-fnd-redis`, engine `valkey` 7.2(파라미터 계열 `valkey7`), cache.t4g.small × 2(Primary + Replica, Multi-AZ, 자동 승격), `noeviction`, TLS + AUTH, 스냅샷 없음. Token은 `auth_token_wo` + `auth_token_wo_version = 1`(State · Plan에 저장 안 됨). 중지 기능 없음 |
| Backup S3 | `seokpan-fnd-backup-<계정ID>`, 버전 관리, `periodic/` 7일 만료 · `protected/` 보존, 버킷 정책 없음(HTTPS · 삭제 금지는 Backup User Boundary의 explicit Deny) |
| Backup IAM User | `seokpan-fnd-backup`, Boundary `seokpan-fnd-backup-boundary`. Access Key는 Terraform 밖에서 발급(**아직 미발급**) |
| Data SG | `seokpan-fnd-rds`(RDS: 온프렘 `/32` 규칙 1개), `seokpan-fnd-redis`(규칙 0개). egress 규칙 없음. ROSA Worker → Data SG 규칙은 **rosa State가 추가**(SG 본체만 foundation) |
| 이름 규칙 | foundation 자원 접두사 `seokpan-fnd-`, 태그 `Component = data` |

### 2-3. SQL 계정

| 계정 | 용도 | 권한 |
|---|---|---|
| `db_admin` | 구조 변경 · 가져오기 · Migration | `stone_game.*` DML · DDL (1차의 BINLOG/SLAVE MONITOR는 복사 안 함) |
| `identity_svc` | App 회원 | `member` CRUD(실제 사용은 SELECT · INSERT) |
| `game_svc` | App 게임 · 랭킹 | 게임 6개 테이블 + `member`의 컬럼 3개(`member_id`, `nickname`, `rating` SELECT · `rating` UPDATE) |
| `backup_dump` | 15분 백업 | `SELECT, SHOW VIEW, TRIGGER ON stone_game.*`, `REQUIRE SSL`, `MAX_USER_CONNECTIONS 2`, Host = 백업 작업 VM `/32` |

- 모든 계정 `REQUIRE SSL`, 비밀번호는 1차와 다르게 새로 발급(SOPS, 64자리 16진수)
- 생성 순서: `db_admin` · `backup_dump`(DB 단위) → 가져오기 → `identity_svc` · `game_svc`(테이블 · 컬럼 단위라 테이블이 있어야 GRANT 가능)
- 덤프에서 `--routines --events` 제외, 덤프 전에 Routine · Event · Trigger 0개 확인

### 2-4. 1차 원본 DB

- MariaDB 11.8.9, DB `stone_game` 1개, 테이블 8개, 약 0.36MB, utf8mb4_unicode_ci, KST, 날짜 컬럼 모두 DATETIME(±9시간 변환 안 함)
- View · Routine · Trigger · Event 0개, PK 없는 테이블 0개, FK 7개, Alembic revision `20260902_0002`
- 1차 Primary `mariadb-02` = `192.168.51.40`, Replica `mariadb-01` = `192.168.52.40`. 덤프는 **Replica**에서 `db_admin`으로(`read_only=1`, TLS)
- 1차 복제 이력: Primary가 mariadb-01 → 02로 바뀐 적이 있어 Replica `gtid_slave_pos`에 과거 도메인 `2-2-43`이 있음 → **GTID는 문자열 비교 금지, 도메인 단위로 "Primary ⊂ Replica" 확인**
- 시간대 계약: 게임 계열(game · move · game_result)은 App이 UTC 저장, 회원 계열(member · member_stats · rating_history)은 DB 세션 시간대(KST)
- 민감 컬럼: `member.login_id`, `member.password_hash`. 1차 회원 15명은 내부 인원의 시연용 임시 계정

### 2-5. 백업 · 복원 설계

- 주기 15분(`*:00/15`, `Persistent=false` — 주말 못 한 회차를 월요일에 몰아 실행하지 않음), 일반 사본 7일(실제로는 `-mtime +7`이라 7~8일)
- RPO 판정: 성공 백업 간격 + 로컬 도착 지연 + 시각 오차 ≤ 30분. 15분 Timer만으로 RPO를 보장한다고 하지 않음
- 백업 한 회차 순서: `flock` → `paused` 파일 확인(있으면 DB 접속 없이 SKIP 기록) → NTP · 시계 오차 1초 미만 → 디스크 100MiB → Routine · Event · Trigger 0 → Backup ID 결정(덤프 시작 시각 하나에서 `T_DUMP`와 함께) → 덤프 · gzip · age → S3 `periodic/` → (S3 성공) 그 S3 객체를 내려받아 / (실패) 로컬 파일을 `sp-copy`로 복구 DB VM에 전송 → `last-success`(S3 + 확보 모두 성공 시만) · `history.tsv`(OK / PARTIAL / SKIP / FAIL) → (S3 성공 OK 회차만) `s3-pending` 재전송 회당 최대 4개 · 300초
- Backup ID 형식: `<ID_PREFIX>-YYYYMMDDTHHMMSSZ` (예행 `rehearsal-…`, 운영 `periodic-…`)
- 복구 DB VM 사본: `/srv/seokpan-hybrid-recovery/copies/<Backup ID>.sql.gz.age` + `.sha256`, `.part`로 받다가 SHA-256 일치 시 정상 이름
- 복원 사본 자동 선택: `periodic-*`만, Backup ID 데이터 시각 최신순(파일 도착 시각 아님), SHA-256 실패 시 이전 사본. 예행 사본은 `--rehearsal` · `--id`로만
- 장애 시 판정 사슬: SHA-256 → age 해독 → gunzip → 가져오기 종료 코드 `0 0 0` → Revision · 테이블 8개. Schema 해시는 `AUTO_INCREMENT` 때문에 기준값으로 쓰지 않음
- `restore.sh`는 30분 넘은 사본도 막지 않는다 → **선택된 Backup ID 시각과 장애 시각(T0)을 사람이 대조해 RPO 판정**(Data 계약 v2.4 4.2절)

### 2-6. Recovery (장애 시 온프렘)

- 복구 DB: `192.168.54.60`, MariaDB 11.8.9, TLS 강제(Recovery DB CA), 3306은 worker-01 `192.168.51.30` · worker-02 `192.168.52.30` `/32`만. 복구 App `SEOKPAN_DATABASE_EXPECTED_HOST = 192.168.54.60`(IP 방식)
- 복구 계정 6개 미리 생성(`db_admin` · `identity_svc` · `game_svc` × Worker 2대). `DROP DATABASE` 뒤에도 계정 · 권한 유지됨(MariaDB 동작)
- Recovery Redis: Namespace `seokpan-recovery`, Valkey 7.2.14, 메모리 requests/limits 512Mi, `maxmemory 384mb`, `noeviction`, `save ""`, `appendonly no`, `emptyDir`. 전용 CA(Recovery DB CA와 분리), 서버 인증서 SAN `recovery-redis.seokpan-recovery.svc` · `.svc.cluster.local`(~2027-04-11), AUTH Token은 Cloud와 별도
- GitOps Recovery Bundle v2: 고정 덤프 대신 `database_restore`(Infra #48 · `ansible/data/controller/restore.sh` · periodic · `rpo_limit_seconds` 1800)

---

## 3. 현재 상태 (2026-10-13 22:00 KST, 하차 정리 반영)

### 3-1. 진행도

- 설계 100% · 코드 · 절차 100% · 환경 준비 약 89% · 실행 검증 약 52% → 전체 약 86%(Data 7개 영역 × 4단계 = 28칸 중 24칸)
- 요약: **VPN 전에 할 수 있는 Data 준비는 대부분 끝남. 남은 것은 VPN · ROSA · 팀 회신을 기다리는 실행 단계.**

### 3-2. AWS (10/13 16:12 KST 이유빈 foundation Apply, Terraform 1.16.4 · provider 6.67.0)

- RDS `available`, Multi-AZ, 삭제 보호, 대기 변경 0, **데이터 없음**(생성 이후 `DatabaseConnections` 최댓값 0), Endpoint 해시 `bce030b4bebb`
- Valkey 2노드 가동(과금 중), Backup S3 비어 있음, Backup User 키 없음
- Apply 뒤 Data 확인 `check_data_apply.sh`: **NG 0 · 54개 항목**(VPC 1 · SG 12 · RDS 16 · Valkey 13 · S3 7 · User 5)
- 재-Plan 변경 0 (PR #63 · #64 뒤, Infra #23)
- Data 출력 인계: 이유빈 controller `/home/ansible/.local/share/seokpan-hybrid/foundation-execution/actual-output-handoff-1r02rz2l/`(`ksh` 읽기만) — `c-data-outputs.json`(해시 `5541f3147882`, Data 9 + `vpc_id` · `network_subnets`) · `handoff-manifest.json`(`46d67ecebfc3`). `check_data_handoff.sh`로 일치 확인
- 정태훈 대조용 해시: `rds_address` `bce030b4bebb` · `rds_port` `757db91a8096` · `redis_primary_endpoint` `7ebc3226552f` · `redis_port` `48f599a9094e`
- NAT · VPN · ROSA 없음

### 3-3. 온프렘 VM

**백업 작업 VM**
- VMware 표시 `Hybrid-backup-01`, hostname `hybrid-backup-01`, Server-02(C:) · VMnet2 · `192.168.52.50/24` · 게이트웨이 vrouter-02 `.10` · DNS 8.8.8.8, 2 vCPU · 4GiB, CentOS Stream 9(커널 `5.14.0-590.el9`), root 로그인
- 디스크: OS 40GiB / `/dev/sdb` 10GiB → `/srv/seokpan-hybrid-backup`(xfs 라벨 `sp-backup`, `nodev,nosuid,noexec`, 700)
- 도구: MariaDB-client · common · shared · client-compat **11.8.9**(versionlock 4개), age v1.3.2, AWS CLI 2.37.5(자격증명 없음), chrony
- `/etc/seokpan-hybrid-backup/`: `recipients.txt`(백업 공개키 2줄: 김상희 · 이유빈), `ap-northeast-2-bundle.pem`, `backup.env`
- 스크립트 `/usr/local/sbin/seokpan-hybrid-backup`, `seokpan-hybrid-backup.service` / `.timer`
- 전송 키 `/root/.ssh/seokpan-hybrid-copy_ed25519`(암호 문구 없음, 무인 Timer용) → 복구 DB VM `sp-copy`
- 상태 폴더 `/srv/seokpan-hybrid-backup/state/`(`history.tsv` · `last-success` · `s3-pending` · `s3-resend.tsv`)
- **지금: Timer disabled · `source.cnf` 없음 · `backup.env`의 `ID_PREFIX=rehearsal`(전환 때 #44 10-4에서 `periodic`으로) · `S3_BUCKET` 비어 있음 · `paused` 없음 · `last-success` 없음**
- 전원을 껐다 켜면 VMware가 하드웨어 시계를 KST로 넣어 잠시 9시간 어긋남 → 백업 스크립트가 NTP 동기화를 확인한 뒤 시작
- `/srv/seokpan-hybrid-backup/rehearsal/`에 10/8 예행 폴더가 남아 있음(종료 때 #57 대상)
- 스냅샷 `baseline-tools-installed` → `paths-renamed`

**복구 DB VM**
- VMware · hostname `hybrid-recovery-db-01`, Server-04 C: · VMnet2 · `192.168.54.60/24` · 게이트웨이 vrouter-04 `.10`, 2 vCPU · 4GiB, CentOS Stream 9 커널 `575`
- 디스크: OS 40GiB / sdb 10GiB → `/var/lib/mysql`(xfs `sp-dbdata`) / sdc 5GiB → `/srv/seokpan-hybrid-recovery`(xfs `sp-recovery`, 700)
- MariaDB-server 11.8.9(versionlock 6개), `/etc/my.cnf.d/seokpan-hybrid-recovery.cnf` = bind `127.0.0.1,192.168.54.60` · `skip-name-resolve` · utf8mb4_unicode_ci · 1차 SQL Mode · KST · TLSv1.2/1.3 · `require_secure_transport = ON`
- 받기 전용 계정 `sp-copy`(비밀번호 잠금, `/srv/seokpan-hybrid-recovery`는 ACL `--x`) + `/usr/local/sbin/seokpan-recv-copy`
- 복원 도구 `/usr/local/lib/seokpan-hybrid-recovery/`(700 root): `restore.sh` · `table_hashes.sh`
- USB 호환성 3.x(2.0에서는 USB 인식 안 됨), exFAT 모듈 있음
- **지금: `stone_game` 없음 · `copies/` 비어 있음 · 복구 계정 6개와 권한만 있음**

### 3-4. controller (Ansible 서버, CentOS Stream 9, 팀원별 리눅스 계정)

- 김상희 계정 `ksh` — **하차 뒤 팀 공용 온프렘 Data 작업 공간(팀 공통 비밀번호). AWS 키 비활성화, GitHub 로그인은 김상희 계정 그대로 → `ksh`에서 AWS · GitHub 작업 금지(6-2절)**. 이유빈 `ansible`(키 사용은 이유빈 본인만 — 기술적 차단이 아니라 사용 규칙), 정태훈 `jth`
- 도구: Terraform 1.16.4(정확 고정) · AWS provider 6.67.0(lock) · AWS CLI 2.37.5 · SOPS 3.13.3 · age v1.3.2(`/usr/local/bin`) · controller의 `mariadb-dump`는 **10.5.29 — 11.8 원본 · RDS 덤프에 쓰지 않음**
- 전체 `dnf update` 금지, root로 Terraform 실행 금지
- MFA 세션: `source scripts/tf-session.sh <personal|bootstrap|foundation|rosa|clear>` → MFA 코드 → 1시간 세션
- `ksh` `~/recovery/`(700): 저장소와 같은 스크립트 + 예행 측정 기록 11개(`.times` · `.tsv`, 시각 · 해시만) + `ca/`(RDS 공개 번들)
- `ksh` `~/.ssh/seokpan-recovery_ed25519`(암호 문구, 복구 DB VM root에 `from="192.168.54.70"` 제한으로 등록), `~/.ssh/config` 별칭 `seokpan-recovery`
- controller IP `192.168.54.70` (Server-04)

### 3-5. 스크립트 기준본과 설치본 해시 (infra main `0b4497d` 이후, 설치본 = 저장소)

| 파일 (`ansible/data/…`) | SHA-256 앞 12자리 | 설치 위치 |
|---|---|---|
| `backup-vm/seokpan-hybrid-backup` | `1d99cc303d90` | 백업 작업 VM `/usr/local/sbin/` |
| `backup-vm/seokpan-hybrid-backup.service` | `c5d4df879a19` | 백업 작업 VM systemd |
| `backup-vm/seokpan-hybrid-backup.timer` | `ed1afefbbc1a` | 백업 작업 VM systemd |
| `recovery-db-vm/seokpan-recv-copy` | `f400647f9ff8` | 복구 DB VM `/usr/local/sbin/` |
| `controller/restore.sh` | `0440f66554ab` | controller `~/recovery/` · 복구 DB VM `/usr/local/lib/seokpan-hybrid-recovery/` |
| `controller/table_hashes.sh` | `5beac6da6e9c` | 위와 같음 |
| `controller/check_data_apply.sh` | `fe3d3c3dd03f` | controller `~/recovery/` |
| `controller/check_backup_gate.sh` | `9d21774a4255` | controller `~/recovery/` |
| `controller/check_data_handoff.sh` | `38fdd5431bb4` | controller `~/recovery/` |
| `controller/check_rds_master_secret.sh` | `893e0227574c` | controller `~/recovery/` |
| `tests/check_data_handoff_test.sh` | `382643895def` | 회귀 시험 11 Case(root 아닌 계정에서) |

- 고칠 때: 저장소 PR → merge → 설치 → 해시 대조. 이전 판은 백업 작업 VM `/root/seokpan-hybrid-backup.<해시>`에만 보관
- `restore.sh` 옵션: `--rehearsal` · `--id <Backup ID>` · `--select-only` · `--replace`(없으면 기존 DB 보호) · `--compare-src` · `--key <경로>`(권한 600/400, `AGE-SECRET-KEY-1` 검사) · `--local`(복구 DB VM root 콘솔에서 SSH 없이, 호스트 이름 검사, `--compare-src` 불가)
- **`restore.sh`의 기본 키 경로는 김상희 키(`ksh` 안)다 → `ksh`에서는 그대로, 다른 계정 · VM 콘솔에서는 `--key`를 준다**
- `check_backup_gate.sh` 종료 코드: 0 = 모두 OK, 1 = NG 하나라도, 2 = NG 없이 판정 불가(`MIN_OK` 2 이상, 1시간 판정은 `MIN_OK=5`)

### 3-6. 비밀값 위치 (값은 없음)

| 비밀값 | 위치 | 열 수 있는 사람 | 해시 |
|---|---|---|---|
| Valkey AUTH Token | `~/secrets/seokpan/foundation-data.sops.yaml` | 김상희 · 이유빈 · 정태훈 | `9a86f90e6ba6` |
| Cloud SQL 비밀번호 4개 | `~/secrets/seokpan/data-sql-accounts.sops.yaml` | 같은 3명 | `021bd0da994a` |
| 복구 SQL 비밀번호 3개 | `~/secrets/seokpan/recovery-sql-accounts.sops.yaml` | 같은 3명 | `ce2d6eeca6fc` |
| Recovery Redis(인증서 · 키 · CA · AUTH 5개 키) | `~/secrets/seokpan/recovery-redis.sops.yaml` | 같은 3명 | `4c931e6240e0` |
| RDS 마스터 비밀번호 | AWS Secrets Manager(RDS 관리) | IAM 사람 사용자 4명(personal MFA 세션) | ARN 해시 `f3e3c0cd0fe2` |
| 백업 해독 키 | 김상희: `ksh` `~/secrets/seokpan/backup-age/backup-kimsanghee.key`(`4a11b7dda5af`) + `age -p` 잠금 사본 / 이유빈: `ansible` 계정 + 잠금 사본(이유빈 USB, exFAT) | 김상희 키: `ksh`로 로그인한 팀원(하차 뒤 공용) · 이유빈 키: 이유빈 본인 | — |
| Recovery DB CA | `ksh` `~/secrets/seokpan/recovery-ca/`(`ca.key` 암호 문구, `ca.crt` `0d6b4a51439a` ~2027-10-07, `server.crt` `4202fae21f74` ~2027-04-05, `server.ext` · `server.csr` · `ca.srl`) + Windows 오프라인 사본(6-3절) `recovery-ca-offline-20261007.tar.age`(묶음 해시 `e6dfd7652b07dc63`, `age -p` 잠금) | 암호 문구 = 팀 공통 비밀번호. `ksh` 계정으로 로그인해 사용 | — |
| Recovery Redis CA | `ksh` `~/secrets/seokpan/recovery-redis-ca/`(`ca.key` 암호 문구 · `ca.crt` CA 지문 `9c3e26bd…2efc` ~2027-10-13 · `ca.srl`) + Windows 오프라인 사본(6-3절, 묶음 해시 `b6a7e0643a78`, 사본 안 `ca.key` = `44545145d05e`) | 암호 문구 = 팀 공통 비밀번호. 위와 같음 | — |

- SOPS 파일은 `ksh` · `ansible` · `jth` 세 홈에 같은 파일(600). sops는 `~/.config/sops/age/keys.txt`를 자동으로 읽음. 표의 "김상희" 몫(`ksh`)은 하차 뒤 `ksh`로 로그인한 팀원이 쓴다
- 김상희 SOPS용 age 개인키: `ksh` `~/.config/sops/age/keys.txt`. 오프라인 사본 4개(Recovery DB CA · Recovery Redis CA · 백업 해독 키 · SOPS 키)의 위치와 해시는 6-3절
- 백업 해독 키(age)와 SOPS용 age 키는 **서로 다른 키**
- Valkey Token 공급(Terraform): infra README "Redis Token 공급 절차" — subshell 안에서 `TF_VAR_redis_auth_token`으로만, 끝나면 unset. ephemeral 값이라 plan과 저장된 plan의 apply 모두 같은 SOPS 원본으로 공급

### 3-7. 김상희 Windows PC의 파일 (교육장 PC `desktop-qacm9s0`, 사용자 `soldesk`, 10/14 확인)

작업에 꼭 필요한 파일은 PC에 없다. 스크립트 · 패치 기준본은 infra `ansible/data/`, 설치본은 controller · VM. **PC 파일을 근거로 명령을 안내하지 말 것.**

**프로젝트 작업 폴더 `C:\하이브리드 클라우드 09\Project\2차\`**

| 폴더 · 파일 | 내용 | 처리 |
|---|---|---|
| `보안\` | 오프라인 사본 4개(6-3절) | 후임에게 전달 |
| `VPN 연결\` (README · TEST-PROCEDURE · vpn-report.zip) · `vpn-report\` | VPN PoC 보고서 · 시험 절차 | 이유빈에게 전달 권장(#16). 공인 IP 포함 → 팀 내부만 |
| `스크립트\` | 스크립트 5개 | 쓰지 않음. `table_hashes.sh`(`5beac6da6e9c`) · `check_rds_master_secret.sh`(`893e0227574c`)만 저장소와 같고, `restore.sh`(`e6444667ff47`) · `check_data_apply.sh`(`51f536301969`) · `check_backup_gate.sh`(`63e59d8bf0c2`)는 10/8 옛 판 |
| `패치파일\` | 패치 8개 | 불필요(모두 PR로 반영) |
| `문서\` | 설계 문서 사본 · Data 계약 v2 · v2.2 · lab Redis 기준 · 이관 Runbook v1 · worklog(10/13 21:24) · `i44_v20.py` | 이력. 최신은 docs 저장소 · #19 · #44 · Project 지식 |
| `foundation-data-draft\` · `HANDOFF_foundation_data.md` · `link-fix-20261008\` · `data-resend-checks-pr.md` | 작업 초안 | 불필요 |
| `실습환경\` | OCP 실습 서버 접속 정보(RDP · xlsx) | 접속 정보 포함 → 팀 내부만 |
| `기획안\` · `아키텍처\` · `이미지\` | 기획안 · 그림 | 팀 공용 자료와 같음 |

**`C:\Users\soldesk\Downloads`**

| 파일 | 내용 | 처리 |
|---|---|---|
| `vpn-onprem-aws-proposal.md` · `vpn-report.zip` · `vpn-test-report.pdf` | VPN PoC | 위 `VPN 연결\`와 같은 자료 |
| `check-db-runtime (1).sh` · `.zip` | lab DB 실행 Gate 확인 스크립트(조회만, GitOps #26). 저장소에 없는 유일한 사본 | 선택 |
| `RDS_SSL_권한_검토.md` · 두 패치 · `README.md` · `terraform-version-guide.md` · 옛 worklog · `progress-20261007-*.png` | 이력 · 초안 | 불필요 |
| `terraform.json` | Terraform State 사본(계정 번호) | 공유 금지 · 삭제 권장 |
| `event_history.json` | CloudTrail 내보내기(계정 번호 · Access Key ID · IP) | 공유 금지 · 삭제 권장 |

---

## 4. Runbook과 주요 Issue 색인

Runbook은 infra Issue 본문이 최신 기준본(맨 위 버전 줄), 변경 이력은 코멘트. 실행 검증 후 docs로 옮기고 Close한다.

| Issue | 판 | 내용 |
|---|---|---|
| [Infra #44](https://github.com/seokpan/seokpan-hybrid-infra/issues/44) | v2.5 | 1차 → RDS 이관. 실행 순서 0 → 1 → 3 → 4 → (쓰기 중지) 1-1 → 2 → 5 → 6 → 7 → 8 → 9 → (전환 판단) → 10 |
| [Infra #45](https://github.com/seokpan/seokpan-hybrid-infra/issues/45) | v1.4 | RDS Stop / Start. 이관 전이면 3-0 분기 |
| [Infra #46](https://github.com/seokpan/seokpan-hybrid-infra/issues/46) | v1.4 | 복구 DB VM 구성 기준 |
| [Infra #48](https://github.com/seokpan/seokpan-hybrid-infra/issues/48) | v1.5 | 복원 절차. C장 = controller 없이 복구 DB VM 콘솔에서 |
| [Infra #57](https://github.com/seokpan/seokpan-hybrid-infra/issues/57) | — | 종료 시 실데이터 삭제 D1 ~ D8 |
| [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19) | — | foundation Data · Data 계약 · 비밀값 공급 기록 |
| [Data 계약 v2.4](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6143942560) | v2.4 | App · GitOps와의 약속. App #1 · GitOps #6이 이 코멘트를 가리키므로 작은 개정은 **같은 코멘트를 고쳐 쓰고** 변경 기록 코멘트를 따로 단다 |
| [Infra #23](https://github.com/seokpan/seokpan-hybrid-infra/issues/23) | — | foundation 통합 · 출력 인계 |
| [Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) | — | 1차 DB 점검 · 이관 범위 · 실데이터 취급 조건 · 1차 쓰기 중지 합의 |
| [Infra #16](https://github.com/seokpan/seokpan-hybrid-infra/issues/16) | — | VPN · Cost 입력 |
| [Infra #55](https://github.com/seokpan/seokpan-hybrid-infra/issues/55) | — | S3 실패 사본 재전송. V4(실제 S3 재전송 확인)만 남음 |
| [Infra #41](https://github.com/seokpan/seokpan-hybrid-infra/issues/41) | Closed | 백업 해독 키 2명 등록 방식 |
| [Infra #60](https://github.com/seokpan/seokpan-hybrid-infra/issues/60) | Closed | controller 없는 복원 |
| [Docs #43](https://github.com/seokpan/seokpan-hybrid-docs/issues/43) | — | Cost Gate Data 입력 |
| [Docs #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8) | — | 팀 인계 연결 |
| [Docs #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) | — | 발표 Evidence 후보 |
| [Docs PR #107](https://github.com/seokpan/seokpan-hybrid-docs/pull/107) | merged | 정태훈 1차 쓰기 중지 준비(`execution/FIRST_SERVICE_WRITE_STOP_PREPARATION.md`) |
| [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) · [GitOps #6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) | — | Data 계약을 받는 쪽 |

docs 진행 기록: `execution/05_IMPLEMENTATION_AND_VALIDATION.md` 8장(Data는 8.10절 ~ 8.29절), `execution/WORK_TRACKER.md`, `execution/HANDOFF_TEMPLATE.md`.

### 4-1. 이관 Runbook #44 핵심 (v2.5 기준 — 실행 전 Issue 본문 재확인)

- **0-A:** 인계 파일에서 `ho` 함수로 RDS 주소 · Secret ARN · 버킷 이름을 읽음 + `rot_check`(회전 창 확인)
- **0-1:** foundation Apply · 출력 수신 · 자원 확인 — **완료**
- **0-2 경로 · 0-3 TLS 실제 접속:** VPN 뒤
- **0-12:** 3단계 앞 `rot_check 1800`, 쓰기 중지 요청 전 `rot_check 7200`
- **1단계:** 1차 Replica 접속 파일 · 접속 확인 · 객체 수 · Revision
- **3 · 4단계:** RDS 마스터 접속, DB 단위 계정(`db_admin` · `backup_dump`) — 쓰기 중지 전에 함. 마스터 접속 파일은 controller personal 세션에서 읽어 ssh 표준입력으로 백업 작업 VM 0600 파일로, 4단계 끝에 삭제 → 7단계 직전 3단계 재실행 → 8단계 끝 삭제
- **1-1단계(쓰기 중지 뒤):** 복제 반영 확인 — 덤프 직전 · 직후 Primary `gtid_binlog_pos`의 모든 도메인 값이 Replica `gtid_slave_pos`에 있음 + IO · SQL Yes · 지연 0 · 오류 0 + Primary = Replica `stone_game` 해시. 하나라도 다르면 덤프 폐기. 비교는 controller에서 `ssh root@192.168.52.50 'bash -s -- --expect-tables 8 --defaults-extra-file=<cnf>' < ~/recovery/table_hashes.sh`, 결과는 `~/recovery/mig/`(`pre-primary` · `pre-replica` · `src` · `rds`.tsv)
- **2단계:** 덤프 → gzip → age (예행: 1초 미만, 암호문 20,423바이트, 압축 전 107,140바이트)
- **5 · 6단계:** RDS 가져오기 → 비교(`pre-replica = src` = `rds`)
- **7 · 8단계:** 테이블 · 컬럼 단위 계정 · 연결 입력 인계
- **9단계:** Cloud 시험 쓰기(정태훈) → 전환 / 복귀 판단(정태훈). **복귀하면 이번 RDS 데이터는 버리고 1-1부터 새 덤프**
- **10장(전환 결정 뒤):** 10-1 Backup User 키를 controller에 남기지 않고 VM으로 바로 · 10-2 S3 권한 · 10-3 `source.cnf` = `backup_dump@RDS` · 10-4 `S3_BUCKET` · **`ID_PREFIX=periodic`** · 손 실행 1회 · Timer · Gate(`check_backup_gate.sh`) · `@@max_connections` 전달. 10-5: S3 장애 뒤 재전송 속도(OK 회차마다 4개, 2시간 장애 → 약 30분)
- 시간: 쓰기 중지 구간 Data 몫 약 39분(1-1 ~ 6 24분 + 7 · 8 15분), 전체 중지 예산 75분
- 시작 조건: 준비(0 · 1 · 3 · 4)는 foundation Apply 뒤(VPN 필요), 최종 쓰기 중지는 ROSA Ready · 배포 입력 준비 뒤
- 1차 쓰기 중지 실행은 정태훈 담당(Argo CD 자동 Sync · SelfHeal 때문에 `scale`만으로 0 유지가 안 될 수 있음)

### 4-2. RDS Stop Runbook #45 핵심 (v1.4)

- 계획: 10/15 저녁 ~ 10/19 아침 Stop(주말 포함), 이관 · 검증 창은 가동, 10/22 이후 미정
- RDS는 Stop 7일 뒤 자동 Start → 6일째 수동 Start. Apply는 `available`일 때만. 수동 스냅샷 옵션 안 씀
- 이관 뒤: Stop 전 마지막 사본의 복구 DB VM 도착(SHA-256) 확인(3-1 · 3-2), `paused` 파일 생성(한 줄: UTC 시각 · 사유 · Issue 링크), Start 후 백업 1회 성공 = 재개. `paused`는 #45만 만들고 지움
- **이관 전(지금): 3-0 분기** — 근거 4가지(#44 5단계 미실행 · 생성 이후 최대 DB 연결 0 · Timer disabled · ROSA 없음) 모두 맞으면 Stop. Start 뒤 `available` · Endpoint 해시만 확인. 하나라도 다르면 Stop 보류
- 10/15 Stop 여부는 **팀 결정 전**

---

## 5. 남은 작업 (순서대로)

### 단계 1 — 지금 바로 (선행 조건 없음)
- [ ] 10/15 저녁 RDS Stop 여부 팀 결정 → Stop하면 #45 3-0 → 걸린 시간 실측 → #45 v1.5
- [ ] Windows 오프라인 사본 전달(6-3절)
- [ ] (팀 확인 후) Backup User Access Key 발급 · S3 권한 시험(#44 10-2를 앞당김) → V4 실제 S3 재전송 확인(#55)
- [x] Data 인계의 `jth` 읽기 접근·파일/manifest 결속·연결 값 네 개 해시 대조 완료(10/14 정태훈 회신). 계약 상태 정정·#19 기록은 후속.
- [ ] (선택) 회귀 시험 자동 CI(PR #66 리뷰 의견)

### 단계 2 — VPN 뒤 (이유빈, Infra #16)
- [ ] #44 0-2(경로 · 출발지 IP 보존) · 0-3(TLS 실제 접속)
- [ ] #44 1 · 3 · 4단계(쓰기 중지 전 준비), `@@max_connections` 실측

### 단계 3 — ROSA Ready · 배포 입력 준비 뒤 (정태훈)
- [ ] 쓰기 중지 1-1 → 2 → 5 → 6 → 7 → 8 → 9(정태훈) → 전환/복귀 판단
- [ ] Valkey CA: `openssl s_client`로 체인 · SAN 확인 → `backend-redis-ca` ConfigMap 공급, Runtime 계정 출발지 IP 확인
- [ ] Recovery Redis Secret 3개 · ConfigMap 2개를 `seokpan-recovery`에 공급(경로는 정태훈 결정) → Token 해시 대조

### 단계 4 — 전환 결정 뒤
- [ ] #44 10장: `source.cnf` → `S3_BUCKET` · `ID_PREFIX=periodic` → 손 실행 → Timer enable → `check_backup_gate.sh`(첫 RDS/S3 OK 회차에서 `last-success` = ID 시각 = `T_DUMP`, S3 → 복구 VM SHA, 15분 간격, 로컬 확보 지연)

### 단계 5 — 본 검증 10/19 ~ 21
- [ ] `restore.sh` → 복구 App(정태훈) → RTO · RPO 측정(T18 Run). 결과는 docs `evidence/<test-id>/<run-id>/`
- [ ] 회전 창 **10/20 09:00 ~ 10/21 08:59 KST**에는 #44 3 · 4 · 7 · 8단계 시작 금지

### 단계 6 — 종료
- [ ] 삭제 Runbook #57: Timer 끔 → S3 비우기(모든 버전, personal 세션) → Backup User 키 삭제 → 삭제 보호 해제 Apply → Destroy → 최종 스냅샷 삭제 → 복구 DB `DROP` → VM 삭제 → 키 마지막. 담당 · 날짜 · Destroy 범위는 팀 합의
- 참고: 김상희가 10/13 낸 마감 일정안(10/16까지 Apply · ROSA · 부하 시험 뒤 AWS · ROSA 종료, 10/17 ~ 18 고정 PC 종료, 10/19 ~ 22 발표 준비, 10/23 재구성, 10/24 ~ 26 유지, 10/26 16시 이후 전체 삭제)은 **팀 결정 전**

### 5-1. 회신 대기

김상희가 물어 둔 질문들이다. 하차 뒤에는 Data 후임이 답을 받아 처리한다.

| 답할 사람 | 질문 |
|---|---|
| 이유빈 | VPN 경로 · 출발지 IP 보존(#16). Data 인계의 `jth` 읽기 ACL은 10/14 완료 |
| 정태훈 | Endpoint 해시 네 개 대조는 10/14 통과 회신 완료. 1차 쓰기 중지 실제 경로 · 계정(Docs PR #91 · #107), 복귀 때 RDS `stone_game` 처리, Recovery Secret · ConfigMap 공급 경로, Valkey 7.2.14 Image에 `redis-server` 실행 파일 유무, DB Pool 상한(App이 Pool 환경변수를 읽는지), 복구 App Pod 출발지 IP, rosa Data SG 입력(`mariadb` ← `rds_security_group_id`, `redis` ← `redis_security_group_id` — rosa 검사로는 두 ID가 바뀐 것을 못 잡으므로 Apply 직후 이름 대조) |
| 최유준 | Valkey 단가 반영 Cost Gate(Docs #43), 10/22 이후 RDS(#45 — 이유빈 "시연 구간만", 정태훈 "10/21 후 Stop", 최유준 "10/22 삭제"로 의견이 갈림) |

---

## 6. 하차에 따른 처리

### 6-1. 하차 정리 결과 (2026-10-13 22:00)

| 항목 | 결과 |
|---|---|
| `ksh_data` Access Key | **비활성화(Inactive) 확인** — `ksh`에서 `aws sts get-caller-identity` 실패. 콘솔 암호는 원래 비활성. 사용자는 삭제하지 않음(TF 실행 Role 신뢰 정책에 사람 4명이 들어 있음) |
| `ksh` MFA 세션 | `tf-session.sh clear`로 해제 |
| `ksh`의 GitHub 로그인(김상희 계정) | **유지**(김상희가 하차 뒤에도 GitHub를 계속 씀). `ksh`에서 `git pull`은 됨, push는 안 됨 |
| GitHub 기록(Issue 담당자 · WORK_TRACKER · Docs #8 · 05 문서 8.30절) | 보류 |

### 6-2. `ksh` 공용 계정 규칙 (중요)

controller `ksh` 계정은 팀 공용 **온프렘 Data 작업 공간**으로 남긴다. 비밀번호는 팀 공통 비밀번호. 팀원은 각자 PC에서 VS Code Remote-SSH 또는 ssh로 `ksh`에 로그인해 김상희가 쓰던 파일 · 키 · 스크립트를 그대로 쓴다. CA 개인키 · 오프라인 묶음의 암호 문구도 팀 공통 비밀번호다.

- **`ksh`에서 하는 일:** `~/recovery/` 스크립트, 백업 작업 VM(`ssh root@192.168.52.50`, root 비밀번호) · 복구 DB VM(`ssh seokpan-recovery`, 키 암호 문구) 접속, SOPS 해독(`~/.config/sops/age/keys.txt` 자동), CA 사용, `git pull`로 최신 스크립트 받기 → 설치 → 해시 대조
- **`ksh`에서 하지 않는 일:** AWS 작업(키가 꺼져 동작 안 함), GitHub Issue · PR · 코멘트(`ksh`의 GitHub 로그인은 김상희 계정이라 기록이 김상희로 남음)
- **AWS가 필요한 단계는 각자 계정에서** `source scripts/tf-session.sh personal`(자기 IAM · 자기 MFA): #44 0-A `rot_check` · 3단계(마스터 비밀번호 읽기) · 10-1 · 10-2, `check_data_apply.sh` · `check_backup_gate.sh` · `check_rds_master_secret.sh`. 스크립트는 저장소 `ansible/data/controller/`에서 자기 홈 `~/recovery/`로 복사하고 해시 대조. 백업 작업 VM은 root 비밀번호 SSH라 어느 계정에서도 접속 가능. 이유빈의 Data 출력 인계 파일은 `ksh` · `jth`만 읽을 수 있음 → 다른 계정은 이유빈에게 권한 요청. AWS와 복구 DB VM을 함께 조회하는 스크립트(예: `check_backup_gate.sh`)를 자기 계정에서 돌릴 때 복구 DB VM SSH가 막히면 자기 계정 키를 복구 DB VM에 등록(#46 방식)해야 할 수 있음 — 처음 실행 때 확인
- **`restore.sh` 키:** `ksh`에서는 기본 키(김상희 백업 키)로 그대로 됨. 자기 계정 · 복구 DB VM 콘솔에서는 `--key <자기 키>`
- **기록:** Issue · 05 문서에 "`ksh` 계정, 실제 수행자 ○○○"
- **동시 사용 주의:** 두 사람이 `ksh`로 같은 폴더(`~/recovery/mig/` 등)를 동시에 쓰지 않게 팀 메신저에 먼저 알림
- **#44 이관 Runbook 실행 계정 (중요):** #44 본문의 명령 주석은 "controller (ksh) — personal 세션"이지만 `ksh`는 AWS 불가라 0-A · 3 · 10-2단계가 그대로는 실패한다. **이관은 처음부터 끝까지 이유빈 `ansible` 계정에서 실행하도록 안내하라.** `ansible`에는 자기 IAM · MFA, SOPS 파일(`data-sql-accounts`), 이유빈 백업 해독 키, Data 출력 인계 파일(이유빈 본인 폴더)이 이미 있다. 바꿀 것은 두 가지: ① `ansible` 홈에 `~/recovery/` 생성 · 저장소 `table_hashes.sh` 복사 · 해시 `5beac6da6e9c` 대조 ② 5단계 `age -d -i`의 키 경로를 이유빈 키로. 10-7(운영 Gate)만 복구 DB VM SSH 키가 필요 → `ansible` 키를 복구 DB VM에 등록하거나 그 확인만 `ksh`에서 나눠 실행

### 6-3. 남은 하차 정리 — Windows 오프라인 사본

원본은 모두 controller `ksh`에 그대로 있다. 아래는 controller가 망가졌을 때를 위한 예비 사본이다. 위치: **`C:\하이브리드 클라우드 09\Project\2차\보안\`** (김상희 교육장 PC). 10/14 기록 해시와 대조함(해독 안 함). 4개 모두 `age -p` 잠금(암호 문구가 팀 공통 비밀번호인지는 김상희 확인 필요). 후임에게 폴더째 넘기고 받은 쪽에서 `Get-FileHash`로 대조.

| 파일 | SHA-256 앞자리 | 내용 | 원본 |
|---|---|---|---|
| `recovery-ca-offline-20261007.tar.age` | `e6dfd7652b07dc63` | Recovery DB CA(`ca.key` · `ca.crt` · `server.ext` · `ca.srl`) | `ksh` `~/secrets/seokpan/recovery-ca/` |
| `recovery-redis-ca-offline-20261013.tar.age` | `b6a7e0643a78` | Recovery Redis CA(`ca.key` · `ca.crt` · `ca.srl`) | `ksh` `~/secrets/seokpan/recovery-redis-ca/` |
| `backup-kimsanghee.key.age` | `28c03eb0f8ce64b9` | 김상희 백업 해독 키 잠금 사본(이유빈 USB에도 같은 파일) | `ksh` `~/secrets/seokpan/backup-age/` |
| `keys.txt.age` (10/6) | `e49d45516847cc8d` | 김상희 SOPS용 age 개인키 잠금 사본 — SOPS 파일 4개의 김상희 몫을 여는 키 | `ksh` `~/.config/sops/age/keys.txt` |

### 6-4. 선택 사항
- 백업 받는 사람(김상희 키) 교체: `ksh` 공용 키로 그대로 쓰면 할 일 없음. 교체한다면 실제 백업이 0개인 지금이 가장 쉬움(#41 방식으로 새 보관자가 직접 키 생성 → `recipients.txt` 김상희 줄 교체)
- SOPS 받는 사람은 그대로 둬도 됨(`ksh` age 키로 열림)

### 6-5. 분담할 경우 제안
| 사람 | Data 작업 |
|---|---|
| 이유빈 | 백업 작업 VM · 이관 0 ~ 8단계 · 10장 백업 시작 · RDS Stop/Start · 복원 실행(해독 키 보유, `--local` 예행 성공) |
| 정태훈 | 1차 쓰기 중지 · 9단계 전환 판단 · Recovery Redis 공급 · 복구 App |
| 최유준 | Cost Gate Data 행 · Gate 판정 기록 · RTO/RPO Evidence · 삭제 일정 조율 |

---

## 7. 작업 규칙

### 7-1. 협업 규칙
- Git: 브랜치 `infra/<이슈번호>-<작업명>` · `docs/<이슈번호>-<작업명>`, 터미널에서 생성. push는 개인 PAT, Issue · PR은 GitHub 웹에서
- push 직전 `git fetch origin && git merge origin/main --no-edit`, `git diff origin/main --stat`로 내 변경 확인
- infra · app · gitops: main-protection(PR + 승인 1명, squash만). docs: 보호 없음, **작성자가 리뷰 없이 merge**(수정이 다 끝난 뒤)
- PR 생성 후 사이드바 Development 칸이 비어 있는지 확인(연결돼 있으면 merge 때 Issue가 닫힘). 본문 Issue 번호는 만든 직후 확인
- 리뷰어는 코드와 PR 본문의 일치를 승인 조건으로 본다 → 코드를 고치면 본문도
- merge된 PR 브랜치는 원격에서 지워짐 → 후속 수정은 main에서 새 브랜치. 로컬 삭제는 `git branch -D`(squash라 `-d` 거부)
- 다른 사람 담당 작업을 대신 하면 "배정 실행자 / 실제 수행자"를 나눠 기록(04 문서 2.4절)
- 공용 lab 서버는 담당 Owner가 조회 전용 스크립트를 실행하고 Data 담당은 결과로 판정, 기록은 "실행 / 판정" 분리
- docs 05 문서에 새 절을 넣을 때 `grep -n '^## \|^### 8\.'`로 위치 · 번호 확인
- 설계 근거는 Project 지식 사본이 아니라 docs main 최신본에서 확인

### 7-2. 실데이터 취급(Infra #17)
- 덤프 · 행 내용은 저장소 · Issue · PR · Evidence 금지(행 수 · 관계 · SHA-256만)
- 생성 즉시 age 암호화, 평문은 디스크에 쓰지 않고 파이프로만(필요하면 `/dev/shm` 후 `shred -u`)
- 종료 후 RDS · 최종 스냅샷 · 자동 백업 · S3 모든 버전 · VM 사본 · 복구 DB 데이터 삭제(#57)

---

## 8. 자주 한 실수와 셸 함정

- 명령 예시의 `<...>` 자리표시를 그대로 붙이면 bash가 `<`를 입력 기호로 읽어 변수가 비고, 빈 입력 해시 `e3b0c44298fc`가 "같다"처럼 보인다 → 빈 값 해시도 실패로 본다
- 암호 문구를 묻는 명령(`ssh-add` · `scp` · `ssh-keygen -p` · `age -p` · `openssl genpkey/req -x509/x509 -req`)은 **한 줄씩 단독 실행**. 블록으로 붙이면 남은 줄바꿈이 빈 암호 문구로 들어가 조용히 실패
- `age -p`에서 빈 Enter → 암호 문구를 자동 생성해 화면에 출력. 반드시 직접 입력
- `export A=$(cmd) && …` → `cmd`가 실패해도 종료 코드 0. `A=$(cmd) && export A`로 나눈다
- 조건 확인은 `|| echo "…"`가 아니라 `if … then … else … fi` (echo로는 다음 명령이 멈추지 않음)
- `cmd > file`은 실패해도 빈 파일을 남긴다 → 비밀값 블록은 `trap`으로 임시 파일 삭제 보장 + 임시 이름에 쓰고 성공 시 `mv`
- `ssh` 접속과 그 뒤 명령은 나눠서 붙여넣기(프롬프트가 바뀐 것 확인). `su -`와 다음 명령도 마찬가지 → `su -c '…'`
- 붙여넣기 전에 프롬프트(호스트 · 계정) 확인, `cd 경로 && 명령`으로 묶기(VM root 창에서 `cd` 실패 뒤 `chmod 600 *` 실행 사고)
- 1차 VM에서 새 VM으로 접속하지 않기(1차 VM `known_hosts`가 바뀜). 새 VM 작업은 controller에서
- VM root의 `rm`은 `-i` 별칭
- VS Code 탐색기로 끌어다 놓아 바꾸면 실행 권한이 빠짐(100755 → 100644) → 커밋 전 `git diff --summary`가 빈 출력인지
- 파일을 바꾼 직후 해시부터 확인(저장 안 된 채 다음 단계로 간 적 있음). 저장 전에 커밋 블록을 붙이면 "커밋할 사항 없음"
- 비슷한 행이 이어진 표(README 해시 표)는 파일 이름으로 찾아 고치고, 커밋 전 `git diff … | grep '^[-+]|'`로 바뀐 행 이름 확인
- 패치 적용 순서: 해시 → `git apply --check` → `git apply` → 해시 · 권한 · `git diff --stat` · `git diff --summary`
- 긴 문장 치환은 "원문이 정확히 1번 있을 때만" 바꾸는 python 스크립트로
- "문서용" 블록과 "실행용" 블록을 구분(문서용을 실행해 `umask 077` · `trap` · 빈 `/dev/shm` 파일이 남은 적 있음)
- 파일 이름만 보고 내용 추정 금지(`backend-reference.json`은 Endpoint가 아니라 State 참조였음) → 받은 사람에게 키 이름(값 제외) 확인
- GitHub 코멘트가 많으면 중간이 "Load more"로 접힘 → 코멘트 URL(`#issuecomment-…`)로 바로 열기
- GitHub 편집기에서 `#번호` 뒤 `)`가 추천 창 때문에 빠질 수 있음 → 저장 후 새로고침 확인. 게시 뒤 링크 클릭 확인
- "조회만" 확인 스크립트는 실패 경로에서도 아무것도 쓰지 않게(쓰기 시험 대신 `[ -w ]`), 해시 비교는 정해진 필드로만(PR #66 BLOCKER)
- `tf-session.sh` 출력의 "실행 주체" 줄에는 계정 번호 → Issue에 붙이지 않음. 확인 스크립트 OK · NG 줄은 붙여도 됨
- MFA 세션은 1시간, 세션마다 새 MFA 코드
- VMware 콘솔은 붙여넣기 · 한글 입력 불가 → 짧은 명령, 한글 경로는 글롭, 결과는 사진
- `information_schema.tables.update_time`은 재시작 뒤 비어 있을 수 있음 → 마지막 쓰기 시각은 날짜 컬럼 `MAX()`로

---

## 9. 판정 기준값

| 항목 | 기준 |
|---|---|
| 이관 비교 | 당일 최종 덤프 시점의 테이블 8개 행 수 · 정렬 행 해시 · Schema 해시 · Revision `20260902_0002`(10/2 · 10/8 값은 이력) |
| 복제 반영 | Primary `gtid_binlog_pos` 모든 도메인 ⊂ Replica `gtid_slave_pos`, IO · SQL Yes, 지연 0, 오류 0, Primary = Replica 해시 |
| Apply 직후 Data | `check_data_apply.sh` NG 0 (54개 항목). `require_secure_transport`는 출처(`engine-default`)와 무관하게 값 `1`로 판정 |
| 백업 Gate | 사본 이름 시각 = `T_DUMP` = `last-success`, history · S3 객체 · 복구 DB VM 사본 · `.sha256` SHA-256 일치, 15분 ± 60초 간격, 로컬 확보 지연 ≤ 300초, 데이터 나이 ≤ 30분 |
| 복원 | SHA-256 → 해독 → gunzip → 종료 코드 `0 0 0` → Revision · 테이블 8개 · 계정 6개. RPO는 선택 Backup ID 시각 vs T0 |
| DR 목표 | RTO 10분(장애 시작 → 대표 업무 · 데이터 확인) · RPO 30분 |
| 연결 예산 | (Pod당 연결) × (최대 Pod 4 + 종료 중 1) + 예약 10 ≤ `max_connections`(85 미만). 후보 Pool 3+2 → 60. App이 Pool 환경변수를 읽게 된 뒤 확정 |

### 9-1. 예행 실측(참고, 공식 결과 아님)
- 백업 1회: 1초 미만, 암호문 20,423바이트
- 복원 0~4단계: 손 23초 → `restore.sh` 2초(controller 방식)
- controller 없는 복원(이유빈 키, VM 콘솔 `--local`): 키 해독 시작 → 검증 끝 4분 43초(USB 연결 제외)
- Timer: 1시간 4회 모두 15분 00초, 시계 오차 0.0001초 미만
- 이관 예행: 1단계 26초, 1-1단계 약 11초, 2단계 1초 미만
- 백업 용량(N = 793): 복구 DB VM 약 24MiB, 백업 작업 VM 약 20MiB, S3 약 15MiB, S3 전송 하루 약 2MB

---

## 10. 주요 결정 기록 (최근 → 과거, 요약)

| 날짜 | 결정 |
|---|---|
| 10-13 | 김상희 하차: `ksh`는 팀 공용 온프렘 Data 작업 공간(팀 공통 비밀번호), `ksh_data` Access Key 비활성화, `ksh`의 GitHub 로그인은 유지(김상희 계정) → `ksh`에서 AWS · GitHub 작업 금지 |
| 10-13 | 이관 전 RDS Stop은 #45 3-0 분기(근거 4가지) |
| 10-13 | Data 계약 작은 개정은 같은 코멘트 수정 + 변경 기록 코멘트 |
| 10-13 | 공개 기록에 RDS Endpoint 값 대신 해시 |
| 10-13 | RDS · Valkey 값은 이유빈 `c-data-outputs.json`을 직접 읽음(복사 안 함), GitOps에 실제 주소 커밋 안 함(정태훈) |
| 10-13 | RDS CA는 파일 대신 공식 주소 + SHA-256으로 전달 |
| 10-13 | 마스터 Secret 7일 회전 유지, 회전 창에 #44 3 · 4 · 7 · 8단계 금지 |
| 10-13 | `require_secure_transport`는 값으로 판정, Terraform `apply_method = "pending-reboot"` |
| 10-13 | 해독 키 이동: 각자 키를 `age -p` 잠금 파일로 이유빈 USB에, 암호 문구는 키 주인만. controller 없는 복원은 복구 DB VM 콘솔에서만 |
| 10-13 | 쓰기 중지 끝점 = 9단계 뒤 전환/복귀 판단. 복귀 시 1-1부터 새 덤프 |
| 10-13 | Recovery Redis 전용 CA(Recovery DB CA와 분리), Token은 Cloud와 별도 |
| 10-12 | 이관 실행 순서: 3 · 4단계를 쓰기 중지 전으로 |
| 10-12 | S3 재전송은 회차 기록 뒤(9단계 뒤 10단계) |
| 10-08 | 복원 사본 자동 선택 = `periodic` · Backup ID 시각 최신순 |
| 10-08 | Backup ID 시각 = `T_DUMP` = `last-success` |
| 10-08 | 복구 계정 6개 상시 유지, RTO/RPO 목표 유지(축소 조치는 `restore.sh` · 계정 사전 생성만) |
| 10-08 | 백업 · 복원 스크립트 기준본 = infra `ansible/data/` |
| 10-07 | Runbook은 infra Issue로 운영(본문 = 최신, 코멘트 = 이력) |
| 10-07 | 백업 해독 키 각자 1개 · 받는 사람 2명(김상희 · 이유빈), VM에는 공개키만 |
| 10-07 | S3 일반 사본 경로 `periodic/`(이전 `hourly/`) |
| 10-07 | 복구 DB VM Server-04 · `192.168.54.60`(`.54.40`은 1차 maxscale-02 자리라 제외) |
| 10-06 | Redis 엔진 → Valkey 7.2 |
| 10-06 | 서비스 연결 Role(RDS · ElastiCache) CLI로 사전 생성 |
| 10-06 | Data 코드를 foundation Root에 직접 배치(`data_*.tf`, 모듈 삭제) |
| 10-05 | DR 목표 RTO 10분 · RPO 30분 · 15분 백업(이전 30분 · 90분 · 1시간) |
| 10-02 | 1차 실데이터 그대로 논리 덤프 이관(가명화 안 함), 취급 조건 유지 |
| 10-01 | B1 아키텍처, ROSA Classic Multi-AZ, RDS MariaDB Multi-AZ, Terraform state bootstrap / foundation / rosa |

---

## 11. 용어

| 용어 | 뜻 |
|---|---|
| controller | 팀 공용 Ansible 서버(CentOS). 팀원별 리눅스 계정으로 Terraform · 스크립트 실행 |
| 백업 작업 VM | `hybrid-backup-01`. 이관 덤프와 15분 백업을 만드는 온프렘 VM (이전 이름 "Data VM") |
| 복구 DB VM | `hybrid-recovery-db-01`. 사본 보관과 장애 시 복원 대상 |
| Backup ID | `periodic-YYYYMMDDTHHMMSSZ` 등. 시각 = 덤프 시작(UTC) = 데이터 시점 |
| `T_DUMP` | 덤프 시작 시각. Backup ID · `last-success`와 같아야 함 |
| Gate | `check_backup_gate.sh`로 하는 백업 운영 판정 |
| Data 계약 | App · GitOps가 Data 계층에서 받는 값의 약속(Infra #19 코멘트) |
| 3-0 분기 | #45에서 이관 전 RDS Stop 절차 |
| V4 | #55의 실제 S3 재전송 확인(Apply 뒤에만 가능) |
| T18 | 03 상세설계의 Offline Recovery 공식 시험 |
| Window A / B | ROSA 정상 통합 / 최종 검증 가동 구간 |
| Cost Gate | 첫 Full Apply 전 비용 판정(Docs #43) |

---

## 12. 새 세션 시작 문장 예시

```
석판 2차 프로젝트 Data 영역을 이어서 진행합니다.
첨부한 seokpan-data-handoff-for-ai.md를 먼저 읽고, 지금 상태와 남은 작업을 파악해 주세요.
(이 문서는 2026-10-13 22:00 스냅샷이고, 그 뒤 바뀐 것: ○○○)
오늘 할 작업: ○○○ (예: #45 3-0 분기로 10/15 RDS Stop)
실행은 제가 직접 하니, 어디서(호스트 · 계정) 실행하는 명령인지 꼭 표시해 주세요.
```
