#!/usr/bin/env python3
"""Bounded source/metadata maintenance. Never runs application or deployment code."""
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.request

PAIRS = [
 ('사용자 정태훈의 요청으로 Codex가', 'Codex 실행 환경에서'),
 ('요청 정태훈(tjung03), 실제 예행·기록 Codex.', '실제 예행·기록의 수행 주체와 환경은 연결된 Run 원본을 따른다.'),
 ('작성·검토 지원 Codex, 요청 정태훈.', '문서 담당 정태훈.'),
 ('B/AI가 독립 조회한 것은 아니며', '독립 조회로 검증한 것은 아니며'),
 ('B/AI의 CA bytes/Hash·TLS 독립검증 완료가 아니다', 'CA bytes/Hash·TLS 독립검증 완료가 아니다'),
 ('사용자가 제공한', '제공된'),
 ('사용자 전달 D 메시지', 'D의 전달 메시지'),
 ('사용자 확인으로', '전달 확인에 따라'),
 ('사용자 이번 확인으로', '이번 전달 확인에 따라'),
 ('사용자 18:44:47 KST 확인으로', '18:44:47 KST 전달 확인으로'),
 ('사용자 병합 요청에 따라 #5 이후', '#5 병합 이후'),
 ('사용자 그림 검토/표시 확인 의견', '그림 검토·표시 확인 의견'),
 ('사용자 질문에 따라 제작 계획 §5.1에', '제작 계획 §5.1에'),
 ('요청 정태훈, Source 구현·게시/검사·기록 지원 Codex.', 'Source 구현·게시·검사와 실제 실행 결과는 구분한다.'),
 ('두 Run의 요청자는 정태훈, 실제 수행자는 Codex이며', '두 Run의 실제 수행자는 Codex이며'),
 ('사용자의 21:28 KST 요청에 따라 현재 AI 후속은', '21:28 KST에 확정된 후속 범위는'),
 ('강사 DR 피드백과 사용자 원문 두 요청을 다시 대조했습니다.', '강사 DR 피드백과 기존 두 검토 범위를 다시 대조했습니다.'),
 ('사용자 프로젝트 소스 재등록 요청에 따른 현행화이고', '프로젝트 소스 재등록을 위한 현행화이며'),
]
CURRENT = '''
## 현재 실행 기준 — 2026-10-07 병합 후

Docs #64·#67은 각각 `94d5955612f589f40343360709513568bc5f0dc0`·`d2371a44f4c9b35cf8082991ec9700ccea2ec524`에 병합됐고 두 작업 브랜치는 삭제됐다. GitOps #17의 내부 Registry 소비 Source는 `fa3cea313e2cb1533d9703082619b085a3de25cc`에 반영됐다. 현재 안내와 과거 관측을 구분한다.

| 병행 작업 | 완료된 범위와 직접 조건 |
|---|---|
| lab 이미지 | 승인 FE/BE Digest·별도 Migration의 내부 Registry 경로 연결 완료. D의 워커 Pull4건 보고 유지. 실제 적용 직전 최종 SA·보존·사용창 확인 |
| lab Valkey/App | 서버 선언은 아직 main에 없음. D 초안 제안의 실제 수락/PR → C Data·B StatefulSet 허용/UID/Probe/자원 검토. Service/Ready와 DB/Schema·CA/목적 Secret·Route·권한·사용창·live Diff 수락 → 필요한 단일 Migration → Backend → Frontend → 새 Run |
| Cloud 금고 | 공개키 전달·C 암호문 공급은 완료. C 계정별 확인 보고와 B 본인 복호화·암호문 해시 대조·독립 사본 확인은 별도. Cloud 금고를 lab 작업의 선행조건으로 묶지 않음 |
| ROSA 준비 | 본인 도구·Caller/Backend·지원·가용시간/사양·비용 입력은 독립 준비. 실제 Plan은 A의 제한 출력·공통 prerequisite·C Data SG2 필요. OCP 철거·전체 A 업무·전체 Recovery 완료를 일괄 선행조건으로 두지 않음 |
| Pool·비용 | Engine2·process·종료 중 연결·예약 예산을 B/C가 확인한 뒤 소비 코드→D 새 Build/Digest. 후보3+2/60은 미채택. Cost PARTIAL, B 비용 입력19~24행·실제 가동/재시험/삭제 시각은 별도 |
| DR·기록 | RTO10분·영속 DB RPO30분·DB 운영 중 Backup15분 계획 주기. 예약 주기와 실제 G+D+U·전체 T18 달성은 구분. 원 Issue/PR/Run과 TH81·실제 완료2를 유지 |

원 작업: [Docs21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [GitOps10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10), [App1](https://github.com/seokpan/seokpan-hybrid-app/issues/1)·[App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4), [Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). FE/BE replicas0·Migration suspend/current/300초·단일 실행·삭제 보호는 유지한다. Cloud ECR·Recovery Harbor와 lab 내부 Registry는 서로 다른 경로다.

'''

