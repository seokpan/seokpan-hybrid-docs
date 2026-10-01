#!/usr/bin/env python3
"""Build editable, font-embedded design SVGs and matching PNG exports.

Requirements: Pillow, fonttools, Inkscape; Noto Sans CJK KR Regular.
The supplied font must also be installed for Inkscape PNG rendering.
"""
import argparse
import base64
import io
import json
from pathlib import Path
import subprocess
from xml.sax.saxutils import escape

from PIL import Image, ImageFont
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
INK = '#152C43'
MUTED = '#52677A'
PALETTE = {
    'cloud': ('#EAF2FC', '#316FB4'),
    'local': ('#E8F5F1', '#237E70'),
    'data': ('#F0EDFC', '#7461A8'),
    'recovery': ('#FFF1E3', '#B97428'),
    'neutral': ('#F1F4F7', '#60788E'),
}
META = [
    ('01-logical-architecture', '전체 논리 아키텍처', 'Cloud Primary + On-Prem Restore-based Recovery',
     '02 §3~4 · 03 §3-A.1~5 · 04 §1 / §5.5', '실제 운영 상태·복구 준비 완료 여부는 문서 05의 증거로 확인'),
    ('02-physical-architecture', '전체 물리 아키텍처', '서울 VPC · 3 AZ · 9 Subnet · 관리 책임과 배치 목표',
     '03 §3-B.3~6 / §3-B.8~9 / §3-D.10 / §3-F.18 · 04 §5.5', '실제 AZ 이름·Host·VM 주소/용량·서비스 배치 AZ는 확인 대기'),
    ('03-hybrid-network', 'Hybrid 네트워크와 경로', 'RDS 사설 왕복과 인터넷 HTTPS 경로의 분리',
     '03 §3-B.1 / §3-B.5 / §3-B.8~9 / §3-D.9.3 · 04 §1', '실제 Host /32·Gateway·ENI·SG·DNS와 수신 Source IP 확인 필요'),
    ('04-service-traffic-tls', '사용자 트래픽과 TLS', '같은 공개 Host의 FE · HTTP API · WSS 분기',
     '03 §3-B.8.3 / §3-E.3~7 · 04 §1', '실제 Host·Path·Port·Route·Probe·Timeout은 Source 확인 후 반영'),
    ('05-state-reconnect-consistency', '상태 책임과 재접속·업무 확정', '공유 Runtime · 영속 확정 · 사용자 통지를 별도 책임으로 관리',
     '03 §3-D.5 / §3-D.10.7 / §3-E.10~14', '인증·Schema·요청 식별·원자성·재접속의 실제 구현은 확인 대기'),
    ('06-cicd-release-flow', 'CI/CD와 Release 전달', 'Image 후보에서 검토·배포·Recovery 보존까지',
     '03 §3-A.8 / §3-F.16~17 · 04 §5.2 / §5.4', '실제 Job·Scan·Digest·PR·Runtime Pull·보존본의 연결 확인 필요'),
    ('07-iac-gitops-ownership', 'Terraform·Ansible·GitOps 소유권과 수명', '세 Root/State · 최초 설치 인계 · 로컬 복구 적용 예외',
     '02 §15~19 · 03 §3-A.7 / §3-F.3~9 / §3-F.17.3 / §3-F.19 · 04 §2', '실제 Plan·Role·Lock·State 연결·삭제 보호 동작은 구현 Gate'),
    ('08-identity-secret-supply', '관리 인증과 Secret 공급', '사람 · 자동화 · 앱 · 복구 재료의 권한과 보관 범위',
     '03 §3-C / §3-F.6 · 04 §5.2~3 / §5.6', '실제 발급·MFA·Policy·공급·로그인/회수·오프라인 복원은 확인 대기'),
    ('09-observability-evidence', '관측과 Evidence', '신호 수집 · 담당 판단 · 실행 결과와 보호 원본 보존',
     '02 §13 · 03 §3-G.8~9 · 04 §5.4 / §8.5', '실제 수집 경로·Exporter·receiver·보존 위치·Run은 확인 대기'),
    ('10-backup-offline-recovery', '백업과 On-Prem 오프라인 복구', '정상 시 사전 준비와 AWS 접속 불가 시 실행의 분리',
     '03 §3-C.12.7 / §3-D.9.3~9.8 / §3-F.17.3 / §3-G.7 · 04 §5.1 / §5.5', '실제 Backup·독립 Storage/Key·도구 호환·복원 결과는 확인 대기'),
    ('11-ha-failure-domains', 'HA와 장애 영향 범위', '플랫폼 HA · 상태 정합성 · Restore-based Recovery',
     '02 §25~27 · 03 §3-B.9.8 / §3-E.14 / §3-F.18 / §3-G · 04 §10.2', '장애 주입·서비스 영향·MTTR/RTO/RPO·재시험은 아직 미실행'),
    ('12-migration-responsibility', '1차에서 2차로의 책임 이전', '기존 검증 상태를 보존하고 역할별 유지·이전·대체',
     '00 §6 / §8 / §12 · 02 §2.3 · 03 §3-A.6 / §3-D.2~7', 'Seed SHA·실제 Migration/전환·개별 자원의 최종 판정은 확인 대기'),
]


