"""Build willhsu.dev/hunter/: how to play a level 35 Beast Mastery hunter in WoW Forever.

The look, the keyboard board and the tooltip code come from alaranarises/index.html at build time,
so that page stays the source of the style. Run: python3 tools/hunter35/build.py (from anywhere).
Facts: Wowhead's Forever BM guides (Docoda, updated 12 to 20 Nov 2026), Forever tooltips
(nether.wowhead.com dataEnv=16), Blizzard's dev notes and hotfix threads; read 21 Nov 2026.
"""
import json, os, re, sys

SITE = os.path.expanduser('~/projects/willhsu.dev')
sys.path.insert(0, SITE + '/tools/alaranarises')
from h import section, habits, table, note, sources, esc  # noqa: E402

base = open(SITE + '/alaranarises/index.html').read()
STYLE = re.search(r'<style>.*?</style>', base, re.S).group(0)
EXTRA = re.search(r"EXTRA = '''(.*?)'''", open(SITE + '/tools/alaranarises/build.py').read(), re.S).group(1)
BACKDROP = re.search(r'(<canvas class="backdrop".*?</script>)', base, re.S).group(1)
JS_CORE = re.search(r"(    const tip = document.getElementById\('float-tip'\);.*?)    // --- to-do ticks", base, re.S).group(1)
# chips should find pet-bar keys too
JS_CORE = JS_CORE.replace(
    "for (const [k, v] of Object.entries(LAYERS.shift.keys)) if (v === id) return 'Shift-' + k;",
    "for (const [k, v] of Object.entries(LAYERS.shift.keys)) if (v === id) return 'Shift-' + k;\n"
    "      for (const [k, v] of Object.entries(LAYERS.ctrl.keys)) if (v === id) return 'Ctrl-' + k;")
assert 'LAYERS.ctrl.keys' in JS_CORE

ICON = 'https://wow.zamimg.com/images/wow/icons/large/'

def ic(name, size=22):
    return f'<img class="ic" src="{ICON}{name}.jpg" alt="" width="{size}" height="{size}" loading="lazy">'

# ---------------------------------------------------------------- spells on the bars
# role: builder = shot, finisher = pet & hawk, cooldown, defensive = escape, utility = control & utility
S = {}
def sp(key, name, icon, role, rows, desc, pro='', badge=''):
    S[key] = {'name': name, 'icon': icon, 'role': role, 'rows': rows, 'desc': desc}
    if pro: S[key]['pro'] = pro
    if badge: S[key]['badge'] = badge

sp('serpent', 'Serpent Sting', 'ability_hunter_quickshot', 'builder',
   [['Rank 5 (level 34)', '115 Mana'], ['Instant', '15 sec']],
   '200 Nature damage over 15 seconds. One per target.',
   'Skip it on mobs that die in a few seconds. Keep it ticking on elites and bosses.')
sp('hawk', 'Summon Hawk', 'ability_hunter_animalhandler', 'finisher',
   [['11% of base mana', '35 yd range'], ['Instant', '6 sec cooldown']],
   'A hawk dives the target and keeps attacking for 18 seconds. Two can be out at once. Your Unleashed Fury and Ferocity points make hawks hit harder and crit more.',
   'Shares its cooldown with Arcane Shot. Hawk, hawk, then Arcane.', 'BM talent · Forever only')
sp('arcane', 'Arcane Shot', 'ability_impalingbolt', 'builder',
   [['Rank 4', '11% of base mana'], ['Instant', '6 sec cooldown']],
   '85 Arcane damage, instantly.',
   'Shares its cooldown with Summon Hawk. Only press it when both hawks are out.')
sp('aimed', 'Aimed Shot', 'inv_spear_07', 'builder',
   [['Rank 2', '115 Mana'], ['2 sec cast', '6 sec cooldown']],
   'Your big hit: a shot with +70 damage. Baseline from level 20 in Forever. Auto Shot keeps firing while you cast it.',
   'Shares its cooldown with Multi-Shot. Rank 3 at 36.')
sp('multi', 'Multi-Shot', 'ability_upgrademoonglaive', 'builder',
   [['13.9% of base mana', 'Hits 3 targets'], ['Instant', '6 sec cooldown']],
   'Shoots up to three targets at once.',
   'Shares its cooldown with Aimed Shot, so on one target it costs you your biggest hit.')
sp('mark', 'Mark & Send (macro)', 'ability_hunter_snipershot', 'builder',
   [['Hunter\'s Mark rank 2', '30 Mana'], ['Instant', '2 min duration']],
   'Marks the target (+59 ranged attack power against it, and you can see it through stealth) and sends your pet in, in one press.',
   'The macro is in the Macros section. Without it, put plain Hunter\'s Mark here.')
sp('intim', 'Intimidation', 'ability_devour', 'cooldown',
   [['8% of base mana', '1 min cooldown'], ['Instant', '']],
   'Your pet\'s next hit stuns for 3 seconds with +100% crit chance, and makes a lot of threat.',
   'Use it at the start of a pull to glue the mob to the pet, or to stop a runner or a caster.', 'BM talent')
sp('concussive', 'Concussive Shot', 'spell_frost_stun', 'utility',
   [['8% of base mana', '12 sec cooldown'], ['Instant', '']],
   'Slows the target by 50% for 4 seconds.',
   'Slow a runner, or slow the mob coming at you while you back off.')
