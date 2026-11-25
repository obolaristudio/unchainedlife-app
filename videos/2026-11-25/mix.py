import json,subprocess,sys,importlib
d,mus=sys.argv[1],sys.argv[2]; S=importlib.import_module('spec_'+d); T=S.T
sc=[s[0] for s in json.load(open(f'{d}/scenes.json'))[1:]]
cues=[('impact',0.0,0.5)]+[('whoosh',t-0.15,0.22) for t in sc]
cues+=[('pop',t,0.25) for _,t in S.SLIDES+S.POPS]
cues+=[('impact',t,0.5) for t in S.STAMPS]+[('ding',t,0.35) for t in S.DINGS]
cues=[(n,max(0,t),v) for n,t,v in cues]
ins=['-i',f'{d}/voz.wav','-stream_loop','-1','-i',f'music/{mus}.mp3']
fc=[f"[0:a]aformat=sample_rates=44100:channel_layouts=stereo,volume=1.0,asplit[v][vk]",
    f"[1:a]atrim=0:{T},aformat=sample_rates=44100:channel_layouts=stereo,volume=0.16,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m0]",
    "[m0][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[m]"]
labs=[]
for i,(n,t,v) in enumerate(cues):
    ins+=['-i',f'../../brand/sfx/{n}.mp3']
    fc.append(f"[{i+2}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume={v},adelay={int(t*1000)}|{int(t*1000)}[s{i}]"); labs.append(f'[s{i}]')
fc.append(''.join(labs)+f"amix=inputs={len(labs)}:normalize=0[sfx]")
fc.append(f"[v][m][sfx]amix=inputs=3:normalize=0,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]','-ar','44100','-c:a','pcm_s16le',f'{d}/mix.wav'],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{d}/overlay.mp4','-i',f'{d}/mix.wav','-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','22','-maxrate','1500k','-bufsize','3000k','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',f'{d}/reel.mp4'],check=True)
print('ok',d,len(cues))
