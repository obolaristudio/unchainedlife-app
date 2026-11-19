import json, subprocess, os, re, sys
S = sys.argv[1]
os.chdir(S)
FPS = 30
DUR = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","voz2.wav"]).decode())
END = DUR + 0.6

# (start, src) ; src: "img/NN.png" or "vid/NN.mp4"
cuts = [
 (0.00, "vid/00.mp4"), (3.66, "vid/01.mp4"), (9.68, "img/02.png"), (16.20, "img/03.png"),
 (24.60, "img/04.png"), (33.84, "vid/05.mp4"), (41.32, "img/06.png"), (43.68, "vid/07.mp4"),
 (49.52, "img/08.png"), (56.58, "vid/01.mp4"), (60.24, "img/09.png"), (65.64, "vid/10.mp4"),
 (72.10, "vid/11.mp4"), (75.20, "img/09.png"), (78.30, "vid/00.mp4"), (80.50, "vid/11.mp4"),
 (83.04, "vid/01.mp4"),
]
os.makedirs("seg", exist_ok=True)
segs = []
for i, (st, src) in enumerate(cuts):
    en = cuts[i+1][0] if i+1 < len(cuts) else END
    d = en - st
    out = f"seg/{i:02d}.mp4"
    if not os.path.exists(src):
        src = src.replace("vid/", "img/").replace(".mp4", ".png")
    if src.endswith(".png"):
        n = int(round(d*FPS))
        z = "min(1.0+0.0016*on,1.25)" if i % 2 == 0 else "max(1.22-0.0016*on,1.0)"
        vf = (f"scale=2160:3840,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS},"
              f"eq=contrast=1.06:saturation=1.05")
        cmd = ["ffmpeg","-loglevel","error","-y","-loop","1","-i",src,"-vf",vf,"-frames:v",str(n),"-pix_fmt","yuv420p","-c:v","libx264","-crf","18",out]
    else:
        vd = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]).decode())
        k = max(d / vd, 1.0)
        vf = f"setpts={k:.4f}*PTS,fps={FPS},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,eq=contrast=1.06"
        cmd = ["ffmpeg","-loglevel","error","-y","-i",src,"-an","-vf",vf,"-t",f"{d:.3f}","-pix_fmt","yuv420p","-c:v","libx264","-crf","18",out]
    if not os.path.exists(out): subprocess.run(cmd, check=True)
    segs.append(out)
open("seg/list.txt","w").write("".join(f"file '{os.path.basename(s)}'\n" for s in segs))
subprocess.run(["ffmpeg","-loglevel","error","-y","-f","concat","-safe","0","-i","seg/list.txt","-c","copy","base.mp4"], check=True)

# ---------- captions (ASS) ----------
W = json.load(open("words.json"))
RED = {"chip","cérebro","pedir","problema","solução","empregos","renda","universal","alta","neuralink","20","paralisado",
       "inteligência","artificial","máquina","perder","cheque","apocalipse","13","sinal","mão","direita","testa","comprar","vender",
       "impossível","existe","teoria","sinais","trabalhar","comentários","musk"}
