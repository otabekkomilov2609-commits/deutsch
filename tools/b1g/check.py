#!/usr/bin/env python3
"""B1 grammatika JSON tekshiruvchisi. Foydalanish: python3 check.py B1-L6.json [...]"""
import json, re, sys

def norm(s):
    return re.sub(r"\s+", " ", str(s).replace("’", "'").replace("‘", "'")).strip()

def strip_end(s):
    return re.sub(r"[.?!]$", "", norm(s))

def check(path):
    E = []
    try:
        D = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"JSON o'qilmadi: {e}"]
    m = re.search(r"B1-L(\d+)\.json$", path)
    n = int(m.group(1)) if m else None
    tab = "b11" if n and n <= 12 else "b12"
    if n and D.get("id") != f"B1-{tab}-{n}-G":
        E.append(f"id noto'g'ri: {D.get('id')} (kutilgan B1-{tab}-{n}-G)")
    meta = D.get("meta") or {}
    for k in ("title", "stitle"):
        if not meta.get(k):
            E.append(f"meta.{k} yo'q")
    ex = D.get("ex") or {}
    if n and ex.get("title") != f"Lektion {n} · Grammatik":
        E.append(f"ex.title: {ex.get('title')}")
    if ex.get("lv") not in ("B1.1", "B1.2") or (n and ex.get("lv") != ("B1.1" if n <= 12 else "B1.2")):
        E.append(f"ex.lv: {ex.get('lv')}")
    if not ex.get("sub"):
        E.append("ex.sub yo'q")
    secs = ex.get("sec") or []
    if len(secs) != 1:
        E.append(f"sec soni {len(secs)} (1 bo'lishi kerak)")
        if not secs:
            return E
    items = secs[0].get("items") or []
    nq = sum(1 for it in items if it.get("t") != "info")
    if not (28 <= nq <= 42):
        E.append(f"savollar soni {nq} (30–38 kerak)")
    types = {}
    for k, it in enumerate(items):
        t = it.get("t")
        types[t] = types.get(t, 0) + 1
        P = f"#{k} ({t})"
        if t not in ("info", "mark", "gap", "mc", "cat", "order"):
            E.append(f"{P}: noma'lum tur")
            continue
        if not it.get("h"):
            E.append(f"{P}: h yo'q")
        if t == "info":
            if "<table" not in it.get("h", ""):
                E.append(f"{P}: info'da jadval yo'q")
            if not it.get("ru"):
                E.append(f"{P}: info.ru yo'q")
            continue
        gw = it.get("gw") or {}
        if not gw.get("uz") or not gw.get("ru"):
            E.append(f"{P}: gw.uz / gw.ru yo'q")
        if gw.get("uz") and "'" in re.sub(r"<[^>]+>", "", gw["uz"]).replace("’", ""):
            # o' g' — U+2018 bo'lishi kerak
            if re.search(r"[og]'", gw["uz"]):
                E.append(f"{P}: gw.uz da o' / g' — ‘ (U+2018) ishlating")
        if t == "mark":
            w = it.get("s", "").split(" ")
            a = it.get("a") or []
            if not a or any((not isinstance(i, int)) or i < 0 or i >= len(w) for i in a):
                E.append(f"{P}: a indeks noto'g'ri {a} (so'zlar: {len(w)})")
            if "  " in it.get("s", ""):
                E.append(f"{P}: s da ikki bo'sh joy")
            if it.get("fix") is not None and not it["fix"].strip():
                E.append(f"{P}: fix bo'sh")
        elif t == "gap":
            s = it.get("s", "")
            c = s.count("___")
            a = it.get("a") or []
            if c == 0 or c != len(a):
                E.append(f"{P}: ___ soni {c}, a soni {len(a)}")
            if any(not isinstance(x, list) or not x or not all(isinstance(v, str) and v.strip() for v in x) for x in a):
                E.append(f"{P}: a — ro'yxatlar ro'yxati bo'lsin [[\"…\"]]")
            ch = [x.strip() for x in re.findall(r"\*([^*]+)\*", it.get("h", ""))]
            if 2 <= len(set(ch)) <= 6:
                low = [x.lower() for x in ch]
                for al in a:
                    if isinstance(al, list) and not any(str(v).lower() in low for v in al):
                        E.append(f"{P}: h da variantlar sanalgan ({', '.join(ch)}), lekin javob {al} ular orasida yo'q")
        elif t == "mc":
            o = it.get("o") or []
            if not (2 <= len(o) <= 4):
                E.append(f"{P}: o soni {len(o)}")
            if not isinstance(it.get("a"), int) or not (0 <= it["a"] < len(o)):
                E.append(f"{P}: a indeks noto'g'ri")
            if len(set(o)) != len(o):
                E.append(f"{P}: takror variant")
            if not it.get("q"):
                E.append(f"{P}: q yo'q")
        elif t == "cat":
            c = it.get("c") or []
            ii = it.get("i") or []
            if len(c) < 2 or not (3 <= len(ii) <= 9):
                E.append(f"{P}: c/i soni")
            if any(not (isinstance(x, list) and len(x) == 2 and isinstance(x[1], int) and 0 <= x[1] < len(c)) for x in ii):
                E.append(f"{P}: i elementlari [matn, indeks] bo'lsin")
        elif t == "order":
            w = it.get("w") or []
            a = it.get("a", "")
            if not (3 <= len(w) <= 11):
                E.append(f"{P}: plitka soni {len(w)}")
            if norm(" ".join(w)) != strip_end(a):
                E.append(f"{P}: w.join ≠ a\n      w: {' '.join(w)}\n      a: {a}")
            for al in it.get("alt") or []:
                if sorted(norm(x) for x in w) != sorted(strip_end(al).split(" ")) and sorted(" ".join(w).split(" ")) != sorted(strip_end(al).split(" ")):
                    E.append(f"{P}: alt boshqa plitkalardan: {al}")
            if len(set(w)) != len(w):
                E.append(f"{P}: bir xil plitka ikki marta: {w}")
            if not it.get("q"):
                E.append(f"{P}: q (berilgan gap) yo'q")
    if types.get("info", 0) < 1:
        E.append("info yo'q")
    for need in ("mark", "gap", "order"):
        if types.get(need, 0) < 3:
            E.append(f"{need} kam ({types.get(need, 0)})")
    if not any(it.get("t") == "mark" and it.get("fix") for it in items):
        E.append("«Xatoni toping» (mark+fix) yo'q")
    # bir xil h guruhining birinchi itemida bsp
    prev = None
    for k, it in enumerate(items):
        if it.get("t") == "info":
            prev = None
            continue
        if it.get("h") != prev and not it.get("bsp"):
            E.append(f"#{k}: guruhning birinchi itemida bsp yo'q")
        prev = it.get("h")
    return E

if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        e = check(p)
        print(f"== {p}: {'OK' if not e else str(len(e)) + ' ta muammo'}")
        for x in e:
            print("  -", x)
        bad += len(e)
    sys.exit(1 if bad else 0)
