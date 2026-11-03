from h import *

S = []

S.append(section('ladder', 'The ladder: item 102 to 344',
  'Midnight squished item levels. The boost set is 102. Leveling greens at 90 are about 253 to 259. Season 2 gear runs on five tracks, six ranks each, and every rank costs 20 of that track\'s Mistcrest.',
  table(['Track', 'Rank 1 to 6', 'Crest', 'Where it drops'], [
    ['<span class="vet">Adventurer</span>', '266 to 282', 'Adventurer Mistcrest', 'Outdoor events, Heroic dungeons, Delve tier 4'],
    ['<span class="vet">Veteran</span>', '279 to 295', 'Veteran Mistcrest', 'LFR, Heroic dungeons (10 crests a run), Delves 5 to 6, Field Accolade caches'],
    ['<span class="champ">Champion</span>', '292 to 308', 'Champion Mistcrest', 'Normal raid, Mythic 0, keys +2 to +5, Delves 7 to 10, Renown 9 vendor gear'],
    ['<span class="hero">Hero</span>', '305 to 321', 'Hero Mistcrest', 'Heroic raid, keys +6 to +9, Delve tier 8 Trovehunter map and tier 11 (15 crests a run), first world boss item of the week'],
    ['<span class="myth">Myth</span>', '318 to 334', 'Myth Mistcrest', 'Mythic raid, keys +10 and up, Gilded Stash after tier 11 delves, Labyrinth vendor (321)'],
    ['<span class="myth">Myth 9/6</span>', '344', 'none', 'Last two Mythic raid bosses and their vault slots only'],
    ['Ascendant Venomstones', 'Hero 321 to about 331, Myth 334 to about 344', '10 Venomstones, one use per item', '12.1.5. Weapon, trinket or neck at max rank. Sources give 328/340 or 331/344; check the tooltip in game'],
  ], 'Live values from the Midnight Season 2 wiki page (28 Oct 2026) and Icy Veins. Ignore charts that still show 259 to 328: those are PTR numbers.')
  + note('<b>Crests are uncapped</b> since the 20 Oct 2026 hotfix. Three lower crests trade for one higher at the Crest Exchange in Silvermoon once you have that track\'s Feat of Strength. Under about 286 item level, pug groups will not take you, so get there through delves and the vendors below before you touch the Group Finder for keys.', 'info')
))

S.append(section('fresh90', 'Fresh 90: the first two days',
  'In order of item level per hour. Everything here is solo or queueable. Do the vendor lines first, they are the free ones.',
  table(['Do this', 'Gets you', 'Track'], [
    ['<b>Zul\'jarra\'s Forces to Renown 9</b> (Coiled Isle world quests, Vaults of Atal\'Utek dailies)', 'Neck, helm, belt, trinket and bracers from the quartermaster', '<span class="champ">Champion</span>'],
    ['<b>Field Accolades</b> from Void Strikes and Ritual Sites, turned in to Maren Silverwing in Silvermoon. World quests pay 30 each on Heroic World Tier, 10 on Normal', 'Caches with a Veteran piece', '<span class="vet">Veteran</span>'],
    ['<b>First two Weekly Apex Caches</b> and Venom-Cursed Fragments', 'Veteran, then Champion pieces', '<span class="vet">Veteran</span> → <span class="champ">Champion</span>'],
    ['<b>Heroic dungeons</b>, queue opens at item level 266', '276 drops, vault slot 289, 10 Veteran crests a run', '<span class="vet">Adventurer 4</span>'],
    ['<b>Prey hunts</b> on the Coiled Isle, four or five a week', 'Normal 266, Hard 279, Nightmare 292. Vault 279 / 292 / 305', 'up to <span class="champ">Champion</span>'],
    ['<b>World boss</b> Nymrissa Wavecaller, Tidebound Grotto on the Coiled Isle', 'First item of the week is guaranteed Hero track', '<span class="hero">Hero</span>'],
    ['<b>Bountiful Delves tier 8</b> as soon as Valeera and you survive them', '295 from the coffer, 305 Hero from the weekly Trovehunter map, vault 305', '<span class="champ">Champion 2</span> → <span class="hero">Hero 1</span>'],
    ['<b>Mythic 0</b>, one run of each of the eight dungeons per day', '292, vault 302', '<span class="champ">Champion 1</span>'],
    ['<b>LFR Venomous Abyss</b>, needs average 276', '279 to 289 by wing, vault 292', '<span class="vet">Veteran</span>'],
    ['<b>Labyrinth of Kindo\'jan</b> (12.1.5)', 'Wah\'du sells 321 gear for Mythical Soul Fragments, one a week; chambers count as World activities for the vault', '<span class="myth">Myth 2</span>'],
  ])
  + note('<b>Delve tier 8 is the breakpoint.</b> Tiers 9 to 11 drop the same 295 and 305 and only add crests, so go to 11 for Hero and Myth crests, not for the coffer. Four Bountiful delves a day, each needs a Restored Coffer Key (100 shards, shard cap 600 a week). Valeera Sanguinar is your companion and now levels to 80; past level 15 she only gains XP in Bountiful delves.', 'tip')
))