class Canvas:
    def __init__(self, number, font_path, height=1200):
        self.meta = META[number-1]
        self.number, self.h, self.font_path = number, height, font_path
        self.parts, self.texts, self.audit, self.cards = [], [], [], []
        self.fonts = {}
        self.rect(0, 0, 1800, height, '#FBFCFE', radius=0)
        self.rect(0, 0, 1800, 10, '#237E70', radius=0)
        self.text(64, 56, 'SEOKPAN  /  HYBRID CLOUD', 18, MUTED, weight=600)
        self.rect(1432, 34, 304, 42, '#E8F5F1', radius=21)
        self.text(1584, 62, '설계 목표 · 구현/시험 미확인', 18, '#237E70', anchor='middle')
        self.text(64, 120, f'{number:02d}  {self.meta[1]}', 39, INK, weight=700)
        self.text(64, 161, self.meta[2], 23, MUTED)

    def font(self, size):
        if size not in self.fonts:
            self.fonts[size] = ImageFont.truetype(str(self.font_path), size)
        return self.fonts[size]

    def width(self, text, size):
        return self.font(size).getlength(text)

    def rect(self, x, y, w, h, fill='#FFFFFF', stroke=None, radius=16, sw=1.6):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"'+
                          (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>' )

    def text(self, x, y, value, size=21, color=INK, weight=400, anchor='start'):
        value = str(value)
        width = self.width(value, size)
        left = x if anchor == 'start' else x-width/2 if anchor == 'middle' else x-width
        self.audit.append({'text': value, 'x': round(left, 2), 'y': y, 'w': round(width, 2), 'size': size})
        self.texts.append(value)
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

    def wrap(self, value, max_width, size):
        result=[]
        for para in str(value).split('\n'):
            line=''
            for char in para:
                if self.width(line+char, size)>max_width and line:
                    result.append(line.rstrip()); line=char.lstrip()
                else:
                    line+=char
            result.append(line.rstrip())
        return result

    def para(self, x, y, value, width, size=21, color=MUTED, step=None):
        step = step or size*1.5
        lines=self.wrap(value,width,size)
        for i,line in enumerate(lines):
            self.text(x,y+i*step,line,size,color)
        return y+(len(lines)-1)*step

    def panel(self, x, y, w, h, title, theme='neutral', subtitle=None):
        fill, color=PALETTE[theme]
        self.rect(x,y,w,h,fill,color,18)
        self.text(x+24,y+38,title,25,color,700)
        if subtitle:
            self.para(x+24,y+70,subtitle,w-48,20,color)

    def card(self, x, y, w, h, title, lines=(), theme='neutral', tag=None, size=21):
        fill,color=PALETTE[theme]
        self.rect(x,y,w,h,'#FFFFFF','#CCD8E3',12)
        self.rect(x,y+14,5,h-28,color,radius=2)
        tx=x+22
        if tag:
            self.rect(x+20,y+16,50,35,fill,radius=8)
            self.text(x+45,y+40,tag,17,color,700,anchor='middle')
            tx=x+82
        title_lines=self.wrap(title,w-(tx-x)-18,24)
        for i,t in enumerate(title_lines):
            self.text(tx,y+40+i*32,t,24,INK,700)
        cy=y+40+len(title_lines)*32
        for line in lines:
            cy=self.para(x+22,cy,line,w-44,size)+size*1.5
        used=cy-size*1.5 if lines else y+40+(len(title_lines)-1)*32
        if used>y+h-15:
            raise ValueError(f'Card text exceeds height: {title}, {used} > {y+h-15}')
        self.cards.append({'title':title,'x':x,'y':y,'w':w,'h':h})

    def arrow(self, points, label=None, color='#60788E', dashed=False, label_pos=None):
        d='M '+' L '.join(f'{x},{y}' for x,y in points)
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.8" stroke-linejoin="round"'+
                          (' stroke-dasharray="9 7"' if dashed else '')+f' marker-end="url(#arrow-{color[1:]})"/>')
        if label:
            x,y=label_pos or ((points[0][0]+points[-1][0])/2,(points[0][1]+points[-1][1])/2-10)
            w=self.width(label,19)+20
            self.rect(x-w/2,y-23,w,32,'#FBFCFE',radius=6)
            self.text(x,y,label,19,color,anchor='middle')

    def note(self, y, title, body, theme='neutral', h=100):
        fill,color=PALETTE[theme]
        self.rect(64,y,1672,h,fill,radius=14)
        self.text(86,y+34,title,23,color,700)
        self.para(86,y+68,body,1628,20,color)

    def finish(self):
        self.rect(64,self.h-122,1672,1,'#CED9E3',radius=0)
        self.text(64,self.h-89,'기준: 승인 Project Source 00~04 · 2026-10-01  |  제작: 2026-10-02 KST',18,MUTED)
        self.text(64,self.h-58,'근거: '+self.meta[3],18,MUTED)
        self.text(64,self.h-27,'확인 대기: '+self.meta[4],18,MUTED)
        for t in self.audit:
            if t['x']<0 or t['x']+t['w']>1800 or t['y']-t['size']<0 or t['y']>self.h:
                raise ValueError('Text outside canvas: '+str(t))
        font=TTFont(self.font_path, recalcTimestamp=False)
        opts=subset.Options();opts.flavor='woff';opts.desubroutinize=True
        sub=subset.Subsetter(options=opts)
        sub.populate(text=''.join(self.texts));sub.subset(font);font.flavor='woff'
        stream=io.BytesIO();font.save(stream)
        data=base64.b64encode(stream.getvalue()).decode()
        markers=[]
        for color in ['#60788E','#316FB4','#237E70','#7461A8','#B97428']:
            markers.append(f'<marker id="arrow-{color[1:]}" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L9 4.5L0 9Z" fill="{color}"/></marker>')
        style=f'@font-face{{font-family:SeokpanDiagram;src:url(data:font/woff;base64,{data}) format("woff");}}text{{font-family:SeokpanDiagram,"Noto Sans CJK KR",sans-serif;}}'
        svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="{self.h}" viewBox="0 0 1800 {self.h}" role="img" aria-labelledby="title desc">\n'
             f'<title id="title">{escape(self.meta[1])} — 설계 목표</title>\n'
             f'<desc id="desc">{escape(self.meta[2]+'. '+self.meta[4]+'. 실제 구축/시험 결과가 아닌 승인 설계 기준.')}</desc>\n'
             '<defs>'+''.join(markers)+'</defs>\n<style>'+style+'</style>\n'+ '\n'.join(self.parts)+'\n</svg>\n')
        out=ROOT/'diagrams'/f'{self.meta[0]}.svg'
        out.write_text(svg)
        return {'id':f'{self.number:02d}','slug':self.meta[0],'title':self.meta[1],'height':self.h,
                'source_refs':self.meta[3],'pending':self.meta[4],'texts':self.audit,'cards':self.cards}