sp('wingclip', 'Wing Clip', 'ability_rogue_trip', 'defensive',
   [['Rank 1', '40 Mana'], ['Melee range', '']],
   'Slows the target by 50% for 10 seconds.',
   'Something reached you: Wing Clip, step back past 8 yards, keep shooting.')
sp('rapid', 'Rapid Fire', 'ability_hunter_runningshot', 'cooldown',
   [['100 Mana', '5 min cooldown'], ['Instant', '15 sec']],
   '+40% ranged and melee attack speed for 15 seconds.',
   'Elites, big pulls, bosses. At 40 it goes with Bestial Wrath.')
sp('mend', 'Mend Pet', 'ability_hunter_mendpet', 'defensive',
   [['Rank 3', '155 Mana'], ['5 sec channel', '68 health per sec']],
   'Heals your pet over 5 seconds while you stand still.',
   'Start it early, around half health. It is slow.')
sp('feign', 'Feign Death', 'ability_rogue_feigndeath', 'defensive',
   [['80 Mana', '30 sec cooldown'], ['Instant', 'Lasts 6 min']],
   'You play dead and drop out of combat. Forever\'s tooltip: if you don\'t cancel it, after 6 minutes you actually die.',
   'Solo: resets a bad pull. In groups: drops the threat you pulled off the tank.')
sp('hawkasp', 'Aspect of the Hawk', 'spell_nature_ravenform', 'utility',
   [['Rank 3', '+50 ranged attack power'], ['Instant', 'Stays on']],
   'Your fighting aspect. Your Deadly Aspects talent makes Auto Shot sometimes speed up your shooting by 30% for 12 seconds while it is on.',
   'Always on in a fight. Rank 4 at 38.')
sp('cheetah', 'Aspect of the Cheetah', 'ability_mount_jungletiger', 'utility',
   [['Instant', '+30% run speed'], ['Dazed for 4 sec if hit', '']],
   'Run speed between pulls.',
   'Swap back to Hawk before you pull. Getting hit dazes you.')
sp('monkey', 'Aspect of the Monkey', 'ability_hunter_aspectofthemonkey', 'defensive',
   [['Instant', '+8% dodge'], ['', '']],
   'Dodge chance, for when you are stuck in melee.',
   'Dodges also light up Mongoose Bite.')
sp('freezing', 'Freezing Trap', 'spell_frost_chainsofice', 'utility',
   [['Rank 1', '50 Mana'], ['Shared trap cooldown', '30 sec']],
   'Freezes the first enemy that steps on it for up to 10 seconds. Any damage breaks it. Rank 2 at 40 makes it 15 seconds.',
   'Traps work mid-fight in Forever. All traps share one 30 sec cooldown.')
sp('frost', 'Frost Trap', 'spell_frost_freezingbreath', 'utility',
   [['60 Mana', 'Shared trap cooldown'], ['10 yd area', '30 sec']],
   'Slows everything in 10 yards by 60% for 30 seconds.',
   'Kiting a pack, or slowing adds while the pet holds one.')
sp('explosive', 'Explosive Trap', 'spell_fire_selfdestruct', 'utility',
   [['Rank 1 (level 34)', '275 Mana'], ['10 yd area', 'Shared trap cooldown']],
   '105 to 135 Fire damage to everything nearby, then 150 more over 20 seconds.',
   'Your AoE before Volley at 40. Expensive: only on 3 or more mobs.')
sp('immolation', 'Immolation Trap', 'spell_fire_flameshock', 'utility',
   [['Rank 2', '90 Mana'], ['Single target', 'Shared trap cooldown']],
   '215 Fire damage over 15 seconds to the enemy that triggers it.',
   'Drop it under a mob the pet is tanking. One Fire and one Frost trap can be down at once.')
sp('distract', 'Distracting Shot', 'spell_arcane_blink', 'utility',
   [['Rank 3', '50 Mana'], ['Instant', '8 sec cooldown']],
   'Makes threat, so the target turns to you.',
   'Peel a mob off your healer, then Feign Death.')
sp('raptor', 'Raptor Strike', 'ability_meleedamage', 'defensive',
   [['Rank 5', '55 Mana'], ['Melee', '6 sec cooldown']],
   'A melee hit: weapon damage +35.',
   'Only when something is on you and you can\'t step away.')
sp('mongoose', 'Mongoose Bite', 'ability_hunter_swiftstrike', 'defensive',
   [['Rank 2', '40 Mana'], ['Melee', '5 sec cooldown']],
   'A melee hit you can only use right after you dodge.',
   'Lights up after a dodge. Press it if it glows.')
sp('counter', 'Counterattack', 'ability_warrior_challange', 'defensive',
   [['45 Mana', 'Melee'], ['After a parry', '5 sec root']],
   'Baseline in Forever. After you parry: half weapon damage +40, and roots the target for 5 seconds.',
   'The root buys you room to walk back out to range.')
sp('disengage', 'Disengage', 'ability_rogue_feint', 'defensive',
   [['Rank 2 (level 34)', '100 Mana'], ['Melee', '5 sec cooldown']],
   'Lowers your threat on the target. Blizzard doubled the threat drop on 8 Oct.',
   'Groups: tap it when you are close to pulling aggro.')
sp('scare', 'Scare Beast', 'ability_druid_cower', 'utility',
   [['Rank 2', '1.5 sec cast'], ['30 sec cooldown', 'Fear up to 15 sec']],
   'Fears a beast.',
   'The extra cat or wolf on a pull. Damage can break it early.')