S.append(section('mplus', 'Mythic+ and the Great Vault',
  'End-of-dungeon loot and the vault slot each key level earns. Method and the wiki disagree on the +7 to +9 vault item (311 or 315), so expect either.',
  table(['Key', 'End of dungeon', 'Vault', 'Crests'], [
    ['+2 to +3', '295 <span class="champ">C2</span>', '305 <span class="hero">H1</span>', 'Champion 12 / 14'],
    ['+4', '298 <span class="champ">C3</span>', '308 <span class="hero">H2</span>', 'Hero 10'],
    ['+5', '302 <span class="champ">C4</span>', '308 <span class="hero">H2</span>', 'Hero 10'],
    ['+6', '305 <span class="hero">H1</span>', '311 <span class="hero">H3</span>', 'Hero 12'],
    ['+7', '305 <span class="hero">H1</span>', '311 or 315', 'Hero 14'],
    ['+8', '308 <span class="hero">H2</span>', '311 or 315', 'Hero 18'],
    ['+9', '308 <span class="hero">H2</span>', '311 or 315', 'Myth 10'],
    ['+10 to +11', '311 <span class="hero">H3</span>', '318 <span class="myth">M1</span>', 'Myth 12 / 14'],
    ['+12 and up', '311 <span class="hero">H3</span>', '318 <span class="myth">M1</span>', 'Myth 16'],
  ])
  + table(['Vault row', 'Slot 1', 'Slot 2', 'Slot 3'], [
    ['Dungeons', '1 key or M0', '4', '8'],
    ['Raid', '2 bosses', '4', '6 (one source says 5 and 8)'],
    ['World', '2 activities (delves, prey hunts, world boss, Labyrinth chambers, Curse Surges)', '4', '8'],
  ], 'Great Vault thresholds. From the second week of the season, any three filled slots can be traded for a Nebulous Voidcore bonus roll instead of an item.')
  + table(['Raid difficulty', 'Bosses 1 to 2', '3 to 4', '5 to 6', '7 to 8', 'Vault'], [
    ['LFR', '279', '282', '285', '289', '292 <span class="champ">C1</span>'],
    ['Normal', '292', '295', '298', '302', '305 <span class="hero">H1</span>'],
    ['Heroic', '305', '308', '311', '315', '318 <span class="myth">M1</span>'],
    ['Mythic', '318', '321', '324', '<b>344</b>', '334, or 344 from the last two'],
  ], 'The Venomous Abyss. Kith\'ix, the one-boss raid from 12.1.5, drops 285 / 298 / 311 / 324 by difficulty and counts for the raid row.')
))

