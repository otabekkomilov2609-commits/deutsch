/* ===== 🎯 telc Prüfungstraining — B1 (2026-10-24, Otabek: mock qabul qilindi «qil bo'masa»)
   Imtihon formatida: taymer, javoblar oxirida tekshiriladi, har bir javobga izoh (uz/ru), telc profili.
   Ma'lumot: tl-data (tools/telc/B1-L*-T.json). Turlar: sb1 (a/b/c bo'shliq), sb2 (15 so'zlik bank), l1 (sarlavha), l2 (a/b/c savol), l3 (e'lon / x).
   Natija: accK("tl:"+id) = {s,n,p,b(eng yaxshi %),t(soniya),d(kun),a(javoblar)} — bulut zaxirasiga o'zi tushadi. ===== */
let TLD=null; function tlData(){ if(!TLD){ try{ TLD=JSON.parse(document.getElementById("tl-data").textContent)||{}; }catch(e){ TLD={}; } } return TLD; }
const TL={id:null,a:[],sel:-1,t0:0,iv:null,done:false,res:null};
const TL_PN={sb1:"Sprachbausteine T1",sb2:"Sprachbausteine T2",l1:"Lesen T1",l2:"Lesen T2",l3:"Lesen T3"};
function tlEl(){ let e=document.getElementById("tl"); if(!e){ e=document.createElement("div"); e.id="tl"; e.className="lrn"; e.setAttribute("role","dialog"); e.setAttribute("aria-modal","true"); e.hidden=true; document.body.appendChild(e); } return e; }
function tlN(D){ return D.part==="l1"||D.part==="l2"?5:10; }
function tlGet(id){ try{ return JSON.parse(localStorage.getItem(accK("tl:"+id))||"null"); }catch(e){ return null; } }
function tlPct(id){ const r=tlGet(id); return r?r.b:null; }
function tlL(x){ return x?(state.lang==="ru"?(x.ru||x.uz):(x.uz||x.ru)):""; }
function tlOpen(id){ const D=tlData()[id]; if(!D) return; try{ actEv("open",id); }catch(e){} TL.id=id; TL.a=new Array(tlN(D)).fill(null); TL.sel=D.part==="sb2"?0:-1; TL.warn=false; TL.done=false; TL.res=null; TL.t0=Date.now();
  const el=tlEl(); el.hidden=false; document.body.style.overflow="hidden"; el.scrollTop=0; tlDraw(); el.scrollTop=0; clearInterval(TL.iv); TL.iv=setInterval(tlTick,1000); }
function tlClose(){ clearInterval(TL.iv); const el=tlEl(); el.hidden=true; el.innerHTML=""; document.body.style.overflow=""; try{ progMarks(); }catch(e){} }
function tlTick(){ const D=tlData()[TL.id], e=document.getElementById("tl-tm"); if(!D||!e||TL.done) return; const left=D.min*60-Math.round((Date.now()-TL.t0)/1000);
  e.textContent="⏱ "+(left<0?"−":"")+Math.floor(Math.abs(left)/60)+":"+String(Math.abs(left)%60).padStart(2,"0"); e.classList.toggle("late",left<0); }
function tlLet(i){ return "abcdefghijklmnop"[i]; }
function tlOpts(D,i){ /* i-slot uchun variantlar: [[qiymat, yorliq], …] */
  if(D.part==="sb1") return D.o[i].map((o,k)=>[k,tlLet(k)+") "+o]);
  if(D.part==="l2") return D.q[i].o.map((o,k)=>[k,tlLet(k)+") "+o]);
  if(D.part==="sb2") return D.bank.map((w,k)=>[k,w]);
  if(D.part==="l1") return D.heads.map((h,k)=>[k,h]);
  if(D.part==="l3") return D.ads.map((x,k)=>[k,x.t]).concat([[-1,"x"]]);
  return []; }