def clean(text):
    for before, after in PAIRS:
        text = text.replace(before, after)
    return text

def checks(text):
    return collections.Counter(re.findall(r'^\s*[-*] \[([ xX])\]', text, re.M))

def archive(text):
    return '\n<details>\n<summary>이전 시점의 관측·검토 이력 — 현재 실행 지시와 구분</summary>\n\n' + text.strip() + '\n\n</details>\n'

def write_checked(path, text):
    old = path.read_text()
    if checks(old) != checks(text):
        raise ValueError('Completion states changed: '+str(path))
    path.write_text(text)

def source_docs(root):
    for path in root.rglob('*.md'):
        rel = path.relative_to(root).as_posix()
        if '.git' in path.parts or rel.startswith('.github/') or rel.startswith('evidence/T') or rel in ('design/00_PROJECT_STARTING_POINT.md','execution/REPOSITORY_CONSISTENCY_AUDIT.md'):
            continue
        old = path.read_text(); new = clean(old)
        if old != new: write_checked(path, new)
    boundaries = {
      'TJUNG03_EXECUTION_BOARD.md':'## 먼저 열 이슈와 기록 순서',
      'TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md':'## 1. 지금 무엇을 만드는가',
      'WORK_TRACKER.md':'## Current Observation',
      '05_IMPLEMENTATION_AND_VALIDATION.md':'## 0 팀 전체의 05 진입 안내',
    }
    for name, boundary in boundaries.items():
        path=root/'execution'/name; old=path.read_text()
        if '## 현재 실행 기준 — 2026-10-07 병합 후' in old:
            raise ValueError('Current revision already applied: '+name)
        first, rest=old.split('\n',1); index=rest.index(boundary)
        prior, body=rest[:index],rest[index:]
        if name=='TJUNG03_EXECUTION_BOARD.md':
            body=body.replace('핵심구현현동결','핵심구현동결')
            body=body.replace('사전검증용 Harbor Image','Harbor 승인 원본을 보존 복사한 내부 Registry Image')
            body=body.replace('새Harbor사전Image/Scan/Digest/Platform','승인 원본·내부 Registry 사본/Scan/Digest/Platform')
        if name=='TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md':
            body=body.replace('subPath', 'subPath')
            body=body.replace('## 4. B의 지난 작업과 아직 하지 않은 실행','## 4. B의 이전 작업·당시 실행 상태 — 현재는 상단 기준 적용')
            body=body.replace('## 5. 지금 진행하는 두 갈래','## 5. 단계별 작업·학습 이력 — 당시 대기와 현재 조건 구분')
        if name=='WORK_TRACKER.md':
            body=body.replace('## Current Observation','## Current Observation\n\n현재 Source·직접 조건은 상단 실행 기준을 따른다. 아래 표는 표에 명시한 관측일의 이력이다.')
            body=body.replace('## Work Links','## Work Links\n\n현재 상태는 각 원 Issue/PR을 확인한다. 아래 Draft·대기 표시는 작성 시점의 이력이며 현재 실행의 일괄 차단 조건이 아니다.')
            body=body.replace('## Team Access','## Team Access\n\n다음은 당시 계정·접근 보고다. 실제 실행 직전의 B Caller·목적 Role·클러스터 권한 확인을 대체하지 않는다.')
        if name=='05_IMPLEMENTATION_AND_VALIDATION.md':
            body=body.replace('### 0.2 최신 저장소 관측과 팀 보고','### 0.2 저장소 관측과 팀 보고 — 당시 시점의 이력')
        write_checked(path, first+'\n'+CURRENT+body+archive(prior))
    path=root/'architecture/tools/build_diagrams.py';text=path.read_text()
    text=text.replace('실제 Host·Path·Port·Route·Probe·Timeout은 Source 확인 후 반영','실제 Host·배포·연결·Probe/Timeout 동작은 환경별 확인')
    text=text.replace('관리자 → Public API 6443 → Cluster API  |  실제 /api·/ws 등의 Path나 Service Port는 아직 정하지 않음','관리자 → Public API 6443  |  Source 선언: FE / → 8080 · API /api/v1 · WSS /ws/v1 → BE 8000')
    text=text.replace('if self.number in {1, 2, 4, 12}:', "if self.number == 4:\n            provenance = '기준: 승인 설계 · GitOps #17 Source 선언  |  제작: 2026-10-02 · 접속 계약 개정: 2026-10-07 KST'\n        elif self.number in {1, 2, 12}:")
    path.write_text(text)
    path=root/'design/source-manifest.json';manifest=json.loads(path.read_text())
    for item in manifest['files']:
        raw=(root/item['path']).read_bytes();item['bytes']=len(raw);item['sha256']=hashlib.sha256(raw).hexdigest()
    manifest['consistency_revision']={'date':'2026-10-07 KST','scope':'Merged #64/#67 recheck; independent current guidance; diagram04 Source path/port caption correction','runtime_validation':'NOT_PERFORMED','svg_png_policy':'Only diagram04 is regenerated; other eleven pairs and historical Run payloads retained'}
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    path=root/'architecture/PRODUCTION_REVIEW.md'
    path.write_text(path.read_text()+'''\n## 2026-10-07 병합 후 접속 Source 정정\n\n#64/#67 병합본을 대조한 뒤 그림04의 Path·Port 미정 설명을 GitOps #17의 `/api/v1`·`/ws/v1`·FE Service8080·BE8000 선언에 맞췄다. 실제 Host·Route 배포·접속/Probe 동작은 별도 검증이다. 그림04의 생성 원본과 SVG/PNG만 개정하며 다른11쌍과 기존 Run 원본은 보존한다. 전체 생성 layout과 원문·XML·글리프·PNG 및 manifest 보존 회귀는 연결된 이번 검증 Run에서 확인한다. 이전 integrity-only 결과를 전체 기하 검사로 바꾸지 않는다.\n''')

