import json,re,html,subprocess,sys,os
cfg=__import__(sys.argv[1])
D=cfg.D; os.makedirs(f'{D}/hf/assets',exist_ok=True)
STOCK=os.path.dirname(os.path.abspath(__file__))+'/stock'
W=json.load(open(f'{D}/words.json'))
T=round(W[-1]['e']+1.6,2)
# ---------- background
if 'bg' in sys.argv:
    PW,PH=1080,1100
    for i,(a,b,c,off) in enumerate(cfg.SCENES):
        b=T if b is None else b; d=round(b-a,3); src=f'{STOCK}/{c}.mp4'
        w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(','))
        dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
        off=min(off,max(0,dur-d-0.1)); loop=['-stream_loop','-1'] if dur<d+off else []
        cw=round(h*PW/PH)
        if cw>w: panel=f'scale={PW}:-2,crop={PW}:{PH}'
        else: panel=f'crop={cw}:{h}:(iw-{cw})/2:0,scale={PW}:{PH}:flags=lanczos'
        # slow zoom drift + entry zoom
        z=f"zoompan=z='min(1.0+0.0009*on+0.18*max(0\\,1-on/9),1.4)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={PW}x{PH}:fps=30"
        fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},{z},eq=saturation=1.05:contrast=1.03,setsar=1[p];"
            f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.25:saturation=0.7,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
        subprocess.run(['ffmpeg','-loglevel','error','-y',*loop,'-ss',str(off),'-t',str(d),'-i',src,'-filter_complex',fc,'-an','-r','30','-c:v','libx264','-crf','17','-preset','veryfast',f'{D}/sc_{i:02d}.mp4'],check=True)
    open(f'{D}/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(cfg.SCENES))))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',f'{D}/list.txt','-c','copy',f'{D}/hf/assets/bg.mp4'],check=True)
    print('bg ok')
# ---------- captions
words=[]
SK=getattr(cfg,'SKIP',[])
for i,w in enumerate(W):
    if any(i>0 and i+1<len(W) and W[i-1]['w']==a and w['w']==b and W[i+1]['w']==c for a,b,c in SK): continue
    t=cfg.REP.get(w['w'],w['w']); words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
