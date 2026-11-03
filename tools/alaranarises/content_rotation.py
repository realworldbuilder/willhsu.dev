from h import *

S = []

S.append(section('idea', 'The idea in one paragraph',
  '',
  '<p class="section-note">Aimed Shot makes <b>Precise Shots</b>. Black Arrow spends them and is the hardest hit you have when it is lit. Explosive Shot, Volley and Rapid Fire come back every 16 to 45 seconds and are pressed the moment they return. Trueshot every two minutes turns the next fifteen seconds into the Withering Fire window where Black Arrow fires extra arrows. Steady Shot is what you press when nothing else is ready. That is the whole spec; the lists below are the order when two things are ready at once.</p>'
  + habits([
    ('Precise Shots', 'Two stacks after every Aimed Shot. Make Black Arrow or Arcane Shot (Multi-Shot in AoE) 60% cheaper and stronger. Never let them sit while you cast another Aimed Shot: that wastes the next two.'),
    ('Deathblow', 'The proc that lets Black Arrow fire in the middle of a fight (it is always usable above 80% and below 20% health). Rapid Fire always grants one (Soul Drinker); Aimed Shot has a chance; Wailing Arrow procs it.'),
    ('Trick Shots', 'Makes Aimed Shot and Rapid Fire cleave. Multi-Shot on three or more targets gives it, Volley gives it for six seconds without eating it, and Bleak Powder hitting two or more enemies gives it (fixed in 12.1.5).'),
    ('Lock and Load', 'A free, instant Aimed Shot. Spend it as it comes; it has no line of its own in the Dark Ranger list.'),
    ('Withering Fire', 'Trueshot\'s window. Black Arrow fires two extra arrows at nearby targets at 30% damage (Blighted Quiver adds two more), and you get a free Deathblow. Black Arrow is about three times its normal value inside it.'),
    ('The eagle', 'Avian Specialization. No pet, so no Misdirection target of your own, no taunt and nothing to hold a mob. In return Aimed Shot and Rapid Fire hit harder and Harrier\'s Cry is a burst button. Fetch: Eagle (Ctrl-7) loots for you.'),
  ])
))

S.append(section('opener', 'Single target: the opener',
  'Pre-pull and the first ten seconds. Potion and the Voracious Heart trinket go with Trueshot.',
  prio([
    ('Hunter\'s Mark (Shift-1), before the pull', 'Flat damage buff on up to five targets since 12.1. Put it on the thing that will live longest.'),
    ('Aimed Shot (1), start it about 2.5 seconds before the tank pulls', 'It lands as combat starts and you already hold two Precise Shots.'),
    ('Black Arrow (Q)', 'The target is above 80%, so it is usable. Starts the DoT and the Corpsecaller minion engine.'),
    ('Explosive Shot (E), then Explosive Shot again', 'The 12.1 version stacks when double-cast and the two-piece tier makes it last longer.'),
    ('Volley (R)', 'Six seconds of free Trick Shots. Fine on a single target too.'),
    ('Trueshot (G), potion, trinket', 'Opens Withering Fire, hands you a Deathblow and a Dark Hound.'),
    ('Aimed Shot (1), Black Arrow (Q), Rapid Fire (3)', 'Deathblow makes Aimed Shot hand you a free Black Arrow; Rapid Fire guarantees the next Deathblow.'),
  ])
))

S.append(section('st', 'Single target: the priority',
  'Top to bottom, press the highest thing that is ready. Assisted Highlight glows the same answer on your bar.',
  prio([
    ('Black Arrow (Q) with Precise Shots up', 'About three times its damage inside Trueshot. Precise Shots should never cap at two.'),
    ('Explosive Shot (E) on cooldown, back to back when you can', 'It stacks, and with the four-piece every burst takes half a second off Aimed Shot and Rapid Fire.'),
    ('Volley (R) on cooldown', 'Trick Shots for six seconds and Salvo if talented.'),
    ('Aimed Shot (1) during Trueshot if you are about to cap two charges, or when Precise Shots is down and Black Arrow is ready', 'Two charges sitting there is wasted damage. Watch the little counter on key 1.'),
    ('Trueshot (G) on cooldown', 'Two minutes. Do not save it for a phase that may never come.'),
    ('Rapid Fire (3) on cooldown', 'As Dark Ranger you cast it regardless of Precise Shots: guaranteed Deathblow, and a 30% Lock and Load chance through Windrunner Quiver.'),
    ('Wailing Arrow (the Trueshot button, once per window)', 'Wailing Dead turns G into it for fifteen seconds after Trueshot. Shadow AoE, silences NPCs, procs Deathblow.'),
    ('Arcane Shot (2) to spend Precise Shots', '60% cheaper while the buff is up. Spend before the next Aimed Shot.'),
    ('Aimed Shot (1) on cooldown', 'The builder. 2.5 second cast, two charges.'),
    ('Steady Shot (5)', 'Filler and Focus. Never stop casting.'),
  ])
))

