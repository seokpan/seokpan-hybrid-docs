# 병합 후속·Controller 인증·실행 대기 — 2026-10-08

## 완료 범위

| 작업 | 확인 결과 | 실제 다음 단계 |
|---|---|---|
| App30·34 | C 승인 뒤 병합·PR 브랜치 삭제. 현재 App18819963에 승인된 코드·시험 Blob 포함 | D32 새 Image Build/Scan/Smoke/Digest |
| GitOps33 | C 승인 뒤 main26f7d63d 병합·PR 브랜치 삭제, HEAD2건/병합 main CI 성공 | 기존 등록/Sync 반복 없이 실제 후속 시험 |
| Docs95 | main99afe0db 병합·PR 브랜치 삭제, 기존 Run/팀 기록 보존 | 이번 새 Run·원 Issue·Tracker/05/Index 연결 |
| Controller Source | B/jth의 ef424da0 ff-only·ROSA Lock668098ad 보존 PASS | 성공 Source/Provider/mock 반복 없음 |
| 기본 AWS 인증 | 개인 B 프로젝트 자격 확인. IAM User 인증·현재 Source의 B Trust 대상 일치, 본인 MFA 장치1개 읽기 PASS | 개인 Caller의 독립 준비 조회, 목적 세션/권한은 별도 |

[T03 Source·로컬 설정](../evidence/T03/controller-source-local-access-20261008-01/summary.md)·[T03 기본 Caller/MFA](../evidence/T03/controller-base-caller-mfa-20261008-01/summary.md). 실제 수행은 B/jth@ansible, 수신 시각과 미제공 실행 시각 구분.

현재 config의 ROSA Role/MFA 프로필0은 실제 IAM 역할 없음·MFA 미등록 판정이 아니다. Multi-Factor Authentication(MFA, 다중 요소 인증) 장치1개는 AWS 읽기로 확인됐다. 장치 선택/OTP 호환·MFA 인증 세션·실제 ROSA 목적 Role/Backend 서비스 권한은 아직 미검증. 현재 Source Trust의 AWS User/tjung, Linux jth, GitHub/Red Hat tjung03을 구분한다. User 이름은 현재 Source 대조 기준이며 승인 설계의 고정 이름은 아니다.

## 새 Image 입력·순서

App Source: 188199630ceb5fd67d8fe57d4d5650694e2e00e3. Tag 후보 git-188199630ceb. App30/34 및 D App39 Promotion 후속 포함. App30 코드/시험4개·App34 Full 스펙 Blob이 승인 HEAD와 동일하다.

Migration6파일+alembic.ini는 기존5df2ce28과7개 Blob 동일, Source head20260902_0002. 기존 PR3126 로컬 Full2/UI36 및 Source CI는 원 수행 SHA로 보존. 새 main Image 성공으로 바꾸지 않음.

[GitOps32 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6059607616): Harbor 전용/ENABLE_ECR=false로 해당 SHA 새 Run1회. 실행 전 Source가 바뀌면 실제 checkout SHA와 대상 일치를 먼저 확인. 새 Jenkins Full→Build/Scan/Smoke/Evidence→실제 Source label/FE·BE Digest/Migration Image heads→B 수락→내부 mapping/Pull→Owner 사용창·자원 대조 후 FE→BE 교체. 기존 실패 main4나 승인 Image 승계 없음.

## 지금 착수 가능한 작업

| 담당·원 작업 | 가능한 작업 | 준비된 입력·실행 위치 | 판정 이후 행동 |
|---|---|---|---|
| B Infra25 | 서울 Region·m5.xlarge 제공/사양·Quota 할당/사용량 읽기 | 기본 IAM User 인증·MFA 장치 읽기 완료, 기존 jth Controller/개인 자격 | 공식 지원·실제 Plan 필요량과 대조, 부족분은 A/계정 Owner 조율 |
| D GitOps32 | 새 SHA 단일 Build/Scan/Smoke/Digest | 위 Source·Migration 대응, 기존 Jenkins/Harbor 실행 경로 | B Digest 수락 후 공급/교체 조건 확인 |
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
