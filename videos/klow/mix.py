# Mixagem: voz + SFX da marca (brand/sfx) + musica com ducking. Saida -14 LUFS.
import json,subprocess,sys
S=json.load(open('scenes.json')); SFX='../../brand/sfx/'
cues=[('impact', 0.0, 0.45), ('impact', 4.14, 0.45), ('impact', 39.8, 0.45), ('impact', 54.8, 0.45), ('impact', 61.46, 0.45), ('impact', 68.1, 0.45), ('ding', 14.6, 0.35), ('ding', 57.0, 0.35)]
cues+=[('whoosh',s[0],0.18) for s in S[1:] ]
cues+=[('pop',t,0.3) for t in [8.24, 9.8, 12.3, 13.86, 19.3, 24.3, 31.4, 46.0, 48.36, 50.4, 51.58, 53.4, 63.2, 65.7, 74.95]]
args=['ffmpeg','-v','error','-y','-i','voz.wav','-i',sys.argv[1]]
fc=[];labs=[]
for i,(n,t,v) in enumerate(cues):
    args+=['-i',SFX+n+'.mp3']; d=int(t*1000)
    fc.append(f'[{i+2}:a]adelay={d}|{d},volume={v}[s{i}]'); labs.append(f'[s{i}]')
fc.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0[sfx]')
fc.append('[1:a]volume=0.22,afade=t=in:d=1.5,afade=t=out:st=75.1:d=2.5[m]')
fc.append('[0:a]asplit=2[v][vk]')
fc.append('[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md]')
fc.append('[v][md][sfx]amix=inputs=3:normalize=0,atrim=0:77.6,loudnorm=I=-14:TP=-1:LRA=11[a]')
subprocess.run(args+['-filter_complex',';'.join(fc),'-map','[a]','-ar','48000','mix.wav'],check=True)
print('ok',len(cues))
