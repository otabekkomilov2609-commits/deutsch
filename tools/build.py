#!/usr/bin/env python3
"""streber.uz — tez yuklanadigan nashr (2026-10-21, Otabek: «sayt juda sekin yuklanyapti»).

MANBA:  src/index.html   — to'liq, hamma ma'lumot ichida (shu fayl tahrirlanadi; site/index.html ham shu bilan bir xil patch'lanadi)
NATIJA: index.html       — kichik qobiq: CSS + markup + yuklovchi
        app.<hash>.js    — asosiy skript
        data/<id>.<hash>.json — katta JSON bloklari (ex, lern, hint, ia, …)
Hash nomlar: o'zgarmagan fayl brauzer/SW keshidan keladi, o'zgargani yangi nom bilan yuklanadi.
Ishga tushirish: python3 tools/build.py   (har commit'dan oldin)
"""
import re, hashlib, os, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "index.html")
BIG = ["doc-data","ex-data","lern-data","ia-data","iam-data","tr-data","hint-data","wkj-data","vo-data","wk-data","aud-data","mud-data","say-data"]

def h8(b): return hashlib.sha1(b).hexdigest()[:8]

s = open(SRC, encoding="utf-8").read()
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
keep = set()
files = {}
for bid in BIG:
    m = re.search(r'(<script type="application/json" id="%s">)(.*?)(</script>)' % re.escape(bid), s, re.S)
    if not m: continue
    body = m.group(2)
    try: body = json.dumps(json.loads(body), ensure_ascii=False, separators=(",", ":"))
    except Exception: pass
    data = body.encode("utf-8")
    name = "data/%s.%s.json" % (bid.replace("-data", ""), h8(data))
    open(os.path.join(ROOT, name), "wb").write(data); keep.add(name); files[bid] = name
    s = s[:m.start(2)] + s[m.end(2):]

# asosiy skript: <script> dan keyin birinchi katta blok (const SAYDATA… bo'lgan)
mm = None
for m in re.finditer(r'<script>(.*?)</script>', s, re.S):
    if "function exData()" in m.group(1): mm = m; break
assert mm, "asosiy skript topilmadi"
js = mm.group(1)
js = js.replace('addEventListener("load",()=>navigator.serviceWorker.register("/sw.js").catch(()=>{}));',
                'navigator.serviceWorker.register("/sw.js").catch(()=>{});')  # skript load'dan keyin yuklanadi
jsb = js.encode("utf-8"); app = "app.%s.js" % h8(jsb)
open(os.path.join(ROOT, app), "wb").write(jsb); keep.add(app)
loader = ('<script>(async()=>{const F=%s,A=%s;const st=document.getElementById("ld-st");'
          '/* eski index.html (CDN keshi) yangi fayllarni topolmasa — bir marta o\'zini yangilaydi */const heal=async()=>{try{if(sessionStorage.getItem("ld:heal"))return false;sessionStorage.setItem("ld:heal","1");const r=await fetch(location.pathname,{cache:"reload"});if(r.ok){location.reload();return true;}}catch(e){}return false;};'
          'try{await Promise.all(Object.entries(F).map(async([id,u])=>{const r=await fetch(u);if(!r.ok)throw new Error(u);document.getElementById(id).textContent=await r.text();}));}'
          'catch(e){if(await heal())return;if(st)st.textContent="Yuklanmadi — internetni tekshirib, sahifani yangilang · Не загрузилось — проверьте интернет и обновите страницу";return;}'
          'const sc=document.createElement("script");sc.src=A;sc.onerror=async()=>{if(await heal())return;if(st)st.textContent="Yuklanmadi — sahifani yangilang";};document.body.appendChild(sc);})();</script>'
          ) % (json.dumps(files, ensure_ascii=False), json.dumps(app))
s = s[:mm.start()] + loader + s[mm.end():]
# yuklanish belgisi
s = s.replace('<main id="main"></main>', '<main id="main"><div id="ld-st" class="ld-st">⏳ Yuklanmoqda…</div></main>', 1)
s = s.replace('</style>', '.ld-st{text-align:center;color:var(--muted);padding:40px 16px;font-weight:700}</style>', 1)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(s)

# eski hash'li fayllar 2 kun saqlanadi: GitHub Pages CDN index.html'ni 10 daqiqagacha eski holda beradi — darhol o'chirilsa «Yuklanmadi» (2026-10-21)
import subprocess, time
for f in glob.glob(os.path.join(ROOT, "data", "*.json")) + glob.glob(os.path.join(ROOT, "app.*.js")):
    rel = os.path.relpath(f, ROOT)
    if rel in keep: continue
    try: ts = int(subprocess.run(["git", "log", "-1", "--format=%ct", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip() or 0)
    except Exception: ts = 0
    if ts and time.time() - ts > 2 * 86400: os.remove(f)
# SW: hash'li fayllar ro'yxati (cache-first)
sw = os.path.join(ROOT, "sw.js"); w = open(sw, encoding="utf-8").read()
w = re.sub(r"const V = '[^']*'", "const V = 'streber-%s'" % h8((app + "".join(sorted(files.values()))).encode()), w, count=1)
open(sw, "w", encoding="utf-8").write(w)
print("index.html %.2f MB, %s %.2f MB, data: %d fayl, jami %.2f MB" % (len(s.encode())/1e6, app, len(jsb)/1e6, len(files),
      sum(os.path.getsize(os.path.join(ROOT, f)) for f in files.values())/1e6))