S.append(section('stats', 'Stats',
  'Every hand-written 12.1.5 guide agrees on the shape. Item level first, because Agility beats any secondary.',
  habits([
    ('Weapon damage, then Agility', 'A ranged weapon upgrade beats everything else in the bag. After that, higher item level is more Agility and wins almost every time.'),
    ('Critical Strike', 'Feeds Penetrating Shots, Lethality, Critical Precision and the capstones. The Bell Tolls adds 3% on top. Your best secondary.'),
    ('Mastery', 'Sniper Training: more range and more damage on everything. Second.'),
    ('Versatility', 'Flat damage and flat damage reduction. Third, and the one to like in keys.'),
    ('Haste', 'Only speeds Auto Shot, Focus and Aimed Shot. Last, no breakpoints to chase.'),
    ('Tertiaries', 'Method says Avoidance, then Speed, then Leech. Top key players wear Leech first. Either way, never pick a tertiary over item level.'),
  ])
  + note('The order is <b>Agility &gt; Crit &gt; Mastery &gt; Versatility &gt; Haste</b> from Method, Icy Veins and Murlok. Noxxic\'s auto-generated page puts Versatility and Haste first; ignore it. Nobody publishes a separate Dark Ranger order, so use this one for both hero trees.', 'info')
))

S.append(section('enchants', 'Enchants, gems, sockets',
  'Midnight removed cloak and wrist enchants and brought helm and shoulder enchants back. Prices move, so buy one slot at a time as pieces stop changing.',
  table(['Slot', 'Enchant', 'Note'], [
    ['Weapon', 'Rite of the Hash\'ey', 'What 45 of the top 50 key hunters run. Method lists Acuity of the Ren\'dorei instead; both are fine, Hash\'ey is the popular one'],
    ['Head', 'Empowered Rune of Avoidance', 'Hex of Leeching for keys if you take a lot of chip damage'],
    ['Shoulders', 'Amirdrassil\'s Grace', ''],
    ['Chest', 'Mark of the Worldsoul', 'Unanimous'],
    ['Legs', 'Forest Hunter\'s Armor Kit', 'Leatherworking'],
    ['Boots', 'Lynx\'s Dexterity or Shaladrassil\'s Roots', 'Split evenly among top players; movement speed or stats'],
    ['Rings, both', 'Eyes of the Eagle', 'Unanimous. The Gear Enchanting quest in your log teaches the mechanics with a weaker one'],
    ['Wrist, cloak', 'none', 'No enchant exists for these in Midnight'],
  ])
  + habits([
    ('Gems', 'One Eversong Diamond in your single unique socket: Powerful (most players) or Indecipherable. Every other socket a Flawless Masterful Garnet (Crit and Mastery). For the diamond\'s colour bonus, one each of Deadly Amethyst, Deadly Peridot and Deadly Lapis, then Garnets.'),
    ('Buying sockets', 'Radiant Jewelbinder adds a socket to helm, bracers or belt, from Vaultkeeper Elysa in Silvermoon for 6 Thalassian Tokens of Merit. The season 2 version is the Miasmic Jewelbinder from the Great Vault vendor. Head, wrist and waist only; one socket per piece.'),
    ('Hunter ammo and scopes', 'Engineering makes Laced Zoomshots and Weighted Boomshots (ammo) and Smuggler\'s Lynxeye and Farstrider\'s Hawkeye (scopes). Method\'s consumables list says these replace oils and weapon enchants for hunters, but every spec guide still lists Phoenix Oil plus a normal enchant. Test in game: if the oil buff drops when you load ammo, they do not stack.'),
  ])
))

S.append(section('consumables', 'Consumables',
  'What to carry for a key or a raid night. The boost\'s healing potions and food are fine while leveling.',
  table(['Type', 'Item', 'Made by'], [
    ['Flask', 'Flask of the Shattered Sun (Crit) or Flask of the Magisters (Mastery)', 'Alchemy'],
    ['Combat potion, raid', 'Potion of Recklessness; Light\'s Potential as a second pot at the end of a fight', 'Alchemy'],
    ['Combat potion, keys', 'Liquid Luster (stacking Versatility)', 'Alchemy'],
    ['Health potion', 'Concentrated Silvermoon Health Potion', 'Alchemy'],
    ['Food', 'Hearty Royal Roast (survives a death). Feasts: Harandar Celebration, Silvermoon Parade', 'Cooking'],
    ['Augment rune', 'Void-Touched Augment Rune, one hour, lost on death', 'Vendor and drops'],
    ['Weapon oil', 'Thalassian Phoenix Oil (Crit and Haste). Oils are Enchanting now, not Alchemy', 'Enchanting'],
    ['Cauldrons', 'Cauldron of Sin\'dorei Flasks, Voidlight Potion Cauldron', 'Alchemy'],
  ])
))

