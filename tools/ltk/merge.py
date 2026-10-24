#!/usr/bin/env python3
"""Live test Kommunikation bankini src/index.html ga qo'shadi: <script id="ltk-data"> {A1:{"1":[…]},A2:…,B1:…}.
Faqat check.py'dan o'tgan fayllar olinadi. Takror ishga tushirsa — yangilaydi."""
import json, os, glob, re, subprocess, sys

SRC = "/home/claude/deutsch/src/index.html"
DIR = os.path.dirname(os.path.abspath(__file__))
data = {}
for p in sorted(glob.glob(os.path.join(DIR, "*-[ab].json"))):
    L = re.search(r"(A1|A2|B1)-[ab]\.json$", p).group(1)
    if subprocess.run([sys.executable, os.path.join(DIR, "check.py"), p], capture_output=True).returncode:
        print("✗ o'tkazib yuborildi (check.py):", p); continue
    data.setdefault(L, {}).update(json.load(open(p, encoding="utf-8")))
s = open(SRC, encoding="utf-8").read()
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in blob.lower()
tag = '<script type="application/json" id="ltk-data">'
if tag in s:
    i = s.index(tag) + len(tag); j = s.index("</script>", i); s = s[:i] + blob + s[j:]
else:
    k = s.index('<script type="application/json" id="ex-data">')
    s = s[:k] + tag + blob + "</script>\n" + s[k:]
open(SRC, "w", encoding="utf-8").write(s)
print("ltk:", {L: sum(len(v) for v in d.values()) for L, d in data.items()})
