# 검사 실행·범위
새 고정환경: Node24.19.0/npm12.0.2/Python3.13.15/uv0.12.5/Playwright1.63.0, frontend/backend Lock 바이트 보존.
npm run verify
node scripts/browser-ci.mjs full --run-id full-e2e-ui-20261008-final
node scripts/browser-ci.mjs ui --run-id full-e2e-ui-20261008-final-ui
기존 Full2회/retry0/maxfailures1, loopback8001/5175·합성UI5174, 기존 서버 재사용 없음·종료포트검사PASS. 테스트skip/force/timeout완화 없음.
Backend/제품UI/Lock/Jenkins 변경 없음. Source와 관련 Migration Blob을5df2ce28과 대조, 최종 병합 SHA에서는 다시 대조.
개인 브라우저profile/실환경사용자/외부클러스터/secret/state 없음. raw Browser report/자격 원문을 공개 자료로 복사하지 않음.
