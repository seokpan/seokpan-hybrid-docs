# D 미완료 인계 요청 통합 — 2026-10-11

기존 Issue/PR·직접 회신을 대조한 현재 B 요청이다. 이전 미완료 요청은 아래 기준으로
확인하고 완료 결과·보호 자료·원본 이력은 유지한다. 새 현재 승인/측정으로 과거 빈칸을
소급 채우지 않는다. 자동 발송 기록은 아니다.

## 완료·재요청하지 않는 부분

- Run5 Build·Scan/Smoke·Index 수락, OCI/tar/내부 Registry mapping·ImageStream 대조·임시 SA/Binding 정리 보고.
- worker-2 FE/BE Succeeded/exit0·child imageID 일치. 당시 절차 전체/전체 신규 다운로드는 별도.
- App41 PLAN 경계 수정·승인·병합·Jenkins 연결 Source, 기존 Writer/Transport 성공 시험.
- GitOps37 Source/Image 승인과 이미 병합된34/35/36의 리뷰, lab Stage2의 공급/부분 업무 성공 보고.

## 요청 범위·지금 가능한 부분·선행조건

| 요청 | 지금 가능한 부분 | 실제 실행 선행조건 | 받을 결과·기록 |
|---|---|---|---|
| OCP 자원/창 | 기존 조사 재사용·변경/복구 후보 준비 | Peak·전환/원복·호스트/게스트·현재 자원 | 후보·범위/값·시각/충돌·미확인, GitOps32/6 |
| worker-2 증거 | 보존 기록의 존재 확인 | 새 실행 불필요 | 당시 사용창·실행 직전/FE→BE 사이 requests/Pressure 참조 또는 없음, GitOps32 |
| Source 리뷰 | GitOps38·App43 의견/승인 | AWS/ROSA 인계 불필요 | 해당 PR의 검토 HEAD·의견/Approve |
| Image/Promotion | App42 Scan 수정, Release 검증기·CI 계약/거부 시험 | 승인·병합 Source, Scan/Smoke/Evidence·Agent/기존 Credential·창 | PR/HEAD/시험, Run/Source·metadata·result·Release ID·변경 파일, WRITE 후 PR/CI, App42/15 |
| 부하/관측 | Harness/스크립트 개정·샘플/누락 | 실제 조합·자원/장애 범위 | Client 업무 지연·초회/오류/재시도·Room/인원·timeline·원본, T15/T16 |
| 비용/Registry 수명 | 후보 비교·최신 Data 입력·누락 정리 | 실제 Plan/지원·시간, ECR Preview는 실제 대상 | 최신 원장·총액/미확인·잔존/재시험/삭제·Preview/keepCount 또는 후보, Docs43 |
| Recovery 자산 | 현재 Image/Archive/도구 목록·해시·보호 위치·접근 가능 범위 | 대상/버전·CA·독립 사본/복원 주체 확정 | 기존 참조·남은 항목·호환 미확인/시점, 실제 Bundle/Pull/복원 별도 |

App42의 새 Pipeline 차단은 Run5의 기존 성공/공급을 자동 부정하지 않는다.
App43 병합 후 Pool Source가 Run5에 이미 포함됐다고 승계하지 않는다. 승인된 최종
Source로 Build/Scan/Smoke·Digest/플랫폼·Migration heads를 새 개정으로 연결하며
OCP Run5 후보와 후속 Release의 Source/Image/증거를 섞지 않는다.

## 전달용 문안

