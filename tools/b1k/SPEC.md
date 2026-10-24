# B1 Kommunikation — onlayn mashq to'plami (streber.uz)

Har bir Momente B1 Lektioni uchun bitta «💬 Kommunikation» to'plami: shu Lektionning Redemittel'i (kommunikativ iboralari) vaziyatda o'rganiladi va telc Mündliche Prüfung'ga tayyorlaydi.
Natija — bitta JSON fayl: `/home/claude/deutsch/tools/b1k/B1-L{N}-K.json`.

## Qat'iy qoidalar
1. **Gaplar bizniki.** Momente/telc/Blitz kitob va varaqlaridan gap, dialog, qahramon ko'chirilmaydi. Redemittel (iboralar) — umumiy til birliklari, ularni ishlatish mumkin. Ismlar: Laylo, Timur, Malika, Aziz, Sevara, Nodir, Jonas, Lena, Paul, Mia …
2. **Ish hayoti yo'q** — o'quvchilar ishlamaydi (o'qish, kurs, universitet, sport, ko'ngilli ish, oila, do'stlar, sayohat, uy, bo'sh vaqt).
3. **Nemischa B1, 100% to'g'ri**, tabiiy og'zaki nutq. du/Sie — vaziyatga mos (do'stga du, rasmiyga Sie).
4. **Distraktorlar** — HAMMASI haqiqiy Redemittel, faqat boshqa funksiyadan yoki noto'g'ri registrdan (masalan, dalda kerak — variantlarda tanqid, taklif, rozilik iboralari). Ikkinchi to'g'ri javob bo'lmasin.
5. **Izohlar (gw)** — har item'da `{"uz","ru"}`, 1–2 gap: funksiya nima, qaysi ibora kalit (<b>…</b>). O'zbekcha lotin, `‘` (U+2018): o‘, g‘; fe’l — `’`. Bir xil `h` dagi itemlarda gw bir xil bo'lishi mumkin.
6. Topshiriq (`h`) nemischa, qisqa, Momente uslubida. Guruhning birinchi item'ida `bsp` (namuna) majburiy.

## Tuzilma
```json
{"id":"B1-b11-{N}-K","meta":{"title":"Kommunikation · …","stitle":"funksiya · funksiya"},
 "ex":{"title":"Lektion {N} · Kommunikation","sub":"funksiya · funksiya","lv":"B1.1","sec":[{"k":"komm","ic":"💬","t":"Kommunikation","items":[ … ]}]}}
```
L13–24: `B1-b12-{N}-K`, lv "B1.2".

## Qadamlar (jami 22–28 item, shu tartibda)
1. **info** (1 ta) — Redemittel kartasi: funksiyalar bo'yicha jadval (har funksiyada 3–5 ibora), pastda `ex-note` o'zbekcha izoh; `ru` — xuddi shu, izoh ruscha.
   `{"t":"info","h":"<h4>…</h4><table class=\"ex-tb\"><tr><th>Funktion</th><th>Redemittel</th></tr><tr><td>…</td><td>…<br>…</td></tr></table><p class=\"ex-note\">…</p>","ru":"…"}`