function tlAnsTxt(D,i,v){ if(v==null) return "—"; if(D.part==="sb2") return D.bank[v]; if(D.part==="sb1") return D.o[i][v]; if(D.part==="l2") return tlLet(v)+") "+D.q[i].o[v]; if(D.part==="l1") return tlLet(v)+") "+D.heads[v]; if(D.part==="l3") return v===-1?"x — "+(state.lang==="ru"?"подходящего объявления нет":"mos e’lon yo‘q"):tlLet(v)+") "+D.ads[v].t; return String(v); }
function tlGapHTML(D,i){ const v=TL.a[i], ok=TL.done?(v===D.a[i]):null, lbl=v==null?"":(D.part==="sb2"?D.bank[v]:D.o[i][v]);
  return `<button type="button" class="tl-g${v!=null?" f":""}${TL.sel===i&&!TL.done?" on":""}${ok===true?" ok":ok===false?" bad":""}" data-tlg="${i}"><i>${i+1}</i>${esc(lbl)}</button>${TL.done&&!ok?`<b class="tl-fx">${esc(D.part==="sb2"?D.bank[D.a[i]]:D.o[i][D.a[i]])}</b>`:""}`; }
function tlTextHTML(D){ return esc(D.text).split("\n").map((ln,k)=>{ const h=ln.replace(/\[(\d+)\]/g,(m,n)=>tlGapHTML(D,+n-1)); return k===0?`<h5>${h}</h5>`:`<p>${h||"&nbsp;"}</p>`; }).join(""); }
function tlPickRow(D,i,letters){ /* l1 / l3: harf tugmalari */ const v=TL.a[i], used=new Set(TL.a.filter((x,j)=>j!==i&&x!=null&&x!==-1));
  return `<div class="tl-lt">${letters.map(([val,lt])=>{ const on=v===val, ok=TL.done&&val===D.a[i], bad=TL.done&&on&&val!==D.a[i]; return `<button type="button" class="tl-l${on?" on":""}${used.has(val)&&!on?" used":""}${ok?" ok":""}${bad?" bad":""}" data-tlp="${i}|${val}"${TL.done?" disabled":""}>${lt}</button>`; }).join("")}</div>`; }