def logical(c):
    c.card(64,208,310,130,'사용자 / Client',['HTTPS · WSS'],tag='WEB',theme='cloud')
    c.card(432,208,490,130,'Public Ingress / Route',['같은 공개 Host · FE/API/WSS 분기'],tag='TLS',theme='cloud')
    c.arrow([(374,273),(432,273)],color='#316FB4')
    c.card(964,208,362,130,'Source / GitOps',['App · Infra · GitOps · Docs'],tag='GIT')
    c.card(1368,208,368,130,'관리 접속',['Public API · GitHub Team IDP'],tag='OPS')
    c.panel(64,380,1060,594,'AWS / Cloud Primary','cloud','정상 사용자 요청의 필수 경로는 AWS 안에서 종료')
    c.panel(88,470,610,474,'ROSA Classic Multi-AZ','cloud')
    c.card(112,534,562,102,'Router / Route',['Edge TLS 종료 · 내부 HTTP'],theme='cloud',tag='NET')
    c.card(112,658,270,127,'Frontend',['Web 제공'],theme='cloud',tag='FE')
    c.card(404,658,270,127,'Backend',['업무 · API · 실시간 처리'],theme='cloud',tag='BE',size=20)
    c.card(112,810,270,109,'OpenShift GitOps',['Desired State 반영'],theme='cloud',size=20)
    c.card(404,810,270,109,'Native + UWM',['플랫폼/앱 관측'],theme='cloud',size=20)
    c.card(730,470,370,155,'RDS for MariaDB',['Multi-AZ DB instance','영속 업무 기록'],theme='data',tag='DB')
    c.card(730,647,370,155,'ElastiCache Redis OSS',['Primary + Replica · Multi-AZ','Session / Room / Game Runtime'],theme='data',tag='RT',size=20)
    c.card(730,824,178,120,'ECR',['Cloud Image'],theme='cloud',size=19)
    c.card(930,824,170,120,'S3',['Backup/State','별도 Bucket'],theme='cloud',size=19)
    c.panel(1160,380,576,594,'On-Prem / 운영과 복구','local','1차 자산 보존 · 정상 Cloud Runtime의 필수 경로 아님')
    c.card(1184,470,248,132,'Jenkins',['Test / Build / Scan','ECR Push · PR 작성'],theme='local',size=20)
    c.card(1456,470,256,132,'Harbor',['승인 Recovery Image','사전 보존'],theme='local',size=20)
    c.card(1184,626,248,132,'Data 작업 VM',['Migration · Backup','RDS 사설 접속'],theme='local',size=20)
    c.card(1456,626,256,132,'전용 VPN VM',['WireGuard Gateway','On-Prem 선제 연결'],theme='local',size=20)
    c.card(1184,782,528,162,'오프라인 복구 환경',['보존 Backup / Bundle / Key · 새 Redis / App','새 전용 MariaDB VM에 직접 TLS 연결'],theme='recovery',tag='DR',size=20)
    c.note(1000,'Hybrid의 역할','RDS 작업은 VPN · S3/ECR/GitHub는 인터넷 HTTPS  |  복구는 장애 전 로컬 보존본으로 시작',h=74)


def physical(c):
    c.panel(64,206,1672,800,'AWS 서울 Region / VPC 192.168.64.0/20','cloud','AZ-A/B/C는 역할 이름 · 실제 AZ 이름/ID 미확정 · 생성 Subnet 9개')
    for i,(x,az) in enumerate([(88,'AZ-A'),(640,'AZ-B'),(1192,'AZ-C')]):
        c.panel(x,298,520,436,az,'cloud')
        c.card(x+20,360,480,98,f'Public · 192.168.{64+i}.0/24',[f'NAT-{chr(65+i)} · Public API/Ingress 관리 자원 영역'],theme='cloud',size=19)
        c.card(x+20,478,480,122,f'ROSA Private · 192.168.{67+i}.0/24',['관리형 Control Plane / Infra / Worker 영역','同 AZ NAT로 Egress'.replace('同','같은')],theme='cloud',size=20)
        c.card(x+20,620,480,94,f'Data Private · 192.168.{70+i}.0/24',['RDS / Redis Subnet Group · 인터넷 기본 Route 없음'],theme='data',size=19)
    c.card(88,758,520,148,'ROSA 규모와 배치',['Control Plane 3 + Infra 3 + Worker 3 최소','Worker m5.xlarge · FE/BE 각 3 Replica는 초기 후보','Pod 10.128.0.0/14 · Service 10.240.0.0/16'],theme='cloud',size=20)
    c.card(640,758,520,148,'관리형 Data의 수와 책임',['RDS: Primary + 동기 Standby','Redis OSS: Primary 1 + 비동기 Replica 1'],theme='data',size=20)
    c.card(1192,758,520,148,'Network 공통 자원',['IGW · NAT 3 · S3 Gateway Endpoint','VPN EC2 1 + EIP · Public AZ-A 배치는 후보'],theme='cloud',size=20)
    c.para(88,949,'ROSA 설치 입력: Public/ROSA Private 6개  |  Data Subnet 3개 ≠ 서비스 인스턴스 3개',1624,21)
    c.para(88,983,'예비 7블록: 192.168.73.0/24~192.168.79.0/24 · 미생성  |  Data 응답: 승인 Host /32 → VPN ENI',1624,20)
    c.panel(64,1034,1672,214,'On-Prem / 기존 자산과 2차 전용 역할','local')
    c.card(88,1098,390,126,'기존 기반 보존',['1차 Cluster · Jenkins · Harbor','Recovery Storage · vRouter'],theme='local',size=20)
    c.card(498,1098,390,126,'새 전용 VPN Gateway VM',['학원망에서 Outbound WireGuard','실제 Host/IP/용량 미확인'],theme='local',size=20)
    c.card(908,1098,390,126,'Data 작업 VM',['Backup / Migration 실행','복구 DB VM과 별도'],theme='local',size=20)
    c.card(1318,1098,394,126,'새 전용 복구 DB VM',['격리 MariaDB · 직접 TLS','기존 DB/MaxScale 보존'],theme='recovery',size=20)


