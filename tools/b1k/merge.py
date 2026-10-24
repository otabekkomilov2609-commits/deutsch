#!/usr/bin/env python3
"""B1 Kommunikation JSON'larini src/index.html ga qo'shadi: ex-data (mashq) + MATS (Lektion kartasidagi yozuv).
Takror ishga tushirilsa — eskisini yangilaydi. Foydalanish: python3 merge.py [L raqamlari...] (bo'sh — hammasi)"""
import json, os, re, sys, glob

SRC = "/home/claude/deutsch/src/index.html"
DIR = os.path.dirname(os.path.abspath(__file__))

def main(nums):
    s = open(SRC, encoding="utf-8").read()
    tag = '<script type="application/json" id="ex-data">'
    i = s.index(tag) + len(tag); j = s.index("</script>", i)
    ex = json.loads(s[i:j])
    files = sorted(glob.glob(os.path.join(DIR, "B1-L*-K.json")), key=lambda p: int(re.search(r"L(\d+)", p).group(1)))
    added = []
    mats_lines = []
    for p in files:
        n = int(re.search(r"L(\d+)-K\.json$", p).group(1))
        if nums and n not in nums:
            continue
        D = json.load(open(p, encoding="utf-8"))
        id_ = D["id"]; tab = "b11" if n <= 12 else "b12"
        ex[id_] = D["ex"]
        m = {"id": id_, "title": D["meta"]["title"], "stitle": D["meta"]["stitle"], "part": "k", "ic": "💬", "file": "", "thumb": "",
             "name": f"B1.{1 if n <= 12 else 2} Lektion {n} - K", "type": "uebung", "key": str(n), "pages": 0, "date": "2026-10-24",
             "lvl": "B1", "tab": tab, "ex": True, "beta": True, "noCur": True}
        mats_lines.append(json.dumps(m, ensure_ascii=False) + ",")
        added.append(id_)
    blob = json.dumps(ex, ensure_ascii=False, separators=(",", ":"))
    assert "</script" not in blob.lower()
    s = s[:i] + blob + s[j:]
    # MATS: eski B1 G yozuvlarini olib tashlab, yangisini qo'shamiz
    for id_ in added:
        s = re.sub(r'\n\{"id": "' + re.escape(id_) + r'", [^\n]*\},', "", s)
    k = s.index("const MATS = [") + len("const MATS = [")
    s = s[:k] + "\n" + "\n".join(mats_lines) + s[k:]
    open(SRC, "w", encoding="utf-8").write(s)
    print("qo'shildi:", len(added), added)

if __name__ == "__main__":
    main(set(int(x) for x in sys.argv[1:]))