sp('scorpid', 'Scorpid Sting', 'ability_hunter_criticalshot', 'utility',
   [['9% of base mana', '20 sec'], ['Instant', '']],
   'Forever changed it: the target has 2% less chance to hit for 20 seconds.',
   'Replaces Serpent Sting (one sting per target). Worth it on a hard-hitting elite.')
sp('flare', 'Flare', 'spell_fire_flare', 'utility',
   [['50 Mana', '15 sec cooldown'], ['10 yd area', '30 sec']],
   'Reveals stealthed enemies in an area.',
   'Rogues and stealthed mobs.')
# pet bar
sp('petattack', 'Pet: Attack', 'ability_ghoulfrenzy', 'finisher', [['Pet bar slot 1', '']], 'Sends the pet at your target.')
sp('petfollow', 'Pet: Follow', 'ability_tracking', 'finisher', [['Pet bar slot 2', '']], 'Calls the pet back to you. Also stops it fighting.')
sp('petstay', 'Pet: Stay', 'spell_nature_timestop', 'finisher', [['Pet bar slot 3', '']], 'Parks the pet where it stands.')
sp('claw', 'Claw', 'ability_druid_rake', 'finisher',
   [['Rank 5 (pet level 32)', '25 Focus'], ['21 to 29 damage', 'Autocast']],
   'The pet\'s main attack. Cats and raptors have it. A pet without Claw loses a lot of damage.',
   'Rank 6 at 40. Learn ranks from tamed beasts (Pet section).')
sp('bite', 'Bite', 'ability_racial_cannibalize', 'finisher',
   [['Rank 5 (pet level 32)', '35 Focus'], ['40 to 48 damage', '10 sec cooldown']],
   'A heavier hit on a cooldown.')
sp('growl', 'Growl', 'ability_physical_taunt', 'finisher',
   [['Rank 4', '15 Focus'], ['5 sec cooldown', 'Autocast']],
   'Makes threat so mobs stay on the pet. Not a full taunt.',
   'Leave autocast ON solo. Right-click it to turn autocast OFF in groups.')
sp('dash', 'Dash', 'ability_druid_dash', 'finisher',
   [['Rank 1 (pet level 30)', '30 sec cooldown'], ['+40% speed', '15 sec']],
   'The pet runs faster.', 'Cats have it. Gets the pet to a runner or back to you.')
sp('aggressive', 'Pet: Aggressive', 'ability_racial_bloodrage', 'finisher', [['Pet bar slot 8', '']],
   'The pet attacks anything near it. Back in Forever.', 'Never in dungeons: it pulls extra packs.')
sp('defensive', 'Pet: Defensive', 'ability_defend', 'finisher', [['Pet bar slot 9', '']],
   'The pet fights whatever attacks you or it. The default.', 'Solo and in groups.')
sp('passive', 'Pet: Passive', 'ability_seal', 'finisher', [['Pet bar slot 10', '']],
   'The pet only attacks when you tell it to.', 'For careful pulls next to other packs.')

LAYERS = {
    'main': {'label': 'Main bar · X C V on the bottom-right bar', 'keys': {
        '1': 'serpent', '2': 'hawk', '3': 'arcane', '4': 'aimed', '5': 'multi',
        'Q': 'mark', 'E': 'intim', 'R': 'concussive', 'F': 'wingclip', 'G': 'rapid', 'T': 'mend', 'Z': 'feign',
        'X': 'hawkasp', 'C': 'cheetah', 'V': 'monkey'}},
    'shift': {'label': 'Shift · bottom-left bar: traps, melee, escapes', 'mod': 'Shift-', 'keys': {
        '1': 'freezing', '2': 'frost', '3': 'explosive', '4': 'immolation', '5': 'distract',
        'Q': 'raptor', 'E': 'mongoose', 'R': 'counter', 'F': 'disengage', 'G': 'scare', 'T': 'scorpid', 'Z': 'flare'}},
    'ctrl': {'label': 'Ctrl · the pet bar (default binds)', 'mod': 'Ctrl-', 'keys': {
        '1': 'petattack', '2': 'petfollow', '3': 'petstay', '4': 'claw', '5': 'bite', '6': 'growl', '7': 'dash',
        '8': 'aggressive', '9': 'defensive', '0': 'passive'}},
}

def chips(*ids, title=''):
    t = f'<p class="combo-title">{title}</p>' if title else ''
    return '<div class="combo">' + t + ''.join(f'<span class="step" data-ref="{i}"></span>' for i in ids) + '</div>'

def prio(title, items, cls='prio'):
    lis = ''.join(f'<li><span data-ref="{i}"></span><span class="when">{w}</span></li>' for i, w in items)
    return f'<div class="{cls}"><h3>{title}</h3><ol>{lis}</ol></div>'

def macro(name, icon_hint, body, where, why, tag):
    return f'''<div class="macro">
          <div class="macro-head"><b>{name}</b><span class="mtag {'ok' if tag == 'sourced' else 'try'}">{'from wowforeverguides.com' if tag == 'sourced' else 'test it first'}</span></div>
          <pre class="code">{esc(body)}</pre>
          <p><b>Icon:</b> {icon_hint} · <b>Goes on:</b> {where}</p>
          <p class="mwhy">{why}</p>
        </div>'''

