# B1 grammatika mashqlari — yozish qo'llanmasi (streber.uz)

Maqsad: Momente B1 (Hueber) har bir Lektioni uchun saytdagi onlayn **Grammatik** mashq to'plamini yozish.
Natija — bitta JSON fayl: `/home/claude/deutsch/tools/b1g/B1-L{N}.json` (N = 1…24).

## 1. Qat'iy qoidalar

1. **Gaplar o'zimizniki.** Momente kitobidagi gaplar, qahramonlar (Luisa, Fridolin, Mirko …) va matnlar KO'CHIRILMAYDI. Mavzu va so'zlar Lektion mavzusidan; gap, vaziyat, ism — yangi. Ismlar: aralash (Aziz, Laylo, Malika, Timur, Nodir, Sevara, Jonas, Lena, Paul, Mia, Ben, Anna …).
2. **Til darajasi:** grammatika — shu Lektionning B1 grammatikasi; so'zlar — A2–B1, Lektion mavzusidan (pastdagi jadvalga qarang). Ekzotik so'z yo'q.
3. **Nemischa 100% to'g'ri bo'lsin.** Har bir gapni qayta o'qing: artikl, kelishik oxiri, fe'l o'rni, vergul (Nebensatz oldidan vergul shart), umlaut (ä ö ü ß). Bitta xato ham qabul qilinmaydi. Shubhali gapni yozmang — oddiyroq gap yozing.
4. **Topshiriq (h) nemischa**, qisqa, Momente uslubida: «Ergänzen Sie.», «Verbinden Sie die Sätze mit *obwohl*.», «Markieren Sie den Fehler.» …
5. **Izoh (gw)** — har bir item'da, o'zbekcha (`uz`) va ruscha (`ru`). Qisqa (1–3 gap): qoida + bitta misol (<b>…</b> bilan). O'zbekcha lotin yozuvida, apostrof belgisi `‘` (U+2018): o‘, g‘, so‘z, bo‘ladi. Bir xil `h` dagi itemlarda `gw` odatda bir xil (guruh izohi).
6. **Lösung yo'q alohida** — javoblar JSON ichida (a, alt, fix).
7. Hech qanday ish hayotiga tayangan savol emas (o'quvchilar ishlamaydi) — «Fokus Beruf» olinmaydi. Ish mavzusidagi Lektionlarda (L6, L10, L14, L19) vaziyat — o'qish, amaliyot, kelajak rejasi, tanishlar haqida.

## 2. Fayl tuzilishi

```json
{
  "id": "B1-b11-6-G",                      // L1–12: b11, L13–24: b12
  "meta": {"title": "Grammatik · obwohl · trotzdem", "stitle": "obwohl · trotzdem · Verb am Ende"},
  "ex": {
    "title": "Lektion 6 · Grammatik",
    "sub": "obwohl · trotzdem · Verb am Ende",
    "lv": "B1.1",                           // L13–24: "B1.2"
    "sec": [{"k":"gram","ic":"📘","t":"Grammatik","items":[ … ]}]
  }
}
```

`meta.stitle` va `ex.sub` bir xil (3–5 qisqa bo'lak, « · » bilan).

## 3. Item turlari (faqat shular)

Har bir item'da: `t`, `h` (topshiriq), `bsp` (namuna, guruhning birinchi itemida majburiy, qolganlarida ham bo'lishi mumkin — bir xil), `gw` {uz, ru}. `info`da gw yo'q.

**info** — qoida ekrani:
```json
{"t":"info","h":"<h4>…</h4><table class=\"ex-tb\"><tr><th>…</th><th>…</th></tr><tr><td>…</td><td>…</td></tr></table><p class=\"ex-note\">…</p>","ru":"<h4>…</h4>… (xuddi shu, izoh ruscha)"}
```
`h` — nemischa jadval + o'zbekcha qisqa izoh (`ex-note`); `ru` — xuddi shu jadval, izoh ruscha. Muhim so'zlar `<b>`. 1–3 ta info (Lektionda 2 mavzu bo'lsa — har biriga).

**mark** — gapdagi so'z(lar)ni belgilash (Taniyman):
```json
{"t":"mark","h":"Markieren Sie das Verb im Nebensatz.","bsp":"…","s":"Ich bleibe heute zu Hause , obwohl das Wetter schön ist .","a":[10],"gw":{…}}
```
`s` — so'zlar BITTA BO'SH JOY bilan ajratilgan; tinish belgilari ham alohida «so'z» (` , ` ` .`). `a` — belgilanishi kerak bo'lgan so'zlarning indekslari (0 dan; `s.split(" ")` bo'yicha). Bir nechta bo'lishi mumkin.

**mark + fix** — Xatoni toping:
```json
{"t":"mark","h":"Markieren Sie den Fehler.","bsp":"…","s":"Obwohl er müde war , er ist zum Training gegangen .","a":[5],"fix":"Obwohl er müde war, ist er zum Training gegangen.","gw":{…}}
```
`a` — xato so'z(lar) indeksi (odatda 1 ta, ko'pi bilan 2). `fix` — to'g'ri gap (oddiy yozilishda). Xato — real o'quvchi xatosi (fe'l o'rni, kelishik oxiri, bog'lovchi …).

