> **현재 후속 — 2026-10-09:** A bootstrap Apply·재-Plan 변경 없음 보고 수신. Foundation 전체 Plan/Apply·B ROSA 서비스 권한은 대기다. [현재 인계 순서](B_SOURCE_BATCH_AND_HANDOFF_20261009.md)를 따른다. 아래 이전 실패/진단은 당시 기록이다.

# 병합 후속·Controller 인증·실행 대기 — 2026-10-08

현재 추가 수신: D의 Run #5 OCI 복사·bastion 반입/Registry·Worker requests 보고, A PR #54 B 승인·병합 대기를 [새 공급 후속](OCP_RUN5_SUPPLY_FOLLOWUP_20261009.md)에 연결했다. 실제 push·내부 mapping·Pull·교체나 ARN/SG 인계 완료를 뜻하지 않는다. Controller의 격리 오프라인 시험은 Linux 파일3건·SG/Plan10·OCP계산5 PASS를 수신했고 임시 사본 제거·설치 없음으로 마쳤다.

> **현재 확인 — 2026-10-09:** EC2 JSON 전달 오류는 로컬 `ParamValidation`으로 확인했고 정규 임시 파일 교정 후 기존 Controller의 제한 읽기2회가 성공했다. [교정 부분 Run](../evidence/T03/controller-seoul-ec2-input-corrected-20261009-01/summary.md)에서 조회 조건의 인스턴스0·예약0과 미확인 범위를 구분한다. 이 오류에 대한 A IAM 변경 요청/진단 반복은 필요 없다. 프로젝트 AWS 계정 ID·공통 Role/정책·ROSA 작업용 권한/State 저장소·SG2·지원/Quota·비용/사용창 입력은 계속 대기한다. [B 선행 검사·requests 계산](B_OFFLINE_PREPARATION_REVIEW_20261009.md)을 준비했고, 새 Image는 App18819963/Run #5/#32 수락 기준이다. 실제 전체 Plan·OCP 공급/교체·Pool·이관·Recovery는 각 조건 뒤 수행한다. 아래 이전 날짜의 안내는 당시 이력이다.


## 진행 현황

- [x] App30/34·GitOps33·Docs95 병합·PR 브랜치 삭제 확인
- [x] Controller Source/Lock·기본 IAM User/MFA 장치 읽기 및 서울 용량 부분 결과 수신
- [x] D의 새 Run5 Build/Scan/Smoke·Digest 보고 수신
- [x] EC2 진단v1/v2 결과 수신·추가 자동 API 재시도 종료
- [x] EC2 원인 로컬 ParamValidation 확인·교정 조회 완료. 전체 Quota 잔여량은 미확인
- [x] 새 Image 출처·FE/BE Index Digest의 Harbor 공급 후보 수락
- [ ] 보호 보존 근거·내부 mapping/Child Digest·OCP 공급/교체 조건 대조
- [ ] EBS 할당량 기준 차이·기존 사용량·목적 세션/Backend·지원/비용/전체 Plan 수락

| 작업 | 확인 결과 | 실제 다음 단계 |
|---|---|---|
| App30·34 | C 승인 뒤 병합·PR 브랜치 삭제. 현재 App18819963에 승인된 코드·시험 Blob 포함 | D32 Run5 성공 보고 수신, 공급 후보 수락, 내부 mapping/Pull·교체 조건 확인 |
| GitOps33 | C 승인 뒤 main26f7d63d 병합·PR 브랜치 삭제, HEAD2건/병합 main CI 성공 | 기존 등록/Sync 반복 없이 실제 후속 시험 |
| Docs95 | main99afe0db 병합·PR 브랜치 삭제, 기존 Run/팀 기록 보존 | 이번 새 Run·원 Issue·Tracker/05/Index 연결 |
| Controller Source | B/jth의 ef424da0 ff-only·ROSA Lock668098ad 보존 PASS | 성공 Source/Provider/mock 반복 없음 |
| 기본 AWS 인증 | 개인 B 프로젝트 자격 확인. IAM User 인증·현재 Source의 B Trust 대상 일치, 본인 MFA 장치1개 읽기 PASS | 개인 Caller의 독립 준비 조회, 목적 세션/권한은 별도 |
| 서울 용량 읽기 | 서울 활성·m5.xlarge 4 vCPU/16 GiB·4개 AZ, Quota13개/17회 호출 보고 수신 | EBS50↔문서300 기준·기존 사용량/실제 소요·ROSA 지원 대조 |
| D 새 Image | Run5 SUCCESS·새 FE/BE Digest/Image head 보고 수신, B 공급 후보 수락 | 보존/내부 mapping·Child Digest·Pull·교체 조건 확인 |

