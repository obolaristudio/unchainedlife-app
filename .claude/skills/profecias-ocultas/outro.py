# outro.py VIDEO_DIR VOICE_WAV  -> VIDEO_DIR/final_siga.mp4
import sys, subprocess, os
D=sys.argv[1]; V=os.path.abspath(sys.argv[2]); O=os.path.dirname(os.path.abspath(__file__))+"/outro"
dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",V]))
T=dur+1.3; sw=min(1.6, T*0.4); FPS=30
mus=os.path.join(D,"musica.mp3"); md=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mus]))
ms=max(0,md-T-1)
vf=(f"[0:v]scale=2160:3840,zoompan=z='min(1.0+0.0008*on,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(T*FPS)}:s=1080x1920:fps={FPS},trim=0:{sw}[a];"
    f"[1:v]scale=2160:3840,zoompan=z='min(1.0+0.0008*(on+{int(sw*FPS)}),1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(T*FPS)}:s=1080x1920:fps={FPS},trim=0:{T-sw},setpts=PTS-STARTPTS[b];"
    f"[a][b]concat=n=2:v=1:a=0,fade=t=in:d=0.25,fade=t=out:st={T-0.4}:d=0.4,format=yuv420p[v]")
af=(f"[2:a]adelay=350|350,aformat=sample_rates=44100:channel_layouts=stereo[vo];"
    f"[3:a]atrim={ms}:{ms+T},asetpts=PTS-STARTPTS,aformat=sample_rates=44100:channel_layouts=stereo,volume=0.2,afade=t=in:d=0.4,afade=t=out:st={T-0.8}:d=0.8[m];"
    f"[vo][m]amix=inputs=2:normalize=0:duration=longest,atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[ao]")
subprocess.run(["ffmpeg","-loglevel","error","-y","-loop","1","-i",O+"/card.png","-loop","1","-i",O+"/card2.png","-i",V,"-i",mus,
  "-filter_complex",vf+";"+af,"-map","[v]","-map","[ao]","-t",f"{T}","-c:v","libx264","-crf","19","-c:a","aac","-b:a","192k",D+"/outro.mp4"],check=True)
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",D+"/final.mp4","-i",D+"/outro.mp4","-filter_complex",
  "[0:v]fps=30,format=yuv420p,setsar=1[v0];[1:v]fps=30,format=yuv420p,setsar=1[v1];[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
  "-map","[v]","-map","[a]","-c:v","libx264","-crf","19","-preset","medium","-c:a","aac","-b:a","192k","-movflags","+faststart",D+"/final_siga.mp4"],check=True)
print("ok",T)