S.append(section('crafted', 'Crafted gear and embellishments',
  'Two embellished items at once, no more. Crafted gear tops out at 331, so it is only worth wearing for those two slots.',
  habits([
    ('Spark of Tides', 'One a week from the weekly quests: Trailing Xal\'atath (Vereesa Windrunner, Silvermoon, 100 Fading Voidwhispers), Sparks of War (Zerella, Falconwing Square, PvP) or Turn Back the Surge (Talon Commander Zela, Tokka\'s Landing, three Curse Surges). Armour costs two Sparks.'),
    ('Crafted item level', 'Spark only: 305. Add 80 Hero crests: 318. Add 80 Myth crests: 331.'),
    ('The two pieces', 'Farstrider\'s Trophy Belt and Farstrider\'s Plated Bracers, Leatherworking mail, Crit and Mastery, each with the Arcanoweave Lining embellishment (a mana wyrm that grants primary stat to you and an ally). 97 of 100 top-player embellishment slots are Arcanoweave.'),
    ('Do not craft a weapon', 'Nebulous Voidcore bonus rolls can hand you a Myth-track weapon from a boss. A crafted one would be dead gold.'),
    ('New season 2 embellishments', 'Adorned Fang, Snakeskin Lining, Polished Ammolite, Hunter\'s Ritual Stone, Coiled Snake-Eye. None of the hunter guides rate them over Arcanoweave; skip unless a sim says otherwise.'),
  ])
))

S.append(section('trinkets', 'Trinkets and the tier set',
  'Bloodmallet single-target sim from 28 Oct 2026, cross-checked with Method, Maxroll and the top 50 key hunters.',
  table(['#', 'Trinket', 'From', 'Why'], [
    ['1', 'Voracious Heart of Ula\'tek', 'Ula\'tek, Venomous Abyss', '90 second on-use Agility; line it up with Trueshot every time'],
    ['2', 'Font of Venomous Rage', 'Ula\'tek, Venomous Abyss', 'Four minute on-use channel, big Nature hit plus splash. Do not try to sync it with Trueshot if you also carry Voracious Heart'],
    ['3', 'Zul\'jin\'s Guillotine Technique', 'The Coiled Altar, Venomous Abyss', 'Axe proc that scales with missing health. Single target only'],
    ['4', 'Vile Vial of Volatile Venom', 'Altar of Fangs', 'On-use Agility, the dungeon one'],
    ['5', 'Lustrous Golden Plumage', 'Kings\' Rest', 'On-use Agility'],
    ['Keys', 'Twisted Horror\'s Tendril', 'Kith\'ix', 'Stacking Crit proc, number two among key hunters, strongest in AoE. Swap it in for the Coiled Altar trinket in keys'],
  ])
  + habits([
    ('Skulking Viper\'s Ambush, the hunter tier', 'Two pieces: Explosive Shot lasts one second longer and does 5% more. Four pieces: Aimed Shot and Rapid Fire do 5% more, and every Explosive Shot burst takes half a second off both cooldowns. Explosive Shot on cooldown is already rule two of the rotation; the set is why.'),
    ('Where the pieces drop', 'Head from The Twin Fangs, hands from Entombed Sentinels, chest from Vashnik the Malignant, shoulders from The Lost Explorers, legs from Sszorak. Ula\'tek drops the Slumbering Coil Curio, a token Kirana in Silvermoon turns into any slot.'),
    ('The Catalyst', 'In the Silvermoon Bazaar next to the Voidforge. Venomblight Manaflux charges: one every two weeks, cap eight, plus extra from Serpent Scion and (after your first set bonus) from keys, raid bosses and Bountiful delves. Converted pieces keep their secondaries.'),
  ])
))