function tlBody(D){ const ru=state.lang==="ru", P=D.part;
  if(P==="sb2") return `<div class="tl-txt">${tlTextHTML(D)}</div>${TL.done?"":`<div class="tl-bank">${D.bank.map((w,k)=>`<button type="button" class="tl-w${TL.a.includes(k)?" used":""}" data-tlw="${k}"><i>${tlLet(k)}</i>${esc(w)}</button>`).join("")}</div>`}`;
  if(P==="sb1") return `<div class="tl-txt">${tlTextHTML(D)}</div><div class="tl-sheet">${D.o.map((o,i)=>`<div class="tl-row" id="tl-r${i}"><b>${i+1}</b>${o.map((x,k)=>{ const on=TL.a[i]===k, ok=TL.done&&k===D.a[i], bad=TL.done&&on&&k!==D.a[i]; return `<button type="button" class="tl-o${on?" on":""}${ok?" ok":""}${bad?" bad":""}" data-tlp="${i}|${k}"${TL.done?" disabled":""}><i>${tlLet(k)}</i>${esc(x)}</button>`; }).join("")}</div>`).join("")}</div>`;
  if(P==="l2") return `<div class="tl-txt">${esc(D.text).split("\n").map((ln,k)=>k===0?`<h5>${ln}</h5>`:`<p>${ln}</p>`).join("")}</div><div class="tl-sheet">${D.q.map((q,i)=>`<div class="tl-q" id="tl-r${i}"><p><b>${i+1}</b> ${esc(q.s)}</p>${q.o.map((x,k)=>{ const on=TL.a[i]===k, ok=TL.done&&k===D.a[i], bad=TL.done&&on&&k!==D.a[i]; return `<button type="button" class="tl-o wide${on?" on":""}${ok?" ok":""}${bad?" bad":""}" data-tlp="${i}|${k}"${TL.done?" disabled":""}><i>${tlLet(k)}</i>${esc(x)}</button>`; }).join("")}</div>`).join("")}</div>`;
  if(P==="l1"){ const L=D.heads.map((h,k)=>[k,tlLet(k)]);
    return `<div class="tl-box"><h6>${ru?"Заголовки":"Sarlavhalar"} a–j</h6>${D.heads.map((h,k)=>`<div class="tl-hd${TL.a.includes(k)?" used":""}"><i>${tlLet(k)}</i>${esc(h)}</div>`).join("")}</div>
      ${D.texts.map((t,i)=>`<div class="tl-card" id="tl-r${i}"><div class="tl-ch"><b>${ru?"Текст":"Matn"} ${i+1}</b>${TL.a[i]!=null?`<span>→ ${esc(tlLet(TL.a[i])+") "+D.heads[TL.a[i]])}</span>`:""}</div><p>${esc(t)}</p>${tlPickRow(D,i,L)}</div>`).join("")}`; }
  if(P==="l3"){ const L=D.ads.map((x,k)=>[k,tlLet(k)]).concat([[-1,"x"]]);
    return `<div class="tl-sheet">${D.sits.map((s,i)=>`<div class="tl-card" id="tl-r${i}"><div class="tl-ch"><b>${i+1}</b><span class="tl-sit">${esc(s)}</span></div>${TL.a[i]!=null?`<div class="tl-chosen">→ ${esc(tlAnsTxt(D,i,TL.a[i]))}</div>`:""}${tlPickRow(D,i,L)}</div>`).join("")}</div>
      <h6 class="tl-h6">${ru?"Объявления":"E’lonlar"} a–l</h6><div class="tl-ads">${D.ads.map((x,k)=>`<div class="tl-ad"><b><i>${tlLet(k)}</i>${esc(x.t)}</b><p>${esc(x.body)}</p></div>`).join("")}</div>`; }
  return ""; }
function tlDraw(){ const D=tlData()[TL.id], el=tlEl(), sc=el.scrollTop, ru=state.lang==="ru", n=tlN(D), filled=TL.a.filter(x=>x!=null).length;
  el.innerHTML=`<div class="lrn-bar"><button class="btn" data-tlx="close" aria-label="←">←</button><div class="lrn-tt"><b>${esc(D.title)}</b><small>Lektion ${D.lek} · telc Deutsch B1 · ${esc(D.sub)}</small></div><span class="tl-tm${TL.done?" end":""}" id="tl-tm">${TL.done?"✓ "+vdFmt(TL.res.t):"⏱ "+D.min+":00"}</span></div>
    <div class="tl-in">${TL.done?tlResHTML(D):""}
      <div class="tl-task" lang="de">${esc(D.h)}</div>${TL.done?"":`<div class="tl-tip">💡 ${tlL(D.tip)}</div>`}
      ${tlBody(D)}
      <p class="tl-src">${esc(D.src||"")}</p>
      ${TL.done?`<div class="tl-foot"><button type="button" class="btn" data-tlx="again">🔁 ${ru?"Ещё раз":"Qayta ishlash"}</button><button type="button" class="btn primary" data-tlx="close">${ru?"Готово":"Tayyor"}</button></div>`
        :`<div class="tl-foot sticky"><span>${filled} / ${n} ${ru?"заполнено":"to‘ldirildi"}</span><button type="button" class="btn primary" data-tlx="check">${TL.warn?(ru?`Пусто: ${n-filled} — всё равно проверить`:`${n-filled} ta bo‘sh — baribir tekshirish`):(ru?"Проверить":"Tekshirish")}</button></div>`}</div>`;
  el.scrollTop=sc; tlTick(); }
