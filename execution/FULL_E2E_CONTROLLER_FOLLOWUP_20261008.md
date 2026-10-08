# Full e2e·Controller 후속 — 2026-10-08

## 진행 현황

| 작업 | 현재 근거 | 다음 작업 |
|---|---|---|
| Full e2e 보완 | [App #34](https://github.com/seokpan/seokpan-hybrid-app/pull/34), clean HEAD3126ae28. Full2·UI36·unit278·tooling81·정적/빌드 PASS. [검증 Run](../evidence/T09/full-e2e-ui-followup-20261008-01/summary.md) | 리뷰·병합 → 최종 main SHA → D #32 단일 새 Build |
| Controller 최초 검사 | c5d8/Lock6680 최신화·격리 Root init/validate PASS, 최초 mock BLOCKED. [최초 Run](../evidence/T03/controller-source-provider-20261008-01/summary.md) | 당시 실패와 실행 SHA 보존 |
| Controller 교정 | 필수 입력 오류7개 확인. 합성 입력 공급 후 exit0·mock2/2·Source/Lock/원 로그 보존 PASS. [교정 Run](../evidence/T03/controller-oidc-mock-retry-20261008-01/summary.md) | 실제 Caller·Backend·지원·비용·입력 수락 |
| A 정책 수신 | [Infra #47](https://github.com/seokpan/seokpan-hybrid-infra/issues/47#issuecomment-6057625147): 원본/사본18개·manifest17개 해시 및 권한 검사 보고 수신 | 정책/신뢰 검토·실제 역할4개·ARN Map·권한 적용·제한 출력 |

Full e2e(End-to-End, 전체 사용자 흐름 검사)는 loopback의 휘발성 Memory Backend 검사다. 실제 SQL/Valkey/TLS/OCP·Image Build/Scan/Digest 성공을 뜻하지 않는다. Controller 검사는 OpenID Connect(OIDC, 클러스터 외부 인증 연결)의 합성 입력과 모의 Provider를 사용했다. 실제 Cloud Plan과 구분한다.

A의 실행 보고 수신을 B의 직접 재검사로 표현하지 않는다. B의 새 인계 archive 생성과 A가 기존 원본 사본을 수신한 경로도 별도 기록. 정책 원문·Token·실제 보호 경로·전체 State/Saved Plan은 공개 기록 대상에서 제외.

## VPCE 미제공 정책

보관 후보8개 중7개 확보는 당시 조회 범위다. 실제 Controller Operator 목록6개에 필요한 정책은 모두 있으며 VPCE는 해당6개에 포함되지 않는다. 현재 필수 정책의 누락이 아니며 추가 자동 공급 예약이나 영구 제외 결정도 없다.

Provider·지원 patch·API 목록·PrivateLink 설계 변경 후 새 필수ID가 나타나면 해당 공식 정책만 추가 확보하고 manifest·Policy Map·A 구현을 검토한다. 기존 묶음 보존·성공 조회 전체 반복 불필요.

근거: [현행 oidc.tf](https://github.com/seokpan/seokpan-hybrid-infra/blob/c5d8c4242cf62bcc995715c9f8b6964c2f40dc7a/terraform/rosa/oidc.tf), [공식 Provider1.7.7](https://github.com/terraform-redhat/terraform-provider-rhcs/blob/v1.7.7/provider/rosa_operator_roles/classic/rosa_operator_roles_data_source.go). Provider가 PrivateLink/patch별 정책을 자동 제외한다고 설명하지 않는다. 실제 IAM ARN·권한은 A 공급 후 대조.

## 새 Image·병합 순서

D의 Jenkins main4/a09-4-5df2ce280188은 Full 단계 FAILURE, 새 Image/Digest 없음. Backend1774·Frontend278·UI36·audit0 통과와 이후 Image/Scan/Smoke/Evidence skip은 D 수행 보고로 수신. 최신 main6c에서도 같은149행 실패를 재현했고 App34에서 스펙1파일만 보완했다.

App30(기동 정리)과 App34(Full 스펙)는 파일 의존·충돌 없음. 새 승인을 받은 PR부터 병합 가능하지만 D 재빌드는 두 App 변경 병합 후 최종 main SHA 하나로 진행한다. 미병합 수정이 기존5df Image에 포함됐다고 승계하지 않는다.

최종 SHA·Migration 디렉터리6파일+alembic.ini·head20260902_0002 대조 → D32 Build/Scan/Smoke/Digest → B 수락 → 내부 mapping/새 Pull → 실제 교체 조건 확인. GitOps33은 별도 설정 검사이며 Image Build의 직접 선행조건은 아니다. 문서 PR도 Source PR 병합을 기다릴 필요 없음.

## C의 SG·Pool 회신

| ROSA 입력키 | Foundation 출력 | 확인할 GroupName·포트 |
|---|---|---|
| mariadb | rds_security_group_id | seokpan-fnd-rds·RDS3306 |
| redis | redis_security_group_id | seokpan-fnd-redis·Valkey6379 |

Security Group(SG, 인스턴스 통신 허용 규칙)의 두 Source는 같은 VPC·Component=data. Foundation은 SG 본체와 온프렘 백업/32→RDS3306 별도 Rule1개를 소유, Redis 규칙은0개. Worker→Data2개 규칙은 ROSA State 소유다.

형식·서로 다름·같은 VPC 검사만으로 ID 맞바뀜을 검출하지 못하므로 **출력명↔입력키↔GroupName**을 함께 대조한다. 실제 공급은 A의 Foundation Apply 뒤 보호 경로로 진행하며 날짜는 Foundation 비용·실행 조건 뒤 결정. C는 직후 이름·VPC·태그·RDS 기존 Rule1개/Redis0개의 읽기 대조 결과만 공개한다. 현재 실제 ID 미공급을 Source 설명으로 완료 처리하지 않는다.

C는 [Pool 예산 준비](DB_CONNECTION_BUDGET_PREPARATION.md)에 동의했고 실제 상한·예약·설정 수락을 Cloud App 활성화 조건으로 제안했다. 기본 Pool 상한90과85미만 예상의 충돌은 위험 판단이며 실제 RDS 조회값은 아님. RDS 생성 후 B/C 결정, 3+2/60 미채택 유지. Pool 완료는 첫 ROSA Plan의 전체 선행조건이 아니다.

## 남은 입력·실행

1. **B Source:** Infra ef424da0은 C Data Ansible8파일만 추가, 모든 Terraform/ROSA19파일·Lock·실행 helper 동일. c5 시험 근거 유지. 다음 Cloud 준비 전 개인 변경·원격 delta·ff-only·Lock만 확인, 성공한 정책/버전/Provider/mock 반복 불필요.
2. **A·C/A:** 정책·신뢰 적합성, 역할4개·실제 ARN Map·목적 권한·기반/Backend 제한 출력·기존 State 실행자·공급 시점, 실제 Data SG2개.
3. **A/B·B:** 프로젝트 Red Hat 조직·관리자·AWS/OCM 연결, 정확 Caller/Backend·구독·서울 지원 GA/m5.xlarge·disk·Quota. 버전39개 enabled/rosa만으로 전체 수락 불가, STS flag UNKNOWN.
4. **B/A/D:** 예비 비용·실행자·사용창 수락 → 첫 전체 Cloud Plan. 유료 생성은 전체 Plan 리뷰·비용·가동/삭제 조건 수락 뒤 진행.
5. **B·기존 관리 담당:** kubectl/oc·승인 kubeconfig·실제 1차 Context 읽기 준비. 쓰기 중지 제어·실행자/창 → 이관 당일 중지 유지 → C 비교 → ROSA current/App. kubeconfig 자동 전달·임의 복사/패키지 설치 없음.
6. **D/B OCP:** Worker requests99/95%·실사용82/85%는10/8 18시 D 보고. 최신 자원·종료 중 Pod·Pruner·Quota·Owner 창·Gate/live Diff 확인 후 FE→BE. 272Mi/옛 보고만으로 실행 수락하지 않음.

제공 HTML은 당시 참고 자료다. 관리 추정70/88%를 공식 WBS/TH 완료율로 사용하지 않는다. 최신 원 Issue/PR/Run 우선, TH81/기존완료2·Q 미완료·설계03/04 종료·DR10/RPO30/Backup15·CP3/Infra3/Worker3·Cost PARTIAL/$450/$500 유지. 멘토링/OADP 보류, Index 연결 제출과 D 수신 구분.

## 다음 로컬 확인 묶음 — 준비 완료·Controller 미실행

논리 참조 controller-source-local-access-20261008 / Source SHA25697aa4567429ea80ad21bce0e7cb3e01426fc9bcea2e868eb8ffad3d60cc0e44a.
검토된 Infra ef424da0의 ansible/data 변경만 개인 변경·새 원격 변경·ignored 파일 충돌이 없는 경우 ff-only, 기존 ROSA Lock 보존. jth의 보호 AWS config에서 목적 Role/MFA 설정 유무를 값 없이 확인하고 credentials 파일은 존재·소유자/권한만 확인한다.

실제 계정/프로필명·ARN·자격 값 출력/자격 파일 내용 조회·AWS/RHCS API·State/Output/Plan·기존 성공 시험 반복 없음. Role 프로필 존재가 인증·권한 PASS를 뜻하지 않음. Python3.9 구문·정적 조건 검사 완료, 실제 실행 판정은 다음 원 Infra25/새 Run으로 기록.
