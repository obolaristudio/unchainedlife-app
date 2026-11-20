import sys,subprocess,importlib.util
d=sys.argv[1]; music=sys.argv[2]
spec=importlib.util.spec_from_file_location('cfg',f'{d}/cfg.py'); C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
S='/home/user/unchainedlife-app/brand/sfx/'
cues=[(0.0,'impact',0.5)]
for t,_ in C.HEADS[1:]: cues.append((t,'whoosh',0.3))
for o in C.OVS:
    if o['k']=='chips':
        for it in o['items']: cues.append((it[0],'pop',0.28))
    elif o['k'] in('big','count'): cues.append((o['t'],'ding',0.3))
    elif o['k']=='bars':
        for b in o['bars']: cues.append((b[0],'ding',0.25))
    elif o['k']=='stamp': cues.append((o['t'],'impact',0.45))
inp=['-i',f'{d}/voice.wav','-stream_loop','-1','-i',music]; fc=[]; lab=[]
for i,(t,n,v) in enumerate(cues):
    inp+=['-i',S+n+'.mp3']; ms=int(t*1000)
    fc.append(f'[{i+2}:a]volume={v},adelay={ms}|{ms}[s{i}]'); lab.append(f'[s{i}]')
T=C.T
fc.append(f'[1:a]atrim=0:{T},volume=0.16,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m]')
fc.append('[0:a]asplit[v1][v2]')
fc.append('[m][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[md]')
fc.append(f'{"".join(lab)}amix=inputs={len(lab)}:normalize=0[sfx]')
fc.append('[v1][md][sfx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1[out]')
subprocess.run(['ffmpeg','-loglevel','error','-y',*inp,'-filter_complex',';'.join(fc),'-map','[out]','-t',str(T),'-ar','48000',f'{d}/mix.wav'],check=True)
print('mix ok',len(cues))
