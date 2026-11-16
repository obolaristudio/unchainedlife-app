# Fundo do Reel espirulina (estilo IA): clipe 4:5 no topo, ida-e-volta + câmera lenta para cobrir cada cena.
import subprocess,json
S=[(0,8.2,1),(8.2,15.4,2),(15.4,19.5,3),(19.5,27.1,4),(27.1,35.3,5),(35.3,42.8,6),(42.8,53.0,7),(53.0,64.8,8),(64.8,77.7,9)]
json.dump(S,open('scenes.json','w'))
L=5.0
for i,(a,b,c) in enumerate(S):
    d=round(b-a,3)
    if d<=L: chain=f"[0:v]trim=0:{d},setpts=PTS-STARTPTS[v]"
    else:
        f=d/(2*L)  # ida e volta (10 s) esticado para d
        chain=f"[0:v]trim=0:{L},setpts=PTS-STARTPTS,split[x][y];[y]reverse[r];[x][r]concat=n=2:v=1[pp];[pp]setpts={f:.4f}*PTS[v]"
    fc=chain+f";[v]fps=30,scale=1080:1352:flags=lanczos,setsar=1,pad=1080:1920:0:0:color=0x1D3324,trim=0:{d},format=yuv420p[o]"
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'clips/c{c}.mp4','-filter_complex',fc,'-map','[o]','-an','-c:v','libx264','-crf','16','-preset','veryfast',f'sc_{i:02d}.mp4'],check=True)
open('list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i','list.txt','-c','copy','hf/assets/bg.mp4'],check=True)
print('ok')
