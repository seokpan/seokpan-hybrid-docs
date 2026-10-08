# Controller 정책 사본 읽기 검증 — 2026-10-08

- 실제 실행: B, 기존 Controller jth@ansible. 전달된 실행 로그의 판정만 수신. 조회 코드를 재실행하거나 정책 원문을 업로드하지 않음.
- 사본 논리 참조: `rosa-policy-20261008T061153Z-6caf4295`.
- 현재 소유자·권한: PASS, 폴더700/파일600.
- manifest 등록 파일 해시: 17개 일치 PASS. manifest는 독립 서명되지 않았으며 파일과 manifest의 동시 변경·외부 원본 진위 확인을 대신하지 않음.
- 누락 정책 ID: `openshift_aws_vpce_operator_avo_aws_creds_policy`.
- A 보호 인계·수신: NOT CONFIRMED. API/AWS/IAM/Terraform 호출·파일 수정: NOT RUN.

## Source 대조·판정 경계

[현행 ROSA cluster.tf](https://github.com/seokpan/seokpan-hybrid-infra/blob/c5d8c4242cf62bcc995715c9f8b6964c2f40dc7a/terraform/rosa/cluster.tf)는 private=false, aws_private_link=false. [oidc.tf](https://github.com/seokpan/seokpan-hybrid-infra/blob/c5d8c4242cf62bcc995715c9f8b6964c2f40dc7a/terraform/rosa/oidc.tf)는 실제 Operator 목록6개와 Foundation Policy Map의 policy_name 일치를 요구. [RHCS1.7.7 공식 역할 Source](https://github.com/terraform-redhat/terraform-provider-rhcs/blob/v1.7.7/provider/rosa_operator_roles/classic/rosa_operator_roles_data_source.go)는 STSCredentialRequests 목록을 조회해 역할·정책 이름을 생성.

공식 정책 이름8개를 실제 필수 역할8개로 해석하지 않음. 이번 누락만으로 전체 PASS나 첫 Plan 차단을 확정하지 않음. 실제 STS Operator 목록·필요 정책과 A의 실제 ARN Map 대조는 미실행/미수신. 이름 유사성을 근거로 다른 정책으로 대체하거나 Source의6개 Guard를 약화하지 않음.

## 다음 담당·입력

1. B: 보호 사본의 조회 출처·코드 해시·manifest·원 정책 파일을 기존 승인 보호 경로로 A에게 인계, 실제 전달/수신 기록.
2. A/B: 실제 Classic Operator 목록과 공급 Policy Map 대조. Account Role4와 Support Trust 확보 결과를 공통 IAM 준비에 사용하되 실제 기존 자원/Trust/목적 권한·State 주체는 별도 확인.
3. B: 개인 clone origin/main·개인 변경·Lock 수락, 목적 Caller/Backend·지원/Quota/disk·예비 비용/Owner/창을 확인해 첫 전체 Plan 준비.

## 기록 범위

[앞선 API 조회 Run](../redhat-policy-read-20261008-01/summary.md)의 당시 미검증 표시는 보존하고 이번 새 Run으로 연결. 실제 검사 시각·시계 동기화는 전달 로그에 없어 null. Token·정책 원문·실제 보호 경로·전체 State/Output/Plan은 공개 파일 제외. 전체 T03·ROSA 준비/Plan·TH81/기존완료2·Q·Cost·DR 완료 가산 없음. D Index 수신 별도 대기.