def hybrid(c):
    c.panel(64,206,1672,232,'정상 Cloud 사용자 경로 / On-Prem·VPN 비의존','cloud')
    c.card(88,274,340,135,'Client',['HTTPS / WSS'],theme='cloud',tag='WEB')
    c.card(560,274,510,135,'Public Ingress → ROSA',['FE / BE · 관리 API는 별도'],theme='cloud',tag='APP')
    c.card(1202,274,510,135,'RDS / Redis',['Cloud 내부 사설 Data 접속'],theme='data',tag='DB')
    c.arrow([(428,340),(560,340)],color='#316FB4')
    c.arrow([(1070,340),(1202,340)],color='#316FB4')
    c.panel(64,470,780,477,'On-Prem / Data 작업 경로','local')
    c.panel(1038,470,698,477,'AWS / 사설 Data 접근','cloud')
    c.card(88,554,320,142,'Job Host',['Data VM · 승인 /32','Migration / Backup'],theme='local')
    c.card(460,554,360,142,'기존 vRouter',['Data CIDR → 전용 Gateway','최소 Host · 원본 IP 보존 목표'],theme='local',size=20)
    c.arrow([(408,625),(460,625)],color='#237E70')
    c.card(460,786,360,136,'전용 VPN Gateway',['wg0 · On-Prem 10.200.0.2','LAN/vRouter 왕복 Route'],theme='local',size=20)
    c.arrow([(640,696),(640,786)],color='#237E70')
    c.card(1062,786,300,136,'VPN EC2 1 + EIP',['AWS 10.200.0.1','Tunnel 10.200.0.0/30'],theme='cloud',size=20)
    c.card(1062,554,650,142,'RDS for MariaDB',['사설 Endpoint · 목적별 SQL 인증 · TLS','Data Route: 승인 Job Host /32 → VPN ENI'],theme='data',size=20)
    c.arrow([(1212,786),(1212,696)],'TLS',color='#7461A8',label_pos=(1248,747))
    c.arrow([(820,830),(1062,830)],color='#237E70')
    c.arrow([(1062,864),(820,864)],color='#237E70',dashed=True)
    c.text(941,747,'WireGuard',22,'#237E70',anchor='middle')
    c.text(941,777,'UDP 51820',20,'#237E70',anchor='middle')
    c.text(941,914,'On-Prem 선제 연결',18,'#237E70',anchor='middle')
    c.note(960,'인터넷 경로와 Route 경계','S3/ECR/GitHub/API는 인터넷 HTTPS · On-Prem의 S3 Gateway Endpoint VPN 경유 사용 없음\nRoute / AllowedIPs / Host Forward Firewall / SG는 별도 · Pod/Service CIDR 직접 광고 없음 · 팀 Route Table 5 + Main 별도',h=114)


def traffic(c):
    c.card(64,212,340,133,'Client / 같은 공개 Host',['HTTPS · WSS'],theme='cloud',tag='WEB')
    c.card(516,212,440,133,'Public Ingress LB',['사용자 공개 진입'],theme='cloud',tag='LB')
    c.card(1068,212,668,133,'OpenShift Router / Route',['Edge TLS 종료 · 의미별 Path 분기'],theme='cloud',tag='TLS')
    c.arrow([(404,278),(516,278)],color='#316FB4')
    c.arrow([(956,278),(1068,278)],color='#316FB4')
    c.panel(64,430,1672,480,'ROSA / 내부 HTTP · ClusterIP Service → Pod','cloud')
    positions=[(88,'FE Service → FE Pod',['Web 화면 제공','FE를 임의 API Proxy로 두지 않음']),
               (648,'BE Service → BE Pod',['HTTP API · 업무 처리','서버에서 사용자/업무 권한 확인']),
               (1208,'BE Service → BE Pod',['WebSocket · 실시간 통신','재접속 시 현재 상태/권한 확인'])]
    for x,title,lines in positions:
        c.card(x,556,504,148,title,lines,theme='cloud',size=20)
    c.parts.append('<path d="M1400 345V503M340 503H1460" fill="none" stroke="#316FB4" stroke-width="2.8"/>')
    for tx,label in [(340,'FE Path'),(900,'API Path'),(1460,'WSS Path')]:
        c.arrow([(tx,503),(tx,556)],label,color='#316FB4',label_pos=(tx,534))
    c.card(648,786,504,99,'RDS for MariaDB',['TLS · 서버 이름/CA · SQL 인증'],theme='data',size=20)
    c.card(1208,786,504,99,'ElastiCache Redis OSS',['TLS · 서버 이름/CA · AUTH'],theme='data',size=20)
    c.arrow([(900,704),(900,786)],color='#7461A8')
    c.arrow([(1460,704),(1460,786)],color='#7461A8')
    c.parts.append('<path d="M900 746H1460" fill="none" stroke="#7461A8" stroke-width="2.8"/>')
    c.text(88,824,'BE 전체의 Data 연결',22,'#7461A8',weight=700)
    c.para(88,858,'두 BE 칸은 HTTP/WSS 역할 표현이며\n별도 제품·Deployment 추가를 뜻하지 않음',510,20)
    c.note(954,'관리 API는 사용자 서비스와 별도','관리자 → Public API 6443 → Cluster API  |  실제 /api·/ws 등의 Path나 Service Port는 아직 정하지 않음',h=120)


