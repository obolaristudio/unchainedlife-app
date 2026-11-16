# Mixagem: voz + SFX da marca (brand/sfx) + musica com ducking. Saida -14 LUFS.
import json,subprocess,sys
S=json.load(open('scenes.json')); SFX='../../brand/sfx/'
cues=[('impact',0.0,0.5),('impact',12.4,0.4),('impact',50.62,0.4),('impact',55.3,0.55),('impact',72.3,0.4),('ding',15.5,0.35),('ding',61.0,0.4)]
cues+=[('whoosh',s[0],0.18) for s in S[1:] if s[0]!=55.3]
cues+=[('pop',t,0.3) for t in [8.7,20.3,23.3,24.2,25.4,29.4,32.2,38.6,41.4,44.2,48.5,52.6,62.0,66.4,69.2,79.5]]
args=['ffmpeg','-v','error','-y','-i','voz.wav','-i',sys.argv[1]]
fc=[];labs=[]
for i,(n,t,v) in enumerate(cues):
    args+=['-i',SFX+n+'.mp3']; d=int(t*1000)
    fc.append(f'[{i+2}:a]adelay={d}|{d},volume={v}[s{i}]'); labs.append(f'[s{i}]')
fc.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0[sfx]')
fc.append('[1:a]volume=0.22,afade=t=in:d=1.5,afade=t=out:st=80.4:d=2.5[m]')
fc.append('[0:a]asplit=2[v][vk]')
fc.append('[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md]')
fc.append('[v][md][sfx]amix=inputs=3:normalize=0,atrim=0:82.9,loudnorm=I=-14:TP=-1:LRA=11[a]')
subprocess.run(args+['-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','mix.wav'],check=True)
print('ok',len(cues))