def t(x):
    h=int(x//3600); m=int(x%3600//60); s=x%60
    return f"{h}:{m:02d}:{s:05.2f}"
groups=[]; cur=[]
for w in W:
    cur.append(w)
    if len(cur)>=3 or re.search(r"[.,?!:]$", w["w"]):
        groups.append(cur); cur=[]
if cur: groups.append(cur)
ev=[]
for gi,g in enumerate(groups):
    st=g[0]["s"]; en=groups[gi+1][0]["s"] if gi+1<len(groups) else g[-1]["e"]+0.4
    en=min(en, g[-1]["e"]+0.5)
    # karaoke: each word pops when spoken
    for wi,w in enumerate(g):
        ws=w["s"]; we=g[wi+1]["s"] if wi+1<len(g) else en
        parts=[]
        for wj,x in enumerate(g[:wi+1]):
            word=x["w"].upper()
            key=re.sub(r"[^\wÀ-ÿ]","",x["w"].lower())
            col="&H3539E5&" if key in RED else "&HFFFFFF&"
            pop=r"{\fscx112\fscy112\t(0,90,\fscx100\fscy100)}" if wj==wi else ""
            parts.append(r"{\c"+col+"}"+pop+word+r"{\fscx100\fscy100}")
        ev.append(f"Dialogue: 1,{t(ws)},{t(we)},Cap,,0,0,0,,"+" ".join(parts))
def card(a,b,txt,style="Top"):
    ev.append(f"Dialogue: 2,{t(a)},{t(b)},{style},,0,0,0,,{{\\fad(150,150)}}{txt}")
card(0.0,3.6,r"O CHIP NO {\c&H3539E5&}SEU CÉREBRO")
card(9.68,16.2,r"CRIE O {\c&H3539E5&}PROBLEMA{\c&HFFFFFF&}\NVENDA A {\c&H3539E5&}SOLUÇÃO")
card(26.7,33.8,r"RENDA UNIVERSAL {\c&H3539E5&}ALTA{\c&HFFFFFF&}\N{\fs40}Musk, abril/2026")
card(37.8,43.6,r"NEURALINK: {\c&H3539E5&}20+{\c&HFFFFFF&} PACIENTES")
card(63.0,75.1,r"{\c&H3539E5&}APOCALIPSE 13:16-17")
card(80.5,83.0,r"É UMA {\c&H3539E5&}TEORIA")
card(83.04,END,r"VOCÊ COLOCARIA\N{\c&H3539E5&}O CHIP?{\c&HFFFFFF&}\N{\fs44}comenta aqui ↓")
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,82,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,7,3,2,70,70,560,1
Style: Top,Inter ExtraBold,82,&H00FFFFFF,&H00FFFFFF,&H00000000,&HB4000000,-1,0,0,0,100,100,1,0,3,18,0,8,60,60,230,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open("caps.ass","w").write(ass)

# ---------- audio ----------
R = "/home/user/unchainedlife-app/brand"
sfx = [(0.0,f"{R}/sfx-earshot/impact_deep.wav",0.7)]
for st,_ in cuts[1:]:
    sfx.append((max(st-0.25,0),f"{R}/sfx-earshot/whoosh_fast_crisp.wav",0.22))
sfx += [(60.5,f"{R}/sfx-earshot/riser_tension.wav",0.35),(63.0,f"{R}/sfx-earshot/impact_punch.wav",0.6),
        (80.45,f"{R}/sfx-earshot/impact_classic.wav",0.5),(83.0,f"{R}/sfx/ding.mp3",0.4)]
inputs=["-i","voz2.wav","-f","lavfi","-t",f"{END}","-i",
        "aevalsrc='0.5*sin(2*PI*55*t)*(0.6+0.4*sin(2*PI*0.25*t))+0.25*sin(2*PI*82.4*t)+0.12*sin(2*PI*110*t)*(0.5+0.5*sin(2*PI*1.1*t))':s=44100"]
fc=["[0:a]aformat=sample_rates=44100:channel_layouts=stereo,asplit=2[v][vsc]",
    f"[1:a]aformat=channel_layouts=stereo,lowpass=f=300,volume=0.10,afade=t=in:d=2,afade=t=out:st={END-2}:d=2[dr]",
    "[dr][vsc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[duck]"]
mix=["[v]","[duck]"]
for k,(st,f,vol) in enumerate(sfx):
    inputs += ["-i",f]
    idx=k+2
    fc.append(f"[{idx}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume={vol},adelay={int(st*1000)}|{int(st*1000)}[s{k}]")
    mix.append(f"[s{k}]")
fc.append("".join(mix)+f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg","-loglevel","error","-y",*inputs,"-filter_complex",";".join(fc),"-map","[a]","-ar","48000","-t",f"{END}","mix.wav"],check=True)

# ---------- final ----------
vf = ("[0:v]ass=caps.ass,"
      "fade=t=in:st=0:d=0.2,fade=t=out:st=%.2f:d=0.4[v]" % (END-0.4))
subprocess.run(["ffmpeg","-loglevel","error","-y","-i","base.mp4","-i","mix.wav","-filter_complex",vf,
                "-map","[v]","-map","1:a","-c:v","libx264","-crf","19","-preset","medium","-pix_fmt","yuv420p",
                "-c:a","aac","-b:a","192k","-movflags","+faststart","-shortest","final.mp4"],check=True)
print("ok", END)
