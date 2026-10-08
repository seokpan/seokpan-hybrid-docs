# 등록 선언 비교·리뷰 정정 후속 — 2026-10-08

## 원 작업과 변경

[GitOps #25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25)·[변경 요청](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25#pullrequestreview-5449781239)에 현재2파일 diff·SHA B 등록 Source·checker 기존 병합·최신 검증 근거를 연결한다. 안내의 현재 보류 Source 설명을 실제 비교 입력 조건으로 정정해 같은 브랜치 HEAD53314d33fcc061e5de4da2f8d3570edd6d5a7273에 반영했다. 검사기·테스트·YAML·targetRevision·replicas·Secret·Gate 변경 없음. PR 제목·본문 갱신 후 ggbun2 재리뷰 요청, 새 승인 대기.

## 수행·검증

- 로컬: Windows 격리 Source. Kustomize5.7.1·Python3.13.15·PyYAML6.0.2, 등록 회귀21PASS.
- 현 등록 Root의 Workload SHA B=bfee2669e62bf823969ce224e5599eccace5d024 입력: 선언 구조 PASS. Workload 승인·실제 RBAC/Owner/사용창·등록/Sync NOT VERIFIED.
- 같은 Render에 SHA A=244b48b885d7ac645c402e561a032ae65a8f3461 입력: 정확 SHA 불일치 BLOCKED, 기대하는 거부 결과.
- Windows 전체69:66PASS/3FAIL. 기존 POSIX fake Kustomize 실행 제약이며 실패·검사/skip 정책 보존.
- [Linux CI37706970618](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37706970618): 정확 HEAD53314d3·Job113083529337·69건 실행/통과 확인. 기존 Python3.12/PyYAML6.0.2/Kustomize5.7.1 정책 유지.
- 당시 구 HEAD/3파일 변경·기존 실패/검사 원 기록은 이력. SHA A PASS를 현53314d3의 검증으로 소비하지 않음.

## 승인된 PR의 후속

- [App20 승인](https://github.com/seokpan/seokpan-hybrid-app/pull/20#pullrequestreview-5449718861): e348895, Source 보완 없음. 의존성/cleanup 예외 정책의 추후 변경 검토와 새 Backend Image/Runtime 수락 별도.
- [App22 승인](https://github.com/seokpan/seokpan-hybrid-app/pull/22#pullrequestreview-5449755134):663b522, Source 보완 없음. Issue21의 현재 상태 정리, Frontend CI 추가는 비차단 후속. 새 Image·실제 UI/Backend/Route 검증 별도.
- [Infra43 승인](https://github.com/seokpan/seokpan-hybrid-infra/pull/43#pullrequestreview-5449687427):7d89def, Source 보완 없음. 기존 선택 Workspace/State 위치·Backend 재초기화는 실제 Plan 전 조건. non-default Workspace를 무검토로 재구성하거나 새 State를 생성하지 않음.

## 한계

Source 검사·승인/리뷰 수신이며 Controller·클러스터·Cloud·금고·DB 재조회/실행 없음. 기존 등록·선택 Sync·본체 금고 성공 보고와 남은 Stage2/Gate/Ready/Route·독립 복원·비용 조건 유지. 전체 T09/T18·RTO/RPO·TH/Q 완료를 추가하지 않는다. Docs72는 원 PR의 병합·브랜치 정리 결과를 수신할 때까지 열린 상태로 유지.
