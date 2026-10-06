# Planning & Design

> **최초 기준 문서:** 제공된 Project Source 00~04, 최초 문서 묶음의 결정 기준일 2026-10-01 KST. 후속 개정은 아래 이력과 최신 설계 기준을 따르며 각 원문의 작성/현행화 기준일은 서로 다름  
> **저장소 등록 작업일:** 2026-10-02 KST  
> **최초 등록 방식:** 업로드 원문을 바이트 단위로 복사하고 승인 상태·당시 관측을 보존
> **2026-10-03 보완 이력:** DR 요구 재검토에 따른 02/03/04 정합 보완을 [PR #20](https://github.com/seokpan/seokpan-hybrid-docs/pull/20)으로 검토·병합 완료. 당시 새 목표·주기·구조 선택은 실제 근거 비교 전이었으며, 최초 업로드 식별값·승인 이력을 보존하고 프로젝트 소스 자동 등록을 주장하지 않음

> **2026-10-05 DR 설계 선택 완료:** [h-docs PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)의 main 병합으로 현재 설계 기준은 **RTO 10분·영속 DB RPO 30분·DB 운영 중 Portable Backup 15분 계획 주기**이며 기존 **Cloud Primary + On-Prem Backup/Restore 구조를 유지**한다. 근거·적용 범위는 [03 §3-I.14.5](03_DETAILED_DESIGN.md#recovery-design-decision-20261005)를 따른다. 위 2026-10-03 미확정 표기와 해당 개정 본문의 후보·병합 전 표기는 작성 당시 이력으로 보존하며 현재 설계 선택을 다시 대기시키는 조건으로 해석하지 않는다. 설계 선택·산출물 반영은 완료됐으며 실제 운영 주기 적용·전체 RTO/RPO 달성·최종 T18 Acceptance는 미검증이다.

현재 진행 현황:

- [x] 프로젝트 소스 00~04 원문 정리
- [x] 문서 단계와 실제 구현·검증 상태 구분
- [x] 원문 SHA-256·크기 기록 및 복사본 일치 확인
- [x] 다이어그램 제작 계획 작성 및 후속 진행 요청 확인
- [x] 설계 그림 12장 SVG/PNG 제작·자체 검증
- [ ] 사용자 그림 검토 의견 반영
- [ ] 실제 구현 증거로 구축 결과판 작성

## 문서별 역할

| 번호 | 문서 | 현재 읽는 방법 |
| --- | --- | --- |
| 00 | [00_PROJECT_STARTING_POINT.md](00_PROJECT_STARTING_POINT.md) | 1차 실제 기준·역사적 출발점·결정 계보. 과거 후보를 현재 목표로 해석하지 않음 |
| 01 | [01_PROJECT_CHARTER.md](01_PROJECT_CHARTER.md) | 목적·범위·기간·비용·성공 기준. Charter 작성 당시 유예한 구조 결정은 후속 승인으로 연결 |
| 02 | [02_TARGET_ARCHITECTURE.md](02_TARGET_ARCHITECTURE.md) | 승인된 Cloud Primary + On-Prem Restore-based Recovery의 상위 목표 |
| 03 | [03_DETAILED_DESIGN.md](03_DETAILED_DESIGN.md) | 승인·종료된 세부 설계. 주소 계획·책임·규약·시험 목표를 포함하며 실제 입력/Runtime는 별도 |
| 04 | [04_IMPLEMENTATION_READINESS.md](04_IMPLEMENTATION_READINESS.md) | 문서 전체 종료. 03 이후 확정된 운영 결정·사람별 배정·전용 복구 DB VM·인증/보관·실행 인계 |

00~04를 하나의 통합 최신 문서로 재작성하지 않습니다. 현재 설계 해석은 사용자의 최신 명시적 결정과 승인 Project Source를 따릅니다. 같은 항목에서 03보다 후속인 04가 구체화한 운영 결정은 04를 적용하고, 이전 단계의 당시 기록은 보존합니다.

예를 들어 02의 일반적인 Hybrid 연결 설명은 03에서 RDS 사설 접근용 WireGuard와 S3/ECR/GitHub HTTPS 경로로 구체화됩니다. 03의 당시 사람별 배정·Release 형식 확인 대기는 04에서 채택된 결정으로 이어집니다. 과거의 미확정 표기를 현재의 새 승인 대기로 되돌리지 않습니다.

이번 복구 목표 피드백은 [03 §3-I.14](03_DETAILED_DESIGN.md#recovery-design-review-20261003)를 중심으로 검토합니다. 02의 기존 1차 Redis 재사용 설명은 이미 승인된 새 Recovery Redis에 맞추고, 03은 장애 시작부터 실제 클라이언트 업무/Data 완료까지의 RTO 경계를 정합화합니다. 04는 최소 예행·운영 인계를 연결합니다. 00의 역사적 출발점과 01의 목적·Scope·예산·Freeze는 유지하며, 실제 상위 범위 변경이 채택될 때만 수정합니다.

## 05와의 관계

04 §1·§11.3과 프로젝트 지침은 다음 문서를 **`05_IMPLEMENTATION_AND_VALIDATION.md`**로 정의합니다. 05는 실제 입력·Source·코드·Plan/Cost Gate·통합·Migration·검증·Evidence를 기록하는 단계입니다.

설계 문서의 종료는 새 피드백에 따른 재검토 금지가 아닙니다. 이번 DR 후속 작업은 00–04 설계 대조·정합 보완과 05의 필요한 최소 예행을 병행했고, 실측·사용자 영향·팀 부담·일정/비용을 비교해 목표·주기·구조의 설계 선택과 산출물 반영을 h-docs PR #30으로 마쳤습니다. 05 전체 Cloud/ROSA 구현 완료를 설계 변경의 선행조건으로 두지 않았습니다. 이후 05에서는 실제 운영 입력·백업 최신성·전체 업무 재개 시간을 검증하고 설계 기준과 차이를 기록합니다.

05는 전체 설계 다이어그램의 시작을 막는 선행 문서가 아닙니다. 설계 목표를 보여주는 그림은 00~04로 제작하고, 실제 배치·환경값·성과·RTO/RPO는 05의 Source/Run/Evidence로 확인합니다. [실행 안내](../execution/README.md)와 [05 구현·검증 문서](../execution/05_IMPLEMENTATION_AND_VALIDATION.md)는 PR #5로 공유됐으며, 실제 시험 PASS는 해당 Run의 증거로 판단합니다. 최초 그림 제작 당시 첨부 범위는 00~04와 지침이었습니다.

## 원문 추적

[source-manifest.json](source-manifest.json)의 `files`는 현재 저장소 문서의 바이트 수·SHA-256이며, `original_upload_files`는 최초 제공 원문의 식별값입니다. 변경 전 기준 Commit과 보완 범위를 함께 기록합니다. Manifest의 `DR_DESIGN_REVIEW_PR_CANDIDATE`는 후보 작성 당시 검토 상태이며, 현재 병합 여부는 위 PR 이력과 구분합니다. 2026-10-03부터 현재 02/03/04를 업로드 원문과 바이트 동일하다고 표현하지 않습니다. 이 기록은 문서 개정 추적용이며 설계의 실환경 검증이나 Runtime PASS를 뜻하지 않습니다.

원문의 표기 기준일은 00~01이 2026-09-30, 02~04가 2026-10-01 KST입니다. 복사본의 원문 날짜와 현재 승인 상태는 별개로 해석합니다. 프로젝트 지침 `PROJECT_INSTRUCTIONS.md`는 제공된 Project Source에서 적용했으며 이번 00~04 등록 범위에는 복사하지 않았습니다. 해당 지침의 식별정보는 [검토 기록](../architecture/REVIEW_RECORD.md)에 남깁니다.

문서 안의 외부 Source/Issue/PR 및 당시 관측은 원문 시점의 기록입니다. 이후 변경은 새 결정·구현 기록과 연결하며 원문을 현재 관측으로 바꾸지 않습니다. 제공 사본을 확인 가능한 범위에서 비밀정보 패턴 검사했으며, 후속 공개 자료도 실제 Credential·State/Plan·평문 Backup·개인정보를 포함하지 않도록 확인합니다.

## 다음 작업

- [ ] [아키텍처 목차](../architecture/README.md)의 그림 12장 사용자 검토 의견 반영
- [ ] 실제 구현·검증 기록이 제공되면 구축 결과와 설계 차이 연결

설계 그림의 제작·자체 검증과 파일 형식/출처는 [제작 검토 기록](../architecture/PRODUCTION_REVIEW.md)에서 확인합니다. 최초 업로드와 당시 승인 이력은 보존하며 이번 정합 보완·목표 재검토 상태는 별도 기록입니다.

