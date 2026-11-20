import sys, json, numpy as np
from faster_whisper import WhisperModel
a=np.fromfile(sys.argv[1],dtype=np.int16).astype(np.float32)/32768
m=WhisperModel("small",device="cpu",compute_type="int8")
segs,_=m.transcribe(a,language="pt",word_timestamps=True)
W=[]
for s in segs:
  print(f"[{s.start:6.2f}] {s.text.strip()}")
  for w in s.words: W.append({"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)})
json.dump(W,open(sys.argv[2],"w"),ensure_ascii=False)
