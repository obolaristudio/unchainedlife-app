import json,subprocess,sys
D,music=sys.argv[1],sys.argv[2]
C=json.load(open(f'{D}/cues.json')); T=C['T']
SFX='/home/user/unchainedlife-app/brand/sfx/'
ev=[('impact',t,0.5) for t in C['impact']]+[('whoosh',t-0.05,0.22) for t in C['cuts']]+[('pop',t,0.3) for t in C['pops']]+[('ding',t,0.35) for t in C['ding']]
ins=['-i',f'{D}/voz.wav','-stream_loop','-1','-i',music]; fc=[]
for i,(n,t,v) in enumerate(ev):
    ins+=['-i',SFX+n+'.mp3']; ms=int(max(0,t)*1000)
    fc.append(f'[{i+2}:a]volume={v},adelay={ms}|{ms}[s{i}]')
fc.append(f'[1:a]atrim=0:{T},volume=0.16,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m]')
fc.append('[0:a]asplit[v][vk]')
fc.append('[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[md]')
fc.append('[v][md]'+''.join(f'[s{i}]' for i in range(len(ev)))+f'amix=inputs={len(ev)+2}:normalize=0:duration=first,apad=whole_dur={T},loudnorm=I=-14:TP=-1.5:LRA=11[a]')
subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','-c:a','pcm_s16le',f'{D}/mix.wav'],check=True)
print('mix ok')