S.append(section('aoe', 'AoE and keys',
  'Explosive Shot on different targets, Volley on cooldown, keep Trick Shots up, and Black Arrow\'s Bleak Powder cone does the rest.',
  table(['Targets', 'What changes'], [
    ['1', 'List above. Arcane Shot spends Precise Shots.'],
    ['2', 'Multi-Shot (4) instead of Arcane Shot, and Bleak Powder hitting both gives you Trick Shots for free.'],
    ['3 or more', 'Multi-Shot grants Trick Shots. Aimed Shot and Rapid Fire now cleave; Rapid Fire eats the buff, so reapply before it.'],
    ['Pack opener', 'Hunter\'s Mark on the five best targets, Explosive Shot on two different mobs, Volley, Trueshot if the pack deserves it.'],
  ])
  + prio([
    ('Explosive Shot (E) on cooldown, on different targets', 'Each target gets its own DoT and its own tier-set cooldown refund.'),
    ('Volley (R) on cooldown', 'Six seconds of Trick Shots that nothing consumes.'),
    ('Aimed Shot (1) with Trick Shots when about to cap, or when Precise Shots is down and Black Arrow is ready', 'Trick Shots makes it cleave.'),
    ('Black Arrow (Q) to spend Precise Shots', 'Bleak Powder: a cone behind the target, eight-target cap. Umbral Reach gives Trick Shots back when it hits two or more.'),
    ('Multi-Shot (4) to apply Trick Shots', 'Only when it is down and Volley is not running.'),
    ('Trueshot (G) on cooldown', 'Withering Fire arrows spray the pack.'),
    ('Rapid Fire (3) with Trick Shots up', 'It consumes the buff to cleave, so apply first.'),
    ('Wailing Arrow once per Trueshot window', ''),
    ('Multi-Shot (4) to spend Precise Shots', ''),
    ('Aimed Shot (1) with Trick Shots up', ''),
    ('Steady Shot (5)', 'Filler.'),
  ])
))

S.append(section('cds', 'Cooldowns and defensives',
  'Where each of the other keys fits.',
  habits([
    ('Trueshot (G), 2 min', 'Burst. Pair with the on-use trinket and the potion. In keys, the biggest pack coming up beats the boss if the boss is not close.'),
    ('Harrier\'s Cry (Shift-F)', 'The eagle\'s burst, from Avian Specialization. Use it on the same pull as Trueshot or the one after; it has no reason to wait.'),
    ('Counter Shot (F), 24 s', 'Your interrupt. Twenty-four seconds is short enough to kick every other cast in a pack; call it in group chat if the tank asks who has the next one.'),
    ('Exhilaration (T)', 'Heals you. Under 50%, press it. Smoke Screen gives you three seconds of Survival of the Fittest with it.'),
    ('Survival of the Fittest (Shift-4)', 'Big damage reduction for a short time. The tank\'s raid-warning or a boss cast bar is the cue. Smoke Screen fires Exhilaration at 50% while it is up.'),
    ('Aspect of the Turtle (Z)', 'You cannot attack while it is up. It is for the moment you would otherwise die. Feign Death (Shift-3) the second it ends if the mob is still on you.'),
    ('Disengage (Shift-2), Binding Shot (Shift-R), Freezing Trap (Shift-5), Intimidation (Shift-E)', 'Space-makers. Dark Chains makes Disengage root-then-slow the nearest enemy. Binding Shot at your own feet is the panic button for melee adds.'),
    ('Misdirection (Shift-Q)', 'On the tank before every pull in a group. There is no pet to take it instead.'),
  ])
))