# ---------------------------------------------------------------- page body
HERO = f'''
    <header class="hero">
      <div class="sheet">
        <div class="crest" aria-hidden="true"><img src="{ICON}ability_hunter_beasttaming.jpg" alt="" width="64" height="64"></div>
        <div>
          <p class="kicker">WoW Forever · Beast Mastery hunter · level 35</p>
          <h1>Beast Mastery at 35</h1>
          <p class="lede">How to play a level 35 BM hunter, alone and in a group. It covers the talents you have, the bars and keys (with macros), the exact button order for each kind of pull, what changes in a dungeon, and which pet to bring. Built on my night elf hunter, checked against Wowhead's Forever guides and Blizzard's hotfixes as of 21 November.</p>
          <div class="tags" aria-label="Build">
            <span class="tag hot">26 points in Beast Mastery</span>
            <span class="tag">The pet does the work</span>
            <span class="tag">Next: Bestial Wrath at 40</span>
          </div>
          <div class="jump">
            <a class="btn" href="#setup">Ten minute setup</a>
            <a class="btn ghost" href="#talents">Talents</a>
            <a class="btn ghost" href="#binds">Keybinds</a>
            <a class="btn ghost" href="#macros">Macros</a>
            <a class="btn ghost" href="#rhythm">The hawk rhythm</a>
            <a class="btn ghost" href="#solo">Solo</a>
            <a class="btn ghost" href="#group">Groups</a>
            <a class="btn ghost" href="#pet">Pet</a>
            <a class="btn ghost" href="#next">36 to 40</a>
          </div>
        </div>
      </div>
    </header>'''

SETUP = section('setup', 'Ten minute setup', 'Do these once, in order. After this, every fight button is under one hand.', habits([
    ('1 · Check your talents', 'Press N, Beast Mastery tab. At 35 you should have 26 points, all in BM. The list is in the next section. Your 35th-level point goes into Frenzy.'),
    ('2 · Turn on the bars', 'Escape, Interface, Action Bars: turn on the bottom-left bar, the bottom-right bar and the right bar. Untick Lock Action Bars while you drag, tick it again after.'),
    ('3 · Make two macros', 'Type /macro, New, give it a name, pick the question-mark icon, paste. "Mark &amp; Send" and "Pet Back" are in the Macros section.'),
    ('4 · Fill the bars', 'Open the spellbook (P) and drag each spell onto the slot shown on the keyboard below. Start the drag on the middle of the icon. Hover each slot after to check the tooltip name: Arcane Shot and Aimed Shot look alike.'),
    ('5 · Set the keys', 'Escape, Key Bindings. Main bar: 1 to 5 and Q E R F G T Z. Bottom-left bar ("Bottom Left Action Button 1 to 12"): the same keys with Shift. Bottom-right buttons 1 to 3: X, C, V. Tick "Character Specific Key Bindings" so your alts keep theirs. Q and E were strafe; you lose that on purpose.'),
    ('6 · Set up the pet bar', 'Leave the pet bar on its default Ctrl-1 to Ctrl-0. Put the pet on Defensive. Claw, Bite and Growl on autocast (the gold border; right-click to toggle). In a dungeon, right-click Growl to switch autocast off.'),
]))

TALENT_ROWS = [
    ('10 to 14', 'Deadly Aspects', '5/5', 'In Aspect of the Hawk, Auto Shot can give +30% shooting speed for 12 sec'),
    ('15 to 16', 'Focused Fire', '2/2', 'You and the pet deal 2% more damage while it is out'),
    ('17 to 19', 'Endurance Training', '3/5', 'Pet health and armor. Mostly here to open the next row'),
    ('20', 'Bestial Swiftness', '1/1', 'Pet runs 30% faster'),
    ('21 to 24, 26', 'Unleashed Fury', '5/5', 'Pet and hawks deal more damage'),
    ('25', 'Summon Hawk', '1/1', 'A hawk for 18 sec, two at once. Forever only'),
    ('27 to 29, 32 to 33*', 'Ferocity', '5/5', 'Pet and hawks crit more'),
    ('30 or 34*', 'Intimidation', '1/1', 'The pet\'s next hit stuns for 3 sec'),
    ('30 to 31 or 31 to 32*', 'Bestial Discipline', '2/2', 'Pet Focus regen +20%, and half your mana regen keeps going while you cast'),
    ('35', 'Frenzy', '1/5', 'After a pet crit, the pet attacks 30% faster for 8 sec (20% chance at 1/5)'),
]
TALENTS = section('talents', 'Your 26 points', 'Wowhead\'s leveling order and its raid order put different points in at levels 30 to 34, but by 35 both hold exactly these. One point per level from 10, all Beast Mastery, so you never need to respec on the way to 60.',
    table(['Levels', 'Talent', 'Points', 'What it does'],
          [[a, f'<b>{b}</b>', c, d] for a, b, c, d in TALENT_ROWS],
          caption='* Leveling order: Intimidation at 30, Bestial Discipline 31 to 32, Ferocity 33 to 34. Raid order: Bestial Discipline 30 to 31, Ferocity 32 to 33, Intimidation 34.')
    + note('<b>Levels 36 to 39:</b> one more point of Frenzy each level, to 5/5 (a guaranteed speed-up after every pet crit). <b>40:</b> Bestial Wrath. Then every point goes into Marksmanship: Lethal Attacks, Careful Aim, Improved Stings, Improved Arcane Shot, Trueshot Aura, Mortal Shots. That ends at 31/20/0, Wowhead\'s raid build.', 'tip'))