```text
D님, 요청이 여러 메시지에 나뉘어 있어 미완료 확인 항목을 아래로 통합했습니다.
이전 메시지의 남은 요청은 이 목록으로 확인 부탁드립니다. 완료 결과와 원본
증거는 유지하며 Registry 공급·worker-2 Pull·Writer/Transport 시험·App41 구현과
GitOps37 Source 승인을 다시 요청하는 것은 아닙니다.

1. OCP 자원 확보/실행창
OCP 변경은 우리 팀에서 결정·진행합니다. B가 기존 조사와 자원 산술·변경/
복구 순서를 정리했으니 현장 입력을 부탁드립니다. cluster/gitops-plugin의
사용처·Peak, 상위 CR의 변경 전후 값·전환/원복 자원·기능 영향, 또는 호스트
가용 RAM/CPU·VM 증설/게스트 인식·재시작 필요 여부를 알려 주세요.
재시작 후보는 Pod 이동/PDB/로컬 데이터와 반대편 수용 여유까지 필요합니다.
날짜·시작/종료·실행/중단 연락·Pruner 등 동시 작업도 함께 정하겠습니다.
기본 ArgoCD/controller/dex·GitopsService 전체 중단/삭제, FE 중단·64Mi 감축,
Priority/SCC/nodeName/Pruner 변경은 현재 실행안으로 채택하지 않았습니다.
실행안 대조→변경 직전 양 Worker 재측정→자원 확보/복구 확인→worker-1 FE/BE
Pull→검토된 SHA의 FE/BE 순차 교체·업무/보호 시험으로 이어가겠습니다.

2. worker-2 기존 증거
당시 사용창과 실행 직전·FE→BE 사이 requests/Pressure 기록이 남아 있는지
참조 또는 없음만 확인 부탁드립니다. 성공 결과는 유지하고 새 측정으로 당시
빈칸을 채우지 않습니다. 지금 재시험 요청은 아닙니다.

3. Source 리뷰
GitOps38·App43은 기존 리뷰 요청에 따라 해당 PR에 의견/Approve 여부를 남겨
주세요. GitOps37의 기존 Source 승인과 실제 교체 조건은 구분해 유지합니다.

4. Image·Release 검증기·Jenkins
App42 Scan 차단 후속의 수정 PR/검사·새 Run 상태, Release JSON 검증기와
GitOps CI의 구현 개정/거부 시험·남은 범위를 알려 주세요. App41 Source는 완료입니다.
실제 Controlled Run은 기존 Credential/Agent·실행창과 Scan/Smoke/Evidence가
준비되면 REMOTE_CHECK 결과부터 검토하고 WRITE 범위를 확인하겠습니다.
Run URL·실제 App/GitOps SHA·metadata 참조·promotion-result 상태/Release ID·
변경 파일을 받고, WRITE 뒤 생성 PR/CI를 확인합니다. 불확실 생성은 자동 재시도하지 않습니다.
App43 병합 후에는 최종 승인 Source의 Build/Scan/Smoke·Digest/플랫폼·Image
Migration heads를 새 개정으로 연결해 주세요. Run5에 신규 Pool 수정이 들어
있다고 승계하거나 Run5 공급을 다시 할 필요는 없습니다.

5. 부하·관측 준비
기존 Harness/스크립트 PR·개정과 비밀정보 없는 출력 예시, 미구현 항목을
알려 주세요. Client HTTP/업무 WS p95, 초회 시도·실패/불명·재시도,
Room/동시 인원·시간, 장애 시작→의존성 복구→Client 업무 수렴과
Metric/Log/Alert 연결을 대조하겠습니다. HTTP Histogram/WS Ping은 업무 WS
측정을 대신하지 않습니다. 전체 부하·장애 실행은 실제 조합과 자원 확보 후입니다.

6. 비용·Registry 수명
최신 원장 개정과 남은 입력, A/B 창·디스크 후보·NAT3·Data 최신 입력의
비교/총액·잔존/재시험/삭제 비용을 알려 주세요. 미정은 후보/미확인으로 유지합니다.
ECR keepCount는 실제 대상의 Lifecycle Preview 뒤 판단하며 기본50을 확정값으로
채택하지 않습니다. AWS 실제 인계가 없으면 지금은 비교·누락 정리까지만 진행하면 됩니다.

7. Recovery 보존 자산
현재 확보한 Image/Archive·필수 도구의 개정/해시·보호 보존 위치와 공급 가능
범위·남은 항목을 알려 주세요. 이미 제공한 자료는 기존 참조면 됩니다.
대상 버전/CA·Controller 외 독립 사본·복원 접근 주체는 C/B/D와 확정하고
실제 전체 Bundle/Pull/복원은 그 후 진행합니다.

항목별 완료/진행/막는 입력·다음 가능 시점과 기존 Issue/PR/보호 증거 참조로
회신 부탁드립니다. 새 양식·Secret/Token 원문은 필요 없고 가능한 부분부터
주시면 됩니다. 미확정 변경·유료 생성·WRITE·장애 시험의 일괄 실행 승인은 아닙니다.
```

## 확인 근거

- [GitOps32 공급·Pull 정정/B 후속](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32)
- [GitOps6 Runtime·Pruner 이력](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)
- [App15 실제 Controlled Run·검증기 요청](https://github.com/seokpan/seokpan-hybrid-app/issues/15#issuecomment-6082658844)
- [App42 새 Pipeline Scan 차단](https://github.com/seokpan/seokpan-hybrid-app/issues/42)
- [Docs43 원장·Data 최신 입력](https://github.com/seokpan/seokpan-hybrid-docs/issues/43)
- [OCP 실행 준비](OCP_CAPACITY_EXECUTION_PREPARATION_20261011.md)·[승인 조건 대조](B_ACCEPTANCE_PREPARATION_AUDIT_20261011.md)

현재 제공된 대화와 위 기록에서 B가 수신할 D 잔여를 통합했다. GitHub에 없는
직접 대화까지 완전히 조사했다는 뜻은 아니며 새 회신은 항목별로 반영한다.
