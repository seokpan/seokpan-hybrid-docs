# 기록·보호 범위

- D의 공개 GitOps32 Run5 보고와 B의 공급 후보 수락 댓글, B의 GitHub Source Blob·AST 대조 요약만 기록.
- Build/Scan/Smoke·Harbor Pull/Image heads는 D 수행 보고 수신. B가 Jenkins·Harbor·Runtime을 직접 재조회하거나 원 metadata 파서를 실행한 결과가 아님.
- Source 대조는 Source18819963와 과거5df2ce28·46e21a74의 Migration6파일/alembic.ini 및 Source head 확인. 실제 DB 접속/Revision·held Migration 실행 없음.
- 공개 댓글의 실제 보호 경로·Credential·Token·전체 로그/metadata 원문·Saved Plan은 복사하지 않음. 후속 보존 입력은 논리 참조·해시·접근/Owner 조건으로 공급.
- 부분 Child Digest를 완전한 Digest로 만들어 기록하지 않음. Registry 공급 Gate 후 push→실제 mapping→Promotion/Pull, 추가 Worker Gate 후 FE→BE 교체. 미생성 mapping을 push 선행조건으로 만들지 않음.
- 기존 실패 Run·Source 시험 SHA·기존Image/Digest·base/Recovery hold·Migration suspend 보존.
