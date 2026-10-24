# telc Deutsch B1 — Prüfungstraining to'plamlari (streber.uz)

Har bir Momente B1 Lektioniga bitta telc qismi: o'quvchi saytda imtihon formatida ishlaydi, oxirida tekshiriladi, har bir javobga o'zbekcha/ruscha izoh chiqadi.

## Qat'iy qoidalar
1. **Matn 100% bizniki.** Momente, telc, Blitz yoki boshqa manbadan gap/matn ko'chirilmaydi. Shaxs, joy, firma, raqam — to'qima (oddiy ismlar: Laylo, Timur, Malika, Jonas, Lena, Paul, Mia, Sevara …). Real brend/siyosatchi yo'q.
2. **Ish hayoti yo'q** — o'quvchilar ishlamaydi: vaziyatlar — o'qish, universitet, kurs, sayohat, sport, ko'ngilli ish, oila, do'stlar, uy-joy, bo'sh vaqt.
3. **Nemischa B1, 100% to'g'ri** (artikl, kelishik, fe'l o'rni, vergul, ß/umlaut). Tabiiy, telc uslubidagi matn. Har bir gapni qayta tekshiring.
4. **Javob yagona.** Har bir slotda faqat bitta to'g'ri javob; distraktorlar grammatik/ma'no jihatdan aniq noto'g'ri, lekin real o'quvchi xatosi (telc uslubi: mavzu to'g'ri, tafsilot mos emas).
5. **Lektion so'zlari va grammatikasi** ishlatilsin (pastdagi jadval).
6. **why** — har bir slot uchun izoh: `{"uz":"…","ru":"…"}`, 1–2 gap. To'g'ri javob NIMA UCHUN to'g'ri va qopqon nima. Kalit so'zni «…» bilan ko'rsating. O'zbekcha lotin, `‘` (U+2018): o‘, g‘; fe’l — `’`.
7. **tip** — bitta strategiya maslahati (uz/ru), 1–2 gap.

## Fayl: `/home/claude/deutsch/tools/telc/B1-L{N}-T.json`

Umumiy maydonlar:
```json
{"id":"B1-b11-{N}-T","lek":N,"lv":"B1.1","part":"sb2","title":"Sprachbausteine Teil 2","sub":"Wortschatz im Text","min":12,
 "h":"(telc uslubidagi nemischa topshiriq)","tip":{"uz":"…","ru":"…"},"src":"Text: streber.uz · Personen und Orte erfunden", … , "why":[…]}
```

### part "sb2" — Sprachbausteine Teil 2 (10 bo'shliq, 15 so'z, har biri bir marta)
```json
"text":"Überschrift\nAnrede,\nText … [1] … [2] … [10] …\nGruß",
"bank":["…15 ta so'z…"], "a":[bank indeksi har bo'shliq uchun, 10 ta, hammasi har xil]
```
`[n]` — bo'shliq belgisi (1–10, tartib bilan). 5 ta ortiqcha so'z — mumkin bo'lgan, lekin hech qaysi bo'shliqqa mos kelmaydigan (har bir bo'shliqni 15 so'zning hammasi bilan tekshiring!). Bank alifbo tartibida.
min: 12

### part "sb1" — Sprachbausteine Teil 1 (10 bo'shliq, a/b/c — grammatika)
```json
"text":"… [1] … [10] …", "o":[["a","b","c"] × 10], "a":[0|1|2 × 10]
```
Xat/e-mail (shaxsiy yoki yarim rasmiy). Bo'shliqlar: konnektorlar, artikl/oxir, predlog, fe'l shakli, olmosh, tayyor iboralar. Javob harflari teng taqsimlangan. min: 12

### part "l1" — Lesen Teil 1 (5 matn, 10 sarlavha, har matnga bitta)
```json
"texts":["matn 1 (60–90 so'z)", … 5], "heads":["sarlavha a", … 10], "a":[heads indeksi × 5, hammasi har xil]
```
5 ta ortiqcha sarlavha — mavzusi yaqin (qopqon), lekin hech qaysi matnga to'liq mos emas. min: 15

### part "l2" — Lesen Teil 2 (bitta matn ~300 so'z, 5 savol a/b/c)
```json
"text":"Überschrift\n… (abzaslar \n bilan)", "q":[{"s":"savol/gap boshi","o":["a","b","c"]} × 5], "a":[0|1|2 × 5]
```
Javob matndagi so'zlar bilan emas, boshqacha ifodalangan; noto'g'ri variantlarda matndagi so'zlar bor, lekin ma'no boshqa. Savollar matn tartibida. min: 15

### part "l3" — Lesen Teil 3 (10 vaziyat, 12 e'lon; bitta vaziyatga mos e'lon yo'q → "x")
```json
"sits":["Ihr Freund … sucht …" × 10], "ads":[{"t":"e'lon sarlavhasi","body":"e'lon matni (25–45 so'z)"} × 12], "a":[ads indeksi yoki -1 (=x) × 10]
```
Har e'lon ko'pi bilan bir marta. Aynan bitta vaziyat -1. Qopqon: mavzu to'g'ri, tafsilot (vaqt, narx, kishi soni, joy, «mit Hund», yosh) mos emas. min: 10

## O'zingizni tekshiring
- `python3 /home/claude/deutsch/tools/telc/check.py /home/claude/deutsch/tools/telc/B1-L{N}-T.json` → OK.
- Har slotni boshqa barcha variantlar bilan o'qib chiqing — ikkinchi to'g'ri javob yo'qmi?
- Oxirida qisqa hisobot: matn mavzusi, qaysi grammatika/so'zlar ishlatildi, shubhali joylar.

## Lektionlar
| N | Lektion | Mavzu va so'zlar | Grammatika | part |
|---|---|---|---|---|
| 1 | Das weiß ich noch genau! | Lebensphasen: Kindheit, Jugend, Schulzeit, Erinnerung, Erlebnis, Gefühl, Geburt, Erwachsene, sich erinnern an | als / wenn | sb2 |
| 2 | Beste Freunde | Freundschaft: Freundeskreis, Geheimnis, Entscheidung, eng, virtuell, vertrauen, sich verlassen auf | darum/daher/deswegen; Adjektive als Nomen | l1 |
| 3 | Das ist genau mein Ding! | Stärken: geduldig, kreativ, zuverlässig, Selbstvertrauen, Stärke, Schwäche | Komparativ/Superlativ vor dem Nomen (+ L1 als/wenn, L2 deswegen) | sb1 |
| 5 | Wär' das etwas für dich? | Wohnen: WG, Gemeinschaft, Einrichtung, Rücksicht, Missverständnis, Mehrgenerationenhaus | Konjunktiv II (wäre, hätte, würde) | l2 |
| 7 | Allein unterwegs | Reisen: Reiseführer, Sehenswürdigkeit, Erholung, Unterkunft, zentrale Lage, gebraucht, Kleinanzeige | Adjektive ohne Artikel (e'lonlarda: «günstige Zimmer, mit eigenem Bad») | l3 |