2. **cat** (1–2 ta) — iborani funksiyasi bo'yicha saralash: `{"t":"cat","h":"Was ist das? Ordnen Sie zu.","bsp":"…","c":["Funktion A","Funktion B"],"i":[["ibora",0],…],"gw":{…}}` (6–8 element).
3. **mc — Situationswahl** (5–6 ta): `{"t":"mc","h":"Was passt? Reagieren Sie.","bsp":"…","q":"Vaziyat yoki sherikning gapi (nemischa)","o":["…4 ta haqiqiy Redemittel…"],"a":i,"gw":{…}}`. Vaziyatlar xilma-xil (do'st, oila, kurs, forum).
4. **order — iborani qurish** (3 ta): `{"t":"order","h":"Bilden Sie Sätze.","bsp":"…","q":"Vaziyat (qisqa, nemischa)","w":[plitkalar],"a":"to'liq gap.","alt":[]}` — `w.join(" ")` = `a` (oxirgi .?! siz). 4–8 plitka.
   + **order dlg** (1 ta) — dialogni tartiblash: `{"t":"order","h":"Ordnen Sie das Gespräch.","dlg":1,"bsp":"…","w":["▪ …","● …",… 4–6 replika, ARALASH tartibda],"a":"replikalar to'g'ri tartibda BO'SH JOY bilan birlashtirilgan"}` — ▪ va ● navbatma-navbat; tartib yagona bo'lsin.
5. **gap — bosh harfdan tiklash** (4 ta): har bo'shliq — bitta so'z, oldida birinchi harf turadi: `"s":"W___ w___ e_ m__ einem Kinoabend?"` → `"a":[["ie"],["äre"],["s"],["it"]]` (bosh harfdan keyingi qismi!). `h`: "Ergänzen Sie die Redemittel." Faqat Lektion iboralari.
6. **chat — sherik bilan suhbat** (1–2 ta, telc Mündlich uslubida): oldindan yozilgan tarmoqli dialog.
```json
{"t":"chat","h":"Planen Sie gemeinsam: …","bsp":"(qisqa namuna)","who":"Timur","goal":["Vorschlag","Zustimmen","Widersprechen","Einigung"],
 "st":[{"p":"sherikning gapi","o":[{"s":"to'g'ri javob","ok":1,"g":0},{"s":"noto'g'ri javob","r":"sherikning qayta so'rovi (nemischa)","why":{"uz":"…","ru":"…"}},{"s":"…","r":"…","why":{…}}]}, … 4–6 qadam],
 "end":"sherikning yakuniy gapi","gw":{"uz":"…","ru":"…"}}
```
   Har qadamda 3 variant, aynan bittasi `ok:1`. Noto'g'ri variantlar — real xato: faqat «Ja, gut.» (telc'da ball yo'q), vaziyatga mos kelmaydigan funksiya, noto'g'ri register (du/Sie), mavzudan chiqish. `r` — sherik tabiiy reaksiya qiladi va qayta so'raydi («Hm, und was meinst du?»). `g` — to'g'ri javob qaysi `goal` ni bajaradi (indeks; bo'lmasa yozilmaydi). Oxirgi qadamda — Einigung (kelishuv).
7. **say — o'zingiz ayting** (3 ta): `{"t":"say","h":"Sagen Sie es auf Deutsch.","bsp":"…","q":"Vaziyat NEMISCHA qisqa (masalan: «Ihr Freund hat Angst vor der Prüfung. Machen Sie ihm Mut.»)","a":"namuna javob (1 gap, Lektion iborasi bilan)","gw":{…}}`

## O'zingizni tekshiring
`python3 /home/claude/deutsch/tools/b1k/check.py /home/claude/deutsch/tools/b1k/B1-L{N}-K.json` → OK. Har bir mc/chat qadamini barcha variantlar bilan qayta o'qing: faqat bitta to'g'ri. Oxirida qisqa hisobot.

## Lektionlar (Redemittel funksiyalari)
| N | Lektion | Kommunikation |
|---|---|---|
| 6 | Ich war ja vorher so aufgeregt! | **kritisch bewerten** (Also, ich bezweifle, dass … · Man muss auch sehen, dass … · Ich bin mir nicht sicher, ob …) · **Mut machen** (Das schaffst du bestimmt! · Das wird schon gut gehen! · Ich bin sicher, dass …) — chat: telc Teil 3 «Abend der Mutigen» rejalashtirish (ish emas: yoshlar markazi) |
| 8 | „Soziales Pflichtjahr", ja oder nein? | **Meinung äußern** (Ich bin der Meinung, dass … · Meiner Meinung nach …) · **zustimmen** (Da stimme ich dir zu. · Das sehe ich genauso.) · **widersprechen** (Da bin ich anderer Meinung. · Das stimmt so nicht, denn …) · **Zweifel** — chat: telc Teil 2 «Soll ein soziales Jahr Pflicht sein?» munozara |
| 21 | Schule neu denken | **Vorschläge machen** (Wie wäre es, wenn … · Wir könnten … · Ich schlage vor, dass …) · **zustimmen / ablehnen** (Gute Idee! · Das finde ich nicht so gut, weil …) · **sich einigen** (Gut, dann machen wir es so. · Sind wir uns einig?) — chat: telc Teil 3 «Projekttag in der Schule» rejalashtirish |
