"""Build editable draw.io XML and a shared layout for the PNG renderer.

Run from repository root: python final-exam/scripts/build-diagrams.py
Then: pwsh -File final-exam/scripts/render-diagrams.ps1
Only Python standard library is required. Coordinates/text have one source.
"""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parents[1] / 'diagrams'
OUT.mkdir(exist_ok=True)

def box(id, x, y, w, h, text, kind='core'):
    return dict(id=id, x=x, y=y, w=w, h=h, text=text, kind=kind)

def edge(id, source, target, points, text, label, dashed=False):
    return dict(id=id, source=source, target=target, points=points,
                text=text, label=label, dashed=dashed)

models = {
 'context-after': dict(width=1600, height=1000,
  title='System Context after CR-FX-01',
  subtitle='Case 03 | CR-FX-02B selected | Design Draft / Proposed | CRs Pending',
  footer='Solid: proposed first release   |   Dashed: Overview / TBD; external delivery Later   |   No hardware or payment integration',
  boxes=[
   box('ACT-01',50,160,280,160,'ACT-01  Resident\n[Person / Core]\nView status; book queue\nChoose external opt-in','actor'),
   box('ACT-02',50,440,280,160,'ACT-02  Dorm Admin\n[Person / Core]\nOpen / close machines\nReview faults; read audit','actor'),
   box('ACT-03',50,720,280,150,'ACT-03  Maid\n[Person / Core]\nRecord relocated laundry\nDetail after 02B: Overview','actor'),
   box('SYS-01',620,340,400,290,'SYS-01\nDorm Laundry Queue and Status\n[Software System / Core]\nQueue and machine status\nStored private notice history\nTimed reminders; audit read'),
   box('EXT-01',1260,400,290,200,'EXT-01\nExternal Notification Channel\n[External System]\nExtension / TBD\nActual delivery: Later','external')],
  edges=[
   edge('E1','ACT-01','SYS-01',[[330,240],[500,240],[500,400],[620,400]],'Queue actions; opt-in\nStatus; private notifications',[350,135,260,65]),
   edge('E2','ACT-02','SYS-01',[[330,520],[620,520]],'Machine actions; audit query\nStatus / audit results',[345,440,260,65]),
   edge('E3','ACT-03','SYS-01',[[330,795],[500,795],[500,580],[620,580]],'Relocation data / result\nOverview after 02B',[350,815,270,65],True),
   edge('E4','SYS-01','EXT-01',[[1020,500],[1260,500]],'Minimal message / outcome\nInterface TBD: DD-FX-01',[1030,270,260,90],True)]),
 'container-after': dict(width=2120,height=1120,
  title='Containers after CR-FX-01',
  subtitle='Case 03 | Proposed first release under CR-FX-02B | Reference stack | CRs Pending',
  footer='Rules and authorization: API Application   |   No direct browser/job access to Database   |   External integration: Overview; delivery Later',
  boundary=[360,140,1360,860],
  boxes=[
   box('ACT-01',30,180,250,145,'ACT-01  Resident\n[Person / Core]\nQueue; status; opt-in','actor'),
   box('ACT-02',30,440,250,145,'ACT-02  Dorm Admin\n[Person / Core]\nMachine actions; read audit','actor'),
   box('ACT-03',30,730,250,145,'ACT-03  Maid\n[Person / Core]\nRelocation: Overview','actor'),
   box('C1',400,370,300,240,'C1  Web App\n[Browser Web App / React]\nMobile-first queue views\nPrivate notification history\nSimple audit view (authorized)\nOpt-in; runs in user browser'),
   box('C2',870,370,330,240,'C2  API Application\n[Server API / Node.js + Express]\nIdentity; role; ownership\nQueue rules; opt-in; recipients\nCreate notices while web closed\nState + audit: one transaction\nAudit failure: rollback; no success\nAudit read: BR-FX-02; team server'),
   box('C3',1360,370,320,240,'C3  Database\n[Database / PostgreSQL]\nQueue; machine status\nPreferences; notice history\nAudit (DR-FX-02); job results\nState + audit: commit / rollback\nTeam-controlled DB server'),
   box('C4',870,770,330,180,'C4  Scheduled Job\n[Scheduled Job / Node.js]\nTrigger due-work evaluation\nTeam server; browser-independent\nSchedule / restart: DD-FX-04'),
   box('EXT-01',1770,770,320,180,'EXT-01\nExternal Notification Channel\n[External System / Tech TBD]\nExtension / TBD: DD-FX-01\nActual delivery: Later','external')],
  edges=[
   edge('E1','ACT-01','C1',[[280,252],[335,252],[335,425],[400,425]],'Queue / opt-in; status\nBrowser interaction',[30,110,300,60]),
   edge('E2','ACT-02','C1',[[280,512],[400,512]],'Actions / audit query + results\nBrowser interaction',[20,610,300,65]),
   edge('E3','ACT-03','C1',[[280,802],[335,802],[335,555],[400,555]],'Relocation / result\nBrowser; Overview',[25,895,310,65],True),
   edge('E4','C1','C2',[[700,490],[870,490]],'Actions; notices; audit read\nProtocol TBD\nDD-G4-01',[700,260,200,95]),
   edge('E5','C2','C3',[[1200,490],[1360,490]],'State + audit transaction\nRollback if audit fails\nSQL; DEC-FX-01',[1195,260,200,95]),
   edge('E6','C4','C2',[[1035,770],[1035,610]],'Due-work request / result\nInternal interface TBD\nDD-G4-01 / DD-FX-04',[775,645,280,90]),
   edge('E7','C2','EXT-01',[[1200,555],[1280,555],[1280,860],[1770,860]],'Minimal message / outcome\nProtocol TBD: DD-FX-01\nCheck opt-in at API',[1750,650,340,90],True)])
}

