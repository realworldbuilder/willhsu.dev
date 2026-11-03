"""Build the Alaranarises guide hub: shared CSS from the setup page, one folder per guide."""
import os, re, sys, importlib
from h import NAV

ROOT = os.path.expanduser('~/projects/willhsu.dev/alaranarises')
base = open(ROOT + '/index.html').read()
STYLE = re.search(r'<style>.*?</style>', base, re.S).group(0)
HEAD_LINKS = re.search(r'(<link rel="icon".*?rel="stylesheet">)', base, re.S).group(1)
BACKDROP = re.search(r'(<canvas class="backdrop".*?</script>)', base, re.S).group(1)

EXTRA = '''<style>
    .sitenav { display: flex; flex-wrap: wrap; gap: 6px; margin: 18px 0 8px; }
    .sitenav a { font-family: var(--display); font-weight: 600; font-size: 13px; letter-spacing: .04em; text-transform: uppercase; color: var(--muted); text-decoration: none; padding: 7px 12px; border: 1px solid var(--border); background: rgba(18,21,34,.7); clip-path: polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px); }
    .sitenav a:hover { color: var(--text); border-color: rgba(255,255,255,.2); }
    .sitenav a.on { color: #0b0d14; background: var(--druid); border-color: var(--druid); }
    .tblwrap { overflow-x: auto; margin-top: 14px; border: 1px solid var(--border); background: var(--panel); }
    .tblwrap + .habits, .tblwrap + .tblwrap, .tblwrap + .prio, .callout + .habits, .prio + .habits { margin-top: 16px; }
    table.tbl { width: 100%; border-collapse: collapse; font-size: 13.5px; min-width: 520px; }
    table.tbl caption { text-align: left; padding: 10px 12px 6px; color: var(--muted); font-size: 12.5px; }
    table.tbl th { text-align: left; font-family: var(--display); font-weight: 600; letter-spacing: .04em; text-transform: uppercase; font-size: 11.5px; color: var(--muted); padding: 10px 12px; border-bottom: 1px solid var(--border); background: var(--panel-2); white-space: nowrap; }
    table.tbl td { padding: 9px 12px; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text); }
    table.tbl tr:last-child td { border-bottom: 0; }
    table.tbl td b { color: var(--gold); font-weight: 600; }
    table.tbl .hero { color: var(--epic); } table.tbl .myth { color: var(--legendary); } table.tbl .champ { color: var(--rare); } table.tbl .vet { color: var(--uncommon); }
    .callout { margin-top: 14px; padding: 12px 14px; border: 1px solid var(--border); border-left: 3px solid var(--gold); background: var(--panel); font-size: 14px; color: var(--text); }
    .callout.c-warn { border-left-color: #ff4d4d; } .callout.c-tip { border-left-color: var(--druid); } .callout.c-info { border-left-color: var(--rare); }
    .callout b { color: var(--gold); }
    ol.prio-list { list-style: none; counter-reset: p; margin-top: 10px; display: grid; gap: 6px; }
    ol.prio-list li { counter-increment: p; display: grid; grid-template-columns: 28px 1fr; gap: 10px; padding: 9px 12px; background: var(--panel); border: 1px solid var(--border); align-items: start; }
    ol.prio-list li::before { content: counter(p); font-family: var(--display); font-weight: 700; color: var(--gold); font-size: 16px; line-height: 1.3; }
    ol.prio-list li b { color: var(--text); display: block; font-weight: 600; } ol.prio-list li span { color: var(--muted); font-size: 13.5px; }
    .prio + .prio { margin-top: 18px; }
    .guidegrid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 10px; margin-top: 14px; }
    .guidecard { display: flex; gap: 12px; align-items: flex-start; padding: 14px; background: var(--panel); border: 1px solid var(--border); text-decoration: none; color: var(--text); }
    .guidecard:hover { border-color: var(--druid); }
    .guidecard img { border-radius: 4px; border: 1px solid var(--border); flex: 0 0 auto; }
    .guidecard b { font-family: var(--display); font-size: 16px; letter-spacing: .02em; display: block; margin-bottom: 2px; }
    .guidecard p { color: var(--muted); font-size: 13px; line-height: 1.45; }
    img.ic { vertical-align: -5px; border-radius: 3px; margin-right: 4px; }
    ul.sources { margin-top: 12px; padding-left: 18px; color: var(--muted); font-size: 13px; line-height: 1.7; }
    ul.sources a { color: var(--rare); text-decoration: none; } ul.sources a:hover { text-decoration: underline; }
    .ticklist { margin-top: 14px; display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 10px; list-style: none; padding: 0; }
    .ticklist li label { display: grid; grid-template-columns: 22px 1fr; gap: 12px; align-items: start; padding: 10px 12px; background: var(--panel); border: 1px solid var(--border); cursor: pointer; }
    .ticklist input { position: absolute; opacity: 0; pointer-events: none; }
    .ticklist .box { width: 20px; height: 20px; margin-top: 2px; border: 2px solid var(--dim); border-radius: 4px; display: inline-block; position: relative; }
    .ticklist input:checked + .box { background: var(--druid); border-color: var(--druid); }
    .ticklist input:checked + .box::after { content: ''; position: absolute; left: 5px; top: 1px; width: 6px; height: 11px; border: solid #0b0d14; border-width: 0 2.5px 2.5px 0; transform: rotate(45deg); }
    .ticklist input:checked ~ .txt { color: var(--dim); text-decoration: line-through; }
    .ticklist .txt b { font-weight: 600; display: block; } .ticklist .txt small { color: var(--muted); font-size: 12.5px; display: block; margin-top: 2px; }
    .resetline { display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-top: 10px; color: var(--muted); font-size: 13px; flex-wrap: wrap; }
    .resetline button { font: inherit; color: var(--muted); background: transparent; border: 1px solid var(--border); padding: 5px 10px; cursor: pointer; }
    .resetline button:hover { color: var(--text); }
    .twocol { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }
    @media (max-width: 760px) { .twocol { grid-template-columns: 1fr; } }
    .kv { display: grid; grid-template-columns: max-content 1fr; gap: 6px 14px; margin-top: 12px; font-size: 14px; }
    .kv dt { color: var(--muted); } .kv dd { color: var(--text); }
    .guidecard-hub { margin-top: 10px; }
  </style>'''