function tlResHTML(D){ const R=TL.res, ru=state.lang==="ru", pass=R.p>=60;
  const rows=D.a.map((c,i)=>{ const v=TL.a[i], ok=v===c; return `<div class="tl-rv${ok?" ok":""}"><div class="h"><b>${i+1}</b> ${ok?"✅":"❌"} ${ok?`<span>${esc(tlAnsTxt(D,i,c))}</span>`:`<s>${esc(tlAnsTxt(D,i,v))}</s> → <span>${esc(tlAnsTxt(D,i,c))}</span>`}</div>${D.why&&D.why[i]?`<div class="why">${tlL(D.why[i])}</div>`:""}</div>`; }).join("");
  return `<div class="tl-score${pass?" pass":""}"><b>${R.s} / ${R.n}</b><small>${R.p}% · ${pass?(ru?"проходной балл telc — 60% ✓":"telc’da o‘tish chegarasi — 60% ✓"):(ru?"нужно 60% — ещё немного!":"o‘tish uchun 60% kerak — yana bir oz!")}</small>${R.prev!=null?`<small>${ru?"Прошлый раз":"Oldingi safar"}: ${R.prev}%</small>`:""}</div>
    ${tlProfHTML(true)}
    <details class="tl-rvs" open><summary>${ru?"Ответы и объяснения":"Javoblar va izohlar"}</summary>${rows}</details>`; }
/* 📊 telc profili: har qism bo'yicha eng yaxshi natijalar o'rtachasi */
function tlProf(get){ get=get||tlGet; const D=tlData(), P={}; Object.keys(D).forEach(id=>{ const r=get(id); if(!r) return; const k=D[id].part; (P[k]=P[k]||[]).push(r.b); });
  const out={}; for(const k in P) out[k]=Math.round(P[k].reduce((a,b)=>a+b,0)/P[k].length); return out; }
function tlProfHTML(sugg){ const pr=tlProf(), ks=["sb1","sb2","l1","l2","l3"], ru=state.lang==="ru"; if(!Object.keys(pr).length) return "";
  const col=v=>v>=75?"var(--green)":v>=60?"var(--blue)":v>=45?"var(--orange)":"#D64545";
  let weak=null; ks.forEach(k=>{ if(pr[k]!=null&&pr[k]<60&&(weak==null||pr[k]<pr[weak])) weak=k; });
  let wid=null; if(weak){ const D=tlData(); wid=Object.keys(D).filter(id=>D[id].part===weak).sort((a,b)=>(tlPct(a)??-1)-(tlPct(b)??-1))[0]; }
  return `<div class="tl-prof"><h6>📊 ${ru?"Ваш профиль telc":"Sizning telc profilingiz"}</h6>${ks.map(k=>`<div class="tl-pr${pr[k]==null?" na":""}"><span>${TL_PN[k]}</span><div class="tl-bar"><i style="width:${pr[k]||0}%;background:${col(pr[k])}"></i></div><b>${pr[k]==null?"—":pr[k]+"%"}</b></div>`).join("")}
    ${sugg&&weak&&wid&&wid!==TL.id?`<p class="tl-sg">⚠️ ${ru?"Слабее всего":"Eng zaif joy"} — <b>${TL_PN[weak]}</b>. <button type="button" class="lrn-link" data-tlgo="${esc(wid)}">${ru?"Потренировать":"Mashq qilish"} → Lektion ${tlData()[wid].lek}</button></p>`:""}</div>`; }
function tlCheck(){ const D=tlData()[TL.id], n=tlN(D), s=D.a.filter((c,i)=>TL.a[i]===c).length, p=Math.round(s/n*100), t=Math.round((Date.now()-TL.t0)/1000), old=tlGet(TL.id);
  const r={s,n,p,b:Math.max(p,old?old.b:0),t,d:actDay(),a:TL.a.slice()}; try{ localStorage.setItem(accK("tl:"+TL.id),JSON.stringify(r)); }catch(e){}
  TL.res=Object.assign({prev:old?old.p:null},r); TL.done=true; clearInterval(TL.iv);
  try{ actEv("tl",TL.id+":"+p); }catch(e){} try{ cloudDirty(); }catch(e){} tlEl().scrollTop=0; tlDraw(); tlEl().scrollTop=0; }
