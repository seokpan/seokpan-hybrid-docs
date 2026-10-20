# B GitHub 최종 기록 대조 — 2026-10-21

## 결론

B AWS 자원 종료는 완료다. VM 자체 폐기 예정이므로 개별 키·보호 파일 폐기를 B 종료의 추가 조건으로 두지 않는다. 이번 대조는 GitHub main·이슈·리뷰와 이미 보존된 파일만 읽었다. Controller·AWS·SQL·부하·설치·Sync·삭제를 재실행하지 않았다. A 자원과 A 종료 판정은 제외한다.

## 대조한 기준

저장소별 main은 개별 시점에 읽었으며 동시점 원자적 상태가 아니다.

| 저장소 | 대조 main |
|---|---|
| docs | `ab9ed7ddf7c2df97893c70cf5dec959b97cfb15c` |
| infra | `cac4c4ecc89ff7b4a92179231d63fcc132d67895` |
| gitops | `dfe43e4711d3049d2dc0560bb61babde9e6807af` |
| app | `d037a55f234a8720e6db9b01b8f31d08a3a16af9` |

- h-docs #138 병합과 main 반영을 확인했다.
- 네 저장소의 루트 README, 아래 실행 문서9개와 관련 이슈6개 본문을 대조했다. 다른 담당 전체 문서나 전체 TH 재수락을 수행한 것은 아니다.
- 이슈: Docs [#6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)·[#8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)·[#21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), Infra [#25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25), GitOps [#10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10), App [#4](https://github.com/seokpan/seokpan-hybrid-app/issues/4). 본문의 후속 완료와 오래된 댓글의 당시 상태를 구분했다.

## 실행 문서와 증거

- [B 최종 종료](B_ROSA_FINAL_CLOSEOUT_20261021.md)
- [B 실제 삭제](B_ROSA_DELETE_EXECUTED_20261021.md)
- [B/D 증거 결합·삭제 Plan](B_D_HPA_FINAL_EVIDENCE_AND_B_DELETE_PLAN_20261021.md)
- [HPA 요청 분석](HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)
- [앱·현재 모니터링·정상 Baseline](B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md)
- [개인 실행판](TJUNG03_EXECUTION_BOARD.md)
- [공동 진행표](WORK_TRACKER.md)
- [완결 작업 결과](TJUNG03_COMPLETED_RESULTS_20261016.md)
- [05 구현·검증 기록](05_IMPLEMENTATION_AND_VALIDATION.md)

위9개 문서의 상대 파일 링크318개는 대상 파일이 모두 존재했다. URL 접근이나 모든 앵커를 검증했다는 뜻은 아니다. [공개 증거 ZIP](evidence/hpa-attempt04-20261020/B-D-public-evidence.zip)의 크기는1,143,117바이트, SHA256은 `46dc17c8b92a711fca8f57ad9486a070e18558067b6411e16314a36d3796d055`이며 내부 manifest7개 해시도 모두 일치했다. 받은 결과의 오프라인 대조이며 시험 반복이 아니다.

기록의 주요 값은 다음과 일치한다.

| 항목 | 유지한 실제 결과·해석 |
|---|---|
| 종료 | B State0·원격 ROSA 부재·정확한 owned 범위 EC2/EBS/ENI/LB0·Snapshot4개 ABSENT |
| 정상 업무 | 기존 Baseline24/24. 실제 롤링 시험 성공으로 확대하지 않음 |
| HPA 요청 | 총47,138건. 100 VU 구간30,084건 성공, p95 90.031ms |
| 중단 | 200 VU2.197초·응답 미확인16/200·RECENT_ERROR_BUDGET_EXCEEDED. 전체 시나리오 통과나 최대 수용량으로 사용하지 않음 |
| B 전체 관측 | 425표본·최대 DB 연결24·최대 Replica6 |
| 실제 D 부하 구간 | B70표본·최대 DB 연결23. 200 VU 구간의 B표본은0 |
| 원복·영상 | Replica3 복귀는 원래 설정 복원 성공과 다름. 시연 영상 촬영 완료는 확인되지 않음 |

## 발견한 문서 표기 보완

1. 루트 README의 10/16 안내·36/81을 최신 종료 문서와 원 이슈의37/81로 맞췄다. 새로운 TH 완료를 추가하지 않았다.
2. 완결 작업 결과의 “ROSA/NAT 유지·삭제 미실행”은 10/16 당시 기록임을 해당 절에 표시했다. 과거 원문·수치·조사 SHA를 보존했다.

## PR #109

[승인 리뷰](https://github.com/seokpan/seokpan-hybrid-infra/pull/109#pullrequestreview-5588343645)는 head `039b75bef5c0d7cd776125151ba5d17c84904dfd`에 대응한다. 최신 head의 CI2개 성공과 clean 병합 상태를 확인했다. 설치기 소스 이름·쓰기 전 전체 입력 검사·회귀 검사·체크섬·게시 증거 확인 절차의 필수 보완은 수락됐다.

수집기 중복 정리·삭제 Gate 단위검사 추가·Snapshot 중간 실패 영수증 개선은 재사용 전 개선 의견이며 이번 병합을 막지 않는다. 승인 head를 추가 변경하거나 종료된 운영을 재실행할 필요가 없다. 병합 여부는 원 PR의 실제 상태를 따른다.

## 미확인 범위

계정 전체 최종 청구와 태그 없는/공유/A 자원의 전체 부재는 B 조회 범위로 증명하지 않았다. 기존 전체 TH·Recovery/RTO/RPO·발표 산출물의 미수락 항목을 이번 B 종료로 완료 처리하지 않는다. 이들은 이미 충족한 B AWS 종료를 보류하는 조건이 아니다.


## 병합 후속 — 2026-10-21

Infra #109와 Docs #139의 main 반영을 확인했다. 병합 commit은 각각 d8c7980492f18b82c2448eed7ab5e6d99aca37e9, fd2d5ebf595c70ee1ebed2b8388a1bd6732d0fa6이다. 앞 절의 병합 추적은 완료됐다. 별도 [네 저장소 전수 대조](TJUNG03_FULL_REPOSITORY_AUDIT_20261021.md)로 범위를 확대했으며 기존 B AWS 종료를 보류하지 않는다.
