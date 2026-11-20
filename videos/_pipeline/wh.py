import sys,json
from faster_whisper import WhisperModel
m=WhisperModel('small',device='cpu',compute_type='int8')
for d in sys.argv[1:]:
    segs,_=m.transcribe(f'{d}/voice.wav',language='pt',word_timestamps=True,beam_size=5)
    W=[{'w':w.word.strip(),'s':round(w.start,2),'e':round(w.end,2)} for s in segs for w in s.words]
    json.dump(W,open(f'{d}/vwords.json','w'),ensure_ascii=False); print(d,len(W))