document.addEventListener("click",e=>{ const t=e.target; if(!t.closest) return; const go=t.closest("[data-tlgo]"); if(go){ tlOpen(go.dataset.tlgo); return; }
  if(!t.closest("#tl")) return; const D=tlData()[TL.id]; if(!D) return;
  const x=t.closest("[data-tlx]"); if(x){ const a=x.dataset.tlx; if(a==="close") tlClose(); else if(a==="check"){ const left=TL.a.filter(v=>v==null).length; if(left&&!TL.warn){ TL.warn=true; tlDraw(); return; } tlCheck(); } else if(a==="again") tlOpen(TL.id); return; }
  if(TL.done) return;
  const g=t.closest("[data-tlg]"); if(g){ const i=+g.dataset.tlg; if(D.part==="sb1"){ const r=document.getElementById("tl-r"+i); if(r){ r.scrollIntoView({block:"center",behavior:"smooth"}); r.classList.remove("pulse"); void r.offsetWidth; r.classList.add("pulse"); } return; }
    if(TL.sel===i&&TL.a[i]!=null){ TL.a[i]=null; } TL.sel=i; tlDraw(); return; }
  const w=t.closest("[data-tlw]"); if(w){ const k=+w.dataset.tlw, prev=TL.a.indexOf(k); let i=TL.sel; if(i<0||i>=TL.a.length) i=TL.a.indexOf(null); if(i<0) return;
    if(prev>=0) TL.a[prev]=null; TL.a[i]=k; const nx=TL.a.findIndex((v,j)=>v==null&&j>i); TL.sel=nx>=0?nx:TL.a.indexOf(null); tlDraw(); return; }
  const p=t.closest("[data-tlp]"); if(p){ const [i,v]=p.dataset.tlp.split("|").map(Number); if(TL.a[i]===v) TL.a[i]=null; else { if(D.part==="l1"||D.part==="l3"){ const j=TL.a.indexOf(v); if(v!==-1&&j>=0&&j!==i) TL.a[j]=null; } TL.a[i]=v; } TL.warn=false; tlDraw(); return; } });
document.addEventListener("keydown",e=>{ if(e.key==="Escape"){ const el=document.getElementById("tl"); if(el&&!el.hidden) tlClose(); } });
/* ustozga xulosa (stCollect.tl) va o'quvchi profilidagi blok */
function tlSum(){ const D=tlData(), o={}; Object.keys(D).forEach(id=>{ const r=tlGet(id); if(r) o[id]=[r.p,r.b,r.d]; }); return Object.keys(o).length?o:undefined; }
function tlProfFrom(tl){ if(!tl) return ""; const D=tlData(), P={}; Object.entries(tl).forEach(([id,v])=>{ const x=D[id]; if(!x) return; (P[x.part]=P[x.part]||[]).push(v[1]); });
  const ks=["sb1","sb2","l1","l2","l3"].filter(k=>P[k]); if(!ks.length) return ""; const avg=k=>Math.round(P[k].reduce((a,b)=>a+b,0)/P[k].length);
  return `<h5>🎯 telc Prüfungstraining<small>${Object.keys(tl).length} ${state.lang==="ru"?"тренировок":"ta mashq"}</small></h5>${ks.map(k=>`<div class="tl-pr"><span>${TL_PN[k]}</span><div class="tl-bar"><i style="width:${avg(k)}%;background:${avg(k)>=60?"var(--green)":"var(--orange)"}"></i></div><b>${avg(k)}%</b></div>`).join("")}`; }
