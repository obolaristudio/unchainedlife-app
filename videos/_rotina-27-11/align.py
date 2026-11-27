# alinha o texto do roteiro aos tempos do whisper -> words_fix.json
import json,re,sys,difflib,unicodedata
v=sys.argv[1]; script=open(f"{v}/roteiro.txt").read()
W=json.load(open(f"{v}/words.json"))
S=script.split()
n=lambda t: re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',t.lower()).encode('ascii','ignore').decode())
a=[n(w['w']) for w in W]; b=[n(t) for t in S]
sm=difflib.SequenceMatcher(None,a,b,autojunk=False); out=[]
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if j2==j1: continue
    if i2==i1:  # insert: time from previous
        t=W[i1-1]['e'] if i1>0 else 0
        for j in range(j1,j2): out.append({'w':S[j],'s':t}); 
        continue
    s0=W[i1]['s']; e0=W[i2-1]['e']; k=j2-j1
    for x,j in enumerate(range(j1,j2)): out.append({'w':S[j],'s':round(s0+(e0-s0)*x/k,2)})
json.dump(out,open(f"{v}/words_fix.json","w"),ensure_ascii=False); print(v,len(out),len(W))