[T03 Source·로컬 설정](../evidence/T03/controller-source-local-access-20261008-01/summary.md)·[T03 기본 Caller/MFA](../evidence/T03/controller-base-caller-mfa-20261008-01/summary.md). 실제 수행은 B/jth@ansible, 수신 시각과 미제공 실행 시각 구분.

현재 config의 ROSA Role/MFA 프로필0은 실제 IAM 역할 없음·MFA 미등록 판정이 아니다. Multi-Factor Authentication(MFA, 다중 요소 인증) 장치1개는 AWS 읽기로 확인됐다. 장치 선택/OTP 호환·MFA 인증 세션·실제 ROSA 목적 Role/Backend 서비스 권한은 아직 미검증. 현재 Source Trust의 AWS User/tjung, Linux jth, GitHub/Red Hat tjung03을 구분한다. User 이름은 현재 Source 대조 기준이며 승인 설계의 고정 이름은 아니다.

## 서울 용량 읽기·미확인 기준

[T03 서울 용량 Run](../evidence/T03/controller-seoul-capacity-20261008-01/summary.md): 실제 B/jth@ansible의 서울 활성·AWS `m5.xlarge` 사양/4개 AZ·할당량13개 조회, 실제 호출17회 보고 수신. CPU100 vCPU, gp2/gp3/io1 각각50 TiB. 최근15분 CPU 자료 없음은 사용량0이 아니며 다른 할당량의 기존 사용량·잔여량도 미확인.

