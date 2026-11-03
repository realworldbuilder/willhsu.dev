from h import *

S = []

S.append(section('week', 'This week',
  'Tuesday 15:00 UTC reset. Ticks are saved in this browser and clear themselves at the reset.',
  '<div class="resetline"><span>Next reset: <b id="next-reset">…</b></span><button data-reset="wk">Clear ticks</button></div>'
  + checklist('wk', [
    ('Open the Great Vault', 'Dornogal or Silvermoon. Take the item or, from week two, a Nebulous Voidcore if three slots are filled with nothing you want.'),
    ('Spark quest', 'Trailing Xal\'atath (Vereesa Windrunner, Silvermoon), or Sparks of War, or Turn Back the Surge. One Spark of Tides a week.'),
    ('World boss: Nymrissa Wavecaller', 'Tidebound Grotto, Coiled Isle. First item of the week is Hero track.'),
    ('Kith\'ix', 'One boss, any difficulty, counts for the raid row. Twisted Horror\'s Tendril lives here.'),
    ('Venomous Abyss wings', 'LFR at 276 average. Two bosses fill the first raid slot.'),
    ('Purging the Vaults', 'The delve weekly. Trovehunter\'s Bounty map, one Hero item at tier 8 or above.'),
    ('Eight world activities', 'Bountiful delves (four a day), prey hunts, the world boss, Labyrinth chambers, Curse Surges all count.'),
    ('Prey hunts, four or five', 'Coiled Isle. Nightmare difficulty puts Hero in the vault and drops Venomstones.'),
    ('Aqir Invasion first boss', 'Eversong or Zul\'Aman, alternating weekly, ten minutes each hour. Aqirologist\'s Satchel.'),
    ('Labyrinth of Kindo\'jan', 'Chambers for the World row; one Mythical Soul Fragment a week toward Wah\'du\'s 321 gear.'),
    ('Weekly Voidcore from Orin Straylight', '5,000 gold, 2,000 Gloomstone Mergel or 100 Veteran crests. Only when you have the spare.'),
    ('Four keys, or eight', 'One key fills slot one. Four and eight fill the rest. Mythic 0 counts.'),
    ('Catalyst charge', 'One every two weeks, cap eight. Convert the off-piece with the worst stats first.'),
    ('Re-check this page\'s numbers', 'Method and Icy Veins both update within a day of a hotfix. If a line here looks off, it moved.'),
  ], 'alaranarises-weekly', 'week')
))

S.append(section('day', 'Every day',
  'Clears at 15:00 UTC.',
  '<div class="resetline"><span>Short list on purpose.</span><button data-reset="dy">Clear ticks</button></div>'
  + checklist('dy', [
    ('Four Bountiful delves', 'Tier 8 once you can. Coffer key each.'),
    ('Mythic 0 lockout', 'One of each of the eight, if you are still under 300.'),
    ('Coiled Isle world quests', 'Zul\'jarra\'s Forces renown toward the Renown 9 vendor gear; Field Accolades on Heroic World Tier pay triple.'),
    ('Vaults of Atal\'Utek dailies', 'Same renown.'),
    ('Repair, restock, sell greys', 'Any vendor with an anvil. Flask, food, pot, rune before a key.'),
  ], 'alaranarises-daily', 'day')
))

S.append(section('session', 'Every session and every pull',
  'Not ticked, just read until they are habits.',
  habits([
    ('Before a key', 'Flask, food, rune, pot in the bag, Misdirection on Shift-Q, the hero tree you mean to run, a quest log under 20.'),
    ('Every pull', 'Hunter\'s Mark on the big one. Misdirection on the tank. Aimed Shot started before the tank is in range. Explosive Shot on two targets. Black Arrow whenever it lights up.'),
    ('Every fight that goes wrong', 'Under 50%: Exhilaration (T). Big hit coming: Survival of the Fittest (Shift-4). Melee on you: Binding Shot at your feet (Shift-R), Disengage (Shift-2). Dying: Turtle (Z), then Feign Death (Shift-3) when it ends.'),
    ('Every level to 90', 'N glows: spend the point. Hero tree empties first. Equip any quest reward with a higher item level; Crit or Mastery breaks ties. Spellbook (P) for anything new.'),
    ('Every patch', 'Re-import the talent string from Method or Icy Veins. Walk the bars: a changed talent leaves a greyed button. Update these pages.'),
  ])
))

S.append(section('sources', 'Sources', '', sources([
    ('Method: Great Vault item levels and tracks', 'https://www.method.gg/guides/wow-midnight-season-2-great-vault-reward-item-levels-and-upgrade-track', ''),
    ('Method: Sparks of Tides', 'https://www.method.gg/guides/how-to-get-sparks-of-tides-in-wow-midnight-season-2', ''),
    ('Season 2 weekly checklist', 'https://expcarry.com/wow-midnight-season-2-weekly-checklist', ''),
    ('Weekly to-do, season 2', 'https://gamingpromax.com/wow-midnight-weekly-to-do-checklist-season-2/', ''),
    ('Icy Veins: 12.1 survival guide', 'https://wp-prod.icy-veins.com/?p=152587', 'world boss rules'),
    ('Labyrinth of Kindo\'jan', 'https://warcraft.wiki.gg/wiki/Labyrinth_of_Kindo%27jan', ''),
    ('12.1.5 overview', 'https://wow.gg/guides/midnight-patch-12-1-5-overview', 'Aqir Invasions, Voidcore vendor'),
  ])))

PAGE = dict(
  slug='weekly/', title='Weekly · Alaranarises', crest='inv_misc_pocketwatch_01',
  kicker='Season 2 · Patch 12.1.5 · reset is Tuesday 15:00 UTC',
  h1='Weekly', lede='The reset list for a level 90 Marksmanship Hunter: what pays Hero and Myth, what fills the vault, and the short daily list. Tick as you go; the page clears itself when the week turns.',
  tags=['Vault 1 / 4 / 8', 'Spark once a week', 'Delve tier 8', 'Ticks clear on reset'],
  jump=[('week', 'This week'), ('day', 'Every day'), ('session', 'Every session')],
  sections=S,
)
