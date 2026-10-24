# B1 grammatika — mustaqil tekshiruv (review)

Siz yozilgan mashq to'plamlarini tekshiruvchi tajribali nemis tili o'qituvchisi (DaF, B1) va muharrirsiz. Fayllar: `/home/claude/deutsch/tools/b1g/B1-L{N}.json`. Qoidalar va item turlari: `SPEC.md` (to'liq o'qing).

## Nimani tekshirasiz (har bir item)

1. **Nemischa to'g'riligi** — artikl, kelishik oxiri, Adjektivdeklination, fe'l o'rni (Nebensatz — oxirida), vergul (Nebensatz oldidan, «sondern»/«aber» oldidan), umlaut/ß, katta-kichik harf, Konjunktiv/Passiv shakllari. Tabiiy nemis tilimi? Sun'iy/g'alati gap bo'lsa — tabiiyroq qiling.
2. **Javob yagonami?**
   - `mc`: faqat bitta variant to'g'ri; distraktorlar aniq noto'g'ri, lekin real o'quvchi xatosi.
   - `gap`: `a` da hamma to'g'ri variantlar bormi (masalan desto/umso, wäret/wärt). `h` da `*…*` variantlar sanalgan bo'lsa — javob ular orasida.
   - `order`: `w` plitkalaridan tuzilishi mumkin bo'lgan BOSHQA to'g'ri tartiblar `alt` da bormi? Bo'lmasa — qo'shing (o'quvchi to'g'ri tuzsa-yu xato deyilmasin). Chegaraviy (marginal) tartiblar — plitkalarni birlashtirib (`"die Meldung"` → bitta plitka) yo'q qiling.
   - `mark` (belgilash): belgilanadigan so'zlar aniqmi? Boshqa so'zni belgilash ham mantiqan to'g'ri bo'lib qolmaydimi?
   - `mark`+`fix` (Xatoni toping): xato BITTA so'zning noto'g'ri SHAKLI bo'lsin (noto'g'ri artikl/oxir/fe'l shakli/bog'lovchi) — o'quvchi aynan shu so'zni bosadi. So'z tartibi xatolari (fe'l noto'g'ri joyda) va «tushib qolgan so'z» xatolari noaniq — ularni shakl xatosiga almashtiring (yangi gap yozing). `fix` — to'g'ri gap, `a` — xato so'z indeksi (`s.split(" ")` bo'yicha, tinish belgilar alohida).
3. **Izohlar (gw.uz / gw.ru, info)** — grammatik jihatdan to'g'rimi, aniq va qisqami, misol to'g'rimi. O'zbekcha — tabiiy, lotin, `‘` (o‘, g‘), `’` (fe’l). Ruscha — tabiiy.
4. **Daraja va mavzu** — so'zlar A2–B1, Lektion mavzusiga mos; ish hayoti vaziyati yo'q; real siyosatchi/brend yo'q.
5. **info jadvallari** — HTML to'g'ri yopilganmi; `rowspan`/`colspan` ishlatilgan bo'lsa — oddiy jadvalga almashtiring (sayt CSS'i qo'llamaydi).

## Qanday ishlaysiz

- Xatoni topsangiz — **faylning o'zida tuzating** (JSON tuzilishini saqlab). Python bilan o'qib-yozing: `json.load` → o'zgartirish → `json.dump(d, f, ensure_ascii=False, indent=1)`.
- Har bir fayldan keyin: `python3 /home/claude/deutsch/tools/b1g/check.py /home/claude/deutsch/tools/b1g/B1-L{N}.json` → OK bo'lsin.
- Boshqa fayllarga (src/index.html, git, boshqa Lektionlar) tegmang.
- Oxirida hisobot: har bir Lektion — nechta item tuzatildi va eng muhim tuzatishlar (oldin → keyin), 3–8 qator.

## Mualliflar o'zlari shubhalangan joylar (albatta ko'ring va hal qiling)

- **L1**: als-gaplarda Präteritum va Perfekt aralash — me'yor, lekin bitta gap ichida izchil bo'lsin.
- **L2**: order q: «Ich frage oft meinen Bruder, weil …» — tabiiyroq qiling.
- **L3**: Wortbildung «___ Glückwunsch zum Geburtstag! (Herz)» → Herzlichen — juda qiyin bo'lsa almashtiring.
- **L4**: order «… damit sie die Regeln besser versteht» — «besser die Regeln» marginal: plitkalarni birlashtiring; chat javobi «Um vor dem Unterricht noch joggen zu gehen.» — to'liq gapga aylantiring.
- **L5**: birlashtirilgan plitkalar («Wenn ich», «würde ich») — mantiqli bo'lsin; «Wenn du nicht so laut Musik hören würdest» — tabiiyroq.
- **L7**: Kleinanzeige qisqa shakllari («Verkaufe gebrauchten Rucksack») — e'lon uslubi, to'g'ri; boshqa gaplar tabiiy bo'lsin.
- **L8**: gap topshirig'i «mit oder ohne „zu"» — tushunarli bo'lsin.
- **L9**: «Wegen den vielen Prüfungen» xato sifatida — qoldirish mumkin (yozma me'yor), izohda «og'zaki nutqda uchraydi, yozmada — Genitiv» deb yozing.
- **L11**: Xatoni toping 2: «Das ist der Becher, dem ich … Tee trinke» — haqiqiy xato «aus» tushib qolgani, belgilanadigan «dem» — noaniq. Almashtiring (masalan: «Das ist die Freundin, die ich gestern geholfen habe.» → der).
- **L12**: forum gap «… sodass ich auch eine machen wollte» — natija mantiqi bo'sh, almashtiring; Xatoni toping 4: «so scharf, sodass» — noaniq, shakl xatosiga almashtiring.
- **L13**: «Sie lassen weder die Blumen noch die Tomaten in Ruhe» — B1 uchun murakkab bo'lsa, oddiyroq.
- **L14**: «wo» bilan gaplar — me'yorga mos; Xatoni toping «wo ich möchte studieren» — so'z tartibi xatosi → shakl xatosiga almashtiring.
- **L15**: «Lena lässt ihr Kleid reinigen, denn sie will schön aussehen.» — tabiiyroq.
- **L16**: «Je länger spare ich» — so'z tartibi xatosi → shakl xatosiga almashtiring.
- **L17**: order «Laylo hat ihre Angst verloren, indem sie ihre Bilder im Café gezeigt hat.» — mantiq; «gepostet» — so'zlashuv, mumkin.
- **L19**: «Konditorei», «Metzgerei» — qiyin bo'lsa, oddiyroq misollar (Bäckerei).
- **L20**: order «Du brauchst die Meldung nicht zu teilen.» — «nicht die Meldung» varianti: plitkalarni birlashtiring yoki hal qiling.
- **L22**: forum gapda Vergangenheit guruhida Gegenwart («als ob ich eine große Prüfung hätte») — guruhga mos qiling.
- **L24**: info jadvalida `rowspan` — oddiy jadvalga almashtiring.
