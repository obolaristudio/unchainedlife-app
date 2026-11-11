# Mixagem: voz + música baixinha com ducking + SFX (brand/sfx) -> MP4 final (-14 LUFS).
import subprocess,sys,json
def mix(video,voice,music,T,cues,out,sfxdir='/home/user/unchainedlife-app/brand/sfx'):
    # cues: [(tempo, 'whoosh|pop|impact|ding', volume)]
    ins=['-i',video,'-i',voice,'-i',music]
    fc=[f"[1:a]aresample=44100,volume=1.0,apad=whole_dur={T}[v0]","[v0]asplit=2[v][vsc]",
        f"[2:a]aresample=44100,atrim=0:{T},volume=0.30,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m0]",
        "[m0][vsc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[m]"]
    labels=['[v]','[m]']
    for k,(t,name,vol) in enumerate(cues):
        ins+=['-i',f'{sfxdir}/{name}.mp3']
        n=3+k
        fc.append(f"[{n}:a]aresample=44100,volume={vol},adelay={int(t*1000)}|{int(t*1000)}[s{k}]"); labels.append(f'[s{k}]')
    fc.append(''.join(labels)+f"amix=inputs={len(labels)}:normalize=0:duration=longest,atrim=0:{T},loudnorm=I=-14:TP=-1.0:LRA=11[a]")
    cmd=['ffmpeg','-loglevel','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-t',str(T),'-movflags','+faststart',out]
    subprocess.run(cmd,check=True)
