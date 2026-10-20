# tjung03 체크박스 단위 최종 대조 — 2026-10-21

## 범위와 현재 완료

이 문서는 상위 이슈·닫힌 이슈·병합 PR 본문·관련 대화 댓글의 체크박스까지 대조한 후속이다. 이전 전수조사의 문서/링크 대조와 별도로 기존 미체크를 실제로 갱신했다.

- 네 저장소의 현재 이슈/PR 본문371개와 기존 대화 댓글717개 및 변경분9개를 대조했다. 변경분은 새 댓글과 수정 댓글을 합친 수이며 전체 개수에 단순 가산하지 않는다.
- 본문·대화 댓글에서 체크930개를 추출했다. tjung03 관련 범위728개와 범위 밖202개를 구분한 [전체 관련 체크 원장](evidence/tjung03-record-audit-20261021/checkbox-ledger.csv)을 보존했다.
- 기존 미체크14개를 실제 완료로 변경했다. 본문18개·날짜가 있는 댓글4개에 현재 판정을 반영하고 API로 전체 본문 일치를 다시 확인했다. [게시 후 대조 영수증](evidence/tjung03-record-audit-20261021/checkbox-readback.json).
- 상위 TH는 기존37/81에서 **41/81 완료·40개 원 기준 미수락**으로 변경했다. B 자원 종료는 완료이며 원 복합 기준의 미수락을 B 재가동 조건으로 사용하지 않는다.
- 이슈/PR의 open/closed 상태와 승인·병합 상태는 변경하지 않았다. 다른 담당자 체크를 B의 실행으로 일괄 완료하지 않았다.
- AWS·ROSA·SQL·Sync·부하·설치·완료 검사는 반복하지 않았다. 이번 추가 검증은 변경한 GitHub 본문/댓글·집계·문서 참조에 한정한다.

## 실제 변경한 기존 체크14개

