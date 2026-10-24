#!/usr/bin/env python3
"""Live test Kommunikation bankini tekshiradi: python3 check.py A2-a.json [...]"""
import json, re, sys, collections

LIM = {"A1": (15, 8), "A2": (20, 10), "B1": (25, 14)}
WORK = re.compile(r"\b(Chef|Chefin|Kolleg\w*|Firma|Büro|Kunde\w*|Abteilung|Meeting|Besprechung|Arbeitgeber|Vorgesetzt\w*)\b")

def words(t): return len(re.findall(r"[\wäöüÄÖÜß’'-]+", t))

def check(path):
    lvl = re.search(r"(A1|A2|B1)-([ab])\.json$", path)
    assert lvl, "fayl nomi: A1-a.json, A2-b.json …"
    L, half = lvl.group(1), lvl.group(2)
    qlim, olim = LIM[L]
    D = json.load(open(path, encoding="utf-8"))
    err, warn = [], []
    exp = [str(n) for n in (range(1, 13) if half == "a" else range(13, 25))]
    for n in exp:
        if n not in D: err.append(f"L{n}: yo'q")
    pos = collections.Counter()
    for n, qs in D.items():
        if n not in exp: err.append(f"L{n}: bu faylga tegishli emas")
        if len(qs) != 8: err.append(f"L{n}: {len(qs)} ta savol (8 kerak)")
        seen_a, seen_q = set(), set()
        for i, it in enumerate(qs):
            tag = f"L{n}#{i+1}"
            if set(it) - {"q", "o", "a"}: err.append(f"{tag}: ortiqcha kalit {set(it)-{'q','o','a'}}")
            q, o, a = it.get("q", ""), it.get("o", []), it.get("a")
            if not q.strip(): err.append(f"{tag}: q bo'sh")
            if len(o) != 4: err.append(f"{tag}: {len(o)} variant (4 kerak)"); continue
            if len(set(x.strip().lower() for x in o)) != 4: err.append(f"{tag}: takror variant")
            if not isinstance(a, int) or not 0 <= a <= 3: err.append(f"{tag}: a noto'g'ri"); continue
            pos[a] += 1
            if words(q) > qlim: warn.append(f"{tag}: savol uzun ({words(q)} so'z > {qlim})")
            for x in o:
                if not x.strip(): err.append(f"{tag}: bo'sh variant")
                if words(x) > olim: warn.append(f"{tag}: variant uzun ({words(x)} > {olim}): {x}")
                if not re.search(r"[.!?…“]$", x.strip()): warn.append(f"{tag}: tinish belgisi yo'q: {x}")
            ln = [len(x) for x in o]
            if ln[a] == max(ln) and ln[a] > 1.5 * sorted(ln)[-2]: warn.append(f"{tag}: to'g'ri javob boshqalardan ancha uzun")
            if '"' in q + "".join(o): warn.append(f"{tag}: \" o'rniga „…“ ishlating")
            if WORK.search(q + " " + " ".join(o)): warn.append(f"{tag}: ish hayoti so'zi? {WORK.search(q+' '+' '.join(o)).group(0)}")
            if o[a].strip().lower() in seen_a: warn.append(f"{tag}: to'g'ri javob takrorlandi")
            seen_a.add(o[a].strip().lower())
            if q.strip().lower() in seen_q: err.append(f"{tag}: savol takror")
            seen_q.add(q.strip().lower())
    tot = sum(pos.values())
    if tot and max(pos.values()) - min(pos[k] for k in range(4)) > tot * 0.15: warn.append(f"a taqsimoti notekis: {dict(pos)}")
    print(f"{path}: {tot} savol · a={dict(sorted(pos.items()))}")
    for e in err: print("  ✗", e)
    for w in warn: print("  !", w)
    print("  OK" if not err else f"  {len(err)} XATO")
    return not err

if __name__ == "__main__":
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