**gap** — bo'sh joy:
```json
{"t":"gap","h":"Ergänzen Sie *wegen* oder *trotz*.","bsp":"…","s":"___ des Regens sind wir spazieren gegangen.","a":[["Trotz"]],"gw":{…}}
```
`s` dagi har bir `___` uchun `a` da bitta ro'yxat (to'g'ri variantlar). Gap boshida — katta harf bilan. Agar `h` da `*a*`, `*b*` yulduzcha bilan 2–6 variant sanalsa — sayt tugmalar ko'rsatadi (shunda guruhning HAMMA itemlari javobi o'sha variantlardan bo'lsin). Ikki qismli: `"s":"Ich trinke ___ Kaffee ___ Tee.","a":[["weder"],["noch"]]`.
**Kontekst qadami:** bitta gap emas, 3–5 gaplik qisqa chat/forum posti ham bo'lishi mumkin — `s` da `\n` bilan qatorlar, bir nechta `___`.

**mc** — tanlash:
```json
{"t":"mc","h":"Was passt?","bsp":"…","q":"Ich lerne jeden Tag, ___ ich die Prüfung bestehe.","o":["damit","um","obwohl"],"a":0,"gw":{…}}
```
`a` — to'g'ri variant indeksi. 2–4 variant. Distraktorlar — real xatolar, ikkinchi to'g'ri javob bo'lib qolmasin.

**cat** — saralash:
```json
{"t":"cat","h":"Ordnen Sie zu.","bsp":"…","c":["Verb am Ende","Verb auf Position 2"],"i":[["weil",0],["deshalb",1], …],"gw":{…}}
```
4–8 element.

