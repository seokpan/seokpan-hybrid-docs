# T03 / controller-seoul-ec2-diagnostic-20261008-01

## 수행·범위

- 실제 수행자: B / jth@ansible. Source `ef424da0a6bfcdd56079ab5be249f429fa0b9c36`, ROSA Lock `668098ad0f1e293982e9bcf8e931128346a00049`.
- 두 진단은 **별도 실행 case**이며 기존 사용량 보충 실패 Run과 구분. 각 CLI 호출1회 보고 수신, 실제 서비스 요청 수·오류 출처는 미확인.
- 전체 T03: **PARTIAL**. 두 case 모두 BLOCKED, 사용량/가용량 숫자 미확보·정확한 원인 미확정.

| case | Controller 표시 시작 시각(UTC) | 수신 시각(UTC) | 원 판정 |
|---|---|---|---|
| v1 | `2026-10-08T13:01:58.931264+00:00` | `2026-10-08T13:11:32.010321+00:00` | BLOCKED / AWS_SERVICE_ERROR / CODE_NOT_IN_ALLOWLIST |
| v2 | `2026-10-08T13:18:50.703071+00:00` | `2026-10-08T13:24:20.096783+00:00` | BLOCKED / AWS_SERVICE_ERROR / UNREGISTERED_OR_UNSAFE_CODE_REDACTED |

실제 종료 시각·Controller/서버 시각 일치 미확인. 시작 표시·수신 시각을 같은 실행 시각으로 사용하지 않음. 원 판정은 [raw](raw.json)·[observations](observations.csv)에 각 case 그대로 보존.

## 현재 판정

- [x] v1/v2 범위 Guard PASS 및 분류 결과 수신
- [x] 두 helper의 정확한 SHA·독립 case·기존5Run 보존
- [x] 추가 자동 API 재시도 종료
- [ ] B 현장·A/계정 Owner의 비공개 확인 입력 수신
- [ ] 실제 사용량/가용량·목적 Role/Backend·지원/비용·첫 전체 Plan 수락

v1의 고정 목록과 v2의 확장된 오류 코드 목록에서도 공개 코드 식별이 되지 않았다. **등록 목록에 없거나 공개 필터에서 제외됐다는 사실만으로 IAM 권한·계정 문제·악성 출력·할당량 부족을 단정하지 않음**. 분류는 로컬 출력 처리 결과이며 원 API 오류 응답을 직접 확인한 판정과 구분.

사용량 숫자가 없으므로 사용량0·가용CPU100으로 처리하지 않음. 앞선 서울 활성·m5.xlarge 사양·Quota13개 읽기·기본 Caller/MFA·정책/Provider/mock 결과는 유지. 기존 성공이나 앞선 실패 Run을 이 결과로 덮어쓰지 않음.

## 다음 입력·행동

- B 현장과 A/계정 Owner가 승인된 비공개 경로에서 오류 분류·실행 위치/계정 범위를 확인. 공개 기록에는 안전한 코드/분류·판정만 인계, 원 오류/응답·자격값/계정/ARN 제외.
- 같은 DescribeInstances 자동 재시도는 추가하지 않음. 원인 확인·Owner 범위 수락과 A 준비표/실제 보호 입력을 수신한 뒤 목적 세션 사전검증으로 연결.
- 실제 역할/Policy Map·SG2·목적 권한/Backend·프로젝트 Red Hat 조직/구독·지원 patch/machine/disk·EBS 기준·예비 비용/Owner/창·전체 Plan은 별도 대기.

[현재 후속](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md), [이전 사용량 보충 Run](../controller-seoul-ec2-usage-20261008-01/summary.md), [05 §9.57](../../../execution/05_IMPLEMENTATION_AND_VALIDATION.md#merged-source-controller-auth-20261008), [원 Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). 전체 T03/TH/Q/Runtime·Cost/DR 완료 가산 없음.