def state(c):
    c.panel(64,206,1672,264,'업무 상태의 책임 / Backend가 각 결과를 구분','neutral')
    c.card(88,276,504,170,'Redis / 공유 Runtime',['Session · Room · Ready · 연결 세대','Game Runtime · Turn · Vote','조건 검사/갱신의 원자성은 실제 구현 확인'],theme='data',size=20)
    c.card(648,276,504,170,'MariaDB / 영속 업무 확정',['Member · Game · Move · Result · Rating','DB Transaction · 고유성/현재 상태 검사','DB와 Redis의 공통 Transaction을 가정하지 않음'],theme='data',size=20)
    c.card(1208,276,504,170,'Client / 현재 상태 확인',['Pub/Sub · WSS 통지는 확정과 별개','통지 누락은 서버 현재 상태로 확인','응답 유실이 곧 업무 미실행은 아님'],theme='cloud',size=20)
    c.panel(64,504,780,441,'단절 → 재접속 / 보존된 서버 상태 확인','cloud')
    steps=[('1  쓰기 보류 · 인증/Session 확인','만료·회수 → 재로그인 안내'),
           ('2  대상 권한 · 새 연결 식별 확인','이전 연결의 늦은 명령/정리 차단'),
           ('3  현재 상태 · 구독 · 버전 공백 확인','미확인 쓰기는 결과 조회 후 재시도 판단')]
    for i,(title,body) in enumerate(steps):
        c.card(88,574+i*114,732,92,title,[body],theme='cloud',size=20)
        if i<2:c.arrow([(454,666+i*114),(454,688+i*114)],color='#316FB4')
    c.panel(880,504,856,441,'부분 실패 / 대상별 재개 Gate','recovery')
    rows=[('DB 확정 전 실패/Commit 불명확','완료 선언 보류 · 기존 요청/영속 기록으로 확인'),
          ('DB 확정 · Redis 갱신 실패','DB 결과 보존 · 해당 Game 진행 제한/정합성 확인'),
          ('DB/Runtime 정상 · 통지만 실패','업무 재실행 대신 현재 상태 조회'),
          ('Redis 전체 소실 / 새 Runtime','완료 DB 기록 보존 · 진행 중단 · 새 로그인/게임')]
    for i,(title,body) in enumerate(rows):
        c.text(904,582+i*88,title,22,'#B97428',weight=700)
        c.para(904,615+i*88,body,808,20)
    c.note(977,'입력 재개 조건','유효한 인증/권한 · 현재 상태 · DB/Runtime 관계 · 미확인 요청의 결과 확인  |  자동 게임 복원·정확히 한 번 처리 보장으로 표현하지 않음',h=97)


def release(c):
    c.panel(64,206,1672,256,'CI / 후보 Image와 검증 결과 생성','local')
    nodes=[(88,360,'App Source',['Source SHA · Test 계약']),
           (532,536,'On-Prem Jenkins',['Test → Build → Scan','지정 Image/Digest와 검증 결과 연결']),
           (1152,560,'Amazon ECR / 후보 Release',['CI Push Principal · 불변 Digest','Cloud Node Runtime Pull은 별도 주체'])]
    for x,w,title,lines in nodes:c.card(x,276,w,161,title,lines,theme='local' if x<1152 else 'cloud',size=20)
    c.arrow([(448,357),(532,357)],color='#237E70')
    c.arrow([(1068,357),(1152,357)],color='#237E70')
    c.panel(64,500,1030,430,'Cloud Promotion / 사람이 검토·Merge','cloud')
    c.card(88,572,454,154,'GitOps Promotion PR',['Digest · 설정/Schema/Secret 개정','Scan/검증 결과 · Recovery 준비 상태','GitOps Writer는 Push/PR만 수행'],theme='cloud',size=20)
    c.card(612,572,458,154,'사람 Review / Merge',['확인한 Commit만 배포 Branch에 Merge','Jenkins 자동 Merge·직접 oc/TF Apply 없음'],theme='cloud',size=20)
    c.arrow([(542,646),(612,646)],color='#316FB4')
    c.card(612,792,458,114,'OpenShift GitOps → Cloud Runtime',['Reader · Sync · Node ECR Pull · 배포 확인'],theme='cloud',size=20)
    c.arrow([(841,726),(841,792)],color='#316FB4')
    c.panel(1130,500,606,430,'Recovery / 승인 Image의 사전 보존','recovery')
    c.card(1154,572,558,154,'Harbor Recovery Image',['검토·승인된 Recovery Release 보존','ECR/Harbor 실제 Digest·플랫폼 Mapping','모든 Build를 승인 Release로 보존하지 않음'],theme='recovery',size=20)
    c.card(1154,792,558,114,'보존 Manifest / Recovery Bundle',['설정/CA/Secret 개정 · 도구 · 로컬 Pull 검증'],theme='recovery',size=20)
    c.arrow([(1433,726),(1433,792)],color='#B97428')
    c.arrow([(1432,437),(1432,480),(1748,480),(1748,646),(1712,646)],'승인·보존',color='#B97428',label_pos=(1570,486))
    c.arrow([(1152,404),(1108,404),(1108,480),(40,480),(40,646),(88,646)],color='#316FB4')
    c.note(967,'Release 추적과 적용 순서','Release ID → Source SHA / FE·BE Digest / 설정·Schema·Secret 개정 → 실제 Run  |  최초 App 수동 Sync 후 자동 Sync/SelfHeal · 자동 Prune 보류',h=107)


