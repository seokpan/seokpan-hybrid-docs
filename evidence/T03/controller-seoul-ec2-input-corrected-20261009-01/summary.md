# T03 / controller-seoul-ec2-input-corrected-20261009-01

## 수행·판정

B / jth@ansible의 기존 교정 실행 판정 수신 기록이다. 이번 문서 작성에서 API를 새로 호출하지 않았다. Controller 표시 시작 `2026-10-08T15:51:36.995087+00:00`, 종료 `2026-10-08T15:51:38.623044+00:00`(KST 10/09 00:51). 실제 Controller/서버 시각 일치와 단일 시점 snapshot은 미확인이다.

Source `ef424da0a6bfcdd56079ab5be249f429fa0b9c36`, Lock `668098ad0f1e293982e9bcf8e931128346a00049`, helper SHA256 `e8c8823946bcbe05b9e6064a5d6fa2891863f9eab869202dfb16805799281398`. Infra 최신 main `aaa8cff…`와의 ROSA/Lock 불변 대조는 별도 Source 검토이며 이 실행 SHA를 바꾸지 않는다.

## 원인과 제한 조회 성공

- 원인은 AWS CLI의 `ParamValidation`: 기존 `file:///dev/stdin` JSON 입력이 오프라인 검사에서 Invalid JSON/EXIT252로 실패했다. 같은 고정 JSON의 inline 전달은 성공했다. 이전 서비스 오류 분류는 로컬 입력 오류로 정정한다.
- 일반 임시 요청 파일 전달로 교정했다. 오프라인 정규 파일 검사 PASS 뒤 CLI 읽기2회 성공, Instance/Capacity Reservation 각각1페이지 완료.
- 조회 조건에서 실행 중 Standard On-Demand 인스턴스0·기본 vCPU 소계0, 해당 Standard 예약0·미사용 예약 vCPU 소계0을 수신했다. Instance Type 조회는 목록이 비어 실행되지 않았다.
- 요청 임시 파일700/600·호출 후 제거는 helper 구현 및 판정 보고 범위다. 자격증명·응답·실제 ID/ARN/계정 값을 저장/게시하지 않았다.

## 남은 조건

전체 T03는 **PARTIAL**. 제한 조회 0건은 전체 계정 사용량0·현재 잔여CPU100·AZ 배치 또는 ROSA 준비 PASS가 아니다. 프로젝트 AWS 계정 ID와 A 입력 대조, 숨은 관리 자원·서비스별 Quota 사용량/계산, 목적 Role/State 저장소·지원·비용·첫 전체 Plan은 미확인이다.

해당 JSON 전달 오류를 해결하기 위한 A IAM 변경 요청은 필요 없다. 성공한 진단·Caller/MFA·Token·정책 조회를 반복하지 않는다. 실제 IAM/Quota/자원 변경·세션 발급·State/Plan/Apply는 NOT RUN.

[최초 실패 Run](../controller-seoul-ec2-usage-20261008-01/summary.md)·[분류 실패 이력](../controller-seoul-ec2-diagnostic-20261008-01/summary.md)을 보존한다. [현재 ROSA 준비](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md)·[B 선행 준비](../../../execution/B_OFFLINE_PREPARATION_REVIEW_20261009.md)·[Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25)에 연결한다. Index 제출과 D의 수신은 별도다.