for name, m in models.items():
    mx = ET.Element('mxfile', host='app.diagrams.net', type='device')
    diagram = ET.SubElement(mx, 'diagram', id=name, name=name)
    graph = ET.SubElement(diagram, 'mxGraphModel', dx=str(m['width']), dy=str(m['height']),
        grid='1', gridSize='10', page='1', pageScale='1',
        pageWidth=str(m['width']), pageHeight=str(m['height']), math='0', shadow='0')
    root = ET.SubElement(graph, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    def vertex(id, text, xywh, style):
        cell=ET.SubElement(root,'mxCell',id=id,value=text,style=style,vertex='1',parent='1')
        x,y,w,h=xywh
        ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    vertex('title',m['title'],[30,20,m['width']-60,45],
        'text;html=0;align=left;fontSize=32;fontStyle=1;')
    vertex('subtitle',m['subtitle'],[30,70,m['width']-60,32],
        'text;html=0;align=left;fontSize=18;')
    vertex('footer',m['footer'],[30,m['height']-70,m['width']-60,50],
        'text;html=0;align=left;fontSize=17;')
    if 'boundary' in m:
        vertex('boundary','SYS-01  Dorm Laundry Queue and Status | Team responsibility',m['boundary'],
                'rounded=0;whiteSpace=wrap;html=0;fillColor=none;strokeColor=#94a3b8;dashed=1;verticalAlign=top;align=left;spacing=12;fontSize=18;')
    boxes={b['id']: b for b in m['boxes']}
    for b in m['boxes']:
        fill,stroke={'actor':('#e2e8f0','#64748b'), 'core':('#dbeafe','#2563eb'),
                     'external':('#fff7ed','#c2410c')}[b['kind']]
        vertex(b['id'],b['text'],[b['x'],b['y'],b['w'],b['h']],
            f'rounded=0;whiteSpace=wrap;html=0;fillColor={fill};strokeColor={stroke};strokeWidth=2;fontColor=#0f172a;fontSize=18;align=center;verticalAlign=middle;'+('dashed=1;' if b['kind']=='external' else ''))
    for e in m['edges']:
        src,tgt=boxes[e['source']],boxes[e['target']]
        p0,p1=e['points'][0],e['points'][-1]
        coords=f"exitX={(p0[0]-src['x'])/src['w']};exitY={(p0[1]-src['y'])/src['h']};entryX={(p1[0]-tgt['x'])/tgt['w']};entryY={(p1[1]-tgt['y'])/tgt['h']};"
        cell=ET.SubElement(root,'mxCell',id=e['id'],value='',edge='1',parent='1',source=e['source'],target=e['target'],
            style='edgeStyle=none;html=0;startArrow=classic;endArrow=classic;strokeColor=#475569;strokeWidth=2;'+coords+('dashed=1;' if e['dashed'] else ''))
        geom=ET.SubElement(cell,'mxGeometry',relative='1',attrib={'as':'geometry'})
        if len(e['points'])>2:
            arr=ET.SubElement(geom,'Array',attrib={'as':'points'})
            for x,y in e['points'][1:-1]:
                ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
        # Connected label is an editable relative edge child, positioned to match PNG.
        lx,ly,lw,lh=e['label']; midx=(p0[0]+p1[0])/2; midy=(p0[1]+p1[1])/2
        label=ET.SubElement(root,'mxCell',id=e['id']+'-label',value=e['text'],vertex='1',parent=e['id'],
            style='edgeLabel;html=0;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=17;fillColor=#ffffff;resizable=1;')
        lg=ET.SubElement(label,'mxGeometry',x='0',y='0',width=str(lw),height=str(lh),relative='1',attrib={'as':'geometry'})
        # Arc length midpoint is how mxGraph places x=0 on an edge.
        import math
        seg=[math.dist(a,b) for a,b in zip(e['points'],e['points'][1:])]
        remaining=sum(seg)/2
        for i, length in enumerate(seg):
            if remaining<=length:
                a,b=e['points'][i:i+2]; ratio=remaining/length
                midx=a[0]+ratio*(b[0]-a[0]); midy=a[1]+ratio*(b[1]-a[1]); break
            remaining-=length
        ET.SubElement(lg,'mxPoint',x=str(lx+lw/2-midx),y=str(ly+lh/2-midy),attrib={'as':'offset'})
    ET.indent(mx)
    ET.ElementTree(mx).write(OUT/(name+'.drawio'),encoding='utf-8',xml_declaration=True)
    (OUT/(name+'.layout.json')).write_text(json.dumps(m,indent=2),encoding='utf-8')
    print(f'Created {name}.drawio and shared layout')
