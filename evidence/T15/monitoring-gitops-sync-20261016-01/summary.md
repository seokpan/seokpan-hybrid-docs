# Run Summary — T15 사전 준비 (모니터링 GitOps Sync·규칙 로드·smoke)

이 Run은 T15(관측·알림·판단)의 **사전 준비 부분 실행**이다. 실제 장애 주입과 Metric/Alert 상관, 알림 조건·확인 지연, 알림 전달은 수행하지 않았다.

## Identity and Scope

- Test / Case / Requirement / Run / Release: T15 / 사전 준비(부분) / 02 §12·§13 / monitoring-gitops-sync-20261016-01 / 해당 없음(앱 Image 없음)
- 대표 Issue / PR / 이전 실패·후속 Run: seokpan-hybrid-gitops Issue #54 / PR #55 (병합 커밋 `16fd14cd1c085a8314a5e2e18b89e2cd3b051626`) / 이전·후속 없음(앱 기동 후 target 확인 Run 예정)
- 환경·대상 / Source·Image·입력/도구 개정: ROSA `seokpan-cloud`, Namespace `seokpan-cloud`, Argo `openshift-gitops` / GitOps `16fd14cd…` (`platform/rosa-monitoring/app`), App·Infra Image 없음
- 배정 실행 책임자 / 실제 수행자 / Reviewer / 협업 내용: D 최유준 / 최유준(Argo·OpenShift 계정 `cyj200115-prog`) / **미지정(리뷰 대기)** / 정태훈: Application·AppProject 최초 등록(Infra Ansible)과 Controller 권한 18개 확인
- 실행 조건·부하·장애 주입 / 대상외 항목과 이유: 부하·장애 주입 없음. 앱 미기동(0 Replica 보류)이라 ServiceMonitor target UP, 앱 지표(`seokpan_http_requests_total`) 수집, Replica·5xx 규칙의 실제 평가는 제외. Alertmanager 수신처 설정과 알림 전달은 이번 범위 밖

## Results

- Render: PASS — `kustomize build platform/rosa-monitoring/app` 성공, 소스 테스트 182개(신규 7개 포함)·Cloud 회귀 19개·Route 회귀 11개 통과 ([GitOps source validation](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/38830427515)). PR #55는 Source 후보 리뷰에서 승인됨(T15 시험 리뷰 아님)
- Deployment: PARTIAL — `seokpan-cloud-monitoring`만 수동 Sync(Prune/Force 미사용)해 Synced/Healthy, ServiceMonitor·PrometheusRule·NetworkPolicy 3종 생성. 앱·Migration은 실행하지 않음. 런타임 동작(target UP 등)은 미확인
- Acceptance: NOT RUN
- Baseline / Target / Actual / 단위·집계 조건: Baseline·Target 없음. 센 값만 기록(객체 3개, 로드된 규칙 3개). 지연·평가 시간은 정밀 측정하지 않음
- 대표 업무·Data 일관성 / 실패·제한: 해당 없음(앱 미기동). 제한: smoke 활성 시작(약 12:05)은 화면의 "7분 전"에서 환산한 근사치이며, firing 확인은 12:12에 한 번 수행. 적용 → firing 지연의 상한은 약 8분이고 정밀 값이 아님
- 실제 시작/종료 UTC / 같은 시각의 KST / 시계·시점 불확실성: 2026-10-16T03:04:26Z ~ 03:59Z(종료는 분 단위) / 12:04:26 ~ 12:59 KST. 시계는 작업 PC·ansible-controller·Argo 화면의 시스템 시계이며 상호 동기화는 검증하지 않음

## Evidence and Recovery

- metrics.csv / timeline.csv / checksums.txt: 이 폴더의 파일. 캡처와 터미널 출력은 `artifacts/`(터미널 출력 5개: 01·03·04·05·08, 캡처 3개: 02·06·07, 이메일 등 마스킹, 토큰 없음)
- 보호 Raw 논리 참조 / 보관자·접근·보존 책임 / 가용성·무결성: 보호 Raw 없음. 공유 파일만 사용, 보관은 최유준, 무결성은 checksums.txt의 SHA-256
- Backup ID·암호문 Hash·Data 기준 시각/확인 수준: 해당 없음(복구 Run 아님)
- 장애/판단·Dump·복원·업무 재개 단계 / RTO·RPO와 계산 근거: 해당 없음
- 영속 Data 손실 / 새 Redis Runtime 손실: 해당 없음

## Follow-up

- 원인·조치 / 수정 Commit·입력 개정: 없음. 관련 개정은 `16fd14cd…` 하나
- 현재 부분 State·자원·Lock·잔존 비용 / 정리·다음 인계: smoke PrometheusRule은 12:14:40 KST에 삭제되어 잔존 없음. Argo 관리 객체 3종은 유지. 새 유료 자원 없음(UWM은 ROSA 기본 구성). 롤백은 Argo에서 모니터링 Application의 리소스 3종 수동 삭제
- 영향받는 재시험·다음 Run / 담당·필요 시점: 앱 기동 후 (1) ServiceMonitor target UP, NetworkPolicy 허용 확인 (2) Replica·5xx 규칙 실제 평가와 정상 Baseline 측정 후 임계값 조정 (3) Alertmanager 수신처와 알림 전달 확인 (4) T15 본체(장애 주입·상관). 담당 D, 앱 기동 일정은 B 확인 필요
