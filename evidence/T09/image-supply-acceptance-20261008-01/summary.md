# T09 / image-supply-acceptance-20261008-01

## 수행·수락 범위

- Build/Scan/Smoke·Harbor 읽기 수행: D. B는 [D Run5 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6060119161)를 수신하고 GitHub Source·Migration 대조 뒤 [공급 후보 수락](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6060263976)을 등록.
- D 보고 시각: `2026-10-08T12:43:06Z`, B 수락 댓글 시각: `2026-10-08T12:51:28Z`·순서 정정 `2026-10-08T12:56:37Z`, 기록 시각: `2026-10-08T12:55:51.577916+00:00`. Jenkins 실제 시작/종료 시각은 미제공이며 댓글 시각과 구분.
- 대상 Source: `188199630ceb5fd67d8fe57d4d5650694e2e00e3`. Run: `a09-5-188199630ceb`, Final tag: `git-188199630ceb`, Harbor 전용 `ENABLE_ECR=false`.
- 전체 T09: **PARTIAL**. 공급 후보 수락과 실제 OCP 공급/Pull·교체·업무/보호 검증 구분.

## 수신·Source 대조

| 근거 | 결과·한계 |
|---|---|
| D Jenkins main5 | SUCCESS. Backend1798·Frontend278·Browser UI36·Full2·npm audit0 보고 수신 |
| D Scan | Trivy0.72.0, BE CRITICAL0/수정 가능한 HIGH0·전체43건, FE0/0/0. BE를 취약점0으로 표시하지 않음 |
| D Smoke/metadata | FE/BE HTTP200·candidate/final Digest·metadata 필드 대응 일치 보고 수신. B 직접 Jenkins/Harbor 재조회·metadata 파서 미실행 |
| B Source 대조 | Migration6파일+alembic.ini 7개 Blob이5df2ce28·46e21a74와 동일, AST Source head20260902_0002 |
| 실제 Image heads | D 보고20260902_0002 수신. 실제 DB Revision은 C 확인 대상, held Migration 미실행 |

## 공급 후보 Digest 수락

- Backend OCI Index: `sha256:ab0e141abbdf43c5589f9b0af7df38f168044541deec1e10ec7295cb394f4290`
- Frontend OCI Index: `sha256:d26d5385a02ed557863abcba9b3e3cde1fac3ceaf2671f170cdc081729620ac4`
- 플랫폼: `linux/amd64`. 내부 Repository/Index mapping 및 **전체 Child Digest**는 후속 입력이며 D가 제공한 일부 앞자리만으로 대체하지 않음.
- App SHA 라벨은 BE에 없고 FE의 nginx 상속 라벨은 App Source 근거에서 제외. 승인04 §10.3·현행 Release 검사에 해당 라벨 필수 조건이 없어, 이번 공급은 **Checkout 전체 SHA → Run/metadata → FE/BE tag·Index Digest** 연결로 Source 추적 수락. 라벨 추가를 위한 즉시 재빌드 불필요.
- 지정된 기존 경로의 Image 복사 등 공급 준비 가능. 기존git-46e21a74dd60·기존Digest 보존.

## 남은 입력·실행 순서

- [ ] D: Run5/metadata 보존 논리 참조·파일 해시·Evidence Index 연결/수신
- [ ] D·Registry Owner: 지정 실행자·기존 승인 공급 경로·Registry 저장공간·Pruner·Quota·Owner창 확인 → 내부 Registry push
- [ ] D/B: push 뒤 원본↔내부 Repository/Index mapping·전체linux/amd64 Child Digest 기록·대조
- [ ] 실제 mapping 대조 뒤 GitOps Promotion·노드Pull 검증
- [ ] B/D·OCP Owner: 추가로 최신 양쪽Worker requests·실사용·종료 중Pod·Owner창 수락 → FE→BE 교체·업무/보호 검증

미생성 내부 Digest를 Registry push의 선행 입력으로 요구하지 않음. Workload 교체 자원 조건은 Registry 공급 조건과 구분. 공급 후보 수락만으로 사용창 확인 없는 push·Promotion·교체를 허용하지 않음.

base/Recovery hold·Migration suspend 유지. 기존 성공 등록/선택Sync 반복 없음. 실제 OCP Runtime·ECR/Cloud·전체T09/TH/Q 완료로 승계하지 않음.

## 연결

[현재 후속](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md), [05 §9.57](../../../execution/05_IMPLEMENTATION_AND_VALIDATION.md#merged-source-controller-auth-20261008), [원 GitOps #32](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32). D Index 제출/수신과 보호 원문 보존 확인은 별도.
