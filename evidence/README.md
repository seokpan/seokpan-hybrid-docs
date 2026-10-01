# Evidence Index and Run Guide

실제 실행 결과는 승인04 §5.4·§10.4에 따라 `evidence/<test-id>/<run-id>/`에 남깁니다. 각 실행 담당자가 자기 결과를 작성하고 최유준이 Index/형식을 연결합니다. 아래는 빈 양식이며 **이 Index에 연결된 실제 Run은 아직 없습니다.** 기존 lab 보고와05의 부분 검사 이력을 여기 새 Run으로 수행했다고 표시하지 않습니다.

## Create a Run

1. [_template/](./_template/summary.md)의 다섯 파일을 실제 test-id/run-id 폴더로 복사합니다. 새 실행·재시험은 별도 Run입니다.
2. release.json에 실제 Source·Image·환경·입력 개정·실행자·시각·조건을 연결합니다. 빈 값은 null로 유지하고 PASS는 해당 증거가 있어야 합니다.
3. summary.md에는 범위·결과·원인·제한·다음 행동, metrics.csv에는 실제 수치/단위/집계, timeline.csv에는 단계 시각을 남깁니다. 헤더만 있는 CSV는 미측정이며 0건/0초 결과가 아닙니다.
4. checksums.txt에는 공유 가능한 실제 파일의 SHA-256을 생성해 넣습니다. 보호 Raw·SQL/Backup·State/Plan·Credential은 Git에 올리지 않고 논리 참조/보관·접근 책임으로 연결합니다.
5. 아래 Index와 관련 작업 Issue·[공통 진행표](../execution/WORK_TRACKER.md)에 링크를 연결합니다. 실패 Run을 보존하고 수정/재시험과 연결합니다.

GitOps의 `releases/<release-id>.json`은 후보/선언이며 Docs의 Run과 구분합니다. 후보 안에 후보 자신을 포함한 GitOps SHA를 넣지 않습니다. 실제 Run은 Commit 후 실제 사용 GitOps SHA를 기록합니다. 이번 release.json은 승인 필드의 빈 Run 양식이며 새 Validator/파이프라인 구현이나 최종 검증을 의미하지 않습니다.

## Run Index

| Test/Case·Requirement | Run·환경 | 실행자·Reviewer | 실제 Source/Release | Render/Deployment/Acceptance | 증거 링크 | 실패/후속 Run·제한 |
| --- | --- | --- | --- | --- | --- | --- |

## Required Boundaries

- UTC ISO 시각과 KST가 같은 시각인지 확인하고 불확실한 시점은 제한으로 남깁니다.
- RTO는 장애 시작부터 대표 업무/Data 확인까지, RPO는 사고와 실제 사용 Backup의 Data 기준 시각 차이입니다. Dump 종료/파일 수정 시각으로 대체하지 않습니다.
- DB 영속 Data와 Redis Runtime 손실을 구분합니다. 복구 명령 성공만으로 업무 복구 PASS가 아닙니다.
- 모든 Run에 적용되지 않는 항목은 summary의 제외 범위에 이유를 남깁니다. N/A는 전체 성공축을 생략하는 수단으로 쓰지 않습니다.
- JSON은 조합/실행 정보, CSV는 수치/시간선, Markdown은 해석을 맡습니다. 실제 값은 원본에서 연결하고 중복 기록이 충돌하면 원본·대상·개정·시점을 확인합니다.
