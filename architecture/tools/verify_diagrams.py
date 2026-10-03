#!/usr/bin/env python3
"""Verify design assets and write a source/output provenance manifest.

Checks file integrity and declared geometry; visual and semantic review is
recorded separately in PRODUCTION_REVIEW.md.
"""
import base64
import hashlib
import io
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from PIL import Image
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
NS={'s':'http://www.w3.org/2000/svg'}


def identify(path):
    raw=path.read_bytes()
    return {'path':str(path.relative_to(REPO)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def main():
    baseline=json.loads((REPO/'design/source-manifest.json').read_text())
    for f in baseline['files']:
        actual=identify(REPO/f['path'])
        assert actual['bytes']==f['bytes'] and actual['sha256']==f['sha256'],f['path']
    specs=json.loads((ROOT/'tools/layout-audit.json').read_text())
    assert [s['id'] for s in specs]==[f'{i:02d}' for i in range(1,13)]
    assets=[]
    for spec in specs:
        svg=ROOT/'diagrams'/f'{spec["slug"]}.svg'
        png=ROOT/'exports'/f'{spec["slug"]}.png'
        raw=svg.read_text();xml=ET.fromstring(raw)
        assert xml.get('viewBox')==f'0 0 1800 {spec["height"]}'
        assert xml.find('s:title',NS) is not None and xml.find('s:desc',NS) is not None
        texts=[''.join(t.itertext()) for t in xml.findall('s:text',NS)]
        assert texts==[t['text'] for t in spec['texts']],svg
        assert '설계 목표 · 구현/시험 미확인' in texts
        assert any(t.startswith('근거: ') for t in texts)
        assert any(t.startswith('확인 대기: ') for t in texts)
        assert not xml.findall('s:script',NS) and not xml.findall('s:foreignObject',NS)
        assert not re.search(r'(?:href|src)=[\"\']https?://',raw)
        fontdata=re.search(r'data:font/woff;base64,([A-Za-z0-9+/=]+)',raw).group(1)
        cmap=TTFont(io.BytesIO(base64.b64decode(fontdata))).getBestCmap()
        missing={c for t in texts for c in t if ord(c) not in cmap and not c.isspace()}
        assert not missing,(svg,missing)
        for t in spec['texts']:
            assert 0<=t['x'] and t['x']+t['w']<=1800
            assert t['size']<=t['y']<=spec['height']
        with Image.open(png) as im:
            im.load()
            assert im.size==(3600, spec['height']*2),png
        for pat in [r'AKIA[A-Z0-9]{16}',r'ASIA[A-Z0-9]{16}',r'gh[pousr]_[A-Za-z0-9]{20,}',
                    r'github_pat_[A-Za-z0-9_]{30,}',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']:
            assert not any(re.search(pat,t) for t in texts),(svg,pat)
        assets.append({'id':spec['id'],'title':spec['title'],'status':'DESIGN_TARGET',
                       'source_refs':spec['source_refs'],'pending':spec['pending'],
                       'svg':identify(svg),'png':identify(png),'svg_size':[1800,spec['height']],
                       'png_size':[3600,spec['height']*2],'embedded_font_glyphs_checked':True})
    physical=(ROOT/'diagrams/02-physical-architecture.svg').read_text()
    for i in range(64,73):
        assert f'192.168.{i}.0/24' in physical
    assert len(list((ROOT/'diagrams').glob('*.svg')))==12
    assert len(list((ROOT/'exports').glob('*.png')))==12
    result={'schema_version':1,'created_date':baseline['recorded_date'],'design_basis_date':baseline['source_basis_date'],
            'status':'DESIGN_TARGET','runtime_validation':'NOT_ASSESSED',
            'source_files':[{'path':f['path'],'sha256':f['sha256']} for f in baseline['files']],
            'checks':{'svg_xml':12,'png_decode':12,'embedded_font_glyphs':12,'declared_geometry':12,
                      'approved_subnet_cidrs':9,'source_identity':5,'high_risk_text_pattern_matches':0},
            'diagrams':assets}
    if 'review' in baseline:
        result['source_review']=baseline['review']
    (ROOT/'diagram-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result['checks'],ensure_ascii=False))


if __name__=='__main__':
    main()