def ownership(c):
    c.panel(64,206,1672,268,'Terraform / 세 Root·State와 제한된 비밀값 아닌 인계','cloud')
    for x,w,title,lines in [
        (88,474,'bootstrap / 이유빈',['Backend · TF 실행 Role · State 기반','현재 Remote 정본 점검 · 이전 반복 없음']),
        (662,474,'foundation / 이유빈',['VPC/Data/Registry/Backup · 공통 IAM','Root 전체 통합 · 전체 Destroy 별도 판단']),
        (1236,476,'rosa / 정태훈',['Cluster/Pool · Cluster-specific IAM/OIDC','ROSA Window 생성/삭제 · 영속 Data 별도'])]:
        c.card(x,276,w,170,title,lines,theme='cloud',size=20)
    c.arrow([(562,361),(662,361)],color='#316FB4')
    c.arrow([(1136,361),(1236,361)],color='#316FB4')
    c.panel(64,512,1020,428,'Cloud / 최초 설치에서 상시 Desired State로 인계','cloud')
    c.card(88,590,434,140,'Infra 최소 Ansible / 최초 예외',['GitOps Operator 설치 선언','GitOps 원본 Root 최초 등록'],theme='cloud',size=20)
    c.card(624,590,436,140,'GitOps / 이후 선언 Owner',['Root/AppProject/Namespace/App','Operator 생성 결과는 Operator 소유'],theme='cloud',size=20)
    c.arrow([(522,660),(624,660)],'인계',color='#316FB4',label_pos=(573,642))
    c.card(88,794,972,119,'Secret 공급 / 별도 Owner',['값·프로젝트 Secret Object를 지정 절차로 공급 · TF/Argo와 같은 객체 중복 관리 금지'],theme='data',size=20)
    c.panel(1124,512,612,428,'On-Prem / Offline 적용 예외','recovery')
    c.card(1148,590,564,140,'GitOps Recovery Overlay',['장애 전 검토·Render·Bundle 보존','장애 후 GitHub 신규 조회 의존 없음'],theme='recovery',size=20)
    c.card(1148,794,564,119,'Ansible / 로컬 복구 Namespace만',['보존본 Apply · 실행 Argo와 같은 객체 중복 관리 금지'],theme='recovery',size=20)
    c.arrow([(1430,730),(1430,794)],color='#B97428')
    c.note(972,'삭제·수명과 실행 책임','State Root ≠ 비용 수명 · ROSA 삭제 ≠ RDS/Redis/Backup 삭제 · NAT/EIP는 의존 확인 후 정리 · 같은 State 쓰기는 지정 실행자 한 사람씩',h=102)


def identity(c):
    c.panel(64,206,1672,290,'목적별 인증 / 사람·자동화·서비스의 인증 경계','neutral')
    for x,w,title,lines,theme in [
        (88,502,'사람 / AWS',['개인 IAM User 4 + MFA','목적별 TF Role · Root 일상 사용 없음','개인 Admin 직접 호출까지 격리한 것은 아님'],'cloud'),
        (648,502,'사람 / ROSA·Argo',['정상 GitHub Team IDP / RBAC · Argo SSO','유지 htpasswd 비상 관리자 하나','초기 ROSA/Argo 인증은 검증 후 회수'],'cloud'),
        (1208,504,'자동화·서비스',['CI Push/Writer · Argo Reader · Node Pull','Backup SQL/S3 · App DB/Redis 인증','서비스·목적별 주체/공급 범위 분리'],'data')]:
        c.card(x,276,w,195,title,lines,theme=theme,size=20)
    c.panel(64,530,1672,414,'SOPS+age 공급과 보관 / 값·Key·예비본을 Git 밖에서 관리','data')
    rows=[('Cloud Bootstrap','정태훈','이유빈','IDP / Reader / Cloud App'),
          ('Automation · CI','최유준','정태훈','Writer PAT / ECR CI / Harbor Publisher'),
          ('Automation · Backup','김상희','이유빈','Backup SQL / S3 전송'),
          ('On-Prem Recovery','김상희','최유준','로컬 DB/Redis/App / Harbor Pull'),
          ('Backup age 개인 Key','김상희','이유빈','SOPS Identity와 별도 목적')]
    cols=[88,560,820,1080]
    for x,t in zip(cols,['보관 범위','주 보관자','예비 보관자','용도/경계']):c.text(x,617,t,21,'#7461A8',700)
    for i,row in enumerate(rows):
        y=667+i*52
        c.rect(88,y-28,1624,42,'#FFFFFF' if i%2==0 else '#F7F5FD',radius=6)
        for x,t in zip(cols,row):c.text(x+8,y,t,20,INK)
    c.note(980,'복구 가능한 공급 경계','암호문 원본 · 사용 사본 · 독립 오프라인 예비 Key/해제 수단 분리  |  개인 AWS Key/MFA·Root Credential은 공유 Bundle에 넣지 않음',h=94)