def norm(x): return re.sub(r'[^\wÀ-ÿ]','',x.lower())
KEY={norm(k) for k in cfg.KEY}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if norm(w["w"]) in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{max(0.1,b-a):.2f}"><div class="capbox">{spans}</div></div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{backgroundColor:"rgba(203,239,75,0)"}},{{backgroundColor:"#CBEF4B",duration:0.06}},{w["s"]:.2f});tl.to("#c{gi}_{j}",{{backgroundColor:"rgba(203,239,75,0)",duration:0.06}},{(g[j+1]["s"] if j+1<len(g) else b):.2f});')
def tm(x): return T if x is None else x
hds=''.join(f'<div id="h{i}" class="clip hd" data-start="{a}" data-duration="{round(tm(b)-a,2)}">{inner}</div>' for i,(a,b,inner) in enumerate(cfg.HEADS))
ovs=''.join(f'<div id="o{i}" class="clip ov" data-start="{a}" data-duration="{round(tm(b)-a,2)}" style="top:{top}px">{inner}</div>' for i,(a,b,top,inner) in enumerate(cfg.OVS))
st=cfg.STAMP
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script><style>
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#F2EFE6}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Inter",sans-serif;color:#141414;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#top{{position:absolute;z-index:9;top:0;left:0;right:0;height:120px;background:#2B2B2B;display:flex;align-items:center;justify-content:space-between;padding:40px 70px 0;font-family:"DejaVu Sans Mono",monospace;font-size:24px;letter-spacing:4px;color:#F2EFE6}}
#top .d{{display:inline-block;width:16px;height:16px;border-radius:50%;background:#CBEF4B;margin-right:12px}} #top .c{{color:#CBEF4B}}
#paper{{position:absolute;z-index:2;left:0;right:0;top:120px;height:300px;background:#F2EFE6;background-image:linear-gradient(#E6E3DA 2px,transparent 2px),linear-gradient(90deg,#E6E3DA 2px,transparent 2px);background-size:44px 44px;border-bottom:4px solid #141414}}
#paper:before{{content:"";position:absolute;left:70px;top:0;bottom:0;width:3px;background:#D9503F}}
#paperb{{position:absolute;z-index:2;left:0;right:0;top:1520px;bottom:0;background:#F2EFE6;background-image:linear-gradient(#E6E3DA 2px,transparent 2px),linear-gradient(90deg,#E6E3DA 2px,transparent 2px);background-size:44px 44px;border-top:4px solid #141414}}
.hd{{position:absolute;z-index:6;left:90px;right:50px;top:135px;height:275px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-family:"DejaVu Sans Mono",monospace;font-weight:700;font-size:28px;letter-spacing:4px;background:#CBEF4B;border:3px solid #141414;padding:4px 14px;margin-bottom:14px;box-shadow:5px 5px 0 #141414}}
.hd .m{{font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-2px}}
.hd .m span{{background:#CBEF4B;border:4px solid #141414;padding:0 12px;box-shadow:7px 7px 0 #141414;display:inline-block;margin:4px 0}}
.cap{{position:absolute;z-index:7;left:60px;right:60px;top:1560px;text-align:center}}
.capbox{{display:inline-block;background:#FBFAF6;border:4px solid #141414;box-shadow:8px 8px 0 #141414;border-radius:14px;padding:14px 22px;font-weight:900;font-size:58px;line-height:1.15;letter-spacing:-1px}}
.capbox span{{padding:0 6px;border-radius:8px}} .capbox .k{{color:#3D7BFF}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;text-align:center}}
.pill{{display:inline-block;background:#FBFAF6;border:4px solid #141414;box-shadow:7px 7px 0 #141414;font-weight:800;font-size:46px;padding:12px 26px;border-radius:16px;margin:8px 0}}
.pill b{{background:#CBEF4B;padding:0 8px}} .pill.r{{background:#F3D3CD}} .pill.r b{{background:none;color:#D9503F}}
.big{{display:inline-block;font-weight:900;font-size:190px;line-height:1;background:#CBEF4B;border:6px solid #141414;box-shadow:12px 12px 0 #141414;padding:0 40px;border-radius:24px}}
.beads{{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;background:rgba(251,250,246,.95);border:4px solid #141414;box-shadow:8px 8px 0 #141414;padding:18px;border-radius:22px;max-width:900px;margin:0 auto}} .beads i{{display:block;width:58px;height:58px;border-radius:50%;border:3px solid #141414}}
.flags{{display:flex;gap:0;justify-content:center}} .flags>div{{background:#FBFAF6;border:4px solid #141414;box-shadow:8px 8px 0 #141414;padding:18px 26px;font-weight:800;font-size:40px;width:460px;text-align:left}} .flags>div+div{{border-left:4px dashed #141414}}
.flags small{{display:block;font-family:"DejaVu Sans Mono",monospace;font-size:26px;letter-spacing:3px;margin-bottom:6px}}
#stamp{{position:absolute;z-index:8;left:0;right:0;top:820px;text-align:center}}
#stamp span{{display:inline-block;background:#CBEF4B;border:8px solid #141414;font-weight:900;font-size:120px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:16px 16px 0 #141414}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1180px;text-align:center}}
#cta span{{display:inline-block;background:#141414;color:#CBEF4B;font-weight:900;font-size:60px;padding:18px 40px;border-radius:60px;border:4px solid #CBEF4B}}
#foot{{position:absolute;z-index:9;top:1845px;left:0;right:0;text-align:center;font-family:"DejaVu Sans Mono",monospace;font-size:20px;letter-spacing:2px;color:#555}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="paper" class="clip" data-start="0" data-duration="{T}"></div><div id="paperb" class="clip" data-start="0" data-duration="{T}"></div>
{hds}{ovs}
<div id="stamp" class="clip" data-start="{st[0]}" data-duration="{st[1]}"><span>{st[2]}</span></div>
<div id="cta" class="clip" data-start="{cfg.CTA}" data-duration="{round(T-cfg.CTA,2)}"><span>💬 Qual peptídeo no próximo?</span><div style="margin-top:26px"><span style="font-size:36px;padding:10px 28px">@obolari_academy</span></div></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="top" class="clip" data-start="0" data-duration="{T}"><div><span class="d"></span>OBOLARI ACADEMY</div><div class="c">PEPTÍDEOS · {cfg.SERIE}</div></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA NEM SUGESTÃO DE USO</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#flash",{{opacity:0.7}},{{opacity:0,duration:0.3}},0);
'''
for i,(a,b,inner) in enumerate(cfg.HEADS):
    H+=f'tl.fromTo("#h{i}",{{y:40,opacity:0,scale:1.25}},{{y:0,opacity:1,scale:1,duration:0.35,ease:"back.out(1.8)"}},{a});\n'
for i,(a,b,top,inner) in enumerate(cfg.OVS):
    H+=f'tl.fromTo("#o{i}",{{opacity:0,x:260}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{a});\n'
for s_ in cfg.SCENES[1:]:
    H+=f'tl.fromTo("#flash",{{opacity:0.18}},{{opacity:0,duration:0.15}},{s_[0]});\n'
for sel,t,kind in cfg.ANIMS:
    if kind=='pop': H+=f'tl.fromTo("{sel}",{{scale:0}},{{scale:1,duration:0.22,ease:"back.out(3)"}},{t});\n'
    if kind=='drop': H+=f'tl.fromTo("{sel}",{{y:-700,opacity:0}},{{y:0,opacity:1,duration:0.6,ease:"bounce.out"}},{t});\n'
    if kind=='count': H+=f'(function(){{const o={{v:0}};const el=document.querySelector("{sel}");tl.to(o,{{v:+el.dataset.to,duration:1.0,ease:"power2.out",onUpdate:()=>{{el.textContent=Math.round(o.v)+(el.dataset.suf||"")}}}},{t});}})();\n'
H+=f'''tl.fromTo("#bg",{{x:0}},{{x:-28,duration:0.05,yoyo:true,repeat:5}},{st[0]});
tl.fromTo("#bg",{{filter:"grayscale(0)"}},{{filter:"grayscale(1)",duration:0.12}},{st[0]});
tl.to("#bg",{{filter:"grayscale(0)",duration:0.2}},{round(st[0]+st[1],2)});
tl.fromTo("#flash",{{opacity:0.85}},{{opacity:0,duration:0.3}},{st[0]});
tl.fromTo("#stamp span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{st[0]+0.05});
tl.fromTo("#cta span",{{scale:0.5,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)",stagger:0.3}},{cfg.CTA});
'''+'\n'.join(js)+'''
window.__timelines=window.__timelines||{};window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open(f'{D}/hf/index.html','w').write(H);print('html ok',T,len(groups))
json.dump({'T':T,'cuts':[s[0] for s in cfg.SCENES[1:]],'pops':[o[0] for o in cfg.OVS],'impact':[0,st[0]],'ding':cfg.DINGS},open(f'{D}/cues.json','w'))
