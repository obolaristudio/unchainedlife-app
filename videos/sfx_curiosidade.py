import json,subprocess
T=json.load(open('timing.json'));st=T['st'];TOTAL=T['TOTAL']
ev=[]
def add(t,expr,dur,vol=1.0):ev.append((max(t,0),expr,dur,vol))
add(0.0,"sin(2*PI*(55*t-30*t*t))*exp(-4*t)",0.7,1.4)
add(0.0,"0.5*sin(2*PI*(300*t+500*t*t))*sin(PI*t/1.3)",1.3,0.35)
add(st[0]+2.0,"sin(2*PI*660*t)*exp(-9*t)+gt(t,0.12)*sin(2*PI*880*t)*exp(-9*(t-0.12))",0.6,0.3)
b0=st[1]-0.05+0.5
for i in range(16):
    f=330*(2**((i*1)/12*1.5));add(b0+i*0.11,f"sin(2*PI*{f:.1f}*t)*exp(-14*t)*0.9",0.25,0.32)
add(b0+16*0.11,"sin(2*PI*1320*t)*exp(-6*t)+0.5*sin(2*PI*1980*t)*exp(-7*t)",0.6,0.3)
for i in range(1,len(st)):
    add(st[i]-0.04,"sin(2*PI*90*t)*exp(-22*t)",0.2,0.9)
    add(st[i]+0.02,"(random(0)*2-1)*exp(-60*t)",0.08,0.25)
add(st[3]-0.9,"sin(2*PI*(180*t+260*t*t))*pow(t/0.9,2)",0.9,0.35)
for l in (0.9,1.8):add(st[4]-0.05+l,"0.6*sin(2*PI*(420*t+300*t*t))*sin(PI*t/1.2)",1.2,0.22)
tl=st[5]-0.05+0.3+1.4
add(tl-1.1,"sin(2*PI*(250*t+500*t*t))*pow(t/1.1,1.5)",1.1,0.35)
add(tl+0.02,"sin(2*PI*1046*t)*exp(-3.5*t)+0.6*sin(2*PI*1568*t)*exp(-4*t)+0.4*sin(2*PI*2093*t)*exp(-5*t)",1.4,0.5)
add(st[5]-0.05+0.3,"sin(2*PI*784*t)*exp(-12*t)",0.3,0.25)
add(st[5]-0.05+1.0,"sin(2*PI*880*t)*exp(-12*t)",0.3,0.25)
add(st[6]-0.05+0.35,"sin(2*PI*120*t)*exp(-16*t)+(random(1)*2-1)*exp(-40*t)*0.4",0.3,0.7)
add(st[7]+0.3,"sin(2*PI*784*t)*exp(-5*t)+sin(2*PI*1175*t)*exp(-5*t)",0.9,0.3)
cmd=['ffmpeg','-y','-loglevel','error'];fl=[]
for i,(t,e,d,v) in enumerate(ev):
    cmd+=['-f','lavfi','-i',f"aevalsrc='{e}':s=44100:d={d}"]
    ms=int(t*1000);fl.append(f"[{i}:a]volume={v},afade=t=out:st={max(d-0.05,0):.2f}:d=0.05,adelay={ms}|{ms}[e{i}]")
fl.append(''.join(f'[e{i}]' for i in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad=whole_dur={TOTAL},atrim=0:{TOTAL}[sfx]")
subprocess.run(cmd+['-filter_complex',';'.join(fl),'-map','[sfx]','sfx.wav'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','voz.wav','-i','mus.wav','-i','wh.wav','-i','sfx.wav','-filter_complex',
 f"[1:a]volume='if(between(t,{tl-0.5},{tl+0.05}),0.04,0.35)':eval=frame[m];[m][0:a]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[md];[0:a][md][2:a]amix=inputs=3:normalize=0[b];[b][3:a]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
 '-map','[a]','-ar','44100','audio2.wav'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i','fr/f%05d.jpg','-i','audio2.wav','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','reel_motsc_v3.mp4'],check=True)
print(len(ev),'efeitos')