S.append(section('hero', 'Dark Ranger: every node',
  'The 12.1.5 tree as it is in game. The talent string on the setup page takes all of it.',
  table(['Node', 'What it does for Marksmanship'], [
    ['Black Arrow (keystone)', 'Kill Shot becomes Black Arrow: Shadow hit plus an eight second DoT. Usable above 80% or below 20% health, or on a Deathblow proc.'],
    ['Bleak Arrows', 'Auto Shot does Shadow damage (ignores armour) and a lot more of it.'],
    ['Soul Drinker', 'Aimed Shot has 10% more Deathblow chance; Rapid Fire always grants Deathblow.'],
    ['Bleak Powder', 'Black Arrow bursts in an eight yard cone behind the target, eight-target cap. Your AoE engine.'],
    ['Umbral Reach', 'Black Arrow DoT doubled; Bleak Powder hitting two or more enemies grants Trick Shots.'],
    ['Corpsecaller', 'The Black Arrow DoT sometimes summons a Dark Minion for 20 seconds.'],
    ['Pact of the Hollow', 'Aimed Shot makes that minion fire Blighted Arrow at up to eight targets.'],
    ['Through the Eyes', 'Black Arrow damage up 10%.'],
    ['The Bell Tolls / Banshee\'s Mark (choice)', '3% crit and 10% minion damage, or 10% crit damage on Black Arrow and Bleak Powder. The string takes The Bell Tolls.'],
    ['Dark Chains', 'Disengage roots then slows the nearest enemy by 40%.'],
    ['Smoke Screen', 'Exhilaration grants three seconds of Survival of the Fittest; Survival of the Fittest fires Exhilaration at 50% health.'],
    ['Wailing Dead', 'Trueshot summons a Dark Hound; for fifteen seconds afterwards the Trueshot button is Wailing Arrow.'],
    ['Withering Fire (capstone)', 'Trueshot grants Withering Fire for its duration plus one Deathblow; Black Arrow fires two extra arrows at nearby targets.'],
    ['Blighted Quiver', 'Two more arrows in that barrage; Trick Shots bonus up 10%, Aspect of the Hydra up 12%.'],
  ])
  + note('<b>Honest note on Sentinel.</b> Icy Veins, Maxroll and the top-50 key sample (47 Sentinel, 3 Dark Ranger) all rate Sentinel higher in every kind of content in 12.1.5. Dark Ranger is playable and it is what this character runs, because Black Arrow is a better teaching tool and the eagle build is already set. If you ever want the last few percent for a hard key, one click in the talent panel swaps hero trees and the only key that changes is Q, which becomes Kill Shot. Headshot and Double Tap were removed from the spec tree in 12.1, so old videos that mention them are out of date.', 'warn')
))

S.append(section('sources', 'Sources', '', sources([
    ('Method: Marksmanship playstyle and rotation (13 Oct 2026)', 'https://method.gg/guides/marksmanship-hunter/playstyle-and-rotation', 'the opener and both priority lists'),
    ('Maxroll: Marksmanship raid guide', 'https://maxroll.gg/wow/class-guides/marksmanship-hunter-raid-guide', 'Sentinel skeleton, target counts'),
    ('Icy Veins: Marksmanship easy mode', 'https://www.icy-veins.com/wow/marksmanship-hunter-pve-dps-easy-mode', 'snippets only, the site blocks automated reads'),
    ('Azortharion: hunter changes in 12.1', 'https://hackmd.io/@Azortharion/HunterPatch121-1', 'Hunter\'s Mark on five, Headshot and Double Tap removed'),
    ('Warcraft Wiki: Black Arrow', 'https://warcraft.wiki.gg/wiki/Black_Arrow', 'and the other node pages, each with dated patch notes'),
    ('Murlok.io: Marksmanship M+', 'https://murlok.io/hunter/marksmanship/m+', 'hero tree split among the top 50'),
  ])))

PAGE = dict(
  slug='rotation/', title='Rotation · Alaranarises', crest='inv_ability_darkrangerhunter_blackarrow',
  kicker='Dark Ranger Marksmanship · Patch 12.1.5 · keys in brackets are the setup page\'s bars',
  h1='Rotation', lede='Opener, single target, AoE, cooldowns and every Dark Ranger node, in the order you press them. Each line says why, so when a patch moves one, you can tell which lines moved with it.',
  tags=['Black Arrow when lit', 'Explosive & Volley on cooldown', 'Never cap Aimed Shot', 'Steady Shot is the filler'],
  jump=[('idea', 'The idea'), ('opener', 'Opener'), ('st', 'Single target'), ('aoe', 'AoE'), ('cds', 'Cooldowns'), ('hero', 'Hero tree')],
  sections=S,
)