BINDS = f'''
      <section id="binds">
        <div class="section-head">
          <div>
            <h2>Keybinds</h2>
            <p class="section-note">Same key plan as my retail hunter. The number row is your shots in priority order. Q E R are the pull and control keys. G is the big cooldown, F is "something is on me", and T and Z keep you alive. Shift is the same keys on the bottom-left bar, for traps and melee. Ctrl is the pet bar.</p>
          </div>
          <div class="tabs" role="group" aria-label="Bar">
            <button class="tab" data-layer="main" aria-pressed="true">Main</button>
            <button class="tab mod" data-layer="shift" aria-pressed="false">Shift</button>
            <button class="tab mod" data-layer="ctrl" aria-pressed="false">Ctrl · pet</button>
          </div>
        </div>
        <div class="board">
          <span class="layer-name" id="layer-name">Main bar</span>
          <div class="keys" id="keys"></div>
          <div class="legend" aria-label="Key colours">
            <span style="--c: var(--builder)"><i></i>Shot</span>
            <span style="--c: var(--finisher)"><i></i>Pet &amp; hawk</span>
            <span style="--c: var(--cooldown)"><i></i>Cooldown</span>
            <span style="--c: var(--defensive)"><i></i>Escape &amp; melee</span>
            <span style="--c: var(--utility)"><i></i>Control &amp; utility</span>
          </div>
          <p class="hint keys-hint">Try it: press your keys. Hold <kbd>Shift</kbd> or <kbd>Ctrl</kbd> to see those bars.</p>
          <p class="hint touch">Tap a key for its tooltip.</p>
        </div>
        {habits([
            ('Bottom-right bar, slots 4 to 12 (click)', 'Call Pet, Dismiss Pet, Revive Pet, Feed Pet, Tame Beast, Eyes of the Beast, Eagle Eye, Aspect of the Beast, Beast Lore.'),
            ('Right bar (click)', 'Tracking (Beasts, Humanoids, Hidden), Hearthstone, food, drink, healing potions, bandages, a stack of pet food.'),
            ('Why the number row', 'A fight reads left to right: 1 Serpent Sting once, then 2 and 4 over and over (hawk, Aimed Shot), with 3 (Arcane) every third time in place of 2. 5 (Multi-Shot) is only for packs.'),
            ('Why the letters', 'Q starts every pull. E (Intimidation) right after. R slows, F gets a mob off you. G is Rapid Fire. T and Z are the far keys so you never press them by accident.'),
        ])}
        {note('<b>If you used my earlier bar prompt:</b> it put Auto Shot on 6, which makes 13 keys for a 12-slot bar. Drop Auto Shot: every shot starts it anyway, and Blizzard added a setting (16 Oct) that switches between Auto Attack and Auto Shot for you.', 'info')}
      </section>'''

MACROS = section('macros', 'Macros', 'Two worth making now and one to try. Write spells without "(Rank 2)" and the macro always uses your best rank. Forever\'s client reads Classic macro conditionals, but none of these has been tested in game yet, so check each one on a target dummy or an easy mob.',
    '<div class="macros">'
    + macro('Mark &amp; Send', 'Hunter\'s Mark (#showtooltip shows it)', "#showtooltip Hunter's Mark\n/petattack [@target,harm,nodead]\n/cast [harm,nodead] Hunter's Mark", 'Q',
            'One press marks the target and sends the pet. This is the first button of every pull.', 'sourced')
    + macro('Pet Back', 'Pet: Follow (the paw)', '/petfollow\n/petpassive', 'Bottom-right bar, or Shift-V',
            'The pet stops and runs to you on Passive. Use it when the pet chases a runner into another pack, or before you Feign Death in a group. Put it back on Defensive after (Ctrl-9).', 'try')
    + macro('Hawk Rhythm', 'Summon Hawk', '#showtooltip\n/castsequence reset=target Summon Hawk, Summon Hawk, Arcane Shot', 'Key 2, in place of plain Summon Hawk',
            'Presses the hawk, hawk, Arcane pattern for you, and starts over on a new target. /castsequence is not confirmed in Forever yet. If nothing happens, go back to plain buttons.', 'try')
    + '</div>')

RHYTHM = section('rhythm', 'The hawk rhythm', 'Everything about BM damage at 35 is two cooldown pairs. Summon Hawk and Arcane Shot share one 6 second cooldown. Aimed Shot and Multi-Shot share another. So every 6 seconds you get one press from each pair.',
    chips('hawk', 'aimed', 'hawk', 'aimed', 'arcane', 'aimed', title='Every 18 seconds, on one target')
    + habits([
        ('Why hawk, hawk, Arcane', 'A hawk lasts 18 seconds and only two can be out. Hawk at 0 s, hawk at 6 s, and at 12 s both are still up, so Arcane Shot gets that slot. At 18 s the first hawk leaves and you summon it again.'),
        ('Why not Multi-Shot', 'On one mob it uses up Aimed Shot\'s cooldown for less damage. Only press it on three mobs.'),
        ('Stand still', 'Auto Shot needs you to stand still for half a second before it fires (a Forever change, 16 Oct). Every step costs you shots. Move, plant your feet, shoot.'),
        ('Don\'t stand too close', 'Under 8 yards (the dead zone) no ranged attack fires. If a mob is on you, step back first.'),
    ]))

