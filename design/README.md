# Planning & Design

> **기준 문서:** 사용자가 제공한 Project Source 00~04, 문서 묶음의 최신 결정 기준일 2026-10-01 KST. 각 원문의 작성/현행화 기준일은 서로 다름  
> **저장소 등록 작업일:** 2026-10-02 KST  
> **보존 방식:** 업로드 원문을 바이트 단위로 복사. 내용·승인 상태·당시 관측·과거 미확정 표기는 수정하지 않음

현재 진행 현황:

- [x] 프로젝트 소스 00~04 원문 정리
- [x] 문서 단계와 실제 구현·검증 상태 구분
- [x] 원문 SHA-256·크기 기록 및 복사본 일치 확인
- [x] 다이어그램 제작 계획 작성
- [ ] 제작 계획 사용자 검토
- [ ] 실제 이미지·다이어그램 제작

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

## 05와의 관계

04 §1·§11.3과 프로젝트 지침은 다음 문서를 **`05_IMPLEMENTATION_AND_VALIDATION.md`**로 정의합니다. 05는 실제 입력·Source·코드·Plan/Cost Gate·통합·Migration·검증·Evidence를 기록하는 단계입니다.

05는 전체 설계 다이어그램의 시작을 막는 선행 문서가 아닙니다. 설계 목표를 보여주는 그림은 00~04로 제작하고, 실제 배치·환경값·성과·RTO/RPO는 05의 Source/Run/Evidence로 확인합니다. 이번에 받은 첨부는 00~04와 프로젝트 지침이며 05 본문은 제공되지 않았습니다. 따라서 05의 최신 진행 상태를 독립 확인했다고 기록하지 않습니다.

## 원문 추적

[source-manifest.json](source-manifest.json)에 각 등록 파일의 이름·바이트 수·SHA-256을 기록했습니다. 이 값은 제공된 원문과 저장소 사본의 동일성을 확인하는 용도이며 설계의 실환경 검증이나 Runtime PASS를 뜻하지 않습니다.

원문의 표기 기준일은 00~01이 2026-09-30, 02~04가 2026-10-01 KST입니다. 복사본의 원문 날짜와 현재 승인 상태는 별개로 해석합니다. 프로젝트 지침 `PROJECT_INSTRUCTIONS.md`는 제공된 Project Source에서 적용했으며 이번 00~04 등록 범위에는 복사하지 않았습니다. 해당 지침의 식별정보는 [검토 기록](../architecture/REVIEW_RECORD.md)에 남깁니다.

문서 안의 외부 Source/Issue/PR 및 당시 관측은 원문 시점의 기록입니다. 이후 변경은 새 결정·구현 기록과 연결하며 원문을 현재 관측으로 바꾸지 않습니다. 제공 사본을 확인 가능한 범위에서 비밀정보 패턴 검사했으며, 후속 공개 자료도 실제 Credential·State/Plan·평문 Backup·개인정보를 포함하지 않도록 확인합니다.

## 다음 작업

- [ ] [다이어그램 제작 계획](../architecture/DIAGRAM_PLAN.md)의 장수·역할·표현 방향 검토
- [ ] 검토 결과를 반영한 설계 다이어그램 제작
- [ ] 실제 구현·검증 기록이 제공되면 구축 결과와 설계 차이 연결