S.append(section('professions', 'Professions',
  'Pick two in Silvermoon. The class answer and the gold answer are different.',
  habits([
    ('Leatherworking + Skinning', 'The class pick. Leatherworking crafts the belt and bracers above and the Adorned Fang embellishment; Skinning feeds it Void-Tempered Leather and sells the rest.'),
    ('Gold instead', 'Inscription (missives on every crafted piece), Jewelcrafting and Alchemy top every 2026 gold list. Herbalism or Mining if you want zero crafting-order effort.'),
    ('Engineering', 'Only if you want the hunter ammo and scopes above. Check that they stack with oil and a weapon enchant before committing.'),
  ])
))

S.append(section('sources', 'Sources', 'Checked 3 Nov 2026. Icy Veins blocks automated reads, so its numbers came through search snippets and its news mirror.',
  sources([
    ('Midnight Season 2', 'https://warcraft.wiki.gg/wiki/Midnight_Season_2', 'tracks, crests, delves, M+ table'),
    ('Method: how to gear fast to 335', 'https://www.method.gg/guides/how-to-gear-fast-and-reach-item-level-335-in-wow-midnight-season-2', ''),
    ('Method: Marksmanship gearing', 'https://method.gg/guides/marksmanship-hunter/gearing', 'trinkets, crafted picks'),
    ('Method: stats, races and consumables', 'https://method.gg/guides/marksmanship-hunter/stats-races-and-consumables', ''),
    ('Method: Great Vault item levels', 'https://www.method.gg/guides/wow-midnight-season-2-great-vault-reward-item-levels-and-upgrade-track', ''),
    ('Method: all Midnight consumables, enchants and gems', 'https://www.method.gg/guides/list-of-all-midnight-consumables-enchants-and-gems', ''),
    ('Maxroll: Marksmanship raid guide', 'https://maxroll.gg/wow/class-guides/marksmanship-hunter-raid-guide', 'enchants, gems, embellishments'),
    ('Murlok.io: Marksmanship M+ top players', 'https://murlok.io/hunter/marksmanship/m+', 'what the top 50 actually wear'),
    ('Bloodmallet: Marksmanship trinkets', 'https://bloodmallet.com/chart/get/trinkets/castingpatchwerk/hunter/marksmanship', ''),
    ('Icy Veins: item level of loot in Season 2', 'https://wp-prod.icy-veins.com/item-level-of-loot-in-midnight-season-2/', ''),
    ('Delve rewards table', 'https://conquestcapped.com/guides/wow/midnight-delves-rewards/', ''),
    ('Blizzard hotfixes, 30 Oct 2026', 'https://worldofwarcraft.blizzard.com/news/24307310/hotfixes-october-30-2026', 'crest cap removed'),
    ('Skulking Viper\'s Ambush', 'https://warcraft.wiki.gg/wiki/Skulking_Viper\'s_Ambush', 'tier set'),
  ])
))

PAGE = dict(
  slug='gear/', title='Gear · Alaranarises', crest='inv_misc_bag_12',
  kicker='Season 2 · Patch 12.1.5 · for a Marksmanship Hunter arriving at 90',
  h1='Gear', lede='Item level 102 is where the boost leaves you. This page is the whole road from there: the tracks and crests, what to do in the first two days at 90, what each key and raid pays, and the stats, enchants, gems and consumables once pieces stop changing.',
  tags=['Fresh 90 first', 'Agility · Crit · Mastery', 'Delve tier 8 is the breakpoint', 'Two embellishments'],
  jump=[('ladder', 'Ladder'), ('fresh90', 'Fresh 90'), ('mplus', 'Keys & vault'), ('stats', 'Stats'), ('enchants', 'Enchants'), ('consumables', 'Consumables'), ('crafted', 'Crafted'), ('trinkets', 'Trinkets & tier'), ('professions', 'Professions')],
  sections=S,
)
