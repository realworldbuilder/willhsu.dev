from h import *

S = []

S.append(section('pool', 'The season 2 pool',
  'Eight dungeons. Five are Midnight\'s own, three are brought back. Timers from the key guides; two sites give The Blinding Vale 30 or 33 minutes instead of 31.',
  table(['Dungeon', 'From', 'Timer', 'Hunter notes'], [
    ['Altar of Fangs', 'Midnight (new in 12.1, three bosses)', '30:00', 'Vile Vial of Volatile Venom trinket. Tuned again in 12.1.5.'],
    ['Murder Row', 'Midnight', '34:00', 'Freightrunner\'s Flask trinket. Cover detection was fixed in 12.1.5; stealth mobs no longer see through walls.'],
    ['Den of Nalorakk', 'Midnight', '32:00', ''],
    ['The Blinding Vale', 'Midnight', '31:00', 'Lightspire Core, the Mastery trinket.'],
    ['Voidscar Arena', 'Midnight', '30:00', 'Void Execution Mandate trinket.'],
    ['Kings\' Rest', 'Battle for Azeroth', '33:00', 'Lustrous Golden Plumage, on-use Agility, top five for the spec.'],
    ['Temple of Sethraliss', 'Battle for Azeroth', '33:00', 'Lots of casters: Counter Shot earns its key here.'],
    ['Ruby Life Pools', 'Dragonflight', '28:00', 'The short one. Big pulls, so Volley and Explosive Shot on two targets every pack.'],
  ])
))

S.append(section('affixes', 'How keys work this season',
  'The ladder from +2 upward. Keys below +6 are the learning tier and the game routes you.',
  table(['Key level', 'What is on'], [
    ['+2 to +5', 'Lindormi\'s Guidance: the marked route enemies have 5% less health and damage, and deaths do not cost time. Icy Veins says it ends at +4; most sites say +5.'],
    ['+5', 'One weekly Xal\'atath\'s Bargain (Ascendant, Voidbound, Pulsar or Devour) is added.'],
    ['+6', 'Guidance removed. Tanks keep the route highlight.'],
    ['+7', 'Fortified or Tyrannical, alternating weekly.'],
    ['+10', 'Both Fortified and Tyrannical.'],
    ['+12', 'The Bargain is replaced by Xal\'atath\'s Guile: each death removes fifteen seconds.'],
    ['Resilient keys', 'Time all eight at +12 and a depleted key never drops below +12; the floor keeps rising, up to +30.'],
  ])
  + table(['Rating', 'Reward'], [
    ['1500', 'Title: the Venomous'],
    ['2000', 'Keystone Master and the Breath of Blight mount'],
    ['2500', 'Keystone Hero'],
    ['3000', 'Keystone Legend and Breath of Ruin'],
    ['3400 or 3600 (sources disagree)', 'Keystone Myth: the Venomous Contender and the Timelost Saddle, now a quest reward in 12.1.5'],
    ['Time a +10', 'That dungeon\'s teleport'],
  ])
  + note('What a key pays is on the <a href="../gear/#mplus">gear page</a>: +2 drops 295, +6 drops Hero track, +10 puts Myth in the vault. Keys at +10 and above also drop Ascendant Venomstones since 12.1.5.', 'info')
))

S.append(section('first', 'Your first keys as a hunter',
  'Things nobody says out loud in the group finder.',
  habits([
    ('Item level before the key', 'Under about 286 you will be declined. Delves tier 8 and the Renown 9 vendor get you there without a single key.'),
    ('Mythic 0 first', 'One run of each of the eight per day, 292 drops, no timer, no affixes. Learn the routes here.'),
    ('Misdirection on the tank', 'Shift-Q before every pull. You have no pet to soak threat and Aimed Shot opens hard.'),
    ('Explosive Shot on two targets', 'Every pack: E on one mob, E on another. That is most of your AoE.'),
    ('Interrupt rotation', 'Counter Shot is 24 seconds. If the group assigns kicks, you take every second cast; if not, kick heals and big AoE casts first.'),
    ('Stand still for Aimed Shot', 'It is a 2.5 second cast. Move during Rapid Fire, Steady Shot or on an instant; plan the cast before the swirlie.'),
    ('Feign Death clears threat and some debuffs', 'Shift-3. If a boss turns to you, Feign before Turtle.'),
    ('Lust', 'You do not have it; the eagle build has no pet. Say so at the start so the group checks who does.'),
  ])
))

