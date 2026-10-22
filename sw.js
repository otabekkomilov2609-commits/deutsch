/* streber.uz — ilova (PWA) service worker.
   Sahifa: avval internetdan (har doim eng yangi versiya), internet yo'q bo'lsa — saqlangan nusxa.
   Shriftlar va kutubxonalar: saqlangan nusxa, fonda yangilanadi. */
const V = 'streber-d414a23c', SHELL = ['/', '/manifest.webmanifest', '/icons/icon-192.png', '/icons/favicon.svg'];
const CDN = /^(fonts\.googleapis\.com|fonts\.gstatic\.com|cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|www\.gstatic\.com)$/;
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(SHELL)).catch(() => {})); self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const r = e.request; if (r.method !== 'GET') return;
  const u = new URL(r.url);
  if (u.origin === location.origin) {
    if (u.pathname.startsWith('/files/')) return;               // PDF varaqlar — to'g'ridan-to'g'ri
    if (/^\/(data\/[^/]+\.[0-9a-f]{8}\.json|app\.[0-9a-f]{8}\.js)$/.test(u.pathname)) {   // hash'li fayllar — keshdan, bo'lmasa tarmoqdan (o'zgarmaydi)
      e.respondWith(caches.open(V).then(c => c.match(r).then(m => m || fetch(r).then(res => { if (res.ok) c.put(r, res.clone()); return res; }))));
      return;
    }
    const nav = r.mode === 'navigate';
    const key = nav ? '/' : r;
    e.respondWith(fetch(r).then(res => { if (res.ok) { const cp = res.clone(); caches.open(V).then(c => c.put(key, cp)); } return res; })
      .catch(() => caches.match(key, { ignoreSearch: true }).then(m => m || caches.match('/'))));
    return;
  }
  if (CDN.test(u.hostname)) {
    e.respondWith(caches.open(V).then(c => c.match(r).then(m => {
      const net = fetch(r).then(res => { if (res.ok || res.type === 'opaque') c.put(r, res.clone()); return res; }).catch(() => m);
      return m || net;
    })));
  }
});
