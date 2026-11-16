import json,re,html
def norm(W):
    out=[];i=0
    def core(t): return re.sub(r'[,.?!:]+$','',t)
    def punct(t): return t[len(core(t)):]
    while i<len(W):
        t=W[i]['w'];s=W[i]['s'];n=W[i+1]['w'] if i+1<len(W) else ''
        c,nc=core(t),core(n).lstrip('-')
        if c=='GHK' and nc.upper()=='CU': out.append({'w':'GHK-Cu'+punct(n),'s':s});i+=2;continue
        if c=='BPC' and nc=='157': out.append({'w':'BPC-157'+punct(n),'s':s});i+=2;continue
        if c=='TB' and nc=='500': out.append({'w':'TB-500'+punct(n),'s':s});i+=2;continue
        if c=='Anti' and nc.lower()=='doping': out.append({'w':'antidoping'+punct(n),'s':s});i+=2;continue
        t=t.replace('CLOW','KLOW').replace('Agência','agência').replace('Mundial','mundial')
        out.append({'w':t,'s':s});i+=1
    return out
def captions(words,T,KEY):
    groups=[];cur=[]
    for w in words:
        cur.append(w)
        if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
    if cur: groups.append(cur)
    caps=[];js=[]
    for gi,g in enumerate(groups):
        a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
        spans=''.join(f'<span class="{"k" if re.sub(r"[,.?!:]+$","",w["w"]) in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
        caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
        for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
    return caps,js
