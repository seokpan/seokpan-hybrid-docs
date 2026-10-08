# ROSA Plan·OCP 후속 실행 준비 — 2026-10-08

* 현재 판단

- App #20/#22·Infra #43·GitOps #25 병합과 해당 원격 PR 브랜치 삭제 완료. Docs #72의 현재 상태 보완 대상이며 새 설계 변경 없음.
- 병합 Infra의 fmt·세션 helper 문법·기존 OIDC 시험 사본 생성/보존 PASS. 병합 GitOps의 Root 등록 SHA B 비교 및 전체 lab release Gate PASS. [새 검사 기록](../evidence/T01/plan-source-readiness-20261008-01/summary.md).
- 본인 Controller의 Caller/Backend·지원/Quota·실제 보호 입력·Cloud Plan은 NOT RUN. OCP 철거·전체 Data 이관/Backup/Recovery는 첫 ROSA Plan의 일괄 선행조건이 아님.
- GitOps #26의 C DB 형식/GRANT/TLS 접속·합성 출처 수락과 D 로그인·방 생성/접속·게임 종료 보고 수신. Vote 및 ERR 원인 미확인. 직접 Runtime 재조회·전체 OCP 수락과 구분.

* 현재 소스와 원 기록

| 대상 | 확인한 병합 개정 | 원본·마무리 |
|---|---|---|
| App #20 | `c35509155886739f987b265d003a6ce7e95caf92` | [마무리](https://github.com/seokpan/seokpan-hybrid-app/pull/20#issuecomment-6050175642), 병합 verify success |
| App #22 / 현재 App main | `1e99e36ed2f8b116fad5db9a6333a71f2c2bdec3` | [마무리](https://github.com/seokpan/seokpan-hybrid-app/pull/22#issuecomment-6050176304), Frontend 병합 CI 없음 |
| Infra #43 / 현재 Infra main | `6849c32d5b24a0e4994b7fbe849a1032211dc9a3` | [마무리](https://github.com/seokpan/seokpan-hybrid-infra/pull/43#issuecomment-6050176904), validate success |
| GitOps #25 / 현재 GitOps main | `61edd0fd60e1004260c0b5082dc792fce847616b` | [마무리](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25#issuecomment-6050200412), validate success |
| Docs main | `0cb6a95d72884778452b4c96ae7383dad258db0e` | C #83의05 §8.18/Tracker 기록 병합 완료. #72 현재 후속은 미병합 |

Runtime Workload의 정확 SHA/Image와 위 저장소 main은 별도로 기록. 현재 Root 선언 targetRevision은 SHA B `bfee2669e62bf823969ce224e5599eccace5d024`. Stage1 SHA A 등록·Valkey4객체 선택 Sync는 완료 이력 유지. 새 App 소스가 기존 승인 lab Image에 포함됐다고 사용하지 않음.

* 오늘 실행 순서·직접 대기

| 순서 | 담당·작업 | 필요한 입력·종료 조건 | 막는 단계 |
|---|---|---|---|
| 1 | B: 기존 Controller·jth·clone/Lock/도구 확인 | 현재 접속·작업 위치·개인 변경·정확 Source/도구 확인 | 실제 인증·Plan |
| 2 | A: Infra #23 기반 출력/공통 prerequisite, bootstrap 목적 서비스 권한 | 실제 VPC·Public3/ROSA Private3·AZ·Classic Account Role4/Operator Policy Map·Backend의 보호 개정, B 수락. 목적 Role의 실제 유효 권한 확인·필요 차이 반영 | 실제 첫 Plan |
| 3 | C/A: Infra #19 Data SG2 공급/통합 | 실제 서로 다른 MariaDB/Redis SG·VPC·Owner/기반 Rule·개정 수락. 생성 전에도 필수 | 실제 첫 Plan |
| 4 | B: 목적 세션·Backend·지원/구독/Quota·Worker disk, B/D 예비 비용·Owner/창 | 정확 조합 수락, execution_review와 기반 개정 일치. 현재 보호 입력 공급/수락은 원 기록에서 미확인 | 실제 첫 Plan |
| 5 | B: 같은 rosa Root의 전체 Plan, A 리뷰 | Code/Lock/입력/Caller 고정, 수량·삭제/교체·기반 보존 영향 확인 | 생성 전 비용/실행 수락 |
| 병행 | D/B/C: OCP #26/#5 잔여 수락 | 실행 Source/Image/Run·Route/Origin·TLS/AUTH/Hostname·Ready·사용창/Gate/live Diff·Prune/Delete 보호, Vote와 ERR 조사 | 해당 OCP 수락, ROSA Plan 전체는 막지 않음 |
| 병행 | D App #2 → B App #4/GitOps #10 | 병합 App Source의 새 Backend/Frontend Build·Scan·Digest·플랫폼/Pull·App/held Migration 대응 | 새 소스의 실제 배포 수락 |