SOLO = section('solo', 'Solo', 'The pet tanks, you shoot. Let it land a couple of hits before you open up, so the mob stays on it.',
    chips('mark', 'intim', 'serpent', 'hawk', 'aimed', 'hawk', 'aimed', 'arcane', title='A normal quest mob')
    + '<div class="prio-grid">'
    + prio('The priority, every fight', [
        ('mark', 'Always first. It also sends the pet.'),
        ('serpent', 'Keep it up on anything that lives longer than about 10 seconds.'),
        ('hawk', 'On cooldown, until two are out.'),
        ('arcane', 'Only in the third slot, when both hawks are up.'),
        ('aimed', 'Whenever it is ready.'),
        ('rapid', 'Elites and any fight going long.'),
    ])
    + prio('Three or more mobs', [
        ('mark', 'Mark the one the pet should hold.'),
        ('multi', 'Hits three. Uses the Aimed Shot cooldown, which is fine here.'),
        ('explosive', 'Drop it where the pack stands. Pricey, so only on 3 or more.'),
        ('frost', 'Instead of Explosive if they are coming at you: slows the pack, you kite.'),
        ('hawk', 'Keep the hawks on the pet\'s target.'),
    ], 'prio aoe')
    + '</div>'
    + habits([
        ('Mobs that die fast', 'Save mana: Mark &amp; Send, let Auto Shot work, one Arcane Shot or Aimed Shot. No Serpent Sting.'),
        ('An elite or a hard mob', 'Full mana first. Both hawks before it reaches the pet. Intimidation as it arrives, then Rapid Fire, Serpent Sting, and the full rhythm. Scorpid Sting instead of Serpent Sting if it hits the pet hard.'),
        ('Two mobs', 'Freezing Trap at your feet, then shoot the second mob so it walks into the trap. The pet kills the first. Traps work in combat in Forever; they all share one 30 sec cooldown. A second beast? Scare Beast it.'),
        ('A runner', 'Concussive Shot (R) or Intimidation (E). A runner brings friends.'),
        ('Something is on you', 'Wing Clip (F), walk back past 8 yards, keep shooting. After a dodge, Mongoose Bite (Shift-E) lights up. After a parry, Counterattack (Shift-R) roots it.'),
        ('The pull went wrong', 'Feign Death (Z). Everything drops. Get up, eat, try again.'),
        ('Between pulls', 'Mend Pet (T) before the next pull, not during it. Feed the pet so it stays happy (green). An unhappy pet does less damage. Aspect of the Cheetah (C) to run, back to Hawk (X) before you shoot.'),
    ]))

DUNGEONS = [
    ('City of Dalaran', '28 to 33', 'New in Forever'),
    ('Scarlet Monastery: Graveyard', '28 to 38', ''),
    ('Gnomeregan', '29 to 38', ''),
    ('Scarlet Monastery: Library', '29 to 39', ''),
    ('Razorfen Kraul', '30 to 40', ''),
    ('Scarlet Monastery: Armory', '32 to 42', ''),
    ('The Drowned City', '35 to 40', 'New in Forever, off the Stranglethorn coast'),
    ('Scarlet Monastery: Cathedral', '35 to 45', 'Late for 35'),
]
GROUP = section('group', 'In a group', 'The tank holds the mobs, your pet joins in, you do damage from range. Your extra jobs: one Freezing Trap per pull, peeling mobs off the healer, and never pulling threat.',
    habits([
        ('Before the first pull', 'Pet on Defensive (Ctrl-9), never Aggressive: it runs into the next pack. Right-click Growl on the pet bar so autocast is off, or the pet steals the tank\'s mobs. Aspect of the Hawk on. Aspect of the Pack (at 40) dazes anyone who gets hit, so never run it in a group.'),
        ('Your trap (the classic trap pull)', 'Ask which mob is yours to trap (usually the moon). Before the pull, put Freezing Trap down between you and the pack. When the tank pulls, hit your mob with Distracting Shot (Shift-5) or Concussive Shot. It runs to you and freezes. Then stay off it: any damage breaks the ice.'),
        ('Wait for the tank', 'Count two or three seconds after the tank\'s first hit. Then Hunter\'s Mark on the skull and the rhythm. Rapid Fire on bosses.'),
        ('Pet on the skull only', 'Mark &amp; Send sends the pet at your target, so only press it on the kill target. Pet Back if it wanders.'),
    ])
    + chips('mark', 'hawk', 'aimed', 'hawk', 'aimed', 'arcane', 'rapid', title='A boss, after the tank has it')
    + '<div class="prio-grid">'
    + prio('Don\'t', [
        ('multi', 'Near a frozen or sheeped mob. It hits three and breaks crowd control.'),
        ('explosive', 'Same: only when nothing nearby is crowd controlled.'),
        ('serpent', 'On trash that dies in seconds. Save the mana; drink when the healer drinks.'),
    ], 'prio aoe')
    + prio('Fixing things', [
        ('disengage', 'You are close to pulling aggro: it lowers your threat.'),
        ('feign', 'A mob turned to you anyway: drop all your threat.'),
        ('distract', 'A mob is on the healer: pull it to you, then Feign Death.'),
        ('intim', 'A caster or a runner: the pet stuns it for 3 sec.'),
        ('wingclip', 'Something is on you and the tank is busy: slow it and walk back to the tank.'),
    ])
    + '</div>'
    + table(['Dungeon', 'Wowhead level range', ''], [[f'<b>{a}</b>', b, c] for a, b, c in DUNGEONS],
            caption='Dungeons for a level 35 hunter, from Wowhead\'s Forever dungeon overview. Razorfen Downs (40 to 50) and Krol\'dok Stronghold (40 to 45) come later.')
    + note('Hunter\'s Mark is ranged attack power, so it only helps you (and other hunters), not the melee. Still put it on the skull first: it is your damage.', 'info'))

