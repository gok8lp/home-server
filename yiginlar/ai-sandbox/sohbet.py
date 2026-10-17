# Iki yapay zekayi birbiriyle konusturan kum havuzu (internetsiz). Sadece Ollama API'sine erisir.
import json, os, sys, time, urllib.request
OLLAMA = "http://ollama:11434/api/chat"
A, B = os.environ.get("MODEL_A", "llama3.2"), os.environ.get("MODEL_B", "gemma3")
KONU = os.environ.get("KONU", "Yapay zekalar insanlara en cok hangi konuda yardim edebilir?")
TUR = int(os.environ.get("TUR", "4"))
def sor(model, sistem, gecmis):
    msgs = [{"role": "system", "content": sistem}] + gecmis
    req = urllib.request.Request(OLLAMA, json.dumps({"model": model, "messages": msgs, "stream": False,
        "keep_alive": 0, "options": {"num_predict": 220, "temperature": 0.8}}).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.load(r)["message"]["content"].strip()
sA = f"Sen {A} adli bir yapay zekasin. {B} adli baska bir yapay zeka ile Turkce sohbet ediyorsun. Kisa (en fazla 4 cumle), samimi ve merakli konus, karsi tarafa soru sor."
sB = f"Sen {B} adli bir yapay zekasin. {A} adli baska bir yapay zeka ile Turkce sohbet ediyorsun. Kisa (en fazla 4 cumle), dusunceli konus, bazen itiraz et."
dosya = f"/sonuc/sohbet-{time.strftime('%Y%m%d-%H%M')}.md"
kayit = [f"# {A} ile {B} sohbeti\n\nKonu: {KONU}\n"]
gA, gB = [{"role": "user", "content": f"Sohbeti sen baslat. Konu: {KONU}"}], []
for i in range(TUR):
    for ad, model, sistem, ben, o in ((A, A, sA, gA, gB), (B, B, sB, gB, gA)):
        if not ben: continue
        t = time.time(); cevap = sor(model, sistem, ben)
        ben.append({"role": "assistant", "content": cevap}); o.append({"role": "user", "content": cevap})
        kayit.append(f"**{ad}** _({time.time()-t:.0f} sn)_: {cevap}\n")
        open(dosya, "w").write("\n".join(kayit)); print(f"[{ad}] {cevap[:120]}", flush=True)
print("Bitti:", dosya)