Backend 정책 소스만으로 rosa 서비스 권한 완료나 권한 부재를 단정하지 않음. Source의 필요한 호출 범위는 Infra `terraform/rosa/REVIEW_AND_EXECUTION_GATES.md`를 사용하고, 실제 거부는 목적 세션으로 좁혀 확인. A/C/D의 보호 출력·권한·원장을 대신 생성하지 않음.

* 1. Controller 접속 확인 — Windows PC / 본인

1차 최신 인벤토리([Infra main `3af8911`](https://github.com/seokpan/seokpan-infra/blob/3af8911be68e7f1c1e8950b5bd6a009049ebf768/ansible/inventory/hosts.yml))의 Controller는 `192.168.54.70`. [1차 안내](https://github.com/seokpan/seokpan-infra/blob/3af8911be68e7f1c1e8950b5bd6a009049ebf768/README.md)는 일반 사용자 jth의 개인 checkout을 지원. 인벤토리의 원격 대상 `ansible_user: root`를 Controller 로그인 계정으로 사용하지 않음.

```powershell
Test-NetConnection -ComputerName 192.168.54.70 -Port 22 -InformationLevel Quiet
ssh -o StrictHostKeyChecking=yes jth@192.168.54.70
```

현재 작업 PC의 TCP22는 연결 실패, SSH 로그인 미시도. 현장 망/VPN·VM 가동·현재 IP·Route/Firewall을 확인. SSH Host Key가 새롭거나 바뀌었다면 기존 fingerprint/VM Console로 대조 후 정상 등록, 검증 해제 옵션이나 기존 known_hosts 일괄 삭제 금지. 접속 실패만으로 Controller 인증·ROSA 권한 실패를 판정하지 않음.

* 2. 본인 checkout·도구 — Controller / jth

```bash
id -un
hostname
pwd
for rosa_clone_candidate in "$HOME/work/seokpan-hybrid-infra" "$HOME/seokpan-hybrid-infra"; do
  if [ -d "$rosa_clone_candidate/.git" ]; then
    printf 'FOUND: %s\n' "$rosa_clone_candidate"
  fi
done
```

둘 다 없으면 실제 개인 clone 위치를 확인. 기존 실패 이력의 `/home/jth/work/seokpan-hybrid-infra`를 존재 확인 없이 사용하지 않음. 아래부터 확인한 clone 최상위에서 실행.

```bash
git status --short --branch
git fetch origin main
git rev-parse HEAD origin/main
git diff --stat HEAD origin/main -- terraform/rosa scripts/tf-session.sh
git diff --name-status -- terraform/rosa scripts/tf-session.sh
git diff --cached --name-status -- terraform/rosa scripts/tf-session.sh
git hash-object terraform/rosa/.terraform.lock.hcl
git rev-parse origin/main:terraform/rosa/.terraform.lock.hcl
for rosa_tool in python3 bash git terraform aws rosa jq; do
  command -v "$rosa_tool" >/dev/null 2>&1 && printf '%s PRESENT\n' "$rosa_tool" || printf '%s MISSING\n' "$rosa_tool"
done
CHECKPOINT_DISABLE=1 terraform version -json
aws --version
rosa version
python3 --version
bash -n scripts/tf-session.sh
```

main/개인 변경/Lock 차이를 수락한 뒤 다음 단계. reset·stash·키/State 초기화·공유 패키지 일괄 업그레이드 없음. 최신 승인 Core1.16.4/AWS6.67.0/RHCS1.7.7 고정. 표준입력 없는 버전 조회로 인증 완료를 판정하지 않음. 기존 `LOCAL_PREPARATION.md`의 오프라인 harness 명령 재사용 가능. oc/sops/age의 확인은 실제 lab/금고 작업에서 별도이며 첫 Plan의 새 일괄 조건으로 만들지 않음.

* 3. 실제 읽기 중심 사전검사 — Controller / jth / 목적 rosa 세션

먼저 A/B가 기존 Backend 초기화 상태·선택 Workspace·기존 State 위치와 목적 Role을 확인. 기존 default Key는 `phase2/rosa/terraform.tfstate`; non-default는 새 prefix `phase2/rosa/env`와 기존 위치 차이를 검토. 기존 State를 버리고 새 빈 State로 연결하지 않음. 보호 입력/Backend 파일·RHCS 인증은 기존 승인 경로로 공급하며 공개 기록에는 논리 참조만 사용.

```bash
set +x
unset TF_LOG TF_LOG_PATH
umask 077
rosa_private_dir="$(mktemp -d "$HOME/rosa-plan-20261008.XXXXXX")"
source scripts/tf-session.sh rosa
[ "${TF_SESSION_MODE:-}" = rosa ] || { printf 'BLOCKED: rosa session\n'; return 1 2>/dev/null || exit 1; }
aws sts get-caller-identity > "$rosa_private_dir/caller.json" || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
rosa whoami > "$rosa_private_dir/rosa-whoami.txt" 2>&1 || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
rosa list versions > "$rosa_private_dir/rosa-versions.txt" 2>&1 || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
rosa list instance-types > "$rosa_private_dir/rosa-instance-types.txt" 2>&1 || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
rosa verify quota --region ap-northeast-2 > "$rosa_private_dir/rosa-quota.txt" 2>&1 || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
```

각 명령의 종료 코드·보호 결과를 개별 확인하고 실패한 단계에서 Plan 진입 중단. helper는 이전 세션을 해제한 뒤 MFA로 새 세션 발급, 실패 후 개인 기본 자격증명으로 돌아갈 수 있으므로 실패 뒤 개인 Admin으로 계속 실행하지 않음. MFA/Token 입력·Caller 원문·자격증명은 녹화/공개 로그/회신 제외. `rosa whoami`의 기존 OCM 로그인과 Provider의 RHCS 인증을 같은 근거로 자동 처리하지 않음. 실제 공급 주체·Account/Region·구독·지원 조합·목적 권한 범위를 보호 환경에서 대조.

[Red Hat CLI 문서](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/cli_tools/rosa-cli)의 `rosa verify quota`는 Quota 조회. `rosa verify permissions`는 non-STS 설치용 검증이므로 현재 Classic STS 목적 Role의 전체 권한 증명으로 사용하지 않음. stable4.20의 정확 GA patch·지원/Quota·Worker disk를 실제 결과로 수락. `rosa init`, Role/OIDC/Cluster create, Apply/Destroy는 이 읽기 절차에 포함하지 않음. 새 OIDC가 아직 없으면 생성 후의 issuer/JWKS·Operator JWT/STS 시험을 첫 Plan 전 완료한 것으로 쓰지 않음.

* 4. 실제 첫 전체 Plan — 입력·권한·예비 비용·Owner 수락 후

아래 변수는 승인된 보호 파일의 절대경로로 본인 환경에서 지정. 예시 tfvars를 실제 입력으로 사용하거나 빈 execution_review를 임의 승인 문자열로 채우지 않음. AWS Provider와 Backend가 동일 목적 세션인지 확인. `cluster_enabled=true`, `worker_sg_binding=null`의 초기 전체 계획이며 Data SG2는 필수. 기존 Cluster가 있을 수 있는 환경에서 false를 안전 모드로 사용하지 않음.

```bash
read -r -p '승인 Backend 설정 파일 절대경로: ' rosa_backend_config
read -r -p '수락한 ROSA tfvars 파일 절대경로: ' rosa_inputs_file
[ -r "$rosa_backend_config" ] && [ -r "$rosa_inputs_file" ] || { printf 'BLOCKED: protected inputs\n'; return 1 2>/dev/null || exit 1; }
terraform -chdir=terraform/rosa init -input=false -lockfile=readonly   -backend-config="$rosa_backend_config" > "$rosa_private_dir/init.log" 2>&1 || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
# init 성공 및 기존 Backend/Workspace/State 위치 수락 뒤에만 다음 명령 실행.
terraform -chdir=terraform/rosa workspace show > "$rosa_private_dir/workspace.txt" || { printf 'BLOCKED: prerequisite command\n'; return 1 2>/dev/null || exit 1; }
terraform -chdir=terraform/rosa plan -input=false -detailed-exitcode   -var-file="$rosa_inputs_file" -out="$rosa_private_dir/rosa.tfplan"   > "$rosa_private_dir/plan.log" 2>&1
rosa_plan_exit=$?
printf 'Plan exit: %s (0=no changes, 2=changes, 1=error)\n' "$rosa_plan_exit"
```

init가 재설정/이관을 요구하면 기존 State/Workspace 검토로 돌아감. 무조건 `-reconfigure`/`-migrate-state`, 새 Workspace, `-target`, State 수정/삭제, force-unlock으로 우회하지 않음. Plan은 Cloud 읽기와 기존 Backend의 Lock 접근을 포함하므로 Shared Execution에서 실행자 B 한 명·A 기반 변경과 충돌 없는 창을 유지. 잠금/권한 실패는 원 작업에 값 없는 단계 판정으로 기록.

Plan 원문/Saved Plan은 보호 디렉터리에서 A와 수량·삭제/교체·보존 영향 검토, 공개/업로드 금지. Plan 성공은 Apply 승인 아님. 생성 전 실제 전체 Plan·D 총비용/누적/잔존·기간/재시험/정리 지연·실행/삭제 책임 수락 필요. CP3/Infra3/Worker3·$450 계획선/$500 한도 유지.

* 5. OCP 병행 후속 — D 환경·B 수락 / 원 #26·#5

- 성공한 SHA A 등록·Valkey4객체 Sync 반복 없음. 기존 실제 SHA B 적용/Sync 여부와 Source/Image를 원 Run·댓글에 연결해 먼저 수락.
- C의 DB 형식/GRANT/TLS 접속·합성 출처 수락은 다시 미공급으로 되돌리지 않음. D 최신 부분 업무 보고와 #26 본문 미체크의 차이는 원 담당이 실행 개정/근거 연결로 보완.
- Vote·게임 종료 후 UI·재접속, Route FE/API/WSS와 허용/거부 Origin·TLS/Hostname·Ready·Owner/사용창/Gate/live Diff·실제 삭제 보호 근거 확인. 살아 있는 업무 객체로 임의 Delete/Prune 시험하지 않음.
- Valkey ERR 증가 원인: D 보고의 EVALSHA failed_calls16/NOSCRIPT16 및 비사용 시간 증가만으로 App Lua 오류나 무해한 초기 협상으로 단정하지 않음. 동일 Source/Image/서버 버전의 짧은 시각별 INFO errorstats/commandstats·클라이언트 재연결/Probe 기록에서 오류 명령을 좁혀 확인. MONITOR·Secret 조회·전체 명령 인자 로그는 수집하지 않음.
- B는 원인/재현·업무 영향이 확인된 부분만 좁은 코드 수정/회귀, D는 현장 측정·Vote/실행 근거 공급. 이 미해결은 해당 업무 판정이며 ROSA 첫 Plan의 일괄 선행조건 아님.

* 전체 잔여 묶음

| TH | 남은 작업 |
|---|---|
| 01–03 | 본인 Controller/개인 변경·Seed/계보/보존 수락, D CI/ECR E2E·Writer/Promotion·새 Source Image·수신 |
| 04–07·14 | Pool/시간/Client 계약·실제 TLS/AUTH·FE/API/WSS·수명/종료/재접속·중복/경쟁/부분 실패, 기존 결함/수정 Branch 후속 PR/검사 |
| 08–09 | OCP 잔여 수락, Cloud Replica/NP/UWM/관리 선언, Recovery Valkey binary/UID/TLS/AUTH/Persistence·Host/CA/Image/Bundle 수락 |
| 10–12 | A/C 기반 입력/목적 권한·B 인증/지원/Quota·첫 전체 Plan·예비/최종 비용/창·공유 실행 |
| 11·15 | 본체 금고 확인 완료와 구분한 Controller 밖 독립 Key/암호문 사본·복원 Identity 검사, 정상 IDP/RBAC·초기 인증 회수, 실제 Offline Data/전체 업무/T18 |
| 13·16–17 | 승인 생성·Worker SG/Data Binding·ECR Pull·Secret/Migration·정상 Baseline/Backup, 조건부 중간 삭제/재생성 및 Window B 공식 장애/부하/관측/복구 |
| 18–19 | 원 Run/정량 결과/영상·발표, 독립 보존·회수·최종 rosa 삭제·잔존/후속 비용·수신/개인 종료 |
| Q·기록 | 미검토 코드/과거 diff/원 thread/CI·산출물 의미 검토, 원 작업→Tracker/05/Index 연결·담당 수신·Milestone/가용시간 확인 |

TH81/기존 완료2·Q 미완료·03/04 종료·DR10분/DB RPO30분/DB 운영 중Backup15분을 유지. 새 소스 검사로 실제 T01~T23/TH/Q 완료를 추가하지 않음.

* 공개 회신할 최소 판정

`Source/Lock 일치 여부 / Controller 계정·도구 버전 확인 / 목적 Caller·Backend·Workspace 일치 여부 / 입력 개정 수신·누락 담당 / 지원·Quota·구독 판정 / Plan 종료 코드·수량·삭제/교체 유무·A 리뷰 / Cost·창 수락 여부 / 실제 실행·미실행 범위 / 원 Issue·새 Run 참조`.

비밀번호·Key·Token·kubeconfig·전체 State/Output·Plan·개인 보호 경로 원문은 회신 제외. 원 기록은 Infra #25·GitOps #10/#26·App #4/#21, 연결은 Docs #21/#8·Tracker/05·새 Run Index.
