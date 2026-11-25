import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
for d in sys.argv[1:]:
    segs,_=m.transcribe(f"{d}/voz.wav",language="pt",word_timestamps=True,vad_filter=False)
    W=[{"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)} for s in segs for w in s.words]
    json.dump(W,open(f"{d}/words.json","w"),ensure_ascii=False); print(d,len(W),W[-1])
