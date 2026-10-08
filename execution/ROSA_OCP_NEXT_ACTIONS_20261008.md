# ROSA Plan·OCP 후속 실행 준비 — 2026-10-08

* 정책 조회 후 현재 상태

- [원 Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6053637165)·[T03 부분 Run](../evidence/T03/redhat-policy-read-20261008-01/summary.md): Controller 인증·필수5/5·Operator7/8·OCM 참조4/4 조회, 보호 사본 생성 완료. Token 재발급/성공 조회 반복 없음. Token 자체의 읽기 전용 권한 판정은 아님.
- [저장 사본 읽기 Run](../evidence/T03/policy-bundle-readback-20261008-01/summary.md): 현재 권한700/600·해시17개 일치 PASS, 누락 AWS VPCE 정책 ID 확인. A 보호 인계/수신과 실제 Operator 목록/Policy Map 대조는 대기. 다음 직접 실행은 본인 Infra clone의 origin/fetch·Branch/개인 변경·ROSA Lock 읽기 대조. fetch는 원격 참조 갱신이며 작업 파일/Branch/State 초기화 없음.
- GitOps31·Docs85 병합/브랜치 삭제 완료. 현재 조회 main은 App9b142a28·Infrac5d8c424·GitOps9d108349·Docsce0b4216. App25 Release 후보 생성기, Infra50/51 README, C Docs87 §8.19/Tracker 변경은 Source 범위로 소비하며 새 Image/실환경 검증으로 사용하지 않음.
- B clone/원격/Lock·목적 Caller/Backend·지원/Quota·Worker disk·예비 비용/실행 창, A 실제 Role4/Policy Map/목적 권한/제한 출력, C/A Data SG2가 첫 Plan 직접 입력. 프로젝트 Red Hat 조직/AWS 연결은 생성/관리 전 수락 필요. Plan 미실행.

- [GitOps26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)은 lab Stage2 완료로 종료. DB 입력·FE/BE Ready·Route/WSS·Valkey 부분 업무 보고 수신. 이월 범위는 다중 투표·WS idle/재접속·Rolling/Pod 삭제·DB/Redis 장애 readiness·Prune/Delete 실제 차단·ROSA ERR 재측정. 본인 GitOps10/App4 후속이며 성공 Sync를 반복하거나 #26을 재개하지 않음.

* 아래 준비 기록의 조회 시점

아래 Source 표와 Token 미설정 표기는 정책 조회 전 준비 이력. 최신 상태는 위 카드와 원 Issue를 사용. 실행 명령은 해당 Source/개인 변경/입력·Owner/사용창을 확인한 뒤 사용하며 과거 미확인 항목을 임의로 완료 처리하지 않음.


* 현재 판단

- App #20/#22·Infra #43·GitOps #25 병합과 해당 원격 PR 브랜치 삭제 완료. Docs #72/#84도 병합·해당 원격 PR 브랜치 삭제 확인. 이후 결과는 새 문서 변경으로 연결하며 설계 기준 유지.
- 병합 Infra의 fmt·세션 helper 문법·기존 OIDC 시험 사본 생성/보존 PASS. 병합 GitOps의 Root 등록 SHA B 비교 및 전체 lab release Gate PASS. [새 검사 기록](../evidence/T01/plan-source-readiness-20261008-01/summary.md).
- B의 기존 `jth@ansible` 세션과 Recovery CA 전체 해시 일치 검사 결과 수신. Terraform1.16.4(Core 일치)·AWS CLI2.37.5·Python3.9.25·jq1.6 확인. 개인 clone HEAD18c3a275·ROSA Lock 없음, 저장소 연결/원격 갱신·Source 대조 대기. RHCS_TOKEN 미설정·ROSA/OCM CLI 미설치. 목적 Caller/Backend·지원/Quota·실제 보호 입력·Cloud Plan은 NOT RUN. OCP 철거·전체 Data 이관/Backup/Recovery는 첫 ROSA Plan의 일괄 선행조건이 아님.
- GitOps #26의 C DB 형식/GRANT/TLS 접속·합성 출처 수락과 D 로그인·방 생성/접속·게임 종료 보고 수신. D의 TLS/AUTH·Route/Origin 및 ERR 협상 원인 후속 보고도 수신. Vote·연결 유지/재접속/Timeout 등 잔여는 아래 구분. 직접 Runtime 재조회·전체 OCP 수락과 구분.

