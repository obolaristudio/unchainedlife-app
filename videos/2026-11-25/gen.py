import json,re,html,sys,importlib
d=sys.argv[1]; S=importlib.import_module('spec_'+d)
W=json.load(open(f'{d}/words.json')); T=S.T
words=[]
for w in W:
    t=S.REP.get(w['w'],w['w'])
    if t: words.append({'w':t,'s':float(w['s'])})
for seq,rep in getattr(S,'SEQ',[]):
    for i in range(len(words)-len(seq)+1):
        if [x['w'] for x in words[i:i+len(seq)]]==seq:
            ss=[x['s'] for x in words[i:i+len(seq)]]; words[i:i+len(seq)]=[{'w':r,'s':(ss[k] if k<len(ss) else ss[-1]+0.08*(k-len(ss)+1))} for k,r in enumerate(rep)]; break
# merge "anti -doping"
mw=[]
for w in words:
    if mw and w['w'].startswith('-'): mw[-1]['w']+=w['w']
    else: mw.append(w)
words=mw
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
def norm(x): return re.sub(r'[^\wÀ-ú$-]','',x).lower()
KEY={norm(k) for k in S.KEY}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.05
    b=max(b,a+0.1)
    spans=''.join(f'<span class="{"k" if norm(w["w"]) in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.3,y:8,backgroundColor:"rgba(203,239,75,0)"}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
HD=''.join(f'<div id="{i}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{h}</div>' for i,a,b,h in S.HEADERS)
OV='\n'.join(f'<div id="{i}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="{st}">{h}</div>' for i,a,b,st,h in S.OVERLAYS)
CSS=open('style.css').read()
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{HD}
{OV}
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {S.TAG}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
'''
for i,a,b,h in S.HEADERS:
    H+=f'tl.fromTo("#{i}",{{y:40,opacity:0,scale:1.15}},{{y:0,opacity:1,scale:1,duration:0.32,ease:"power3.out"}},{a});\n'
for sc in json.load(open(f'{d}/scenes.json'))[1:]:
    H+=f'tl.fromTo("#bg",{{scale:1.12,filter:"blur(6px)"}},{{scale:1,filter:"blur(0px)",duration:0.35,ease:"power2.out"}},{sc[0]});\n'
for i,t in S.SLIDES: H+=f'tl.fromTo("{i}",{{opacity:0,x:220}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
for i,t in S.POPS: H+=f'tl.fromTo("{i}",{{opacity:0,scale:0}},{{opacity:1,scale:1,duration:0.35,ease:"back.out(2.6)"}},{t});\n'
for t in S.PUNCH: H+=f'tl.fromTo("#bg",{{scale:1.09}},{{scale:1,duration:0.4,ease:"power2.out"}},{t});\n'
H+=S.JS+'\n'+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open(f'{d}/hf/index.html','w').write(H);print('ok',d,len(groups))
