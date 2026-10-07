from pathlib import Path
import hashlib,json,re,subprocess,os

root=Path.cwd()
expected={
'TJUNG03_EXECUTION_BOARD.md':('f036ad65371133013f0af3a32c51318d53b125f5b031c3474011f093663cf41e','987ae1e7b924ed1744b0aae5930e4bc8c75d369d1f09952af25246228d025b69'),
'TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md':('2b20c3950004064c40ac9bbf94bf7ddd12d02e2d1afa3962cfdc06f0d89eab8e','1fe42729cd1c62fe55ed062ac7860c754196ae039cc6f400aeef53acbae2d4ba'),
'WORK_TRACKER.md':('eb44ade73052fccae7a8f619028f2279bd5b2322ccefc915c80c7fafe1f24031','5700722938dc550d1c364ed99f4656d8e87ec49a972353ff51afc2594e9afb6c'),
'05_IMPLEMENTATION_AND_VALIDATION.md':('3fcaf214494388c91680d3e188df68aa0b3a4d38fb2889456b0f4efc29f4d72a','73365d3a506f46baa7d3a13ca1c99a049cb4df9955d566dc8f9cb3e0282cb0f9'),
'REPOSITORY_CONSISTENCY_AUDIT.md':('8151bdf592997719821f7788b08c73706ee3d1bab1535573240b8d636bf24f20','c8afe1e9b65d5aa56a268094cd5bac6f4fe47defc42f241c40e1f9ad9b1b5451')}
original={}
for name,(before,after) in expected.items():
    raw=(root/'execution'/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==before,name
    original[name]=raw
assert hashlib.sha256((root/'execution/SOURCE_REVIEW_20261007.md').read_bytes()).hexdigest()=='643cd10c0902275769dd5b397b63fa7f3907e0922bf782eeae3a78bbc2e00028'
old_lab='| lab Valkey/App | 서버 선언은 아직 main에 없음. D 초안 제안의 실제 수락/PR → C Data·B StatefulSet 허용/UID/Probe/자원 검토. Service/Ready와 DB/Schema·CA/목적 Secret·Route·권한·사용창·live Diff 수락 → 필요한 단일 Migration → Backend → Frontend → 새 Run |'
new_lab='| lab Valkey/App | [GitOps #19](https://github.com/seokpan/seokpan-hybrid-gitops/pull/19) main `de130af839626c9d0a030580693a4060c41c9abd` 병합으로 선언·StatefulSet Kind 허용 Source 대기 해소. C Data/실제 공급 개정·AppProject 등록/권한·Service/Ready·DB/Schema·CA/목적 Secret·Route·사용창·live Diff 수락 → 필요한 단일 Migration → Backend → Frontend → 새 Run |'
new_input='\n**추가 병합·등록 확인:** Docs #68(`fff5ac222243a231e5473f4ab39f87aa6cc10f6f`)·Infra #38(`0f47617816b74365f5911ba2e273013ae82d6612`)·App #16(`bdaa9dfa0a09e5d8efb1714ccf62860315b1346e`)·GitOps #18(`12d78ac547729f0e314abfb2ac6238c95b1f3bd7`) 병합·작업 브랜치 삭제, Project v3 등록 확인을 수신했다. 그 뒤 #19 lab Source도 병합됐으며 실제 활성화는 별도다. [원 체크포인트](https://github.com/seokpan/seokpan-hybrid-docs/issues/21#issuecomment-6028672058)와 [S1–S4 검토](SOURCE_REVIEW_20261007.md)를 따른다.\n'
new_source='| App 수정·Image | S1에서 startup 취소 시 runner 누수와 Lua 거부 시 board 변경을 재현·수정해 [App #17](https://github.com/seokpan/seokpan-hybrid-app/pull/17)·[#18](https://github.com/seokpan/seokpan-hybrid-app/pull/18) 리뷰 제출. 실제 병합 → D Backend Build/Scan/Digest → B의 App/held Migration 동일 조합 연결. 기존 승인 Image에 수정이 포함됐다고 승계하지 않음 |\n'
outputs={}
for name in ['TJUNG03_EXECUTION_BOARD.md','TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md','WORK_TRACKER.md','05_IMPLEMENTATION_AND_VALIDATION.md']:
    t=original[name].decode();assert t.count(old_lab)==1
    t=t.replace(old_lab,new_lab)
    marker='| 병행 작업 | 완료된 범위와 직접 조건 |';assert t.count(marker)==1
    t=t.replace(marker,new_input+'\n'+marker)
    marker='| DR·기록 |';i=t.index(marker);t=t[:i]+new_source+t[i:]
    if name=='05_IMPLEMENTATION_AND_VALIDATION.md':
        t+='''

<a id="b-source-startup-lua-review-20261007"></a>
### 9.42 S1 Source 결함 재현과 lab 선언 병합의 인계 — 2026-10-07 KST

[App #4 원 기록](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6029248805)에 생성/종료와 Lua 거부 경로의 결함 2건, [App #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6029292025)에 새 Backend Build 인계를 제출했다. [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6029297406)에는 #18/#19 병합·제한 AppProject·실제 활성화의 직접 조건을 연결했다. 상세 Source·파일/함수·재현·검증·한계는 [S1–S4 검토](SOURCE_REVIEW_20261007.md)에서 추적한다.

| 변경 | 실제 Source 검사 | 다음 입력 |
|---|---|---|
| App #17 startup finally 범위 | 기존 취소1FAIL/정상1PASS → 수정2PASS, 전체1754·별도47 PASS. Run37557811841 | C/D 리뷰·병합·새 Backend Image. 실제 OCP/ROSA 종료 검증은 별도 |
| App #18 Lua 기한 선검사 | 기존 실제Lua3PASS/새2FAIL → 수정5PASS, 기본1752·별도47 PASS. Run37559151544 | Script9→10·Schema 유지, 실제 Valkey 조합에서 재시험. 기존 회귀용 Redis7.2.4 결과를 Valkey PASS로 사용하지 않음 |
| GitOps #19 lab Source | 기존 B 승인·40검사 보고 수신, main de130af의 3-way tree 보존 대조 | 선언 작성 대기는 해소, 실제 Data/CA/Secret·Owner/사용창·AppProject/live Diff와 활성화는 대기 |

서로 중복되는 runner47을 기본suite에 더해 고유 시험 수로 쓰지 않는다. Run의 trigger·검사한 작업 트리·게시 SHA와 Image/실제 배포 개정을 구분한다. C의 §8 기록·과거 Evidence·TH81/완료2·00–04·Project v3와 DR10/30/15·Pool 후보·Cost PARTIAL은 보존한다. 전체 Source/과거 이력의 미검토가 남아 있어 Q10은 완료하지 않는다.
'''
    if name=='WORK_TRACKER.md':
        t+='''

## B Source 검토 인계 — 2026-10-07

원 결과: [App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6029248805) → [App2 Build](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6029292025), [GitOps10 현재 입력](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6029297406). App #17/#18의 red/green·전체 CI와 GitOps #19 Source 병합을 수신한 범위에서 [05 §9.42](05_IMPLEMENTATION_AND_VALIDATION.md#b-source-startup-lua-review-20261007)·[검토 기록](SOURCE_REVIEW_20261007.md)에 연결한다. 팀원 수신·PR 병합·새 Image/Runtime은 각각 별도다. 금고 본인 확인·ROSA 준비·Data/공유 사용창은 직접 의존에 따라 병행하며 새 Shared Execution/Runtime PASS를 만들지 않는다.
'''
    if name=='TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md':
        t+='''

## 이번 Source 검토에서 확인할 두 경계

`asyncio.create_task` 이후 첫 await도 취소될 수 있다. 만든 Task의 정리 책임을 그 await 뒤에서 잡으면 provider가 먼저 닫힐 수 있으므로 실제 생성/종료 순서를 검사한다. [App #17](https://github.com/seokpan/seokpan-hybrid-app/pull/17)은 정상/취소 두 경우를 같은 lifespan으로 확인했다.

Lua 실행 중 다른 명령이 끼어들지 않는 것과 거부한 연산이 이미 수행한 쓰기를 되돌리는 것은 다르다. [App #18](https://github.com/seokpan/seokpan-hybrid-app/pull/18)은 잘못된 다음 기한을 board HSET보다 앞에서 검사하고, 거부 후 상태 불변·정상 재시도를 확인했다. 회귀용 Redis7.2.4에서의 결과와 실제 Valkey/클러스터 업무 수락을 구분한다.

기존 전체 검사 통과→새 경계 검사에서 실패→최소 수정→같은 검사와 기존 검사 재실행의 근거는 [S1–S4 검토 기록](SOURCE_REVIEW_20261007.md)에 연결한다. 이 두 결함의 수정 완료와 모든 Source/과거 이력의 전수 검토 종료는 별개다.
'''
    outputs[name]=t
name='REPOSITORY_CONSISTENCY_AUDIT.md';t=original[name].decode()
t=t.replace('> 상태: IN PROGRESS — 두 중단분의 게시·산출물 복원, PR 설명/리뷰 요청 정정, fixture 요약 후속 보완 및 등록용 소스 제공. 전체 코드/이력 의미 검토와 Q10 수렴은 미완료','> 상태: IN PROGRESS — S1 startup/Lua 결함 2건 재현·수정·회귀·PR 제출, S2 lab #19 병합/직접 의존 대조, S3 PR refs 이력 색인 보완. 전체 의미 검토와 Q10 수렴은 미완료')
t=t.replace('이번 종료 단위는 **중단 작업의 실제 게시 확인과 남은 제출/검증/전달 마무리**다. 범위 안의 새 불일치는 수정했으나, 전체 코드·과거 이력의 의미 검토가 끝났다는 판정은 아니다. 다음 작업은 §8의 미완료 단위에서 이어간다.','이전 중단분의 게시/전달 마무리 이후 S1–S4 검토를 진행했다. 이번에는 실제 재현된 Source 결함 두 건을 수정·재검증하고 새 lab 선언·Image 인계 영향을 연결했다. [이번 검토 전문](SOURCE_REVIEW_20261007.md)과 §9를 우선하며 전체 코드·과거 이력 의미 검토의 미완료를 유지한다.')
t=t.replace('Q07은 7개 비교와 개정본 제공이며 실제 Project 첨부 교체는 아니다.','Q07은 7개 비교·개정본 제공 후 [등록 확인](https://github.com/seokpan/seokpan-hybrid-docs/issues/21#issuecomment-6028672058)까지 연결됐다. 설계 내용 변경이 없으므로 상태 변화만으로 재등록하지 않는다.')
t=t.replace('## 3. 병합·수정 PR과 Source','## 3. 병합·수정 PR과 Source\n\n**현재 정정:** 아래 #68/#38/#16/#18 제출 표는 이전 체크포인트 이력이다. 네 PR은 모두 병합·작업 브랜치 삭제됐다. Docs main fff5ac2·Infra main0f47617·App mainbdaa9df·GitOps #18 main12d78ac이며, 이후 GitOps #19도 main de130af에 병합됐다. Project v3 등록은 실제 확인했다. 현재 리뷰 대상은 이번 Source 결함의 App #17/#18과 별도 Docs 검토 PR이다. 전체 SHA·근거는 [이번 검토](SOURCE_REVIEW_20261007.md#1-사용-source와-수집-범위)에 연결한다.')
t=t.replace('각 PR의 사람 승인·병합은 아직 완료로 기록하지 않는다. 리뷰 요청은 실제 리뷰 수락이 아니다. 다음 작업은 별도 채팅 통보를 기다리지 않고 HEAD·리뷰·검사·병합·브랜치를 재조회한다. Runtime 원 이슈는 문서 PR 병합만으로 닫지 않는다.','위 제출 당시의 리뷰/병합 대기는 현재 해소됐다. 새 Source PR의 리뷰·병합과 기존 네 PR의 완료를 구분하며 다음 작업 전에 실제 상태를 재조회한다. Runtime 원 이슈는 문서 PR 병합만으로 닫지 않는다.')
t=t.replace('D 선언 수락/PR → C Data·B Source/AppProject/UID/Probe·자원 검토 → 실제 Service/Ready','GitOps #19 선언·AppProject Kind Source 병합 → C Data/실제 공급 개정·B 적용 범위/권한·사용창 확인 → 실제 Service/Ready')
t=t.replace('S1 | App `test_hybrid_connections.py` 나머지, DB 시간/Pool·서비스 생성/종료, 공유 상태/Lua·최종화 분기','S1 | 이번 연결·시간/Pool·최종화·startup/vote Lua 검토 이후 Room/Session/연결 세대·WS의 남은 Source/시험 분기')
t+='''

## 9. S1–S4 검토 및 F11/F12 후속 — 2026-10-07

[Source 검토 기록](SOURCE_REVIEW_20261007.md)에 실제 사용 SHA·수집/검토 수준·두 결함·red/green·기존 CI·게시/리뷰·인계와 한계를 보존했다. 새 원 결과는 [App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6029248805), [Build 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6029292025), [GitOps10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6029297406)이다.

- F11: App #17 — startup 취소 경로에서 runner 정리 책임이 첫 await보다 늦게 시작하는 문제. 기존1FAIL/1PASS → 수정2PASS, 기본1754·별도47 PASS.
- F12: App #18 — Lua의 기한 거부 전에 board를 쓰는 문제. 기존 실제Lua3PASS/새2FAIL → 수정5PASS, 기본1752·별도47 PASS. Script9→10/Schema 유지. 회귀용 Redis 결과와 선택 Valkey 실환경을 구분.
- S2: GitOps #19의 lab 선언·제한 StatefulSet Kind·롤백 보완은 병합돼 D 초안 대기가 해소됐다. 실제 활성화/CA/Secret·DB/Schema·사용창은 별도. Recovery 선언/renderer/테스트는 승인 실제 입력과 함께 개정한다.
- S3: 저장된 PR HEAD refs까지 복원해 App98/Infra110/GitOps48/Docs175의431개 도달 이력을 부모·경로·diff 해시로 색인했다. 모든 과거 diff/CI 의미 검토 완료를 뜻하지 않는다.
- S4: source→새 검사→수정→회귀/기존 검사→게시 바이트→원 Issue/리뷰/Build→실행 문서 영향을 확인했다. 나머지 Source/이력 검토가 남아 Q02/03/04/05/10은 유지하며 두 결함 수정만으로 전체 수렴을 선언하지 않는다.

00–04·그림/manifest·C의 기존05 §8·Evidence·TH81/완료2는 변경하지 않는다. 실제 Runtime Run·비용·승인 Image 개정은 이번 기록으로 추가하지 않는다.
'''
outputs[name]=t
for name,text in outputs.items():
    assert hashlib.sha256(text.encode()).hexdigest()==expected[name][1],name
    old=original[name].decode()
    assert re.findall(r'^\s*- \[[ x~]\].*$',old,re.M)==re.findall(r'^\s*- \[[ x~]\].*$',text,re.M),name
    assert old.count('```')==text.count('```'),name
    assert re.findall(r'TH-?\d+(?:\.\d+)?',old)==re.findall(r'TH-?\d+(?:\.\d+)?',text[:len(text)]),name if False else ''
# Added summaries repeat TH81 legitimately; preserve the exact checkbox rows above.
for name,text in outputs.items():
    if name=='05_IMPLEMENTATION_AND_VALIDATION.md':
        old=original[name].decode()
        first=old.index('### 8.9');last=old.index('## 9 ',first)
        assert old[first:last] in text,'C section8 changed'
    (root/'execution'/name).write_text(text)
report=Path(os.environ['RUNNER_TEMP'])/'docs-source-review'
report.mkdir(exist_ok=True)
(report/'expected-hashes.json').write_text(json.dumps({'execution/'+name:after for name,(_,after) in expected.items()},indent=2)+'\n')
print('Five complete postimage hashes and original checkboxes/C section verified')