TICK_JS = '''
  <script>
    // Tick lists: saved in this browser only. mode=week clears after the Tuesday 15:00 UTC reset, mode=day after each 15:00 UTC.
    (() => {
      const now = new Date();
      const periodKey = (mode) => {
        const t = new Date(now);
        if (mode === 'forever') return 'x';
        // shift so the day boundary is 15:00 UTC
        const shifted = new Date(t.getTime() - 15 * 3600 * 1000);
        if (mode === 'day') return shifted.toISOString().slice(0, 10);
        const dow = shifted.getUTCDay(); // Tuesday = 2
        const back = (dow - 2 + 7) % 7;
        shifted.setUTCDate(shifted.getUTCDate() - back);
        return 'w' + shifted.toISOString().slice(0, 10);
      };
      document.querySelectorAll('.ticklist').forEach(ul => {
        const store = ul.dataset.store, mode = ul.dataset.mode || 'forever';
        const key = store + ':' + periodKey(mode);
        let saved = {};
        try { saved = JSON.parse(localStorage.getItem(key) || '{}'); } catch {}
        try { Object.keys(localStorage).forEach(k => { if (k.startsWith(store + ':') && k !== key) localStorage.removeItem(k); }); } catch {}
        ul.querySelectorAll('input').forEach(cb => {
          cb.checked = !!saved[cb.dataset.i];
          cb.addEventListener('change', () => {
            saved[cb.dataset.i] = cb.checked;
            try { localStorage.setItem(key, JSON.stringify(saved)); } catch {}
          });
        });
        const reset = document.querySelector(`[data-reset="${ul.id}"]`);
        if (reset) reset.addEventListener('click', () => { saved = {}; try { localStorage.removeItem(key); } catch {} ul.querySelectorAll('input').forEach(cb => cb.checked = false); });
      });
      const nr = document.getElementById('next-reset');
      if (nr) {
        const t = new Date(now); const s = new Date(t.getTime() - 15 * 3600 * 1000);
        const dow = s.getUTCDay(); const fwd = (2 - dow + 7) % 7 || 7;
        const next = new Date(Date.UTC(s.getUTCFullYear(), s.getUTCMonth(), s.getUTCDate() + fwd, 15, 0, 0));
        nr.textContent = next.toLocaleString(undefined, { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' });
      }
    })();
  </script>'''

def sitenav(active):
    out = []
    for slug, label, _ in NAV:
        href = ('../' + slug) if active != '' else slug
        if active == slug:
            href = '#'
        out.append(f'<a href="{href}" class="{"on" if slug == active else ""}">{label}</a>')
    return '<nav class="sitenav" aria-label="Guides">' + ''.join(out) + '</nav>'

def render(p):
    slug = p['slug']
    up = '../' if slug else ''
    jump = ''.join(f'<a class="btn{" ghost" if i else ""}" href="#{a}">{t}</a>' for i, (a, t) in enumerate(p['jump']))
    tags = ''.join(f'<span class="tag{" hot" if i == 0 else ""}">{t}</span>' for i, t in enumerate(p['tags']))
    body = '\n'.join(p['sections'])
    backdrop = BACKDROP.replace('../assets/azeroth.js', up + '../assets/azeroth.js')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['title']}</title>
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#0b0d14">
  {HEAD_LINKS}
  {STYLE}
  {EXTRA}
</head>
<body>
  {backdrop}
  <div class="wrap">
    <header class="hero">
      <div class="sheet">
        <div class="crest" aria-hidden="true"><img src="https://wow.zamimg.com/images/wow/icons/large/{p['crest']}.jpg" alt="" width="74" height="74"></div>
        <div>
          <p class="kicker">{p['kicker']}</p>
          <h1>{p['h1']}</h1>
          <p class="lede">{p['lede']}</p>
          <div class="tags">{tags}</div>
          <div class="jump">{jump}</div>
        </div>
      </div>
      {sitenav(slug)}
    </header>
    <main>
{body}
    </main>
    <footer>
      <span>Part of the <a href="{up}">Alaranarises guides</a> · unlisted, not linked from <a href="{up}../">willhsu.dev</a></span>
      <span>Icons from Wowhead. Not affiliated with Blizzard Entertainment. Checked against patch 12.1.5 on {p.get('checked', '3 Nov 2026')}.</span>
    </footer>
  </div>
  {TICK_JS}
  {p.get('extra_js', '')}
</body>
</html>
'''

if __name__ == '__main__':
    names = sys.argv[1:] or ['gear', 'rotation', 'dungeons', 'weekly', 'leveling', 'ui']
    for n in names:
        try:
            mod = importlib.import_module('content_' + n)
        except ModuleNotFoundError:
            print('skip', n); continue
        p = mod.PAGE
        d = os.path.join(ROOT, p['slug'])
        os.makedirs(d, exist_ok=True)
        out = render(p)
        open(os.path.join(d, 'index.html'), 'w').write(out)
        print('wrote', p['slug'], len(out))
