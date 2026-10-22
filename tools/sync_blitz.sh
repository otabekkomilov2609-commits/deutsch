#!/bin/bash
# blitzdeutsch.uz — streber.uz'ning nusxasi (Blitz rejimi domen bo'yicha avtomatik yoqiladi). Har build+push'dan keyin ishga tushiriladi.
set -e
SRC=/home/claude/deutsch; DST=/home/claude/blitz
APP=$(grep -o 'app\.[0-9a-f]*\.js' $SRC/index.html | head -1)
mkdir -p $DST; cd $DST; [ -d .git ] || { git init -q -b main; git remote add origin https://github.com/otabekkomilov2609-commits/blitz; }
python3 - "$SRC" "$DST" <<'P'
import sys,os,shutil,fnmatch; S,D=sys.argv[1:]
EX={".git","src","tools","QOLLANMA.md","CNAME","aufnahme.html"}
for n in os.listdir(D):
    if n!=".git": (shutil.rmtree if os.path.isdir(D+"/"+n) else os.remove)(D+"/"+n)
for n in os.listdir(S):
    if n in EX or fnmatch.fnmatch(n,"app.*.js"): continue
    (shutil.copytree if os.path.isdir(S+"/"+n) else shutil.copy2)(S+"/"+n,D+"/"+n)
P
cp $SRC/$APP $DST/

# Blitz brendi: sarlavha, belgi, manifest (2026-10-22)
python3 - "$DST" <<'P'
import sys,re,json; D=sys.argv[1]; f=D+"/index.html"; s=open(f,encoding="utf-8").read()
s=s.replace("<title>Streber — by Otabek Komilov</title>","<title>Blitz · Deutsch</title>")
s=s.replace('href="/icons/favicon.svg" type="image/svg+xml"','href="/icons/blitz-32.png" type="image/png"').replace('href="/icons/favicon-32.png"','href="/icons/blitz-32.png"').replace('href="/icons/apple-touch-icon.png"','href="/icons/blitz-180.png"')
s=s.replace('content="Streber"','content="Blitz"')
s=re.sub(r'(<meta (?:property|name)="(?:og:title|twitter:title)" content=")[^"]*"',r'\1Blitz · Deutsch"',s)
s=re.sub(r'(<meta (?:property|name)="(?:og:image|twitter:image)" content=")[^"]*"',r'\1https://blitzdeutsch.uz/icons/blitz-512.png"',s)
s=re.sub(r'(<meta (?:property|name)="(?:og:description|description|twitter:description)" content=")[^"]*"',r'\1Momente A1–B1: dars materiallari va sinf o‘yinlari — Blitz til markazi ustozlari uchun."',s)
open(f,"w",encoding="utf-8").write(s)
m=json.load(open(D+"/manifest.webmanifest",encoding="utf-8")); m.update({"name":"Blitz · Deutsch","short_name":"Blitz","description":"Blitz til markazi — dars materiallari va o‘yinlar","icons":[{"src":"/icons/blitz-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"/icons/blitz-512.png","sizes":"512x512","type":"image/png","purpose":"any"}]}); m.pop("shortcuts",None); m.pop("screenshots",None)
json.dump(m,open(D+"/manifest.webmanifest","w",encoding="utf-8"),ensure_ascii=False,indent=2)
P
echo blitzdeutsch.uz > CNAME; touch .nojekyll
git add -A; git commit -qm "sync from streber ($(git -C $SRC rev-parse --short HEAD))" || true
git push -q -u origin main
