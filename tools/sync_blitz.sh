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
echo blitzdeutsch.uz > CNAME; touch .nojekyll
git add -A; git commit -qm "sync from streber ($(git -C $SRC rev-parse --short HEAD))" || true
git push -q -u origin main
