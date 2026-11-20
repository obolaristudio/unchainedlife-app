import json,re,html,subprocess,sys,os,importlib.util
d=sys.argv[1]; spec=importlib.util.spec_from_file_location('cfg',f'{d}/cfg.py'); C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W=json.load(open(f'{d}/vwords.json')); T=C.T
words=[{'w':C.REP.get(w['w'],w['w']),'s':w['s']} for w in W]
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
norm=lambda s:re.sub(r'[^\wÀ-ú%-]','',s).lower()
KEY={norm(k) for k in C.KEY}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.05
    spans=''.join(f'<span class="{"k" if norm(w["w"]) in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{max(0.1,b-a):.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.3,scale:0.92}},{{opacity:1,scale:1,duration:0.1}},{w["s"]:.2f});')
heads=C.HEADS; hs=[h[0] for h in heads]+[T]
body=[]
for i,(t,inner) in enumerate(heads):
    body.append(f'<div id="h{i}" class="clip hd" data-start="{t}" data-duration="{round(hs[i+1]-t,2)}"><div class="m">{inner}</div></div>')
    js.append(f'tl.fromTo("#h{i}",{{y:30,opacity:0,scale:1.15}},{{y:0,opacity:1,scale:1,duration:0.35,ease:"power3.out"}},{t});')
    js.append(f'tl.fromTo("#flash",{{opacity:0.35}},{{opacity:0,duration:0.2}},{t});')
def sec_end(t): return min(x for x in hs if x>t+0.01)
for oi,o in enumerate(C.OVS):
    kind=o['k']; t0=o['t']; end=o.get('end',sec_end(t0)); top=o.get('top',1150); oid=f'o{oi}'
    if kind=='chips':
        items=''.join(f'<span class="pill {"v" if "v" in it[2:] else ""}" id="{oid}_{j}">{it[1]}</span>' for j,it in enumerate(o['items']))
        body.append(f'<div id="{oid}" class="clip ov" data-start="{t0}" data-duration="{round(end-t0,2)}" style="top:{top}px"><div class="chips">{items}</div></div>')
        for j,it in enumerate(o['items']): js.append(f'tl.fromTo("#{oid}_{j}",{{opacity:0,x:220}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{it[0]});')
    elif kind=='big':
        body.append(f'<div id="{oid}" class="clip ov" data-start="{t0}" data-duration="{round(end-t0,2)}" style="top:{top}px"><div class="big" style="{o.get("st","")}">{o["h"]}</div></div>')
        js.append(f'tl.fromTo("#{oid} .big",{{scale:2.3,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},{t0});')
        js.append(f'tl.fromTo("#flash",{{opacity:0.55}},{{opacity:0,duration:0.25}},{t0});')
    elif kind=='bars':
        mx=max(b[2] for b in o['bars']); rows=''
        for j,(tb,lab,val,txt,col) in enumerate(o['bars']):
            rows+=f'<div class="br" id="{oid}_{j}"><div class="bl">{lab}</div><div class="bt"><div class="bf" id="{oid}_f{j}" style="background:{col};width:{val/mx*100:.0f}%"></div><div class="bv">{txt}</div></div></div>'
            js.append(f'tl.fromTo("#{oid}_{j}",{{opacity:0}},{{opacity:1,duration:0.2}},{tb});tl.fromTo("#{oid}_f{j}",{{scaleX:0}},{{scaleX:1,duration:0.7,ease:"power2.out"}},{tb});')
        body.append(f'<div id="{oid}" class="clip ov" data-start="{t0}" data-duration="{round(end-t0,2)}" style="top:{top}px"><div class="bars"><div class="bh">{o["title"]}</div>{rows}</div></div>')
    elif kind=='count':
        body.append(f'<div id="{oid}" class="clip ov" data-start="{t0}" data-duration="{round(end-t0,2)}" style="top:{top}px"><div class="cnt"><span class="cl">{o["pre"]}</span><span class="big"><span id="{oid}_n">0</span>{o["suf"]}</span></div></div>')
        js.append(f'tl.fromTo("#{oid}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.25}},{t0});tl.fromTo("#{oid}_n",{{textContent:0}},{{textContent:{o["to"]},duration:1.1,ease:"power2.out",snap:{{textContent:1}}}},{t0});')
    elif kind=='stamp':
        body.append(f'<div id="{oid}" class="clip stamp" data-start="{t0}" data-duration="{o.get("dur",1.1)}"><span>{o["h"]}</span></div>')
        js.append(f'tl.fromTo("#{oid} span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{t0});')
        js.append(f'tl.fromTo("#bg",{{x:0}},{{x:-30,duration:0.05,yoyo:true,repeat:5}},{t0});tl.fromTo("#bg",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.55)",duration:0.12}},{t0});tl.to("#bg",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{t0+o.get("dur",1.1)-0.2});tl.fromTo("#flash",{{opacity:0.85}},{{opacity:0,duration:0.3}},{t0});')
    elif kind=='cta':
        body.append(f'<div id="{oid}" class="clip cta" data-start="{t0}" data-duration="{round(T-t0,2)}"><span>{o["h"]}</span><div class="handle">@obolari_academy</div></div>')
        js.append(f'tl.fromTo("#{oid} span",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"}},{t0});tl.to("#{oid} span",{{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{t0+0.5});')
# scene cuts -> flash small + bg punch
for s in C.CUTS[1:]: js.append(f'tl.fromTo("#flash",{{opacity:0.18}},{{opacity:0,duration:0.15}},{s});')
for t in getattr(C,'PUNCH',[]): js.append(f'tl.fromTo("#bg",{{scale:1.09}},{{scale:1,duration:0.4,ease:"power2.out"}},{t});')
H=open(os.path.dirname(__file__)+'/tpl.html').read()
H=H.replace('%T%',str(T)).replace('%TAG%',C.TAG).replace('%BODY%','\n'.join(body+caps)).replace('%JS%','\n'.join(js))
os.makedirs(f'{d}/hf/assets/fonts',exist_ok=True); open(f'{d}/hf/index.html','w').write(H); print('html ok',len(groups),'caps')
