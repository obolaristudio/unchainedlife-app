import json,sys,subprocess,re
d,music,T=sys.argv[1],sys.argv[2],float(sys.argv[3])
SFX='/home/user/unchainedlife-app/brand/sfx'
S=json.load(open(f'{d}/scenes.json'))
g=open(f'{d}/gen.py').read()
slides=[float(x) for x in re.findall(r"\('#o[\w]+',([\d.+]+)\)",g) if '+' not in x]
cues=[('impact',0.0,0.5)]+[('whoosh',s[0]-0.1,0.22) for s in S[1:]]+[('pop',t,0.25) for t in slides]
cues+= [(n,float(t),v) for n,t,v in json.load(open(f'{d}/extra_cues.json'))]
inputs=['-i',f'{d}/voz.wav','-stream_loop','-1','-i',music]
fc=[]; labels=[]
for k,(n,t,v) in enumerate(cues):
    inputs+=['-i',f'{SFX}/{n}.mp3']; ms=int(max(0,t)*1000)
    fc.append(f'[{k+2}:a]volume={v},adelay={ms}|{ms}[s{k}]'); labels.append(f'[s{k}]')
fc.append(f'[1:a]atrim=0:{T},volume=0.16,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m]')
fc.append('[0:a]asplit[v1][v2]')
fc.append('[m][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[md]')
fc.append(f'[v1][md]{"".join(labels)}amix=inputs={len(labels)+2}:normalize=0:duration=first,apad=whole_dur={T},atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[out]')
subprocess.run(['ffmpeg','-loglevel','error','-y',*inputs,'-filter_complex',';'.join(fc),'-map','[out]','-ar','48000','-c:a','pcm_s16le',f'{d}/mix.wav'],check=True)
print('mix ok',len(cues))
