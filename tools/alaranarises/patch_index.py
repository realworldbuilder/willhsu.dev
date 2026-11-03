"""Reframe the setup page: level 80 of 90, hub nav and guide cards, updated to-do. Idempotent."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import EXTRA, sitenav
from h import cards, note

P = os.path.expanduser('~/projects/willhsu.dev/alaranarises/index.html')
s = open(P).read()

def rep(old, new, count=1):
    global s
    if old not in s:
        if new in s:
            return  # already applied
        raise AssertionError(old[:60])
    s = s.replace(old, new, count)

if 'class="sitenav"' not in s:
    rep('  </style>\n</head>', '  </style>\n  ' + EXTRA + '\n</head>')
else:
    s = re.sub(r'<style>\n    \.sitenav .*?</style>', lambda m: EXTRA, s, count=1, flags=re.S)
    rep('        </div>\n      </div>\n    </header>', '        </div>\n      </div>\n      ' + sitenav('') + '\n    </header>')

rep('<p class="kicker">Boosted to 80 · Dark Ranger Marksmanship · Patch 12.1.5 Midnight</p>',
    '<p class="kicker">Boosted to 80 of 90 · Dark Ranger Marksmanship · Patch 12.1.5 Midnight</p>')
rep('<span class="tag">Level 80 · ilvl 102</span>', '<span class="tag">Level 80 of 90 · ilvl 102</span>')
rep('Skip the Catch Up quests, set this up in ten minutes, go play. Hover anything for its tooltip.',
    'Skip the Catch Up quests, set this up in ten minutes, go play. The cap is 90, so the next stop is the <a href="leveling/">leveling road</a>; the other guides are in the row below. Hover anything for its tooltip.')
# duplicate jump links
rep('''            <a class="btn ghost" href="#why">Why these keys</a>
            <a class="btn ghost" href="#rotation">Rotation</a>
            <a class="btn ghost" href="#why">Why these keys</a>
            <a class="btn ghost" href="#rotation">Rotation</a>''', '''            <a class="btn ghost" href="#why">Why these keys</a>
            <a class="btn ghost" href="#rotation">Rotation</a>''')

# guide cards after the start section
CARDS = cards([
    ('leveling/', 'Leveling 80 to 90', 'The Midnight campaign in order, XP that is free, what a hunter pulls.', 'achievement_level_90'),
    ('rotation/', 'Rotation', 'Opener, single target, AoE, cooldowns, every Dark Ranger node, with the why.', 'inv_ability_darkrangerhunter_blackarrow'),
    ('gear/', 'Gear', 'Tracks and crests, fresh-90 shopping list, stats, enchants, gems, consumables, trinkets.', 'inv_misc_bag_12'),
    ('dungeons/', 'Dungeons & raid', 'The eight keys, affixes by level, first-key manners, the Venomous Abyss, delves.', 'achievement_dungeon_outland_dungeonmaster'),
    ('weekly/', 'Weekly', 'The reset checklist with ticks that clear on Tuesday.', 'inv_misc_pocketwatch_01'),
    ('ui/', 'UI without addons', 'Cooldown Manager, damage meter, nameplates, bags, Edit Mode. Every option this character has on.', 'inv_misc_gear_01'),
])
if 'id="guides"' not in s:
    rep('      <section id="binds">', '''      <section id="guides">
        <div class="section-head">
          <div>
            <h2>The guides</h2>
            <p class="section-note">One page per question. All checked against patch 12.1.5; each ends with its sources.</p>
          </div>
        </div>
        ''' + CARDS + '''
      </section>
      <section id="binds">''')
else:
    s = re.sub(r'(<section id="guides">.*?</div>\n        )<div class="guidegrid">.*?</div>(\n      </section>)', lambda m: m.group(1) + CARDS + m.group(2), s, flags=re.S)

# gear section: now a pointer
GEAR_OLD = re.search(r'<section id="gear">.*?</section>', s, re.S).group(0)
GEAR_NEW = '''<section id="gear">
        <div class="section-head">
          <div>
            <h2>Stats, gear and everything else</h2>
            <p class="section-note">The boost set is item level 102. Quest rewards pass it within an evening, so do not spend gold on gear before 90. The long version is the <a href="gear/">gear page</a>.</p>
          </div>
        </div>
        <div class="habits">
          <div class="habit"><b>Stat priority</b><p>Agility first, then Critical Strike, Mastery, Versatility, Haste (Method, Icy Veins, 12.1.5). When two quest rewards tie on item level, take the one with Crit or Mastery. Ranged weapon upgrades beat everything.</p></div>
          <div class="habit"><b>Gear while leveling</b><p>Take every quest reward that raises item level. Dungeons through the Group Finder (I) drop better. At 90 the <a href="gear/#fresh90">fresh 90 list</a> takes over: vendor gear, delves at tier 8, the world boss.</p></div>
          <div class="habit"><b>Consumables</b><p>The boost gave healing potions, food and bandages; they are on the right bar. Eat out of combat below half health, potion in combat, bandage when neither is up. Flasks and food that matter are on the gear page.</p></div>
          <div class="habit"><b>The windows</b><p>C character, P spellbook, N talents, Shift-P mounts and pets, B bags, M map, L quest log, I group finder. Escape then Edit Mode moves any frame.</p></div>
          <div class="habit"><b>Talents as you level</b><p>Every level to 90 gives points. Open N when it glows: hero points into the two empty Dark Ranger nodes first, then follow the gold highlights.</p></div>
          <div class="habit"><b>Sentinel instead?</b><p>The other hero tree. Every guide rates it higher in 12.1.5 and 47 of the top 50 key hunters run it. Dark Ranger is what this character runs because Black Arrow teaches the spec better. One click in the talent panel swaps; the bars do not change except Black Arrow becomes Kill Shot on Q.</p></div>
          <div class="habit"><b>Assisted Highlight is on</b><p>Options, Gameplay Enhancements. The game glows the button it thinks you should press next, using this exact priority. It only works for abilities on a bar, which is why everything is on one. The Single-Button Assistant spell is not used: it adds a global cooldown penalty.</p></div>
          <div class="habit"><b>Interrupt nag</b><p>The game keeps saying "add an interrupt ability". Counter Shot is already on F; the nag stops once you use it in a fight.</p></div>
        </div>
      </section>'''
s = s.replace(GEAR_OLD, GEAR_NEW)

# to-do list items
TODO_OLD = re.search(r'<div class="todo" id="todo-list">.*?</div>', s, re.S).group(0)
items = [
    ('hearth', 'Set your hearth', 'Innkeeper in Dornogal now, then the first Midnight hub you quest from. Ctrl-6 should bring you back to where the quests are.'),
    ('intro', 'Start the Midnight intro', '"Something on the Horizon": talk to Brann Bronzebeard in Dornogal. That quest is the door to Quel\'Thalas; the Campaign tracker ("Champions of Quel\'Danas" and on) is the road after it.'),
    ('ninety', 'Level to 90', 'Ten levels, about 3.7 million XP. The <a href="leveling/">leveling page</a> has the zone order and the free XP. Nothing on the gear page matters until this is done.'),
    ('ring', 'Do the Gear Enchanting quest', 'It is in your log already and hands you a free ring enchant. Two minutes.'),
    ('house', 'Visit a housing neighborhood', 'Quest "A House For You" in your log. Midnight housing; free decor and a second hearth later.'),
    ('pet', 'Decide on Chinacat', 'Keep the eagle build (recommended), or refund Avian Specialization in the talent panel to get the wolf back for solo leveling.'),
    ('dungeon', 'Run one normal dungeon', 'Group Finder (I), Dungeon Finder, queue as damage. Misdirect the tank (Shift-Q) on every pull and nobody will know it is your first.'),
    ('bars', 'Press every key once in town', 'Shift and Ctrl bars included, so your hands know where things are before a fight asks.'),
    ('prof', 'At 90: pick two professions', 'Leatherworking and Skinning for the class, Inscription or Jewelcrafting for gold. Trainers in Silvermoon. The <a href="gear/#professions">gear page</a> says why.'),
    ('build', 'At 90: swap to the single-target build for bosses', 'Import string is in Start here. Keep the AoE loadout for everything else; switching is a dropdown.'),
    ('weekly', 'At 90: start the weekly list', 'The <a href="weekly/">weekly page</a> ticks itself clean every Tuesday. Vault, Spark, world boss, delves.'),
]
TODO_NEW = '<div class="todo" id="todo-list">\n' + '\n'.join(
    f'          <label><input type="checkbox" data-todo="{k}"><span><b>{a}</b><small>{b}</small></span></label>' for k, a, b in items) + '\n        </div>'
s = s.replace(TODO_OLD, TODO_NEW)

# start step 6: mounts are starred now
rep('Ctrl-1 already summons a random mount; star favourites in the journal if you want to narrow it.',
    'Ctrl-1 summons a random favourite: five are starred (Highland Drake, Renewed Proto-Drake, Cliffside Wylderdrake, Lightwing Dragonhawk, Cerulean Prideclaw), so the turkey stays home.')

open(P, 'w').write(s)
print('patched', len(s))