def observability(c):
    c.panel(64,206,1672,265,'관측 신호 / 플랫폼·앱·관리형 Data·Backup','neutral')
    for x,title,lines,theme in [
        (88,'ROSA / Native + UWM',['Cluster/Node/Pod · App Metric','기존 App 구조화 Log'],'cloud'),
        (648,'AWS / RDS·ElastiCache',['서비스 Metric · 접속/Failover 신호','수집 경로는 실제 구현 확인'],'data'),
        (1208,'App / Backup 업무',['연결/게임/DB·Redis 오류','Backup 최신성·무결성·완성본'],'local')]:
        c.card(x,276,504,170,title,lines,theme=theme,size=20)
    c.card(64,550,512,166,'수집·알림 → 담당 판단',['Native/UWM · 지원되는 수집 경로','업무 영향·탐지 시각·조치 책임','Probe 정상만으로 업무 정상 판정하지 않음'],theme='cloud',size=20)
    c.card(676,550,490,166,'Run / 관련 담당자',['Requirement · 실행 조합 · Actual','PASS / Partial / Fail / Not Tested','Timeline · 실패/제한 · 재시험 연결'],theme='neutral',size=20)
    c.card(1266,550,470,166,'Evidence Index',['Release / Run ID 연결','Source/Commit · 담당 · 검증 범위','보호 원본의 논리 참조'],theme='local',size=20)
    c.arrow([(576,633),(676,633)],color='#60788E')
    c.arrow([(1166,633),(1266,633)],color='#60788E')
    c.panel(64,776,1672,174,'ROSA 삭제 전에 외부 보존 / 공개 결과와 보호 원본 분리','local')
    c.text(88,861,'Release/Run JSON',24,'#237E70',700)
    c.text(500,861,'Summary/Index Markdown',24,'#237E70',700)
    c.text(1000,861,'Metric/Timeline CSV',24,'#237E70',700)
    c.text(1450,861,'대용량 보호 원본',24,'#237E70',700)
    c.para(88,918,'정리된 결과·비밀값 없는 Metadata만 공개 Docs로 연결 · 실제 Credential/State/Plan/Backup 원본은 공개하지 않음',1624,20)
    c.note(980,'기존 On-Prem 관측 기반 보존','새 Cloud Grafana/Loki/외부 APM을 기본 구성에 추가하지 않음 · AWS Metric을 UWM이 직접 모두 수집한다고 단정하지 않음',h=94)


def recovery(c):
    c.panel(64,206,1672,355,'정상 시 / 운영 중 1시간 Backup · 일반 7일 보존 · 마지막 검증본 보호','local')
    nodes=[(88,358,'Data 작업 VM',['VPN/TLS → RDS 논리 덤프','압축 → age 암호화']),
           (536,500,'S3 / Public HTTPS',['제한된 전송 인증으로 업로드','로컬 다운로드·Hash/완성본 확인']),
           (1126,586,'로컬 검증 Backup',['장애 전 동기화 · 시점/무결성/완성본','Recovery Storage 장애 영역 확인'])]
    for x,w,title,lines in nodes:c.card(x,284,w,155,title,lines,theme='local',size=20)
    c.arrow([(446,360),(536,360)],color='#237E70')
    c.arrow([(1036,360),(1126,360)],color='#237E70')
    c.para(88,488,'별도 사전 준비: Harbor 승인 Image · 보존 Manifest/Bundle · 도구/CA · Key/독립 예비본',1624,21)
    c.para(88,531,'RDS PITR은 Portable Backup과 다른 복구 경로 · 실제 독립 저장 장애 영역 확인',1624,21)
    c.panel(64,597,1672,352,'AWS 접속 불가 시 / 로컬 보존본으로 Restore-based Recovery','recovery')
    for x,w,title,lines in [
        (88,464,'검증 Backup 선택 / 해독',['사전 로컬 Backup · 별도 age 개인 Key','사용할 완성본·시점·호환 도구 확인']),
        (668,464,'새 전용 MariaDB VM',['격리 DB 복원 · 직접 TLS','Data 작업 VM / 기존 1차 DB와 별도']),
        (1248,464,'로컬 복구 Namespace',['새 Redis · 별도 Secret · Harbor Pull','Ansible 보존본 Apply → 사용자 안내'])]:
        c.card(x,675,w,158,title,lines,theme='recovery',size=20)
    c.arrow([(552,753),(668,753)],color='#B97428')
    c.arrow([(1132,753),(1248,753)],color='#B97428')
    c.para(88,900,'대표 업무/영속 데이터 확인 · 재로그인/새 게임 · 진행 상태 중단 · 사용자 Host 안내/재접속도 복구 시간에 포함',1624,21)
    c.note(980,'시험 목표 / 아직 달성값 아님','RTO 30분 · RPO 90분  |  장애 후 AWS/S3/GitHub/Cloud IDP/ECR/KMS 신규 조회를 필수 단계로 두지 않음 · 1차 DB/MaxScale/Redis 보존',h=94)


