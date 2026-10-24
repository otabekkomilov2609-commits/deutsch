#!/usr/bin/env python3
"""telc to'plam tekshiruvchisi. python3 check.py B1-L1-T.json [...]"""
import json, re, sys

def why_ok(w):
    return isinstance(w, dict) and w.get("uz") and w.get("ru")

def check(p):
    E = []
    try:
        D = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return [f"JSON: {e}"]
    m = re.search(r"B1-L(\d+)-T\.json$", p)
    n = int(m.group(1)) if m else None
    if n and D.get("id") != f"B1-{'b11' if n <= 12 else 'b12'}-{n}-T":
        E.append(f"id: {D.get('id')}")
    for k in ("lek", "lv", "part", "title", "sub", "min", "h", "tip", "src", "a", "why"):
        if k not in D:
            E.append(f"{k} yo'q")
    if not why_ok(D.get("tip")):
        E.append("tip uz/ru")
    P = D.get("part")
    a = D.get("a") or []
    why = D.get("why") or []
    uzs = [D.get("tip", {}).get("uz", "")] + [w.get("uz", "") for w in why if isinstance(w, dict)]
    if any(re.search(r"[oOgG]'", u) for u in uzs):
        E.append("uz da o' / g' — ‘ (U+2018) ishlating")
    if P in ("sb1", "sb2"):
        t = D.get("text", "")
        nums = [int(x) for x in re.findall(r"\[(\d+)\]", t)]
        if nums != list(range(1, 11)):
            E.append(f"text bo'shliqlari [1]..[10] tartibda emas: {nums}")
        if len(a) != 10 or len(why) != 10:
            E.append(f"a/why soni {len(a)}/{len(why)} (10)")
        if P == "sb2":
            b = D.get("bank") or []
            if len(b) != 15 or len(set(b)) != 15:
                E.append(f"bank 15 ta har xil so'z bo'lsin ({len(b)})")
            if sorted(b, key=str.lower) != b:
                E.append("bank alifbo tartibida emas")
            if len(set(a)) != 10 or any(not (0 <= x < len(b)) for x in a):
                E.append(f"a — 10 ta har xil bank indeksi: {a}")
        else:
            o = D.get("o") or []
            if len(o) != 10 or any(len(x) != 3 or len(set(x)) != 3 for x in o):
                E.append("o — 10 × 3 har xil variant")
            if any(x not in (0, 1, 2) for x in a):
                E.append("a 0..2")
            c = [a.count(i) for i in range(3)]
            if max(c) - min(c) > 1:
                E.append(f"javob harflari notekis: {c}")
            if any(a[i] == a[i + 1] == a[i + 2] for i in range(len(a) - 2)):
                E.append("3 ta ketma-ket bir xil harf")
    elif P == "l1":
        tx, hd = D.get("texts") or [], D.get("heads") or []
        if len(tx) != 5 or len(hd) != 10:
            E.append(f"texts 5 / heads 10: {len(tx)}/{len(hd)}")
        if len(a) != 5 or len(set(a)) != 5 or any(not (0 <= x < 10) for x in a):
            E.append(f"a — 5 ta har xil heads indeksi: {a}")
        if len(why) != 5:
            E.append("why 5")
        for i, t in enumerate(tx):
            w = len(t.split())
            if not (45 <= w <= 110):
                E.append(f"text {i+1}: {w} so'z (60–90)")
    elif P == "l2":
        q = D.get("q") or []
        if len(q) != 5 or any(len(x.get("o", [])) != 3 for x in q):
            E.append("q 5 × 3 variant")
        if len(a) != 5 or any(x not in (0, 1, 2) for x in a):
            E.append("a 5 × 0..2")
        if len(why) != 5:
            E.append("why 5")
        w = len(D.get("text", "").split())
        if not (220 <= w <= 420):
            E.append(f"text {w} so'z (~300)")
    elif P == "l3":
        s, ad = D.get("sits") or [], D.get("ads") or []
        if len(s) != 10 or len(ad) != 12:
            E.append(f"sits 10 / ads 12: {len(s)}/{len(ad)}")
        if len(a) != 10 or a.count(-1) != 1:
            E.append(f"a 10 ta, aynan bitta -1: {a}")
        used = [x for x in a if x != -1]
        if len(set(used)) != len(used) or any(not (0 <= x < 12) for x in used):
            E.append(f"e'lon ikki marta yoki indeks xato: {a}")
        if len(why) != 10:
            E.append("why 10")
        for i, x in enumerate(ad):
            if not x.get("t") or not x.get("body"):
                E.append(f"ad {i}: t/body")
    else:
        E.append(f"part noma'lum: {P}")
    if any(not why_ok(w) for w in why):
        E.append("why elementlari uz/ru")
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
