import sys, numpy as np
from faster_whisper import WhisperModel
a=np.fromfile(sys.argv[1],dtype=np.int16).astype(np.float32)/32768
m=WhisperModel("small",device="cpu",compute_type="int8")
segs,_=m.transcribe(a,language="pt",vad_filter=True)
for s in segs: print(f"[{s.start:6.1f}-{s.end:6.1f}] {s.text.strip()}")
