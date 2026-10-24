#!/usr/bin/env python3
"""B1 Kommunikation tekshiruvchisi. python3 check.py B1-L6-K.json [...]"""
import json, re, sys

def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip()

def check(p):
    E = []
    try:
        D = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return [f"JSON: {e}"]
    m = re.search(r"B1-L(\d+)-K\.json$", p); n = int(m.group(1)) if m else None
    tab = "b11" if n and n <= 12 else "b12"
    if n and D.get("id") != f"B1-{tab}-{n}-K": E.append(f"id: {D.get('id')}")
    ex = D.get("ex") or {}
    if n and ex.get("title") != f"Lektion {n} · Kommunikation": E.append("ex.title")
    if n and ex.get("lv") != ("B1.1" if n <= 12 else "B1.2"): E.append("ex.lv")
    if not (D.get("meta") or {}).get("title") or not ex.get("sub"): E.append("meta.title / ex.sub")
    secs = ex.get("sec") or []
    if len(secs) != 1: return E + ["sec 1 ta bo'lsin"]
    its = secs[0].get("items") or []
    T = {}
    prev = None
    for k, it in enumerate(its):
        t = it.get("t"); T[t] = T.get(t, 0) + 1; P = f"#{k} {t}"
        if t not in ("info", "cat", "mc", "order", "gap", "chat", "say"): E.append(P + ": tur"); continue
        if t == "info":
            if "<table" not in it.get("h", "") or not it.get("ru"): E.append(P + ": jadval/ru")
            prev = None; continue
        gw = it.get("gw") or {}
        if not gw.get("uz") or not gw.get("ru"): E.append(P + ": gw")
        if re.search(r"[oOgG]'", gw.get("uz", "")): E.append(P + ": o' g' — ‘ ishlating")
        if it.get("h") != prev and not it.get("bsp"): E.append(P + ": guruh boshida bsp yo'q")
        prev = it.get("h")
        if t == "mc":
            o = it.get("o") or []
            if not (3 <= len(o) <= 4) or len(set(o)) != len(o) or not isinstance(it.get("a"), int) or not (0 <= it["a"] < len(o)) or not it.get("q"): E.append(P + ": mc")
        elif t == "cat":
            c, ii = it.get("c") or [], it.get("i") or []
            if len(c) < 2 or not (4 <= len(ii) <= 9) or any(not (isinstance(x, list) and len(x) == 2 and 0 <= x[1] < len(c)) for x in ii): E.append(P + ": cat")
        elif t == "order":
            w, a, j = it.get("w") or [], it.get("a", ""), it.get("j", " ")
            if j == "\n":
                if a != "\n".join(w) and sorted(a.split("\n")) != sorted(w): E.append(P + ": dlg a ≠ w")
            elif norm(" ".join(w)) != re.sub(r"[.?!]$", "", norm(a)): E.append(P + f": w.join ≠ a ({' '.join(w)} | {a})")
            if len(set(w)) != len(w) or not (3 <= len(w) <= 10): E.append(P + ": plitkalar")
        elif t == "gap":
            s, a = it.get("s", ""), it.get("a") or []
            if s.count("___") != len(a) or any(not isinstance(x, list) or not x for x in a): E.append(P + ": ___ / a")
        elif t == "say":
            if not it.get("q") or not it.get("a"): E.append(P + ": q/a")
        elif t == "chat":
            st, goal = it.get("st") or [], it.get("goal") or []
            if not it.get("who") or not (3 <= len(st) <= 7) or not it.get("end"): E.append(P + ": who/st/end")
            for qi, q in enumerate(st):
                o = q.get("o") or []
                if not q.get("p") or len(o) != 3 or sum(1 for x in o if x.get("ok")) != 1: E.append(P + f": qadam {qi} — 3 variant, bittasi ok")
                for x in o:
                    if not x.get("s"): E.append(P + f": qadam {qi} s yo'q")
                    if not x.get("ok") and (not x.get("r") or not (x.get("why") or {}).get("uz") or not (x.get("why") or {}).get("ru")): E.append(P + f": qadam {qi} noto'g'ri variantda r/why yo'q")
                    if x.get("ok") and "g" in x and not (0 <= x["g"] < len(goal)): E.append(P + f": qadam {qi} g indeks")
    nq = sum(v for k, v in T.items() if k != "info")
    if not (20 <= nq <= 30): E.append(f"item soni {nq} (22–28)")
    for need, mn in (("info", 1), ("cat", 1), ("mc", 5), ("order", 3), ("gap", 3), ("chat", 1), ("say", 3)):
        if T.get(need, 0) < mn: E.append(f"{need} kam ({T.get(need, 0)})")
    return E

if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        e = check(p); print(f"== {p}: {'OK' if not e else str(len(e)) + ' ta muammo'}")
        for x in e: print("  -", x)
        bad += len(e)
    sys.exit(1 if bad else 0)