def failure(c):
    c.panel(64,206,1020,748,'Cloud / 기본 HA와 App 정합성의 차이','cloud')
    rows=[('Pod / Worker / AZ','ROSA 재배치·다중 Replica → Client 재접속/현재 상태 확인'),
          ('RDS Primary','Multi-AZ 동기 Standby → 접속/미확정 업무 결과 확인'),
          ('Redis Primary','비동기 Replica Failover → 최신 상태 소실/정합성 확인'),
          ('Redis 전체 Runtime 소실','완료 DB 기록 보존 → 진행 중단·새 로그인/게임'),
          ('잘못된 배포 / 데이터 손상','호환 Release·DB 복원 판단 → Schema/쓰기 영향 검증')]
    for i,(title,body) in enumerate(rows):
        c.card(88,278+i*129,972,107,title,[body],theme='cloud' if i<3 else 'data',size=20)
    c.panel(1124,206,612,748,'운영/복구 / 별도 장애 영역','local')
    c.card(1148,278,564,158,'단일 VPN Gateway 상실',['정상 Cloud 사용자 경로는 VPN 비의존','RDS 작업·Backup 경로 영향','자동 AZ Failover 아님 · 수동 재구축'],theme='local',size=20)
    c.card(1148,474,564,158,'On-Prem 전체 상실',['기존 Cloud Runtime과 신규 CI/Backup 영향 구분','Jenkins/Harbor/Storage/Key 장애 영역 확인','새 배포·복구 준비를 계속 가능하다고 단정하지 않음'],theme='local',size=20)
    c.card(1148,670,564,252,'Cloud 접근 불가 / Restore',['로컬 사전 보존본으로 복구','새 전용 DB VM · 새 Redis · App','RTO/RPO는 Run으로 측정','Multi-AZ/PDB = 전체 무중단 보장 아님'],theme='recovery',size=20)
    c.note(986,'허용 시험과 증거','Managed Control Plane EC2 강제종료·etcd 직접 수정은 기본 시험에서 제외 · 실제 탐지/서비스 영향/복구/재시험으로 범위를 판정',h=88)


def migration(c):
    c.panel(64,206,1672,604,'1차 실제 기준 → 2차 목표 역할 / 완료한 Migration으로 표시하지 않음','neutral')
    headers=[(88,'1차 / 최신 검증 상태'),(664,'판정 방향'),(1142,'2차 / 승인된 목표')]
    for x,t in headers:c.text(x,293,t,24,MUTED,700)
    rows=[('kubeadm / Calico / Gateway','Replatform / Replace','ROSA Classic · Route · 플랫폼 Network'),
          ('MariaDB / MaxScale','영속 역할 이전 / Replace','RDS MariaDB · 격리 논리 이전'),
          ('Redis / 공유 Runtime','Replace / 새 Runtime','ElastiCache Redis OSS · 새 Recovery Redis'),
          ('Jenkins / Harbor','Retain / Registry 역할 분담','On-Prem CI · ECR Cloud / Harbor Recovery'),
          ('Argo / Ansible / NFS·관측','역할별 유지·분리 / 개별 판정 대기','GitOps / Infra / Backup·Evidence 경계')]
    for i,(left,decision,right) in enumerate(rows):
        y=354+i*85
        c.rect(88,y-31,1624,68,'#FFFFFF' if i%2==0 else '#F7F9FB',radius=8)
        c.text(104,y,left,22,INK)
        c.text(680,y,decision,21,'#237E70')
        c.text(1158,y,right,21,INK)
        c.arrow([(606,y-6),(650,y-6)],color='#60788E')
        c.arrow([(1084,y-6),(1128,y-6)],color='#60788E')
    c.para(88,778,'기존 16 VM/실제 Source 기준 · 18 VM 계획·ANALYSIS·추가 LB/MaxScale를 가져오지 않음 · 1차 자산과 History 보존',1624,20)
    for x,w,title,lines in [
        (64,480,'Seed 확정 / 격리 예행',['최신 검증 Commit·미반영 변경 기록','DB 이전 · 새 Redis/Release 기능 확인']),
        (660,480,'쓰기 제한 / 최종 복사',['진행 작업 종료·최종 Backup 확인','전환 전 Data/App 검증']),
        (1256,480,'전환 / 되돌림 판단',['실제 증거·사용자 안내·업무 재개 Gate','Cloud 쓰기 후 DNS 되돌림 ≠ Data 복구'])]:
        c.card(x,850,w,162,title,lines,theme='local',size=20)
    c.arrow([(544,931),(660,931)],color='#237E70')
    c.arrow([(1140,931),(1256,931)],color='#237E70')
    c.text(64,1055,'개별 자원의 Retire/완료 판정은 실제 Migration Matrix와 Source를 확인한 뒤 기록',21,MUTED)


BUILDERS={1:logical,2:physical,3:hybrid,4:traffic,5:state,6:release,7:ownership,
          8:identity,9:observability,10:recovery,11:failure,12:migration}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--font',required=True,type=Path)
    p.add_argument('--only',nargs='+',type=int,default=list(BUILDERS))
    p.add_argument('--render',action='store_true')
    args=p.parse_args()
    for name in ['diagrams','exports']:
        (ROOT/name).mkdir(exist_ok=True)
    audits=[]
    for n in args.only:
        c=Canvas(n,args.font,1400 if n==2 else 1200)
        BUILDERS[n](c); audits.append(c.finish())
        if args.render:
            dest=ROOT/'exports'/f'{c.meta[0]}.png'
            temporary=dest.with_suffix('.render.png')
            for attempt in range(2):
                subprocess.run(['inkscape',str(ROOT/'diagrams'/f'{c.meta[0]}.svg'),
                    '--export-type=png',f'--export-filename={temporary}',
                    '--export-width=3600'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                try:
                    with Image.open(temporary) as im:
                        im.load()
                        if im.size != (3600, c.h*2):
                            raise ValueError('Incorrect PNG size')
                    temporary.replace(dest)
                    break
                except OSError:
                    if attempt == 1:
                        raise
    qa=ROOT/'tools/layout-audit.json'
    old=json.loads(qa.read_text()) if qa.exists() else []
    combined={a['id']:a for a in old}
    combined.update({a['id']:a for a in audits})
    qa.write_text(json.dumps([combined[k] for k in sorted(combined)],ensure_ascii=False,indent=2)+'\n')
    print(f'Built {len(audits)} diagrams with editable text and embedded font.')


if __name__=='__main__':
    main()