S.append(section('raid', 'The Venomous Abyss',
  'Eight bosses on the Coiled Isle, opened 18 Aug 2026. Boss order by wing, with the pieces a Marksmanship Hunter wants.',
  table(['#', 'Boss', 'Hunter loot'], [
    ['1', 'Nek\'zali the Soulcoiler', ''],
    ['2', 'The Twin Fangs', 'Tier head'],
    ['3', 'Entombed Sentinels', 'Tier hands; Keeper\'s Seething Core (Haste proc)'],
    ['4', 'Vashnik the Malignant', 'Tier chest'],
    ['5', 'The Lost Explorers', 'Tier shoulders; Gebbo\'s Bottomless Bag; Boots of the Reckless Wayfarer'],
    ['6', 'Sszorak', 'Tier legs; Apex Brute\'s Claw Ring'],
    ['7', 'The Coiled Altar', 'Zul\'jin\'s Guillotine Technique (single-target trinket); Shroud of the Skulking Viper cloak. 344 on Mythic'],
    ['8', 'Ula\'tek', 'Voracious Heart of Ula\'tek and Font of Venomous Rage, the two best trinkets; Caustic Repose Greatbow; Aqirbane Reliquary neck; Slumbering Coil Curio tier token'],
  ])
  + habits([
    ('LFR needs 276 average', 'Wings drop 279 to 289 and fill the raid row of the vault for 292.'),
    ('Kith\'ix', 'The Unbinding of Kith\'ix is the one-boss raid from 12.1.5. 285 / 298 / 311 / 324 by difficulty, counts for the raid row, and drops Twisted Horror\'s Tendril, the key trinket.'),
    ('The tier set', 'Skulking Viper\'s Ambush: two-piece makes Explosive Shot last longer and hit harder, four-piece shaves Aimed Shot and Rapid Fire every time it bursts. Pieces are on the <a href="../gear/#trinkets">gear page</a> with the Catalyst rules.'),
  ])
))

S.append(section('delves', 'Delves',
  'Twelve across five zones, plus the Nemesis delve. Four Bountiful a day; tier 8 is where the loot stops improving.',
  table(['Zone', 'Delves'], [
    ['Zul\'Aman', 'Atal\'Aman, Twilight Crypts'],
    ['Eversong', 'Collegiate Calamity, The Darkway, Parhelion Plaza, The Shadow Enclave'],
    ['Coiled Isle', 'Gnarldor Isle, The Ring of Glory (both new in 12.1)'],
    ['Harandar', 'The Grudge Pit, The Gulf of Memory'],
    ['Voidstorm', 'Shadowguard Point, Sunkiller Sanctum'],
    ['Nemesis', 'Venomfall Deeps (Azta\'rec). Not Bountiful, no vault credit, one-time Myth crests'],
  ])
  + habits([
    ('Valeera Sanguinar', 'Your companion, tank, healer or damage. Level cap 80 this season. Past 15 she only levels in Bountiful delves, keys not required for that.'),
    ('Tiers', '1 to 11, each unlocks the next. Life counter from tier 4. Tier 3 and up require the campaign done on at least one character.'),
    ('Keys', 'Restored Coffer Key = 100 shards, 600 shards a week. Delver\'s Journey rank 6 lets Naleidea Rivergleam sell two a week.'),
    ('Weekly', '"Purging the Vaults" gives a Trovehunter\'s Bounty map, one Hero item at tier 8 or above per week. Tier 11 adds a Gilded Stash with 5 Myth crests, four a week.'),
  ])
))

S.append(section('sources', 'Sources', '', sources([
    ('Method: Season 2 Mythic+ rotation', 'https://www.method.gg/guides/wow-midnight-season-2-mythic-dungeon-rotation', ''),
    ('Season 2 M+ guide with timers and affixes', 'https://conquestcapped.com/guides/wow/midnight-mythic-plus-season-2/', ''),
    ('Wowhead: Lindormi\'s Guidance', 'https://www.wowhead.com/news/new-lindormis-guidance-mythic-affix-provides-basic-dungeon-route-in-midnight-379948', ''),
    ('Venomous Abyss', 'https://warcraft.wiki.gg/wiki/Venomous_Abyss', 'boss order and loot'),
    ('The Unbinding of Kith\'ix', 'https://warcraft.wiki.gg/wiki/The_Unbinding_of_Kith%27ix', ''),
    ('Delve', 'https://warcraft.wiki.gg/wiki/Delve', 'zones, Valeera, tiers'),
    ('Delve rewards table', 'https://conquestcapped.com/guides/wow/midnight-delves-rewards/', ''),
    ('12.1.5 content update notes', 'https://www.bluetracker.gg/wow/topic/eu-en/24304162-12-1-5-content-update-notes/', ''),
  ])))

PAGE = dict(
  slug='dungeons/', title='Dungeons & raid · Alaranarises', crest='achievement_dungeon_outland_dungeonmaster',
  kicker='Season 2 · Patch 12.1.5 · the eight keys, the raid, the delves',
  h1='Dungeons & raid', lede='The dungeon pool with timers, how key levels and affixes stack up this season, what a hunter does in a first key, the Venomous Abyss boss by boss with the pieces you want, and the delve map.',
  tags=['8 dungeons', 'Guidance to +5', 'Venomous Abyss · 8 bosses', 'Delves · tier 8'],
  jump=[('pool', 'Pool'), ('affixes', 'Affixes'), ('first', 'First keys'), ('raid', 'Raid'), ('delves', 'Delves')],
  sections=S,
)
