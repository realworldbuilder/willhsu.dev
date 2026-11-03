"""Helpers for the Alaranarises guide hub pages."""
import html as _html

ICON = 'https://wow.zamimg.com/images/wow/icons/large/'

NAV = [
    ('', 'Setup', 'Bars, keys, first ten minutes'),
    ('leveling/', 'Leveling', '80 to 90, the Midnight road'),
    ('rotation/', 'Rotation', 'Dark Ranger, opener to filler'),
    ('gear/', 'Gear', 'Tracks, crests, stats, enchants'),
    ('dungeons/', 'Dungeons & raid', 'M+ pool, affixes, Venomous Abyss'),
    ('weekly/', 'Weekly', 'Reset checklist with ticks'),
    ('ui/', 'UI', 'No addons, Blizzard options only'),
]

def esc(s):
    return _html.escape(s, quote=False)

def icon(name, size=22):
    return f'<img class="ic" src="{ICON}{name}.jpg" alt="" width="{size}" height="{size}" loading="lazy">'

def section(id_, h2, note, inner, aside=''):
    return f'''
      <section id="{id_}">
        <div class="section-head">
          <div>
            <h2>{h2}</h2>
            {f'<p class="section-note">{note}</p>' if note else ''}
          </div>
          {aside}
        </div>
        {inner}
      </section>'''

def habits(items, cls='habits'):
    out = []
    for b, p in items:
        out.append(f'<div class="habit"><b>{b}</b><p>{p}</p></div>')
    return f'<div class="{cls}">' + '\n'.join(out) + '</div>'

def table(headers, rows, caption='', cls=''):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    trs = []
    for r in rows:
        tds = ''.join(f'<td>{c}</td>' for c in r)
        trs.append(f'<tr>{tds}</tr>')
    cap = f'<caption>{caption}</caption>' if caption else ''
    return f'<div class="tblwrap"><table class="tbl {cls}">{cap}<thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'

def prio(items, title=''):
    """Numbered priority list: items are (label, why)."""
    lis = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in items)
    t = f'<div class="combo-title">{title}</div>' if title else ''
    return f'<div class="prio">{t}<ol class="prio-list">{lis}</ol></div>'

def note(text, kind='note'):
    return f'<div class="callout c-{kind}">{text}</div>'

def checklist(id_, items, store_key, mode='week'):
    """Tickable list. items: (label, detail). mode week/day/forever controls auto-clear."""
    lis = []
    for i, (a, b) in enumerate(items):
        lis.append(f'<li><label><input type="checkbox" data-i="{i}"><span class="box"></span><span class="txt"><b>{a}</b>{f"<small>{b}</small>" if b else ""}</span></label></li>')
    return f'<ul class="checks ticklist" id="{id_}" data-store="{store_key}" data-mode="{mode}">' + ''.join(lis) + '</ul>'

def sources(items):
    lis = ''.join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a>{(" · " + esc(n)) if n else ""}</li>' for t, u, n in items)
    return f'<ul class="sources">{lis}</ul>'

def cards(items):
    out = []
    for href, title, blurb, ic in items:
        out.append(f'<a class="card guidecard" href="{href}">{icon(ic, 40)}<div><b>{title}</b><p>{blurb}</p></div></a>')
    return '<div class="guidegrid">' + ''.join(out) + '</div>'
