import subprocess,json,sys,importlib.util
d=sys.argv[1]; spec=importlib.util.spec_from_file_location('cfg',f'{d}/cfg.py'); C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
cuts=C.CUTS+[C.T]; PW,PH=1080,1100; S='/tmp/claude-0/w/stock'
for i,c in enumerate(C.CLIPS):
    dur=round(cuts[i+1]-cuts[i],3); src=f'{S}/{c}.mp4'
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(',')[:2])
    L=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip())
    off=max(0,min(1.0,L-dur-0.1)); loop=['-stream_loop','-1'] if L<dur+off else []
    if h>w: panel=f'scale={PW}:-2,crop={PW}:{PH}'
    else:
        cw=round(h*PW/PH); panel=f'crop={cw}:{h}:(iw-{cw})/2:0,scale={PW}:{PH}:flags=lanczos'
    z=f"zoompan=z='if(lt(on,8),1.18-0.022*on,1+0.0006*(on-8))':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={PW}x{PH}:fps=30"
    fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},setsar=1,{z}[p];"
        f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.22:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y',*loop,'-ss',str(off),'-t',str(dur),'-i',src,'-filter_complex',fc,'-an','-c:v','libx264','-crf','17','-preset','veryfast','-r','30',f'{d}/sc_{i:02d}.mp4'],check=True)
open(f'{d}/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(C.CLIPS))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',f'{d}/list.txt','-c','copy',f'{d}/hf/assets/bg.mp4'],check=True); print('bg ok')
