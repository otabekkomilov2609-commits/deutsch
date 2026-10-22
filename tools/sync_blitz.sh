#!/bin/bash
# blitzdeutsch.uz — streber.uz'ning nusxasi (Blitz rejimi domen bo'yicha avtomatik yoqiladi). Har build+push'dan keyin ishga tushiriladi.
set -e
SRC=/home/claude/deutsch; DST=/home/claude/blitz
APP=$(grep -o 'app\.[0-9a-f]*\.js' $SRC/index.html | head -1)
mkdir -p $DST; cd $DST; [ -d .git ] || { git init -q -b main; git remote add origin https://github.com/otabekkomilov2609-commits/blitz; }
rsync -a --delete --exclude .git --exclude src --exclude tools --exclude QOLLANMA.md --exclude CNAME --exclude aufnahme.html --exclude 'app.*.js' $SRC/ $DST/
cp $SRC/$APP $DST/
echo blitzdeutsch.uz > CNAME; touch .nojekyll
git add -A; git commit -qm "sync from streber ($(git -C $SRC rev-parse --short HEAD))" || true
git push -q -u origin main
