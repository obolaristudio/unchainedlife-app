import json,re,html,sys,os,subprocess
d=sys.argv[1]; os.chdir(d); C=json.load(open('cfg.json'))
W=json.load(open('vwords.json')); T=C['T']
rep=C.get('rep',{}); merge=C.get('merge',[])
words=[];i=0
while i<len(W):
    done=False
    for m in merge:  # m = [list_of_raw_tokens_prefix_joined, replacement, count]
        n=m[2]; toks=''.join(x['w'] for x in W[i:i+n])
        if toks==m[0]:
            tail=W[i+n-1]['w'][-1] if W[i+n-1]['w'][-1] in ',.?!:' else ''
            words.append({'w':m[1]+('' if m[1].endswith(tail) else tail),'s':W[i]['s']}); i+=n; done=True; break
    if done: continue
    t=W[i]['w']; core=re.sub(r'[,.?!:]$','',t); p=t[len(core):]
    words.append({'w':rep.get(core,core)+p,'s':W[i]['s']}); i+=1
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY=set(k.lower() for k in C['key'])
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if re.sub(r"[,.?!:]$","",w["w"]).lower() in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
body=[]
for k,(a,b,inner) in enumerate(C['hd']):
    body.append(f'<div id="h{k}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>')
    js.append(f'tl.fromTo("#h{k}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{a});' if k else f'tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);')
for k,o in enumerate(C['ov']):
    a,b,top,items=o['a'],o['b'],o.get('top',1200),o['items']
    inner=''.join(f'<span class="pill{" v" if it[1].startswith("!") else ""}" id="o{k}_{j}">{it[1].lstrip("!")}</span>' for j,it in enumerate(items))
    body.append(f'<div id="o{k}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="top:{top}px"><div class="chips">{inner}</div></div>')
    for j,it in enumerate(items): js.append(f'tl.fromTo("#o{k}_{j}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{it[0]});')
for k,s in enumerate(C.get('stamps',[])):
    body.append(f'<div id="st{k}" class="clip stamp" data-start="{s["a"]}" data-duration="{s["d"]}"><span class="{s.get("cls","")}">{s["html"]}</span></div>')
    js.append(f'tl.fromTo("#st{k} span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{s["a"]+0.05});')
    js.append(f'tl.fromTo("#flash",{{opacity:0.8}},{{opacity:0,duration:0.3}},{s["a"]});')
    js.append(f'tl.fromTo("#bg",{{x:0}},{{x:-30,duration:0.05,yoyo:true,repeat:5}},{s["a"]});')
    if s.get('gray'):
        js.append(f'tl.fromTo("#bg",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.6)",duration:0.15}},{s["a"]});')
        js.append(f'tl.to("#bg",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{s["a"]+s["d"]});')
for k,c in enumerate(C.get('counters',[])):
    body.append(f'<div id="ct{k}" class="clip ov" data-start="{c["a"]}" data-duration="{c["d"]}" style="top:{c.get("top",1150)}px"><div class="big"><span id="n{k}">0</span>{c.get("suffix","")}</div><span class="pill">{c["label"]}</span></div>')
    js.append(f'tl.fromTo("#ct{k} .big",{{scale:2.2,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},{c["a"]});')
    js.append(f'tl.fromTo("#n{k}",{{textContent:0}},{{textContent:{c["to"]},duration:1.0,ease:"power2.out",snap:{{textContent:1}}}},{c["a"]+0.1});')
for k,e in enumerate(C.get('drops',[])):  # surprise: big emoji falls from top
    body.append(f'<div id="dr{k}" class="clip drop" data-start="{e["a"]}" data-duration="{e["d"]}">{e["emoji"]}</div>')
    js.append(f'tl.fromTo("#dr{k}",{{y:-900,rotation:-40}},{{y:0,rotation:0,duration:0.45,ease:"bounce.out"}},{e["a"]});')
    js.append(f'tl.fromTo("#bg",{{y:0}},{{y:18,duration:0.05,yoyo:true,repeat:3}},{e["a"]+0.4});')
for t in C.get('flips',[]):
    js.append(f'tl.to("#bg",{{scaleX:-1,duration:0.35,ease:"power2.inOut"}},{t});tl.to("#bg",{{scaleX:1,duration:0.35,ease:"power2.inOut"}},{t+1.4});')
S=json.load(open('scenes.json'))
for s_ in S[1:]: js.append(f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});')
# punch-in zoom on scene entries
for s_ in S: js.append(f'tl.fromTo("#bg",{{scale:1.12}},{{scale:1.0,duration:0.5,ease:"power3.out"}},{s_[0]});')
ca=C['cta_at']
body.append(f'<div id="cta" class="clip" data-start="{ca}" data-duration="{round(T-ca,2)}"><span>{C["cta"]}</span></div>')
js.append(f'tl.fromTo("#cta span",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"}},{ca});tl.to("#cta span",{{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{ca+0.5});')
css=open(os.path.join(os.path.dirname(__file__),'style.css')).read()
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{chr(10).join(body)}
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {C["serie"]}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
os.makedirs('hf/assets/fonts',exist_ok=True)
open('hf/index.html','w').write(H)
json.dump(groups,open('groups.json','w'),ensure_ascii=False)
print('html ok',len(groups),'groups')
