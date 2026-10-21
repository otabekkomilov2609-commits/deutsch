/**
 * streber.uz → Forvo vositachi (proxy). API kaliti shu yerda yashirin turadi, saytda ko'rinmaydi.
 *
 * O'rnatish (Otabek):
 *  1) script.google.com → «Yangi loyiha» → shu kodni joylang → saqlang.
 *  2) ⚙️ «Loyiha sozlamalari» → «Skript xususiyatlari» → «Xususiyat qo'shish»:
 *       FORVO_KEY  = Forvo bergan API kalit   (kalitni hech kimga yubormang)
 *  3) «Joylashtirish» → «Yangi joylashtirish» → turi «Veb-ilova»;
 *       «Kim nomidan bajariladi»: Men;  «Kim kira oladi»: Har kim  → «Joylashtirish» → ruxsat bering.
 *  4) Chiqqan «Veb-ilova URL»ni Claude'ga yuboring (bu URL maxfiy emas).
 *
 * Nima qiladi: ?w=<so'z> → Forvo'dan shu so'zning nemis (DE/AT/CH) ayollar yozuvlarini eng yuqori bahodan
 * boshlab qaytaradi: {ok:true, items:[{u:mp3-havola, by:ism, c:mamlakat}]}. Kunlik limitdan oshmaslik uchun
 * hisoblagich bor (DAILY_MAX); oshsa {ok:false, limit:true} — sayt o'zining ovozlariga o'tadi.
 * Audio saqlanmaydi (Forvo qoidasi): faqat havola 90 daqiqa eslab qolinadi (havola 2 soat ishlaydi).
 */
const DAILY_MAX = 9000;          // Forvo Small Business: 10 000 so'rov/kun — zaxira qoldiramiz
const NATIVE = /^(Germany|Austria|Switzerland|Deutschland|Österreich|Schweiz)$/i;

function doGet(e) {
  const w = String((e && e.parameter && e.parameter.w) || '').trim().slice(0, 80);
  if (!w) return out_({ ok: false });
  if (!take_()) return out_({ ok: false, limit: true });          // har eshitish = 1 so'rov (Forvo mp3 ochilishini ham sanaydi)
  const cache = CacheService.getScriptCache(), ck = 'w:' + w;
  const hit = cache.get(ck); if (hit) return out_(JSON.parse(hit));
  if (!take_()) return out_({ ok: false, limit: true });          // qidiruv = yana 1 so'rov
  let items = ask_(w);
  if (!items.length && /^(der|die|das) /i.test(w) && take_()) items = ask_(w.replace(/^(der|die|das) /i, ''));
  const res = { ok: true, items: items.slice(0, 3) };
  cache.put(ck, JSON.stringify(res), 5400);
  return out_(res);
}

function ask_(w) {
  const P = PropertiesService.getScriptProperties(), key = P.getProperty('FORVO_KEY');
  if (!key) return [];
  const hosts = [P.getProperty('FORVO_HOST') || 'apicommercial.forvo.com', 'apifree.forvo.com'];
  for (const h of hosts) {
    const url = 'https://' + h + '/key/' + key + '/format/json/action/word-pronunciations/word/' +
      encodeURIComponent(w) + '/language/de/sex/f/order/rate-desc/limit/10';
    try {
      const r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
      if (r.getResponseCode() !== 200) continue;
      const j = JSON.parse(r.getContentText() || '{}');
      const it = (j.items || []).filter(x => x && x.pathmp3 && (x.sex || 'f') === 'f' && NATIVE.test(String(x.country || '')));
      if (!P.getProperty('FORVO_HOST')) P.setProperty('FORVO_HOST', h);
      return it.map(x => ({ u: x.pathmp3, by: x.username || '', c: x.country || '', r: +x.rate || 0 }));
    } catch (err) { /* keyingi host */ }
  }
  return [];
}

/* kunlik hisoblagich (UTC 22:00 da Forvo limiti yangilanadi — biz sutka bo'yicha sanaymiz) */
function take_() {
  const lock = LockService.getScriptLock(); lock.waitLock(5000);
  try {
    const P = PropertiesService.getScriptProperties();
    const d = Utilities.formatDate(new Date(Date.now() + 2 * 3600e3), 'UTC', 'yyyy-MM-dd');
    let n = +P.getProperty('n:' + d) || 0;
    if (n >= DAILY_MAX) return false;
    P.setProperty('n:' + d, String(n + 1));
    return true;
  } finally { lock.releaseLock(); }
}

/* bugun nechta so'rov ketganini ko'rish: funksiyani tanlab ▶ Run */
function bugungiHisob() {
  const d = Utilities.formatDate(new Date(Date.now() + 2 * 3600e3), 'UTC', 'yyyy-MM-dd');
  Logger.log(d + ': ' + (PropertiesService.getScriptProperties().getProperty('n:' + d) || 0) + ' ta so‘rov');
}

function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
