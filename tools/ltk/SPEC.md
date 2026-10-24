# 🎯 Live test · 💬 Kommunikation — savollar banki (streber.uz)

Ustoz Live test yaratganda «💬 Kommunikation» turini tanlaydi. O'quvchi telefonida **bitta vaziyat (nemischa)** va **4 ta javob (nemischa)** ko'radi, bittasini bosadi. Doskada jonli reyting. Savol proyektorda va telefonda **bir o'qishda tushunilishi** kerak.

Natija: `/home/claude/deutsch/tools/ltk/{LEVEL}-{a|b}.json` (a = L1–12, b = L13–24):
```json
{"1":[{"q":"…","o":["…","…","…","…"],"a":2}, … 8 ta], "2":[…], …}
```
`a` — to'g'ri variant indeksi (0–3). Variantlar o'yinda aralashtiriladi, lekin faylda ham a=0/1/2/3 taxminan teng taqsimlansin.

## Har bir Lektion uchun — 8 ta savol
- **Faqat shu Lektionning Kommunikation funksiyalari va Redemittel'i.** Funksiyalar ro'yxati: `ref/LEKS.txt` (6-ustun). A1/A2 uchun shu Lektionning tayyor mashqi: `ref/{LEVEL}-L{N}-K.json` (info/cat/gap/order/mc ichidagi iboralar — Redemittel manbai). B1 da ref yo'q bo'lsa — Momente B1 shu funksiya uchun beradigan standart Redemittel (masalan «Zweifel ausdrücken»: Ich bezweifle, dass … · Ich glaube nicht, dass … · Ich bin (mir) sicher, dass …).
- 8 savol Lektionning **hamma** funksiyalarini qamrasin (3 funksiya bo'lsa — taxminan 3+3+2).
- Grammatika va so'zlar — shu daraja (A1 juda sodda; A2 — A1.2–A2.1; B1 — B1).

## Savol (`q`)
- Nemischa, **qisqa**: A1 ≤ 15 so'z, A2 ≤ 20, B1 ≤ 25. Bitta vaziyat + kerak bo'lsa sherikning gapi „…“ ichida.
  Masalan: `Ihre Freundin hat morgen eine Prüfung und hat Angst. Was sagen Sie?` · `Timur: „Gehen wir am Samstag ins Kino?“ Sie haben keine Zeit.`
- Oxiri «Was sagen Sie?» / «Was antworten Sie?» / «Was fragen Sie?» bo'lishi mumkin — lekin har gal emas, vaziyatning o'zi aniq bo'lsa kerak emas.
- **Ish hayoti yo'q** — o'quvchilar ishlamaydi. Ofis, boshliq (Chef/Chefin), hamkasb (Kollege), firma, mijoz vaziyatlari YO'Q. Lektion mavzusi «Beruf» bo'lsa ham vaziyat: kurs, universitet, maktab, guruh loyihasi, WG, oila, do'stlar, sport klubi, ko'ngilli ish (FSJ), sayohat, qo'shnilar, shifokor, do'kon.
- Ismlar: Laylo, Timur, Malika, Aziz, Sevara, Nodir, Jonas, Lena, Paul, Mia, Frau Weber, Herr Braun …
- **Kitobdan ko'chirilmaydi:** Momente Kursbuch/Arbeitsbuch gaplari, dialoglari, qahramonlari (Vittorio, Nora va h.k.) yo'q. Redemittel (ibora) — umumiy til birligi, ishlatiladi; gap va vaziyat — bizniki.

## Variantlar (`o`) — eng muhim qism
Har bir noto'g'ri variant 4 savoldan o'tadi:
1. **Qayerdan?** — shu Lektion yoki shu darajaning oldingi Lektionlaridagi **haqiqiy Redemittel**, faqat **boshqa funksiya / boshqa vaziyat** uchun. O'tilmagan, notanish ibora bo'lmasin (o'quvchi darhol chetlab o'tadi).
2. **Nemis tilida shunday deyiladimi?** — har bir variant grammatik jihatdan **100% to'g'ri**, tabiiy nemischa. O'ylab topilgan ibora yo'q. Variant grammatika xatosi bilan noto'g'ri bo'lmaydi — u **vaziyatga mos kelmagani** uchun noto'g'ri.
3. **Kim shu xatoni qiladi?** — real o'quvchi xatosi: o'xshash funksiyani adashtirish (rozilik ↔ rad etish, maslahat ↔ taklif, tabrik ↔ ta'ziya, Glückwunsch ↔ Gute Besserung), noto'g'ri register (do'stga Sie, notanishga du — faqat vaziyatda kim bilan gaplashilayotgani aniq bo'lsa), savol o'rniga javob, va h.k.
4. **Ikkinchi to'g'ri javob yo'qmi?** — to'rttasini vaziyat bilan alohida o'qib chiqing: aynan bittasi mos. «Ham bo'lishi mumkin» degan variant bo'lsa — almashtiring.

Shakl:
- To'rtta variant **uzunligi va tuzilishi o'xshash** (to'g'ri javob eng uzuni bo'lib qolmasin, eng batafsili ham emas).
- Variant — 1 qisqa gap (A1 ≤ 8 so'z, A2 ≤ 10, B1 ≤ 14). Ikki gap faqat zarur bo'lsa.
- Tinish belgisi bilan tugaydi (. ! ?). Qo'shtirnoq „…“.
- Bir Lektionda bir xil to'g'ri javob ikki marta kelmasin.

## Tekshirish
`python3 /home/claude/deutsch/tools/ltk/check.py /home/claude/deutsch/tools/ltk/{FILE}.json` → OK bo'lishi shart (ogohlantirishlarni ham ko'rib chiqing).
Oxirida har bir savolni 4 ta varianti bilan qayta o'qing (4 savol testi). Qisqa hisobot: nechta savol, qaysi Lektionda qiyinchilik bo'ldi.
