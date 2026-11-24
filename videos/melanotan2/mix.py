import json,subprocess,sys,os
d=sys.argv[1]; os.chdir(d); C=json.load(open('cfg.json')); S=json.load(open('scenes.json')); T=C['T']
SFX='/home/user/unchainedlife-app/brand/sfx/'
cues=[('impact',0.0,0.55)]
cues+=[('whoosh',s[0]-0.15,0.22) for s in S[1:]]
for o in C['ov']:
    cues+=[('pop',it[0],0.3) for it in o['items']]
cues+=[('impact',s['a'],0.5) for s in C.get('stamps',[])]
cues+=[('impact',e['a']+0.35,0.45) for e in C.get('drops',[])]
cues+=[('ding',c['a']+1.0,0.35) for c in C.get('counters',[])]
cues+=[('ding',C['cta_at'],0.35)]
ins=['-i','voz.wav','-stream_loop','-1','-i','music.mp3']
f=[]; lab=[]
for k,(n,t,v) in enumerate(cues):
    ins+=['-i',SFX+n+'.mp3']; ms=max(0,int(t*1000))
    f.append(f'[{k+2}:a]volume={v},adelay={ms}|{ms},apad[s{k}]'); lab.append(f'[s{k}]')
f.append(f'[1:a]atrim=0:{T},volume=0.22,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m]')
f.append('[0:a]asplit[v1][v2]')
f.append('[m][v2]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=350[md]')
f.append(f'[v1][md]{"".join(lab)}amix=inputs={2+len(cues)}:normalize=0:duration=first,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[o]')
f.append('[0:a]apad[v0]')
fc=';'.join(f).replace('[v1][md]','[v1p][md]')
fc=fc.replace('[0:a]asplit[v1][v2]',f'[0:a]apad=whole_dur={T},asplit[v1p][v2]')
subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',fc.replace(';[0:a]apad[v0]',''),'-map','[o]','-ar','48000','-ac','2','mix.wav'],check=True)
# sfx-only track
f2=[x for x in f if x.startswith('[') and x.split(']')[0][1:].split(':')[0].isdigit() and int(x.split(']')[0][1:].split(':')[0])>=2]
subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',';'.join(f2)+f';{"".join(lab)}amix=inputs={len(cues)}:normalize=0,atrim=0:{T}[o]','-map','[o]','sfx.wav'],check=True)
json.dump(cues,open('cues.json','w'))
print('mix ok',len(cues),'cues')