IDENTITY = '''\ndef operator_id(value):
    """Validate an explicit execution label; it is not identity authentication."""
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.@-]{0,79}', value):
        raise argparse.ArgumentTypeError('operator must be an explicit 1-80 character execution label')
    return value

'''

def source_infra(root):
    path=root/'tools/recovery_fixture/run.py';text=path.read_text()
    if 'def operator_id(' in text: raise ValueError('Already updated')
    text=text.replace('def emit_evidence(',IDENTITY+'def emit_evidence(',1)
    text=text.replace('    # Exclusive output creation prevents replacing an earlier Run.','    args.operator = operator_id(args.operator)\n    # Exclusive output creation prevents replacing an earlier Run.',1)
    text=text.replace('"actual_operator": "Codex, user-authorized contribution for tjung03"','"actual_operator": args.operator')
    text=text.replace('"Codex for tjung03"','args.operator')
    text=text.replace('"tjung03; public summaries in new Docs Run"','"local output; transfer/custodian acceptance not recorded"')
    text=text.replace('actual contribution by Codex under tjung03 authorization. C did not execute or review this Run; C Data review pending.','actual operator `{args.operator}`. Execution label does not imply reviewer or handoff acceptance; C Data review is recorded separately.')
    text=text.replace('def run(args):','def run(args):\n    args.operator = operator_id(args.operator)',1)
    text=text.replace('    p.add_argument("--run-id",required=True)','    p.add_argument("--run-id",required=True)\n    p.add_argument("--operator",type=operator_id,required=True)',1)
    path.write_text(text)
    path=root/'tools/recovery_business_fixture/run.py';text=path.read_text()
    text=text.replace('    args.output.mkdir(parents=True,exist_ok=False)','    args.operator = data.operator_id(args.operator)\n    args.output.mkdir(parents=True,exist_ok=False)',1)
    text=text.replace('"actual_operator":"Codex, user-authorized contribution for tjung03"','"actual_operator":args.operator')
    text=text.replace('"Codex for tjung03"','args.operator')
    text=text.replace('"tjung03; source and aggregate evidence only"','"local output; transfer/custodian acceptance not recorded"')
    text=text.replace('Actual execution is Codex contribution authorized by tjung03. None of those teammates performed/reviewed this Run unless their separate review is recorded.','Actual operator is `{args.operator}`. Execution label does not imply reviewer, handoff or custodian acceptance.')
    text=text.replace(',"HISTORICAL_RESULT_HTTP"','')
    text=text.replace('    (args.output/"release.json").write_text','    release["known_limitations"] = ["Historical individual-result HTTP requires old Redis room context; outside adopted recovery Must"]\n    (args.output/"release.json").write_text',1)
    text=text.replace('def run(args):','def run(args):\n    args.operator = data.operator_id(args.operator)',1)
    text=text.replace('    parser.add_argument("--run-id",required=True)','    parser.add_argument("--run-id",required=True)\n    parser.add_argument("--operator",type=data.operator_id,required=True)',1)
    path.write_text(text)
    for folder in ('recovery_fixture','recovery_business_fixture'):
        path=root/'tools'/folder/'README.md';text=path.read_text()
        text=text.replace('--run-id ', '--operator ACTUAL_EXECUTOR_ID --run-id ')
        text+='''\n## 실행 주체와 검증 범위\n\n새 Run은 `--operator ACTUAL_EXECUTOR_ID`로 실제 수행 주체를 명시한다. 이 값은 기록용 표기이며 인증이나 리뷰·인계 수락 증거가 아니다. 기존 Run을 덮어쓰지 않고 새 Run ID/출력 경로를 사용한다. 고정된 과거 App/Redis 조합을 재현하는 부분 fixture이며 Valkey7.2·전체 T18 또는 DR10분/영속 DB RPO30분·15분 Backup 달성을 검증한 것으로 승계하지 않는다. 기존 Evidence는 변경하지 않는다.\n'''
        path.write_text(text)


