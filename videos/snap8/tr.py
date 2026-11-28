import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
import subprocess,numpy as np
raw=subprocess.run(["ffmpeg","-loglevel","error","-i",sys.argv[1],"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True).stdout
a=np.frombuffer(raw,np.float32)
seg,_=m.transcribe(a,language="pt",word_timestamps=True)
W=[{"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)} for s in seg for w in s.words]
json.dump(W,open(sys.argv[2],"w"),ensure_ascii=False);print(len(W),W[-1])
