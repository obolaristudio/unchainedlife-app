# Mixagem: voz + SFX da marca (brand/sfx) + musica com ducking. Saida -14 LUFS.
import json,subprocess,sys
S=json.load(open('scenes.json')); SFX='../../brand/sfx/'
cues=[('impact', 0.0, 0.45), ('impact', 7.38, 0.45), ('impact', 60.0, 0.45), ('ding', 18.0, 0.35), ('ding', 30.4, 0.35)]
cues+=[('whoosh',s[0],0.18) for s in S[1:] ]
cues+=[('pop',t,0.3) for t in [75.35]]
args=['ffmpeg','-v','error','-y','-i','voz.wav','-i',sys.argv[1]]
fc=[];labs=[]
for i,(n,t,v) in enumerate(cues):
    args+=['-i',SFX+n+'.mp3']; d=int(t*1000)
    fc.append(f'[{i+2}:a]adelay={d}|{d},volume={v}[s{i}]'); labs.append(f'[s{i}]')
fc.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0[sfx]')
fc.append('[1:a]volume=0.22,afade=t=in:d=1.5,afade=t=out:st=75.2:d=2.5[m]')
fc.append('[0:a]asplit=2[v][vk]')
fc.append('[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md]')
fc.append('[v][md][sfx]amix=inputs=3:normalize=0,atrim=0:77.7,loudnorm=I=-14:TP=-1:LRA=11[a]')
subprocess.run(args+['-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','mix.wav'],check=True)
print('ok',len(cues))