PETS = [
    ('Claw rank 5', 'Scorpashi Lasher (34 to 35), Desolace · Vile Sting (35, rare), Thousand Needles'),
    ('Bite rank 5', 'Plains Creeper (32 to 33), Arathi · Sparkleshell Snapper (34 to 35), Thousand Needles · Crag Coyote (35 to 36), Badlands · Juvenile Paletusk (33 to 34), Riverglades'),
    ('Dash rank 1', 'Stranglethorn Tiger and Kurzen War Tiger (32 to 33), Stranglethorn Vale · Bonepaw Hyena (33 to 35), Desolace'),
]
PET = section('pet', 'Your pet', 'Most of your damage. A cat or a raptor does the most, because both hit 10% harder than other pets and have Claw. A carrion bird does less but is safer, because its Screech weakens what it fights.',
    habits([
        ('At 35 it should have', 'Claw rank 5, Bite rank 5, Growl rank 4, and Dash if it is a cat. All rank 5s come at pet level 32. Rank 6 Claw and Bite come at 40.'),
        ('Learning a new rank', 'Stable your pet. Tame a beast that knows the rank (you can\'t tame anything above your level in Forever). Use the ability in fights until chat says you learned it. Get your pet back and teach it the rank with Beast Training in your spellbook.'),
        ('Keep it happy', 'Feed it the food its family eats. It loses happiness when it dies or you dismiss it, and an unhappy pet does less damage. Green face on the pet frame = full damage.'),
        ('What it gets from you', 'The pet copies your crit chance (all of it), 10% of your attack power and 30% of your armor, and 2 health for each point of your Stamina. Agility gear makes the pet better too.'),
    ])
    + table(['Rank', 'Beasts that teach it, at or under 35'], [[f'<b>{a}</b>', b] for a, b in PETS],
            caption='From Wowhead\'s Forever "taught by" lists, which come from real tames and may be incomplete. Stranglethorn tigers and raptors spawn more often since a 13 Nov hotfix.'))

NEXT = section('next', 'Levels 36 to 40', 'Visit the trainer every even level. The big one is 40.',
    table(['Level', 'New', 'What it changes'], [
        ['36', '<b>Aimed Shot rank 3</b>, Arcane Shot rank 5, Summon Hawk rank 2, Viper Sting, Mend Pet rank 4, Immolation Trap rank 3', 'Every shot in the rhythm hits harder. Viper Sting drains a caster\'s mana.'],
        ['38', 'Aspect of the Hawk rank 4, Wing Clip rank 2', 'More attack power all the time.'],
        ['40', '<b>Bestial Wrath</b> (talent), <b>Volley</b>, <b>Mail armor</b>, Aspect of the Pack, Freezing Trap rank 2, Hunter\'s Mark rank 3', 'Pet +50% damage for 18 sec every 2 min: put it on G and move Rapid Fire to Shift-G. Volley becomes your AoE. Freezing Trap lasts 15 sec. Mail is trained at the class trainer.'],
    ])
    + note('<b>Stats until then:</b> Agility first (attack power, crit, and the pet gets your crit), then Stamina. Intellect is just mana for now: BM runs low without a paladin, so carry water. Mail at 40.', 'tip'))

MISTAKES = section('mistakes', 'Five mistakes', '', habits([
    ('Arcane Shot on cooldown', 'It eats the hawk\'s cooldown. You lose a hawk each time.'),
    ('Multi-Shot on one mob', 'It eats Aimed Shot, your biggest hit.'),
    ('Shooting on the move', 'Auto Shot waits half a second after you stop. Fewer steps, more shots.'),
    ('Feign Death and walking off', 'Forever\'s tooltip means it: after 6 minutes you actually die. Stand up.'),
    ('Growl on in a dungeon', 'The pet pulls mobs off the tank. Autocast off before the first pull.'),
]))

SOURCES = section('sources', 'Sources', 'Read 21 November 2026. None of the numbers has been checked in game yet; tooltips can lag behind hotfixes. Wrong? Tell me in the guild Discord and I\'ll fix it the same night.',
    sources([
        ('Wowhead: BM leveling tips (Docoda)', 'https://www.wowhead.com/forever/guide/classes/hunter/beast-mastery/dps-leveling-tips', 'talent order, rotation, pets'),
        ('Wowhead: BM talent builds', 'https://www.wowhead.com/forever/guide/classes/hunter/beast-mastery/talent-builds-pve-dps', 'raid order to 60'),
        ('Wowhead: BM overview', 'https://www.wowhead.com/forever/guide/classes/hunter/beast-mastery/overview-pve-dps', 'shared cooldowns, pet scaling'),
        ('Wowhead: BM abilities', 'https://www.wowhead.com/forever/guide/classes/hunter/beast-mastery/dps-abilities', ''),
        ('Wowhead: BM rotation and cooldowns', 'https://www.wowhead.com/forever/guide/classes/hunter/beast-mastery/rotation-cooldowns-pve-dps', ''),
        ('Wowhead: hunter pets', 'https://www.wowhead.com/forever/guide/classes/hunter/best-pets-and-pet-management-guide', ''),
        ('Wowhead: hunter abilities by level', 'https://www.wowhead.com/forever/spells/abilities/hunter', 'plus each spell\'s Forever tooltip'),
        ('Wowhead: dungeon overview', 'https://www.wowhead.com/forever/guide/dungeons-overview-locations-details', 'level ranges'),
        ('Blizzard: dev notes', 'https://us.forums.blizzard.com/en/wow/t/2360696', 'Auto Shot delay, traps, hunter tuning'),
        ('Blizzard: hotfixes', 'https://us.forums.blizzard.com/en/wow/t/2403040', 'to 20 Nov'),
        ('wowforeverguides.com macros', 'https://wowforeverguides.com/tools/macros', 'Mark & Send'),
    ]))

