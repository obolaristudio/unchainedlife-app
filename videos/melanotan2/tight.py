import subprocess,re,sys
src,out,tempo=sys.argv[1],sys.argv[2],float(sys.argv[3])
r=subprocess.run(['ffmpeg','-hide_banner','-i',src,'-af','silencedetect=n=-38dB:d=0.3','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
keep=[];cur=0.0
for s,e in zip(st,en):
    if s<0.05: cur=max(0,e-0.05); continue
    keep.append((cur,s+0.12)); cur=e-0.12
keep.append((cur,dur))
f=''.join(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];' for i,(a,b) in enumerate(keep))
f+=''.join(f'[a{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=0:a=1,atempo={tempo}[o]'
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',src,'-filter_complex',f,'-map','[o]','-ar','44100','-ac','1',out],check=True)
print(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],capture_output=True,text=True).stdout)
