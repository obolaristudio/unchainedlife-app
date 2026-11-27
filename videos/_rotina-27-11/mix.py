import json,subprocess,sys
v=sys.argv[1]; moff=float(sys.argv[2]); C=json.load(open(f'{v}/cfg.json')); T=C['T']
S='/home/user/unchainedlife-app/brand/sfx'; E='/home/user/unchainedlife-app/brand/sfx-earshot'
cues=[(0.0,f'{E}/impact_punch.wav',0.5)]
cues+=[(s[0]-0.12,f'{S}/whoosh.mp3',0.16) for s in C['scenes'][1:]]
cues+=[(p[0],f'{S}/pop.mp3',0.3) for p in C['pills']]
cues+=[(C['stamp'][0],f'{E}/impact_deep.wav',0.55)]
cues+=[(C['counter'][0]+1.2,f'{S}/ding.mp3',0.3),(C['counter2'][0]+1.2,f'{S}/ding.mp3',0.3)]
cues+=[(C['status'][0]+0.2+i*1.6,f'{S}/pop.mp3',0.3) for i in range(len(C['status'][2]))]
ins=['-i',f'{v}/voz_f.wav','-ss',str(moff),'-i','musica.mp3']; fc=[]; lab=[]
for i,(t,f,g) in enumerate(cues):
    ins+=['-i',f]; d=int(max(0,t)*1000)
    fc.append(f'[{i+2}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume={g},adelay={d}|{d}[s{i}]'); lab.append(f'[s{i}]')
fc.append('[0:a]aformat=sample_rates=44100:channel_layouts=stereo,apad=whole_dur=%s,asplit[vo][sc]'%T)
fc.append(f'[1:a]aformat=sample_rates=44100:channel_layouts=stereo,volume=0.22,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m0]')
fc.append('[m0][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[md]')
fc.append(f'[vo][md]{"".join(lab)}amix=inputs={len(lab)+2}:normalize=0:duration=first,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[out]')
subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]','-ar','48000',f'{v}/mix.wav'],check=True)
print('mix ok',v,len(cues))