PAGE_CSS = '''<style>
    .macros { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-top: 14px; }
    .macro { background: var(--panel); border: 1px solid var(--border); padding: 14px 16px; }
    .macro-head { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; flex-wrap: wrap; }
    .macro-head b { font-family: var(--display); font-size: 17px; letter-spacing: .02em; }
    .mtag { font-size: 11.5px; font-family: var(--display); letter-spacing: .06em; text-transform: uppercase; padding: 2px 8px; border: 1px solid var(--border); }
    .mtag.ok { color: var(--druid); border-color: color-mix(in srgb, var(--druid) 50%, transparent); }
    .mtag.try { color: var(--gold); border-color: color-mix(in srgb, var(--gold) 45%, transparent); }
    pre.code { white-space: pre-wrap; word-break: normal; line-height: 1.5; font-size: 12.5px; }
    .macro p { font-size: 13.5px; color: var(--muted); margin-top: 6px; }
    .macro p b { color: var(--text); font-weight: 600; }
    .macro .mwhy { color: var(--text); }
    section .combo + .habits, section .habits + .combo, section .combo + .prio-grid, section .prio-grid + .habits,
    section .prio-grid + .tblwrap, section .habits + .tblwrap { margin-top: 16px; }
    .board { --key: clamp(36px, calc((100vw - 150px) / 10.4), 80px); min-width: 0; }
    .keys { min-width: 0; }
    @media (max-width: 640px) {
      .keys { overflow-x: auto; justify-content: start; padding-bottom: 6px; -webkit-overflow-scrolling: touch; }
      .row:nth-child(2) { padding-left: calc(var(--key) * 0.25); }
      .row:nth-child(3) { padding-left: calc(var(--key) * 0.45); }
      .row:nth-child(4) { padding-left: calc(var(--key) * 0.7); }
    }
    .sitefoot { margin: 56px 0 40px; padding-top: 18px; border-top: 1px solid var(--border); color: var(--dim); font-size: 13px; }
    .sitefoot a { color: var(--muted); }
  </style>'''

DESC = 'How to play a level 35 Beast Mastery hunter in WoW Forever, solo and in groups: talents, keybinds, macros, the hawk rhythm, pulls, dungeon jobs and pets.'

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beast Mastery at 35 · WoW Forever hunter guide</title>
  <meta name="description" content="{DESC}">
  <meta property="og:title" content="Beast Mastery at 35">
  <meta property="og:description" content="{DESC}">
  <meta property="og:url" content="https://willhsu.dev/hunter/">
  <meta name="theme-color" content="#0b0d14">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 2l12 7v14l-12 7L4 23V9z' fill='%23aad372'/%3E%3Cpath d='M16 7l8 4.5v9L16 25l-8-4.5v-9z' fill='%230b0d14'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&display=swap" rel="stylesheet">
  {STYLE}
  {EXTRA}
  {PAGE_CSS}
</head>
<body>
  {BACKDROP}
  <div class="wrap">
    {HERO}
    <main>
      {SETUP}
      {TALENTS}
      {BINDS}
      {MACROS}
      {RHYTHM}
      {SOLO}
      {GROUP}
      {PET}
      {NEXT}
      {MISTAKES}
      {SOURCES}
    </main>
    <footer class="sitefoot">Will Hsu · &lt;Midnight Riders&gt; · <a href="https://realworldbuilder.github.io/midnight-riders/">the guild</a> · <a href="https://www.instagram.com/wowforeverguide/">@wowforeverguide</a> · <a href="/dungeons/">Dungeon guides</a> · <a href="/">More projects</a></footer>
  </div>
  <div id="float-tip" class="tip" role="tooltip"></div>
  <script>
    const ICON = '{ICON}';
    // every button on the bars; numbers from Forever tooltips (Wowhead dataEnv=16), read 21 Nov 2026
    const SPELLS = {json.dumps(S, ensure_ascii=False)};
    const LAYERS = {json.dumps(LAYERS, ensure_ascii=False)};
    const ROWS = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ['Q', 'W', 'E', 'R', 'T'], ['A', 'S', 'D', 'F', 'G'], ['Z', 'X', 'C', 'V']];
    const MOVE = {{ W: 'Forward', A: 'Turn', S: 'Back', D: 'Turn' }};
{JS_CORE}
  </script>
</body>
</html>
'''

# every data-ref must exist
missing = sorted(set(re.findall(r'data-ref="(\w+)"', html)) - set(S))
assert not missing, missing
os.makedirs(SITE + '/hunter', exist_ok=True)
open(SITE + '/hunter/index.html', 'w').write(html)
print('wrote hunter/index.html', len(html), 'bytes')
