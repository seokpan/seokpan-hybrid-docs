# B 독립 Source 보완과 실제 인계 순서 — 2026-10-09

현재 전체 진행:

- [x] Docs #97/#98 병합·브랜치 삭제 보고 수신, EC2 입력 오류 교정/제한 조회 및 Controller 오프라인 시험 완료.
- [x] A bootstrap 실제 Apply·동일 입력 재-Plan 변경 없음·AWS 정책/연결 확인 보고 수신.
- [x] B Cloud 플랫폼/조회 권한·Recovery Bundle·관리 인증 수락의 오프라인 Source 보완.
- [ ] 신규 Source 리뷰·병합 및 환경별 실제 공급/실행 수락.
- [ ] Foundation 전체 Plan/비용/Apply와 B ROSA 서비스 권한·목적 인증/Backend·첫 전체 Plan.

B05/B06/B08은 별도 현황 HTML이 만든 작업 그룹 이름이다. 원 승인 설계의 B 항목이나 TH 체크 번호를 재번호화하지 않는다. 여기서는 Cloud 플랫폼, Recovery Bundle, 관리 인증·Secret 경계로 명시한다. Source 후보/오프라인 시험 완료와 실제 인프라·업무 시험 완료는 별개다.

공개 리뷰 산출물: [GitOps #34 Cloud 플랫폼](https://github.com/seokpan/seokpan-hybrid-gitops/pull/34), [GitOps #35 Recovery 인벤토리](https://github.com/seokpan/seokpan-hybrid-gitops/pull/35). 실제 Cloud/Recovery 입력을 Source에 넣고 실행하는 변경은 이 오프라인 후보 리뷰 이후 별도로 수락한다.

## A 회신 반영과 다음 실제 인계

[A #54 최종 bootstrap 결과](https://github.com/seokpan/seokpan-hybrid-infra/pull/54#issuecomment-6080922047)를 수신했다. bootstrap의 완료를 Foundation 전체 Apply나 B 목적 Role의 ROSA 실행 권한으로 확대하지 않는다. 보고된 B Role seokpan-tf-rosa는 지정 사용자/MFA Trust와 일치하지만 현재 inline1/managed0, 관측 Allow는 S3에 한정됐다. ROSA 서비스 권한·실제 목적 인증·Backend 접근 성공은 아직 미확인이다. EC2 ParamValidation은 전달 오류였으므로 그 오류를 이유로 권한을 늘리지 않는다.

A가 지금 독립적으로 확인할 것은 Foundation 보호 Backend 입력/실행 tfvars, 기존 Data age 암호문에 필요한 입력이 있는지와 공급 가능 범위, B 호출 수요표에 따른 서비스 권한 보완 범위다. 비밀값을 새 공개 양식으로 제출하도록 요구하지 않는다. **항목의 존재/채택 개정/보호 인계 가능 여부**와 미제공 항목·다음 가능한 시점을 먼저 요청한다.

공개 Foundation Source `bbd1d5793fe32e79e02aab2833852c656933b758`의 Backend는 S3이며 key=`phase2/foundation/terraform.tfstate`, workspace_key_prefix=`phase2/foundation/env`, region=`ap-northeast-2`, encrypt/use_lockfile=true다. 따라서 '로컬 Backend 초기화 정보 없음'은 초기화용 보호 입력이 없다는 보고로 기록하며 Backend 종류가 local이라는 뜻으로 바꾸지 않는다. State Bucket·실제 Workspace·기존 초기화/State 존재·실행 인증과 접근 경로는 보호 자료에서 확인한다. 기존 State 위치를 확인하기 전 재초기화/Workspace 생성/State 이전을 시키지 않는다.

| 공개 변수 계약에서 확인할 영역 | A 보호 입력 확인에서 필요한 판정 | B가 지금 임의로 정하지 않을 값 |
|---|---|---|
| aws_region / network_az_ids | 프로젝트 계정의 AZ ID↔이름·3AZ/ROSA Subnet 대응 | 개인 계정 AZ 이름을 다른 계정에 그대로 대응 |
| enable_nat_gateways | Source 기본 false와 승인 NAT3 작업 전제의 실행 입력 정합 | 기본값을 실제 승인 실행값으로 취급 |
| onprem_job_host_cidrs | C 전용 작업 Host /32와 SG/Route 공통 입력 반영 | 빈 기본 목록을 접속 성공으로 취급 |
| RDS Engine/class/storage/master/retention/protection | C 요구·지원 Version·비용/삭제 보호 입력 정합 | Source 기본 사양을 비용 승인으로 채택 |
| redis_auth_token / token_version·Engine/family/node | 보호 금고의 유효 Token 공급 가능 여부·개정·C 조합 정합 | Token 출력/복사 또는 임의 생성 |
| Registry keep count / Backup retention·principal | D Lifecycle 후보/C Backup 개정과 Plan 비용/보호 조건 | 기본50/7일을 실제 수락으로 채택 |

위 표는 공개 변수의 소비 영역 대조이며 완성 tfvars나 암호문 내용 확인 결과가 아니다. 실제 Input 누락은 A가 현장에서 확인한다. B는 A의 Foundation 구현/Apply를 대신하지 않고 인계를 받는 ROSA Root와 목적 권한 계약을 검토한다. Account Role4·Operator Policy Map의 실제 생성/ARN, 프로젝트 AWS 계정·Backend 자료와 SG2는 계속 대기다. Red Hat 조직·정상/대체 담당·AWS 연결/구독·지원 Version·Disk/EBS Quota/실행창도 후보 상태를 유지한다.

## 독립 Source 검사 범위

Cloud 플랫폼 신규6개 시험 그룹, 관리 인증 신규5개를 포함한 Docs 준비 도구20개 시험은 Windows 격리 사본에서 통과했다. Recovery 인벤토리7개 시험 그룹은 로컬에서 통과했고 POSIX 소유/권한·실제 Symlink 검사는 별도 Linux CI에 포함했다. 기존 GitOps 전체 시험은 Windows에서 CRLF ConfigMap과 Linux 실행 Fixture 차이로 실패한 범위를 확인했으며 그 결과를 전체 Source PASS로 기록하지 않는다. 각 신규 GitOps PR의 Linux Source CI에서 기존 선언과 신규 도구를 함께 확인한다. Docs 검사 자료 한 파일은 미수정 상태·원문 해시 확인 뒤 줄바꿈만 Git 원문으로 맞춰 기존 Fixture 해시 검사를 통과했다. 보호 자료·실행 환경 변경은 없었다.

## 실행 분기와 직접 조건

| 순서/분기 | 지금 B가 마친 독립 준비 | 누구의 무엇이 직접 조건인가 | 수신 후 B 작업 → 다음 결과 |
|---|---|---|---|
| Source 공통 | Cloud/Recovery/관리 인증 후보·검사/절차, 기존 OCP Case/자원 계산·기여 근거 | 신규 PR 리뷰 의견/CI | Source 병합·보호 경로에 승인 도구 인계. Runtime 체크는 유지 |
| OCP — ROSA와 병렬 | 기존 Image 수락·Migration/업무 Case 준비 | D32 실제 내부 index/child mapping, 노드 Pull/Owner창/Worker 현재 자원; App41 모드 계약 수정 재리뷰는 별도 | 같은 Image/Config/Schema 조합 수락→FE 다음 BE 순차 교체→다중 투표/WS 유지·재접속·장애·Prune/Delete 차단 새 Run |
| ROSA 기반 | 목적 Role/Backend/SG·Plan 수량 검사 준비 | A Foundation 입력→전체 Plan/비용 승인→Apply/출력, 서비스 권한·공통 ARN/Map·지원/Quota/창; C SG2 판정 | B 목적 인증·기존 State 저장소 사전검증→첫 전체 ROSA Plan→수량/삭제/비용 검토→별도 실행 승인 |
| Cloud 관리/플랫폼 | 제한 Role·수동 Project/Application·Ingress 후보·IdP 수락 절차 | A 실제 ROSA/Team·담당·Owner, 관측 Router/Subject/Namespace | IdP/최소권한/차단 수락→플랫폼 적용/수동 App 등록. Secret·App 입력 별도 |
| Pool / Cloud App | 연결 예산 계산·Cloud3Replica 목표 보류 준비 | C RDS 실제 max/예약 연결·현재 부하, B/C 채택 프로세스/Replica/롤링 예산; ECR/Pull·Endpoint·CA/Secret | Pool 구현/시험→1Replica 실측→3Replica/롤링·Data/업무 수락 |
| 최종 이관 | 기존 서비스의 DB 쓰기 트래픽 중단·재기동 제어/복귀 절차 | 이관 날짜·1차 Cluster 접근 계정/실행 위치/담당/창, C 최종 Dump/Import/행 관계·checksum 결과 | 기존 Writer·Job 중단 실제 확인→최종 Dump/이관/비교→ROSA Migration current→App 검증/진입 전환 |
| Recovery — 대상 준비는 병렬 | Bundle 해시·Manifest/Image 참조 Gate·보호 자료 경계 | C/A 새 격리 대상·Namespace·DB/Engine/Storage/CA·보호 입력, D Image/도구, Controller 외 보존/복원 담당/Identity | 파일 대조→독립 사본/키/복원 Identity→격리 Restore/current/App→RTO/RPO 실측 |
| 프로젝트 종료 | 기여/Source·리뷰·현장 실행 구분과 발표 후보 목록 | 전체 새 Run·비용/보존/삭제 승인·미달 합의 | 증거/시연/발표·Q&A→보존 사본 확인→승인 정리/삭제 확인→최종 종료 |

'병렬'은 직접 조건을 충족한 분기를 다른 분기 전체 완료 없이 시작할 수 있다는 뜻이다. 실제 인계가 없는 분기의 배포를 지금 실행할 수 있다는 뜻은 아니다. 순차적인 Cloud 준비를 A bootstrap 완료만으로 건너뛰지 않는다. 신규 후보는 설치/Owner 변경 없이 검사한 Source이며 어떤 기존 Application에도 연결하지 않았다.

전체 남은 작업:

- [ ] 신규 B Source PR 리뷰/CI·병합 및 승인 개정 보존.
- [ ] D App41 PLAN 계약 수정/재리뷰·Jenkins/검증기 Source와 실제 CI 연결.
- [ ] D 새 공급의 실제 내부 mapping·Pull·Owner창/자원→OCP 조합 시험.
- [ ] A Foundation 보호 입력/서비스 권한/지원·비용·실행창→실제 Foundation 출력·ARN/Map/SG2 인계.
- [ ] B 목적 인증/Backend→첫 ROSA 전체 Plan·수량/삭제/비용→별도 실행·Cluster 인계.
- [ ] IdP/RBAC/Secret·Cloud 플랫폼/NetworkPolicy 실효 검증·캐시 없는 ECR Pull.
- [ ] C RDS 실측→Pool 합의/구현→Cloud App·3Replica/롤링/장애 검증.
- [ ] 1차 서비스 Writer 중단/최종 이관·비교/current/App/전환.
- [ ] Recovery 나머지 입력·독립 사본/복원 Identity/복호화·실제 Restore와 RTO/RPO.
- [ ] 재생성/비용·보존/삭제 보호·Evidence/발표/최종 정리.