**order** — gap tuzish (plitkalar). B1 da ikki vazifa:
- *Bog'lash* — ikki gapni berilgan bog'lovchi bilan bitta gap qilish;
- *Qayta yozish* — gapni boshqa shaklga o'tkazish (Aktiv→Passiv, damit→um … zu, weil→wegen …).
```json
{"t":"order","h":"Verbinden Sie die Sätze mit *obwohl*.","bsp":"Ich bin müde. Ich lerne. → <b>Obwohl ich müde bin, lerne ich.</b>","q":"Es regnet. Wir gehen spazieren.","w":["Obwohl","es","regnet,","gehen","wir","spazieren"],"a":"Obwohl es regnet, gehen wir spazieren.","alt":[],"gw":{…}}
```
- `q` — berilgan gap(lar) (o'quvchi tepada ko'radi).
- `w` — to'g'ri gapning plitkalari; birlashtirilganda (`w.join(" ")`) `a` ning oxirgi `.?!` siz ko'rinishiga AYNAN teng bo'lsin. Vergul oldingi so'zga yopishgan (`"regnet,"`). 4–10 plitka. Ko'p so'zli birikma bitta plitka bo'lishi mumkin (`"zum Training"`).
- `alt` — xuddi SHU plitkalardan tuziladigan boshqa to'g'ri tartiblar (bo'lsa). Masalan `w` da vergul bo'lgani uchun odatda boshqa tartib bo'lmaydi → `[]`. Agar `"Heute"`/`"heute"` kabi katta-kichik harf farqi tartibni belgilasa — yaxshi, ikkinchi to'g'ri javob qolmaydi.
- Javob yagona bo'lishi uchun bog'lovchi gap boshida bo'lsa — u bosh harf bilan (`"Obwohl"`), oxirida bo'lsa — kichik harf va oldingi so'zda vergul.

## 4. Mashq tarkibi (har bir Lektion)

Jami **30–38 item**, 6–8 qadam (qadam = ketma-ket bir xil `h` dagi itemlar):

1. **info** (1–3 ta) — Relevanz → Struktur → Beispiel: jadval, rangli muhim so'zlar.
2. **Taniyman** — `mark`, 4 item (bog'lovchi/fe'l/kelishikni belgilash).
3. **Tanlayman** — `mc` yoki `cat`, 4–5 item.
4. **To'ldiraman (kontekstda)** — `gap`, 6–8 item; kamida 2 tasi 3–5 gaplik chat/forum posti ichida.
5. **Bog'layman / Qayta yozaman** — `order` (q bilan), 6–8 item. Grammatikaga qarab: bog'lovchi Lektionlarida — bog'lash; Passiv, um…zu, wegen, Konjunktiv, Futur, Plusquamperfekt, lassen, brauchen…zu — qayta yozish.
6. **Xatoni toping** — `mark`+`fix`, 4 item.
7. **Wortbildung** (shu Lektionda bo'lsa) — `gap` yoki `cat`, 4–6 item + bitta qisqa `info`.

Itemlarda qiyinlik asta-sekin oshsin. Bitta qadamda bir xil konstruksiya takrorlanmasin — gaplar xilma-xil.

## 5. Lektionlar

| L | id | Lektion | Mavzu / so'zlar | Grammatika | Wortbildung |
|---|---|---|---|---|---|
| 1 | B1-b11-1-G | Das weiß ich noch genau! | Lebensphasen: Kindheit, Jugend, Schulzeit, Erinnerung, Erlebnis, Gefühl, Geburt, Alter, Erwachsene; sich erinnern an | Konnektor **als** (einmalig, Vergangenheit) vs **wenn** (wiederholt / Gegenwart, Zukunft) — Nebensatz, Verb am Ende; immer wenn | — |
| 2 | B1-b11-2-G | Beste Freunde | Freundschaft: Freundeskreis, Geheimnis, Entscheidung, Verbundenheit, eng, virtuell, vertrauen | **darum · daher · deswegen** (= deshalb; Hauptsatz, Verb auf Position 2 danach), Kontrast mit **weil** | **Adjektive als Nomen**: der/die Bekannte, ein Bekannter, die Verwandten, der Erwachsene (Endungen wie Adjektiv) |
| 3 | B1-b11-3-G | Das ist genau mein Ding! | persönliche Stärken: geduldig, kreativ, zuverlässig, Selbstvertrauen, Stärke, Schwäche, vertrauen | **Adjektivdeklination im Komparativ und Superlativ**: ein wichtiger**er** Schritt, der wichtig**ste** Schritt, mit dem besten Freund | **Nomen + -lich**: Freund → freundlich, Ende → endlich, Gefahr → gefährlich, Herz → herzlich |
| 4 | B1-b11-4-G | Morgen, morgen …! | Veränderungen, Gewohnheiten: ändern, Gewohnheit, verzichten auf, Gehirn, Studie, Energie, tatsächlich | **damit / um … zu** (Ziel); gleiche Person → um … zu, verschiedene → damit | — |
| 5 | B1-b11-5-G | Wär' das etwas für dich? | Wohnen: Wohngemeinschaft, Gemeinschaft, Einrichtung, Bibliothek, Waschküche, Rücksicht, Missverständnis | **Konjunktiv II der Gegenwart mit wenn-Satz** (irreal): Wenn ich mehr Platz hätte, würde ich … / wäre / hätte / könnte | **Nomen + (n/s) + Nomen**: Geburtstag**s**kuchen, Toilette**n**papier, Wohnungstür, Arbeit**s**zimmer |
| 6 | B1-b11-6-G | Ich war ja vorher so aufgeregt! | Neuanfang, Mut: aufgeregt, Mut, Sicherheit, (un)abhängig, aufgeben, begegnen, sich trauen | **obwohl** (Nebensatz) ↔ **trotzdem** (Hauptsatz, Position 1/2) | — |
| 7 | B1-b11-7-G | Allein unterwegs | Reisen: Reiseführer, Sehenswürdigkeit, Erholung, verreisen, zentrale Lage, gebraucht, Kleinanzeige | **Adjektivdeklination mit Nullartikel** (ohne Artikel): beste Tipps, mit frischem Brot, bei schönem Wetter, günstige Zimmer | **Nomen + -chen** (Verkleinerung, Umlaut, immer *das*): das Häuschen, Brötchen, Kätzchen, Tischchen |
| 8 | B1-b11-8-G | „Soziales Pflichtjahr", ja oder nein? | Gesellschaft: Gesellschaft, Bürger, Ansicht, Meinung, Rede, Vorbereitung, Umwelt schützen | **Infinitiv mit zu**: Ich versuche, … zu …; Es ist wichtig, … zu …; Lust/Zeit haben, … zu …; trennbare: aufzuräumen | — |
| 9 | B1-b11-9-G | Trotzdem eine super Erfahrung! | Studium, Auslandsaufenthalt: Aufenthalt, Prüfung, Abschluss, Studiengebühr, Schwierigkeit, Dialekt, Mitbewohner | **wegen / trotz + Genitiv** + Adjektivdeklination im Genitiv: wegen des schlechten Wetters, trotz der netten Mitbewohner; weil→wegen, obwohl→trotz | — |
| 10 | B1-b11-10-G | Wie möchte ich arbeiten? | Arbeitswelt allgemein: Tätigkeit, Stelle, Sprachkurs, Aushilfe, Statistik, Rückmeldung | **bis · seit(dem) · bevor · während** (Temporalsätze, Verb am Ende) | — |
| 11 | B1-b11-11-G | Dinge, die den Alltag besser machen | Alltagsgegenstände: Kaffeebecher, Geldbörse, Strom, Rabatt, Verbraucher, giftig, sich eignen, herstellen | **Relativsätze im Dativ** (dem, der, dem, denen) **und mit Präposition** (mit dem, auf die, in dem …) | — |
| 12 | B1-b11-12-G | Das Auge isst mit. | Essen: Gericht, Zutat, Zwiebel, Mehl, Bohne, Senf, Trend, hungrig, enttäuscht | **sodass / so …, dass** (Folge) | **Nomen aus Verben** (Infinitiv als Nomen, immer *das*): aussehen → das Aussehen, essen → das Essen, kochen → das Kochen |
| 13 | B1-b12-13-G | Tauben, meine Lieblingstiere! | Tiere: Taube, Tiger, Hirsch, Nest, Feind, Nachwuchs, wild, faul, frech, in der Lage sein | **zweiteilige Konnektoren**: sowohl … als auch · nicht nur …, sondern auch · weder … noch | **Nomen + -lang**: jahrelang, stundenlang, tagelang, monatelang |
| 14 | B1-b12-14-G | Hast du dich schon beworben? | Bewerbung (Praktikum, Studienplatz, Freiwilligendienst): Anschreiben, Qualifikation, geeignet, Recherche | **Relativsätze mit was und wo**: alles/etwas/nichts/das Beste, was …; die Stadt, wo … | — |
| 15 | B1-b12-15-G | Perfekte Partnerschaft!?  | Film und Liebe: Darsteller, Titel, Streit, weinen, beeindrucken, humorvoll | **Verb lassen**: etwas machen lassen (Ich lasse mein Fahrrad reparieren), jemanden etw. tun lassen, lassen im Perfekt (hat … reparieren lassen) | — |
| 16 | B1-b12-16-G | Zwar nervig, aber wichtig | Banken und Geld: Bargeld, Konto, Zinsen, Schalter, Vermieter, Absicht, sich erkundigen | **je … desto/umso + Komparativ** (je mehr …, desto …) · **entweder … oder** · **zwar …, aber** | — |
| 17 | B1-b12-17-G | Wenn Wände sprechen | Kunst, Street-Art: Galerie, Öffentlichkeit, Publikum, Zeichnung, Fotografie, Malerin | **indem** (Wie? Mittel/Methode; Nebensatz) — Frage: Wie …? → indem … | **miss-**: Erfolg → Misserfolg, Vertrauen → Misstrauen, verstehen → missverstehen |
| 18 | B1-b12-18-G | Was ist Ihre Rolle? | Gesundheit: Praxis, Sprechstunde, Rezept, Wunde, Verband, Grippe, impfen, erkältet | **Plusquamperfekt** (hatte/war + Partizip II) und **nachdem** (nachdem + Plusquamperfekt, Hauptsatz Präteritum/Perfekt) | — |
| 19 | B1-b12-19-G | Mein Zeugnis wurde anerkannt. | Behörden: Antrag, Frist, verlängern, Bescheid, Dokument, Stipendium, offiziell, notwendig | **Passiv Präteritum** (wurde + Partizip II) **und Perfekt** (ist … worden) | **Beruf + -ei** (Bäcker → Bäckerei, Metzger → Metzgerei) · **Adjektiv + -isch** (Theorie → theoretisch, Praxis → praktisch, Politik → politisch) |
| 20 | B1-b12-20-G | Man braucht nur kurz nachzudenken. | Medien, Fake News: Meldung, Presse, Überzeugung, prüfen, behaupten | **brauchen + nicht / kein / nur + zu + Infinitiv** (= müssen nicht / nur müssen) · **ohne … zu / (an)statt … zu** | — |
| 21 | B1-b12-21-G | Schule neu denken | Schule: Schulfach, Aufsatz, Diktat, Klassenfahrt, Erziehung, Konkurrenz, Gymnasium | **Passiv Präsens mit Modalverb**: muss/kann/soll/darf + Partizip II + werden | — |
| 22 | B1-b12-22-G | Ein politisches Leben | Politik: Wahl, Parlament, Bundestag, Kompromiss, Einfluss, Hoffnung | **als ob + Konjunktiv II** (Er tut so, als ob er alles wüsste.) | — |
| 23 | B1-b12-23-G | Was wäre passiert, wenn …? | Geschichte, Ausflug: Grenze, Denkmal, Natur, Turm, Ausflug, Fähre, Pension | **Konjunktiv II der Vergangenheit** (hätte/wäre + Partizip II), mit **wenn**-Satz (irreal in der Vergangenheit) | — |
| 24 | B1-b12-24-G | Wahnsinn, wie die Zeit vergeht! | Zeit: Sekunde, Viertelstunde, Erfindung, Unterschrift, Druck, sich erholen | **Futur I** (werden + Infinitiv): Vermutung (wird wohl …), Vorhersage, Versprechen, Aufforderung (Du wirst jetzt …!) | — |

Uslub namunasi: `example_A2_L17_G.json`, `example_A2_L16_G.json` (A2 dagi tayyor to'plamlar — tuzilish, `gw` uzunligi va ohangi shu kabi bo'lsin).

## 6. O'zingizni tekshiring (yozib bo'lgach)

`python3 /home/claude/deutsch/tools/b1g/check.py /home/claude/deutsch/tools/b1g/B1-L{N}.json` — xatolar ro'yxatini chiqaradi (tuzilish, order plitkalari, mark indekslari, gap soni …). Xato qolmaguncha tuzating. Keyin har bir nemischa gapni yana bir marta o'qing.