[공식 Classic §5.1](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/prepare_your_environment/index)의 Minimum required 열은 EBS3종각300 TiB인 반면 [고정 CLI Source](https://github.com/openshift/rosa/blob/c2e552d6d0ada5a50536507f54ceaeaa198df56e/pkg/aws/quota.go)는 gp2/io1 50 TiB를 검사하고 gp3 항목이 없다. 원 helper의 OPTIMAL_REFERENCE_ONLY 출력은 Run에 보존하되, 이 차이를 무시하고 수락하지 않는다. 현재 Controller의 ROSA CLI 버전은 미선정·미설치. A/B·계정 Owner가 적용할 지원/검사 기준을 확인하거나 증설을 조율한 뒤 해당 Gate를 판정한다.

[EC2 사용량 보충 Run](../evidence/T03/controller-seoul-ec2-usage-20261008-01/summary.md): 범위Guard PASS, 첫API1회 뒤 API_OR_NETWORK_ERROR로 중단. 사용량 숫자 미확보·원인 미확정. 앞선 용량 읽기 결과 유지, 사용량0/가용CPU100으로 간주하지 않음. [진단v1/v2 Run](../evidence/T03/controller-seoul-ec2-diagnostic-20261008-01/summary.md) 수신: 각CLI1회에서 코드 비식별 BLOCKED, 정확한 원인 미확정. 추가 자동 API 재시도 종료. B 현장/A 계정 Owner 비공개 확인으로 안전한 코드/분류만 인계받고, A 준비표/실제 입력 수신 뒤 목적 세션 사전검증으로 연결.

등록/공개 필터에서 식별되지 않았다는 사실만으로 IAM 권한·계정 문제·악성 출력·할당량 부족을 단정하지 않음. 기존 서울 용량/기본 Caller 수신 결과는 유지.

AWS 사양/제공 AZ를 ROSA 지원·A의 실제3개 AZ/배치로 승계하지 않음. 총 CP3/Infra3/Worker3 machine·disk 예산, 프로젝트 계정·목적Role 권한·조직/구독·STS·patch·disk·비용/Owner/창·전체 Plan은 미확인. 기존 Source·Provider/mock·정책·Caller/MFA 성공은 반복하지 않음.

## 새 Image 입력·순서

App Source: 188199630ceb5fd67d8fe57d4d5650694e2e00e3. Tag 후보 git-188199630ceb. App30/34 및 D App39 Promotion 후속 포함. App30 코드/시험4개·App34 Full 스펙 Blob이 승인 HEAD와 동일하다.

Migration6파일+alembic.ini는 기존5df2ce28과7개 Blob 동일, Source head20260902_0002. 기존 PR3126 로컬 Full2/UI36 및 Source CI는 원 수행 SHA로 보존. 새 Image 판정은 D의 별도 Run5 보고에 연결.

[GitOps32 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6059607616)의 Source로 Harbor 전용/ENABLE_ECR=false Run5가 완료됐다는 [D 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6060119161) 수신. Full2·UI36·Frontend278·Backend1798·audit0, Image/Scan/Smoke·새 FE/BE Digest 보고는 D 수행 범위다. B는 [공급 후보 수락](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6060263976)으로 Checkout전체SHA→Run/metadata→tag·IndexDigest 추적을 수락했다. nginx 상속 라벨은 App Source 근거에서 제외하고 즉시 라벨 재빌드 불필요. [T09 수락 Run](../evidence/T09/image-supply-acceptance-20261008-01/summary.md)에 정확 Index Digest·7개 Migration Blob/head 대조·보고 수신 한계를 연결. B 직접 Jenkins/Harbor·metadata 파서 미실행, 실제 내부 공급/Pull·교체/Runtime은 미완료.

공급 순서:

1. 지정 실행자·기존 승인 경로·Registry 저장공간/Pruner/Quota·Owner창 확인 → 내부 Registry push
2. push 뒤 실제 원본↔내부 Index/전체linux/amd64 Child mapping 기록·대조
3. 실제 mapping 대조 뒤 GitOps Promotion·노드Pull 검증
4. 추가로 최신 양쪽Worker requests/실사용·종료 중Pod·Owner창 수락 → FE→BE Workload 교체

미생성 내부 Digest를 push 선행조건으로 요구하지 않음. Registry 공급 조건과 Workload 교체 자원 조건을 구분하고, 사용창 확인 없는 자동 push·교체는 수행하지 않음.

## 지금 착수 가능한 작업

| 담당·원 작업 | 가능한 작업 | 준비된 입력·실행 위치 | 판정 이후 행동 |
|---|---|---|---|
| B Infra25 | 공식 EBS/CLI 기준 차이·지원 조합·총 machine/disk 소요 검토 | 서울 사양/할당량 부분 Run 수신, 기존 개인 Controller | A/B·계정 Owner 기준 수락/증설 조율, 기존 사용량·A 실제 배치/계정 입력 대조 |
| B/D GitOps32 | 수락된 공급 후보의 보존/내부 mapping·전체 Child Digest 준비·대조 | D Run5 성공 보고·B 공급 수락·Source18819963/Migration 대응 | 보호 입력/Owner 창·최신 자원 확인 후 공급/Pull·FE→BE 교체 |
| B/A | Red Hat 서울 Region·Machine·공식 disk/지원 조합 검토 | 기존 인증/39개 GA 목록·승인 설계 | 실제 조직·구독·AWS 연결·선택 patch 수락 구분 |
| B/D·OCP Owner | 최신 양쪽 Worker 자원·종료 중 Pod·Pruner/Quota 읽기 및 시험 창 조율 | 기존 승인 OCP 관리 경로에서 수행, 현재 ROSA Controller에는 oc/kubeconfig 없음 | 자원 여유·Owner 창 확인 후 교체/장애/보호 시험 |
| B·Docs21 | 새 Run·병합 정리·현재 작업/직접 입력 연결 | 원 결과·병합 커밋·정상 UTF-8 원문 | D Evidence Index 수신 확인 |

AWS 읽기는 개인 Caller 준비 확인이다. seokpan-tf-rosa의 권한 검사로 승계하지 않는다. 단순 총 Quota와 기존 사용량/실제 Plan 필요량은 각각 대조. ROSA CLI 미설치 상태에서 rosa verify quota 실행 완료로 기록하지 않음.

## 선행 입력을 기다리는 작업

| 작업 | 선행 조건·담당 | 입력 수신 뒤 B의 실행 |
|---|---|---|
| 실제 공통 Role4·Operator Policy Map | A Infra47의 Source 리뷰/적용·Trust/목적 권한·실제 ARN/개정 | 보호 수신·Source/역할/Policy 의미 대조 |
| Data SG2·기반 출력 | Foundation 비용/실행 Gate 뒤 A Apply, C Infra19 이름/VPC/태그/규칙 판정, A 보호 인계 | mariadb↔rds_security_group_id↔seokpan-fnd-rds / redis↔redis_security_group_id↔seokpan-fnd-redis |
| 목적 Role 세션·Backend | A 목적Role Trust/세션/서비스 권한·보호 Bucket/Key/Prefix·기존 State 담당/개정 | 안전한 MFA 실행 경로 확인→목적 Caller·만료·동일 Backend/Provider 주체 대조 |
| 첫 전체 ROSA Plan | 위 실제 입력·계정 대조·프로젝트 Red Hat 조직/AWS 연결·구독/지원 patch/disk/Quota·예비 비용·Owner/사용창 | 보존된 Source/Lock과 보호 입력으로 전체 Plan, 수량/삭제/교체/기반 영향 리뷰 |
| 유료 생성 | 실제 전체 Plan·총비용/가동/삭제/중단 책임·실행창 수락 | 지정 실행자 한 명이 같은 State 쓰기 |
| Pool 구현·Cloud App 활성화 | C 실제 RDS max_connections·예약10, B 실제 Process/Replica/롤링 예산 합의 | 설정·시험·새 Image·실제 연결/부하. 3+2/60 미채택, 첫 ROSA Plan과 분리 |

A #47의 역할4/Policy10/연결4·모의2개 및 bootstrap 관리권한 추가는 로컬 구현/보고다. [역할 준비](https://github.com/seokpan/seokpan-hybrid-infra/issues/47#issuecomment-6058853653)·[bootstrap 로컬 변경](https://github.com/seokpan/seokpan-hybrid-infra/issues/47#issuecomment-6059326439). 실제 main 병합·IAM 적용·ARN/권한 공급과 구분. VPCE는 현재 실제6개 Operator 목록에 없고 필수 누락0 유지.

C의 [Infra19 합의](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6059291050): Apply 직후 실제 SG 판정은 Infra19에 연결. 형식/같은 VPC만으로 맞바뀐 ID를 잡지 못하므로 출력명·키·GroupName 대조. RDS /32 기존규칙1/Redis Foundation규칙0, Worker→Data2규칙 ROSA 소유 유지.

## 일정·실행 대상 확정 후 진행

- B/C Infra17·44: 1차 클러스터 접근 계정·위치는 이관 날짜를 정할 때 함께 확정. Parent/HPA/AutoSync·SelfHeal/쓰기 주체·중지/복귀 경로 확인→지정 실행자/창→당일 쓰기 중지 유지→C 최종 Dump/Import/비교→ROSA Migration current·Revision·Ready·대표 업무. 현재 ROSA Plan의 일괄 선행조건으로 추가하지 않음.
- OCP 실제 교체/장애/Prune/Delete: 최신 자원·Gate/live Diff·실행 경로·Owner 사용창 수락 후 진행. 기존 성공 등록/선택 Sync 반복 없음, base/Recovery hold·Migration suspend 유지.
- Recovery·금고: CA 해시/금고 본체 해독 성공 보존. 실제 Namespace/ConfigMap·DB/Redis/Registry 나머지 입력·독립 사본/복원 Identity 확인은 대상·보호 경로·Owner/창 확정 후 별도 실행.
- 멘토링/OADP는 보류. 03/04 종료·DR10분/RPO30분/Backup15분·CP3/Infra3/Worker3·Cost PARTIAL/$450계획/$500한도·TH81/기존완료2·Q 미완료 유지.

## 남은 작업 현황

### 지금 가능한 작업

- [ ] B 현장/A 계정 Owner: 비공개 오류 분류·실행/계정 범위 확인 입력, 안전한 판정 인계. 같은 API 자동 재시도 없음
- [ ] B/A: 준비표·실제 보호 입력 수신 뒤 목적 세션 사전검증 연결. 성공한 Caller/MFA/용량 목록 반복 없음
- [ ] B/A: 공식 EBS300 TiB와 CLI Source50 TiB의 기준 차이·적용 CLI/지원 개정 확인, CP/Infra/Worker별 machine·disk 소요 초안
- [ ] B/D: 수락한 Run5의 보존 논리 참조·해시·내부 mapping/전체 Child Digest 대조, 현재 OCP 자원·Pruner/Quota·Owner 창 조율
- [ ] B/Docs21·D: 새 증거 Run6개·원 Issue·Tracker/05/Index 연결과 Index 수신 확인

### 선행 입력 대기

- [ ] A: 실제 역할4개·Policy Map/ARN·목적 권한·기반/Backend 제한 출력, A/C: 실제 SG2 판정·보호 인계
- [ ] A/B·계정 Owner: EBS 기준 수락 또는 증설, 기존 사용량·실제 배치/계정·목적 세션/Backend·조직/구독·STS·지원 patch/machine/disk
- [ ] B/A/D: 실제 소요·예비 비용·Owner/사용창 수락 → 첫 전체 ROSA Plan
- [ ] B/C: 실제 RDS 연결 상한·예약/Process 예산 합의 → Pool 구현·Cloud App 활성화. 첫 ROSA Plan과 분리

### 일정·실행 대상 확정 후

- [ ] B/C: 1차 접근 계정·위치/이관일 확정 → 쓰기 중지·C 최종 이관/비교 → ROSA current·App 검증
- [ ] B/D·OCP Owner: 수락한 새 Image의 Registry 공급 Gate→push→mapping/Pull 및 추가 Worker 자원/창 뒤 FE→BE 교체·업무/장애/Prune/Delete 시험
- [ ] Recovery·금고 Owner: 대상 Namespace·입력·독립 사본·복원 Identity 확인