def api(repository, path, method='GET', payload=None):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    request=urllib.request.Request('https://api.github.com/repos/'+repository+'/'+path,data=data,method=method,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json','User-Agent':'seokpan-consistency-maintenance'})
    with urllib.request.urlopen(request,timeout=30) as response:return json.load(response),response.headers

def pages(repository,path):
    result=[]
    for number in range(1,101):
        values,headers=api(repository,path+('&' if '?' in path else '?')+'per_page=100&page='+str(number));result+=values
        if 'rel="next"' not in headers.get('Link',''):return result
    raise ValueError('Pagination did not end')

def metadata(repository, report):
    short=repository.rsplit('-',1)[-1]
    active={'docs':{21,8,6},'infra':{25},'gitops':{10},'app':{4}}[short]
    records=[];pending=[]
    for kind,path in [('issue','issues?state=all'),('comment','issues/comments')]:
        for item in pages(repository,path):
            if item['user']['login']!='tjung03':continue
            before=item.get('body') or '';after=clean(before)
            if kind=='issue' and item['number'] in active and item['state']=='open' and 'pull_request' not in item:
                boundary='## TH별로 실행 결과를 먼저 남길 곳' if short=='docs' and item['number']==21 else '<details>'
                if boundary not in after: raise ValueError('Expected historical boundary missing')
                after=CURRENT+after[after.index(boundary):]
            if kind=='comment' and item['id']==6022270133:
                after=after.replace('실제 실행은 금고 본인 확인 → lab Valkey 선언·권한/입력 검토 →','Cloud 금고 본인 확인은 Cloud Secret 공급 조건이며 lab 작업과 병행합니다. lab은 Valkey 선언·권한/입력 검토 →')
            if after==before:continue
            if checks(before)!=checks(after) or len(after)>65536:
                raise ValueError('Body limit or completion-state preservation failed: '+str(item.get('number',item['id'])))
            target='issues/'+str(item['number']) if kind=='issue' else 'issues/comments/'+str(item['id'])
            pending.append((target,item,before,after))
    # Preflight every target before issuing any write.
    for target,item,before,after in pending:
        current,_=api(repository,target)
        if current.get('body')!=before or current['user']['login']!='tjung03':raise ValueError('Concurrent edit: '+target)
    for target,item,before,after in pending:
        current,_=api(repository,target)
        if current.get('body')!=before:raise ValueError('Concurrent edit: '+target)
        api(repository,target,'PATCH',{'body':after})
        result,_=api(repository,target)
        if result.get('body')!=after:raise ValueError('Readback mismatch: '+target)
        for key in ('state','assignees','milestone'):
            if key in current and current[key]!=result[key]:raise ValueError('Unexpected metadata change: '+key)
        records.append({'path':target,'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),'readback':'MATCH','checkbox_states_preserved':True})
        destination=report/target.replace('/','_');destination.with_suffix('.before.md').write_text(before);destination.with_suffix('.after.md').write_text(after)
    (report/'metadata-result.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['source-docs','source-infra','metadata']);p.add_argument('--root',type=Path,default=Path.cwd());p.add_argument('--repository');p.add_argument('--report',type=Path);a=p.parse_args()
    if a.mode=='source-docs':source_docs(a.root)
    elif a.mode=='source-infra':source_infra(a.root)
    else:
        a.report.mkdir(parents=True,exist_ok=True);metadata(a.repository,a.report)
