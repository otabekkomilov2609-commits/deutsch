#!/usr/bin/env python3
"""telc to'plamlarini va dvigatelni src/index.html ga qo'shadi (takror ishga tushirsa — yangilaydi).
   engine.js → /* TL-JS */…/* /TL-JS */, engine.css → /* TL-CSS */…/* /TL-CSS */, B1-L*-T.json → tl-data + MATS."""
import json, os, re, glob

SRC = "/home/claude/deutsch/src/index.html"
DIR = os.path.dirname(os.path.abspath(__file__))
s = open(SRC, encoding="utf-8").read()

def block(s, a, b, body, anchor, before=True):
    if a in s:
        i = s.index(a); j = s.index(b, i) + len(b)
        return s[:i] + a + "\n" + body + "\n" + b + s[j:]
    k = s.index(anchor)
    ins = a + "\n" + body + "\n" + b + "\n"
    return s[:k] + ins + s[k:] if before else s[:k + len(anchor)] + ins + s[k + len(anchor):]

s = block(s, "/* TL-JS */", "/* /TL-JS */", open(os.path.join(DIR, "engine.js"), encoding="utf-8").read(), "function exOpen(id){")
s = block(s, "/* TL-CSS */", "/* /TL-CSS */", open(os.path.join(DIR, "engine.css"), encoding="utf-8").read(), "/* 🧪 Beta — yangi o'quvchi paneli (2026-10-20) */")

files = sorted(glob.glob(os.path.join(DIR, "B1-L*-T.json")), key=lambda p: int(re.search(r"L(\d+)-T", p).group(1)))
data, mats = {}, []
for p in files:
    D = json.load(open(p, encoding="utf-8")); n = D["lek"]; tab = "b11" if n <= 12 else "b12"
    D["title"] = {"sb1": "Sprachbausteine Teil 1", "sb2": "Sprachbausteine Teil 2", "l1": "Leseverstehen Teil 1", "l2": "Leseverstehen Teil 2", "l3": "Leseverstehen Teil 3"}[D["part"]]
    data[D["id"]] = D
    sub = {"sb1": "10 bo‘shliq · a/b/c", "sb2": "10 bo‘shliq · 15 so‘z", "l1": "5 matn · 10 sarlavha", "l2": "1 matn · 5 savol", "l3": "10 vaziyat · 12 e’lon"}[D["part"]]
    m = {"id": D["id"], "title": "Prüfungstraining · " + D["title"], "stitle": D["title"], "tlsub": sub + " · " + str(D["min"]) + " daq",
         "part": "pt", "ic": "🎯", "file": "", "thumb": "", "name": f"B1.{1 if n <= 12 else 2} Lektion {n} - telc", "type": "uebung", "key": str(n),
         "pages": 0, "date": "2026-10-24", "lvl": "B1", "tab": tab, "tl": True, "beta": True, "noCur": True}
    mats.append(json.dumps(m, ensure_ascii=False) + ",")
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in blob.lower()
tag = '<script type="application/json" id="tl-data">'
if tag in s:
    i = s.index(tag) + len(tag); j = s.index("</script>", i); s = s[:i] + blob + s[j:]
else:
    k = s.index('<script type="application/json" id="ex-data">')
    s = s[:k] + tag + blob + "</script>\n" + s[k:]
for id_ in data:
    s = re.sub(r'\n\{"id": "' + re.escape(id_) + r'", [^\n]*\},', "", s)
k = s.index("const MATS = [") + len("const MATS = [")
s = s[:k] + "\n" + "\n".join(mats) + s[k:]
open(SRC, "w", encoding="utf-8").write(s)
print("telc:", list(data))