| 원본 | 완료로 반영한 조건 | 기존 근거와 범위 |
|---|---|---|
| [infra #30](https://github.com/seokpan/seokpan-hybrid-infra/pull/30) | 새 HEAD에 대한 사람 재승인. | [동일 HEAD 승인5412668844](https://github.com/seokpan/seokpan-hybrid-infra/pull/30#pullrequestreview-5412668844) 후 db3a7732 병합. 실행 IAM 변경을 뜻하지 않는다. |
| [docs #100](https://github.com/seokpan/seokpan-hybrid-docs/pull/100) | 최종 변경 확인 후 병합 | 최종 HEAD 0c8ccd0b의 [PR100](https://github.com/seokpan/seokpan-hybrid-docs/pull/100) 병합 완료. 오프라인 예산 도구의 병합이며 실제 부하 수락과 구분한다. |
| [docs #101](https://github.com/seokpan/seokpan-hybrid-docs/pull/101) | D 부하/관측 도구의 실제 개정·Client 업무 측정 출력 확인 | [정상 Client 업무24/24](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md)와 [attempt04 도구·원본/해시·47,138요청 분석](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)을 대조했다. HPA 전체 PASS·게임/WSS 최대 수용량을 뜻하지 않는다. |
| [app #43](https://github.com/seokpan/seokpan-hybrid-app/pull/43) | Source 리뷰 의견 반영·승인 후 병합 | [동일 HEAD 승인5481821612](https://github.com/seokpan/seokpan-hybrid-app/pull/43#pullrequestreview-5481821612)와 8526fb8b 병합 완료. 비차단 제안의 처리 설명은 기존 본문을 유지한다. |
| [app #43](https://github.com/seokpan/seokpan-hybrid-app/pull/43) | 실제 RDS·Process/Pod·예약·롤링 예산 확인 및 Pool/timeout 합의 | 선정 Cloud/발표 시험은 size2·overflow0·timeout5초, Pod당 process1/engine2, 피크8Pod×4+예약15=47/전역68로 결합해 [실행](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md)했다. 운영 전 범위의 최종 Pool 수락이나 롤링 시험 성공과 구분한다. |
| [infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) | 앱 DB 접속 TLS 지원 확인 (MariaDB 11.8은 `require_secure_transport` 기본값 1) | App 연결 계약과 [새 Data Pod·목적 계정의 실제 TLS 로그인 및 Cloud 앱 기동](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md)으로 확인했다. 기존 데이터 이관·전체 Recovery 성공은 포함하지 않는다. |
| [infra #46](https://github.com/seokpan/seokpan-hybrid-infra/issues/46) | `backend-database-ca` ConfigMap 생성 (정태훈, 복구 Namespace 확정 후) | [Recovery 보호 입력 Secret3/ConfigMap2 최초 create5·UID/내용 대조](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/TJUNG03_COMPLETED_RESULTS_20261016.md)에 포함해 완료했다. 실제 DB 복원·Recovery FE/BE 업무와 구분한다. |
| [infra #94](https://github.com/seokpan/seokpan-hybrid-infra/pull/94) | 최신 보완 커밋에 대한 팀 재리뷰와 지적 사항 해소 확인. | [최종 HEAD 4a1e5058 승인5583014433](https://github.com/seokpan/seokpan-hybrid-infra/pull/94#pullrequestreview-5583014433)에서 기존 변경 요청2건 해소를 확인했고 9ced0cfd로 병합됐다. B의 코드 재리뷰 완료이며 A의 AWS 실행을 뜻하지 않는다. |
| [infra #94](https://github.com/seokpan/seokpan-hybrid-infra/pull/94) | Git 통합 후 상대 경로·의존성·확인값 참조의 최종 리뷰. | [통합된 최종 보완 HEAD 재리뷰](https://github.com/seokpan/seokpan-hybrid-infra/pull/94#pullrequestreview-5583014433)에서 기존 SSM 경로 일치·수명 관리·보호 경계를 수락한 후 병합됐다. 운영 VPN 실행·인과 검증의 수락과 구분한다. |
| [app #47](https://github.com/seokpan/seokpan-hybrid-app/issues/47) | F4 수정 PR이 병합되었고 이후 Promotion PR의 GitOps CI가 통과했다(정태훈 확인) | [F4 및 Run13 기록](https://github.com/seokpan/seokpan-hybrid-app/issues/47#issuecomment-6158883408)과 [GitOps45 완료 확인](https://github.com/seokpan/seokpan-hybrid-gitops/issues/45#issuecomment-6160603523)에서 Promotion48/49 validate 통과·B 승인·병합을 확인했다. 후보 INCOMPLETE는 유지한다. |
| [docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) | TH-09.1 Cloud ECR·승인 Replica/PDB/Rolling/AZ와 환경별 연결/정책 선언 완성 | [Cloud PR11 Source 승인·병합](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11#pullrequestreview-5415539176) 및 [후속 ECR·Replica/PDB/Rolling/AZ·연결/정책 선언 결합](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md) 완료. 이 항목은 선언 완성이며 실제 롤링 성공·전체 업무 수락을 추가 조건으로 붙이지 않는다. |
| [docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) | TH-17.1 정상 Baseline 뒤 D 조율로 충돌 없는 시험 순서·주입자·중단/되돌림 조건 확인 | [정상 Baseline 이후 D와 시험 순서·단일 주입/중단·복귀 조건을 결합한 실행](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md)과 [HPA 종료 기록](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)을 확인했다. 시간이 부족해 롤링을 생략하고 HPA만 진행한 선정 범위를 유지한다. 실제 원복 성공은 별도이며 최종 폐기 경로에서는 설정 복원을 생략했다. |
| [docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) | TH-17.3 App Resource/Pool·업무 정확성·성능·시간선·실패/재시험·환경 차이 기록 | [정상 업무24/24·실패한 롤링 준비·선정 환경](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md), [HPA47,138요청·단계별 지연/무응답·B425표본/D구간70표본·Guest300정리와 한계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)를 기록했다. 기록 완료이며 HPA 전체 PASS나 장애 원인·최대 수용량 확정이 아니다. |
| [docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) | TH-19.6 해당 State/Owner로 실제 잔존·종속 자원·부분 실패/Orphan 확인. 기반 자원까지 임의 삭제하지 않음 | [B 저장 Plan Apply·State0·원격 ROSA 부재·정확한 owned EC2/EBS/ENI/LB 각0·조회 오류0·Snapshot4개 ABSENT](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_ROSA_FINAL_CLOSEOUT_20261021.md) 완료. 확인 범위는 해당 State/Owner와 정확한 소유 근거이며 A·공유·태그 없는 모든 자원의 부재나 계정 전체 청구0을 주장하지 않는다. |

## 상위 이슈와 닫힌 기록

| 구분 | 처리 |
|---|---|
| 상위 이슈6개 | Docs6/8/21·Infra25·GitOps10·App4에 B 앱/현재 모니터링/선정 시험 기록, HPA 부분 결과/증거, B 삭제/부재, 기존 GitHub 마감을 각각 완료 체크로 표시했다. 원 TH와 팀 전체 수락을 구분한다 |
| 병합 PR의 현재 미체크 | Infra30/94·Docs100/101·App43의 위 완료 조건을 실제 체크했다. 각 PR의 Source/승인/병합과 Runtime 범위는 구분한다 |
| GitOps9/11의 접힌 이전 Stack 체크 | 당시 체크를 변조하지 않고 최상단에 최종 HEAD 승인·병합과 #9 이후 main 전환/CI/리뷰 완료 체크를 추가했다. 남은 복합 Recovery 조건은 자동 완료하지 않았다 |
| 닫힌 Infra26 | #25 통합에 따른 중복 종료를 명시했다. 과거 제안을 별도 진행 중 구현이나 완료 수로 세지 않는다 |
| 닫힌 App1 | 현재 원 완료 기준4개는 모두 완료임을 확인했다. 접힌 이전 Client/Build/Cloud 복합 체크와 후속 App4를 구분했다 |
| 날짜가 있는 B 댓글4개 | Infra25 댓글6063651793, Docs21 댓글6064365404/6081975557, App15 댓글6082658844의 원문과 체크를 보존하고 현재41/81 및 종료 판정을 앞에 연결했다 |

## TH4개를 새로 완료한 이유

| 항목 | 원 요구 동작 | 완료 해석 |
|---|---|---|
| TH-09.1 | Cloud ECR·Replica/PDB/Rolling/AZ·연결/정책 선언 완성 | 선언과 실제 선택 Source 결합 완료다. 실제 롤링 성공을 이 선언 항목의 추가 조건으로 붙이지 않는다 |
| TH-17.1 | 정상 Baseline 뒤 시험 순서·주입자·중단/되돌림 조건 확인 | 정상 이후 D와 실행 조건·중단/복귀 경로를 결합했다. 시간 제약에 따른 HPA 선정과 실제 설정 복원 생략을 기록하며 복원 성공을 주장하지 않는다 |
| TH-17.3 | Resource/Pool·업무/성능·시간선·실패·환경 차이 기록 | 정상·실패한 롤링 준비·HPA 중단/미수행·표본 누락/환경을 기록했다. 기록 완료를 전체 시험 성공과 혼동하지 않는다 |
| TH-19.6 | 해당 State/Owner의 잔존·종속/부분 실패 확인, 다른 기반 제외 | B State0·원격 부재·정확한 owned 인벤토리 각0·Snapshot4개 ABSENT를 수락한다. 태그 없는/공유/다른 Owner 전체 부재와 청구0은 범위 밖이다 |

## 미체크를 유지한 이유

- 롤링은 준비 중 실패해 trigger가 호출되지 않았다. 실제 DB 대기·롤링·종료/재접속의 전체 복합 조건은 완료로 바꾸지 않는다.
- App43의 새 Build/Scan/Smoke·Digest·최종 GitOps 입력을 모두 묶은 원 조건은 전체 수락 증거가 해당 조건으로 연결되지 않아 보존했다. 승인 이미지·실제 Cloud 기동·Pool 예산이 완료된 사실은 별도로 표시했다.
- HPA는 10/50/100 VU 구간을 수행하고 200 VU에서 오류 예산으로 중단했다. 전체 성공·최대 수용량·원인 확정은 하지 않는다.
- 전체 이관·Recovery/RTO/RPO·공식 장애 전체·최종 영상/발표 등 원 복합 기준은 실제 미수행/미수락이다. B 자원 종료를 보류하거나 유료 환경을 다시 만들 요청이 아니다.
- 날짜가 고정된 과거 체크와 다른 담당자의 미체크는 당시 사실과 Owner를 유지한다. B가 실제 완료한 Infra17 TLS/46 CA 공급, App47 F4 확인, Infra94 코드 재리뷰 행만 근거로 갱신했다.
- VM 전체 폐기 예정에 따라 VM 내부 키/파일의 개별 폐기는 B 종료 조건에서 제외한다. A 자원·외부 계정 자격·계정 전체 최종 청구는 별도 범위다.

## 변경 후 검토

1. 기존 원 체크의 문장과 근거를 대조해14개 완료를 반영하고, 과거 접힌 본문의 바이트를 보존했다.
2. 게시 본문18개·댓글4개를 다시 읽어 변경 후 전체 내용과 일치함을 확인했다. 닫힌 이슈/PR을 재개하지 않았다.
3. TH81 원장·루트/05/Tracker/학습 안내·전수 보고서의 현재 집계를41/81로 맞췄다. 과거 날짜별37/81은 당시 집계로 남긴다.
4. 수정 범위의 언어·원장 집계·추가 상대 링크16개·현재 집계 정합을 확인했다. 2차 대조에서 본문3곳의 오래된 현재37/44 표기를41/40으로 추가 정정했고 마지막 대조의 신규 보완은0건이다. 이 체크박스 후속의 내용 검토는 완료했다. 후속 PR의 main 반영은 별도 병합 상태를 따른다.

[체크박스 문서 검토 영수증](evidence/tjung03-record-audit-20261021/checkbox-document-validation.json): 기존 체크14개·관련 원장728행·TH81개 중41개 완료·40개 미수락, 완료 실행 반복0·자원 조회0.