* 현재 소스와 원 기록

| 대상 | 확인한 병합 개정 | 원본·마무리 |
|---|---|---|
| App #20 | `c35509155886739f987b265d003a6ce7e95caf92` | [마무리](https://github.com/seokpan/seokpan-hybrid-app/pull/20#issuecomment-6050175642), 병합 verify success |
| App #22 / 당시 App main | `1e99e36ed2f8b116fad5db9a6333a71f2c2bdec3` | [마무리](https://github.com/seokpan/seokpan-hybrid-app/pull/22#issuecomment-6050176304), Frontend 병합 CI 없음 |
| App #23 / 최종 조회 App main | `070c699c119d2972f551bdfc4fe390678ad45c44` | [D PR23](https://github.com/seokpan/seokpan-hybrid-app/pull/23) 작업 중 병합 추가 확인. Image 변경안 계산 planner/시험이며 annotation·Release JSON·Cloud/Writer는 범위 밖. 새 Image/Runtime 수락 별도 |
| Infra #43 / 현재 Infra main | `6849c32d5b24a0e4994b7fbe849a1032211dc9a3` | [마무리](https://github.com/seokpan/seokpan-hybrid-infra/pull/43#issuecomment-6050176904), validate success |
| GitOps #25 / 현재 GitOps main | `61edd0fd60e1004260c0b5082dc792fce847616b` | [마무리](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25#issuecomment-6050200412), validate success |
| Docs #72/#84 / 조사 시 Docs main | `a355ee1cfdee7804fc214c7f05bb439e847ae6ba` | [72 마무리](https://github.com/seokpan/seokpan-hybrid-docs/pull/72#issuecomment-6050693657)·[84 마무리](https://github.com/seokpan/seokpan-hybrid-docs/pull/84#issuecomment-6050694153), 해당 원격 브랜치 삭제 확인 |
| Recovery Host 변경 / 미병합 | `6c3de8d75f12754ece2cfeb9a1347de66e8cbafe` | [GitOps31](https://github.com/seokpan/seokpan-hybrid-gitops/pull/31), C/D 리뷰 대기·정확 HEAD Linux69PASS. main 병합으로 소비하지 않음 |

Runtime Workload의 정확 SHA/Image와 위 저장소 main은 별도로 기록. 현재 Root 선언 targetRevision은 SHA B `bfee2669e62bf823969ce224e5599eccace5d024`. Stage1 SHA A 등록·Valkey4객체 선택 Sync는 완료 이력 유지. 새 App 소스가 기존 승인 lab Image에 포함됐다고 사용하지 않음.

* 오늘 실행 순서·직접 대기

| 순서 | 담당·작업 | 필요한 입력·종료 조건 | 막는 단계 |
|---|---|---|---|
| 1 | B: 기존 Controller·jth·clone/Lock/도구 확인 | jth@ansible 세션·CA 해시 일치 결과 수신 완료. Core1.16.4·AWS CLI2.37.5·Python3.9.25·jq1.6 확인. 개인 clone HEAD18c3a275/ROSA Lock 없음, 저장소 연결·fetch·Source 대조 대기 | 실제 인증·Plan |
| 1-A | B: Red Hat 인증·Classic 공식 IAM 정책 조회/보호 인계 | 기존 본인 Red Hat 계정으로 읽기 정책 조회 가능. 프로젝트 ROSA 관리 조직은 아직 미정이며 조회 계정으로 자동 확정하지 않음 | A #47 정책 원본 준비. 프로젝트 조직/연결 수락은 실제 실행 전 별도 |
| 2 | A: Infra #47 Account Role4·정책/Trust 및 Infra #23 기반 출력, bootstrap 목적 서비스 권한 | 실제 VPC·Public3/ROSA Private3·AZ·Classic Account Role4/Operator Policy Map·Backend의 보호 개정, B 수락. 목적 Role의 실제 유효 권한 확인·필요 차이 반영 | 실제 첫 Plan |
| 3 | C/A: Infra #19 Data SG2 공급/통합 | 실제 서로 다른 MariaDB/Redis SG·VPC·Owner/기반 Rule·개정 수락. 생성 전에도 필수 | 실제 첫 Plan |
| 4 | B: 목적 세션·Backend·지원/구독/Quota·Worker disk, B/D 예비 비용·Owner/창 | 정확 조합 수락, execution_review와 기반 개정 일치. 현재 보호 입력 공급/수락은 원 기록에서 미확인 | 실제 첫 Plan |
| 5 | B: 같은 rosa Root의 전체 Plan, A 리뷰 | Code/Lock/입력/Caller 고정, 수량·삭제/교체·기반 보존 영향 확인 | 생성 전 비용/실행 수락 |
| 병행 | D/B/C: OCP #26/#5 잔여 수락 | D의 TLS/AUTH·Route/Origin·ERR 협상 원인 보고는 수신 유지. 남은 Vote·연결 유지/재접속/Timeout·실행 Source/Image/Run·Ready·사용창/Gate/live Diff·Prune/Delete 보호 수락 | 해당 OCP 수락, ROSA Plan 전체는 막지 않음 |
| 병행 | D App #2 → B App #4/GitOps #10 | 병합 App Source의 새 Backend/Frontend Build·Scan·Digest·플랫폼/Pull·App/held Migration 대응 | 새 소스의 실제 배포 수락 |

Backend 정책 소스만으로 rosa 서비스 권한 완료나 권한 부재를 단정하지 않음. Source의 필요한 호출 범위는 Infra `terraform/rosa/REVIEW_AND_EXECUTION_GATES.md`를 사용하고, 실제 거부는 목적 세션으로 좁혀 확인. A/C/D의 보호 출력·권한·원장을 대신 생성하지 않음.

* 1. Controller 위치와 Red Hat 계정 구분

- B의 기존 `jth@ansible` SSH 세션 확인. Windows PC에서192.168.54.70 TCP22 연결은 실패했지만, Linux VM에서 이미 접속한 세션을 이용하므로 Windows 재시도는 현재 준비의 선행조건이 아님. PC/VM의 망·Route/Firewall 차이는 별도 미확인.
- 1차 Kubernetes 자산이 있는 Controller에서도 승인된 개인 보호 Workspace를 사용할 수 있음. CA 검사·도구 확인·Red Hat 정책 조회는 Kubernetes 객체 변경이 아니며 OCP 웹 UI/Node에서 실행할 필요 없음.
- Linux `jth` 로그인, OCP 웹 UI 인증, Red Hat Hybrid Cloud Console 계정, 목적 AWS 실행 Role은 서로 다른 인증. 이름이 같거나 앞 단계가 성공했다는 이유로 다음 인증을 완료 처리하지 않음.
- 프로젝트 ROSA 관리 Red Hat 계정·조직은 아직 미선정. 기존 본인 Red Hat 계정의 공식 정책 읽기 조회는 가능하지만 이 결과를 프로젝트 조직/AWS 계정 연결·구독 승인으로 사용하지 않음. 실제 프로젝트 인증·지원/구독·Plan 준비에서 조직/권한·AWS 연결을 별도 수락.
- RHCS_TOKEN 입력은 `set +x` 상태의 `read -r -s` 프롬프트로 받고 셸 환경변수에만 export. 웹 계정/조직은 보호 환경에서 확인하며 Token을 명령 인자·파일·Terraform 변수/State·공개 로그로 복제하지 않음.
- 공식 정책 조회 경로는 RHCS1.7.7 Classic 구현의 `GET /api/clusters_mgmt/v1/aws_inquiries/sts_policies`. 반환된 Classic 권한 정책4개와 Support Trust 원본을 보호 사본으로 인계. Installer Trust는 고정 Provider의 운영 환경 참조와 공식 Classic 소스로 대조하며 실제 IAM Trust 확인은 A 후속. 정책 조회가 지원 patch·Quota·프로젝트 조직 연결·실제 Role 존재를 검증하지 않음.

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
if command -v rosa >/dev/null 2>&1; then rosa version; else printf 'rosa version: NOT RUN (MISSING)\n'; fi
python3 --version
bash -n scripts/tf-session.sh
```

main/개인 변경/Lock 차이를 수락한 뒤 다음 단계. reset·stash·키/State 초기화·공유 패키지 일괄 업그레이드 없음. 최신 승인 Core1.16.4/AWS6.67.0/RHCS1.7.7 고정. 표준입력 없는 버전 조회로 인증 완료를 판정하지 않음. 기존 `LOCAL_PREPARATION.md`의 오프라인 harness 명령 재사용 가능. oc/sops/age의 확인은 실제 lab/금고 작업에서 별도이며 첫 Plan의 새 일괄 조건으로 만들지 않음.

* 3. 실제 읽기 중심 사전검사 — Controller / jth / 목적 rosa 세션

현재 ROSA/OCM CLI가 없으므로 아래 rosa 명령은 아직 미실행. 먼저 기존 공급·설치 담당과 지원 버전을 확정하고 실제 설치 뒤 실행. 정책 원본 읽기 조회에 CLI 설치를 일괄 선행조건으로 추가하지 않음. CLI 설치나 단순 인증 성공을 지원/구독·Quota·실행 준비 완료로 사용하지 않음.

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
- [D #26의 편집된 최신 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26#issuecomment-6050000112): redis-py8.1.0/RESP3 초기 CLIENT MAINT_NOTIFICATIONS 협상으로 ERR 증가, RESP2 또는 협상 비활성화 비교에서 증가0·업무 영향 없음 확인 보고 수신. 비긴급 `MaintNotificationsConfig(enabled=False)` 후보는 별도 후속이며 즉시 프로토콜/코드 변경 없음. ROSA 실제 Engine에서 재측정. EVALSHA 실패16/NOSCRIPT16 초기 fallback은 별도 원 기록 유지.
- [D #10 Route/Origin 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6050495638): FE `/`·API `/api/v1`·WSS `/ws/v1` Route Admitted, Host/TLS·HTTPS·허용 Origin101/거부403·브라우저WSS101 확인 보고 수신. 남은 Vote·장시간 연결/재접속/Timeout·정확 Source/Image/Run 및 보호 수락을 확인하며 성공한 기본 검사를 다시 대기로 만들지 않음. ROSA Host/인증서/Origin은 해당 환경에서 별도 검증.

* Recovery·Pool의 직접 후속

- Recovery Host Source는 GitOps31 리뷰/병합 대기. CA 전체 해시 일치 결과 수신 완료. ConfigMap 생성은 Namespace 확정 후이며 DB Name/목적 계정·Secret·Redis·Registry/Image/Bundle 수락 후 연결 검증. Infra48의10/9 Data-only 예행과10/19–21 전체 Recovery 업무/RTO 검증 구분.
- C가 Data 기준v2.2 §2.6의 예약 연결10을 전달. 실제 RDS `@@max_connections`는 생성 후 C 공급. Pool 예산은 Engine2 × Process 수 × 동시 Pod 수 × `(pool_size + max_overflow)` + 예약10으로 검토하며 Rolling 중 종료 대기 Pod를 포함. 실제 Process/동시 Pod와 RDS 상한 미확인, 임의3+2 확정/미구현 환경변수 추가 없음.
- 현재 Dockerfile의 uvicorn 기본 실행만으로 실제 Process/Runtime Override를 확정하지 않음. B/C 합의 후 App 설정·Source Test → D 새 Build/Scan/Digest → App/held Migration 대응 → 실제 부하/종료/재접속 측정 순서.

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
