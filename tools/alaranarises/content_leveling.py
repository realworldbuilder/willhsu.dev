from h import *

S = []

S.append(section('door', 'Finding the door',
  'The boost drops you in Dornogal with a quest log full of The War Within. None of it is Midnight. Here is what to ignore and where the real start is.',
  habits([
    ('Ignore "Something on the Horizon"', 'Brann Bronzebeard\'s quest is The War Within\'s level-up campaign skip. Same for Surface Bound, A Time to Come Together, The Fleet Arrives and the "Meet Arator" lore chain by the bank. They do nothing for Midnight.'),
    ('The quest is called "Midnight"', 'It is auto-accepted when you own the expansion: "Locate the nearest Image of Lady Liadrin". If it is not in your log, open the Adventure Guide (Shift-J) › Suggested Content.'),
    ('Image of Lady Liadrin', 'Dornogal, Keepers Terrace at 44.2, 34.8. Also Orgrimmar, Valley of Strength at 53.4, 77.3 by the Broken Tusk. Talk to her and you are teleported to the Isle of Quel\'Danas.'),
    ('The intro scenario', 'Defend the Sunwell, then retake Silvermoon: seventeen quests, 15 to 20 minutes on Quel\'Danas plus the Silvermoon half, about an hour all told. Mounting is off during the Sunwell part. It ends in Silvermoon with "Paved in Ash". This is the first Midnight character on the account, so there is no skip.'),
    ('Set your hearth in Silvermoon', 'Wayfarer\'s Rest, the inn. Ctrl-6 then brings you back to the hub for the whole expansion.'),
    ('Fly', 'Skyriding and steady flight work in every Midnight zone from the moment the scenario ends; the Pathfinder gate was removed in March 2026. If a boosted character cannot mount after the intro, summon the Highland Drake once (Ctrl-2) and everything works after.'),
  ])
))

S.append(section('road', 'The road: 80 to 90',
  'Four zones, seventeen campaign chapters, about 3.7 million XP. The campaign alone gets you to 90 or within a world quest of it. Ten hours at a normal pace, five to seven if you skip every side quest.',
  table(['Levels', 'Zone', 'What happens'], [
    ['80 to 83', 'Eversong Woods', 'Silvermoon Court renown starts here. Dungeon Windrunner Spire opens at 81; run it once while its campaign quest is up.'],
    ['83 to 88', 'Zul\'Aman, Harandar and Arator\'s Journey, in any order', 'Pick one and finish it before the next. Murder Row at 83, Voidscar Arena at 85, Den of Nalorakk at 86, each once with the quest.'],
    ['88 to 90', 'Voidstorm', 'The initial questline needs 88. Nexus-Point Xenas at 88. Most people ding 90 in Howling Ridge near the end of the chapters.'],
  ])
  + habits([
    ('Side quests', 'Only the ones that overlap a campaign objective. The campaign plus the first run of each dungeon and the first Delve in each zone is enough XP.'),
    ('Delves while leveling', 'Patch 12.0.7 raised first-time Delve XP a lot. The fastest known route is Delve-heavy. One Delve per zone the first time you pass it is free XP and starts Valeera\'s levels.'),
    ('Prey hunts and renown weeklies', 'Also buffed in 12.0.7. Take them when they are next to you, do not travel for them.'),
    ('Exploration XP is gone', '12.1 cut it by 60%. Flying around uncovering the map no longer levels you.'),
  ])
))

S.append(section('xp', 'XP that is free this week',
  'Stackable. Numbers are the guide sites\' figures.',
  table(['Buff', 'How much', 'How'], [
    ['Darkmoon Faire "WHEE!"', '+10% for one hour', 'The Faire is open 1 to 7 November 2026. Ride the carousel or roller coaster, then quest. Portal in Orgrimmar.'],
    ['War Mode', '+15%', 'Toggle in Orgrimmar or Silvermoon (talent panel, bottom). Other faction can attack you; on a quiet server it is free money.'],
    ['Warband Mentors', '+5% per level-90 character, up to +25%', 'Only if the account already has 90s. None yet on this account means zero today and +5% after this character.'],
    ['Battle Standard of Coordination', '+15% kill XP for 15 minutes', '300 gold from Larissia in Silvermoon or Goram in Orgrimmar. Kill XP only, so pop it for a dungeon or a Delve.'],
    ['Rested XP', 'Double kill XP while the bar is blue', 'Log out in an inn or city. A night in Silvermoon is a free hour of double kills.'],
    ['Timewalking', 'Up to +30% for three hours', 'Only during a Timewalking week: four dungeons stack Mastery of Timeways. Check the in-game calendar; nothing confirmed for this week.'],
  ])
  + note('<b>Things that do not work:</b> heirlooms give no XP since Shadowlands; Draught of Ten Lands stops at 49; the pre-patch Winds of Mysterious Fortune ended in February; Chromie Time ends at 81. The 22nd Anniversary event usually starts around 23 November and brings its own +10%.', 'warn')
))

S.append(section('hunter', 'Leveling as a Marksman',
  'The spec was built for standing still, and leveling is all movement. These are the adjustments.',
  habits([
    ('Pull two or three', 'Hunter\'s Mark the one that will live longest, Aimed Shot the second, Explosive Shot on two of them, Volley, then Black Arrow whenever it lights. Three mobs die about as fast as one.'),
    ('Open from maximum range', 'Aimed Shot is a 2.5 second cast. Start it before the mob notices; it lands as the fight starts and you already have Precise Shots.'),
    ('Move on instants', 'Arcane Shot, Black Arrow, Explosive Shot, Multi-Shot and Volley all cast while moving. Rapid Fire channels while moving. Aimed Shot and Steady Shot do not, so stand for those two.'),
    ('Binding Shot at your feet', 'Shift-R. Anything that reaches you is stunned a moment later, and Disengage (Shift-2) puts you back at range with Dark Chains slowing the nearest one.'),
    ('Exhilaration is a heal', 'T, under half health, no cost. Use it every fight that needs it; it is back in two minutes.'),
    ('The pet question', 'Row three of the spec tree is a choice: Avian Specialization (the eagle, what this character runs) or Unbreakable Bond (a real pet). A tenacity pet like Chinacat holds mobs off you and costs about 3% damage. For solo leveling that is a fair trade; for dungeons and 90 the eagle wins. Swap in the talent panel, no re-taming needed, the stable is still there.'),
    ('Dark Ranger or Sentinel for leveling', 'Nobody has measured it for questing. Dark Ranger\'s Bleak Powder cone suits the multi-mob pulls above; Sentinel is a touch stronger on a single target. Keep Dark Ranger until 90, decide then with the <a href="../rotation/#hero">rotation page</a>.'),
    ('Spend every talent point', 'N glows at each level: the two empty Dark Ranger nodes first, then the gold highlights. The Apex talents at the end of the spec tree open as you level; Marksmanship\'s is the Take Aim line.'),
    ('Dungeons while leveling', 'Group Finder (I), queue as damage, Misdirection on the tank (Shift-Q) before every pull. One run of each Midnight dungeon with its campaign quest is the whole plan; after that the quest XP beats the queue time.'),
  ])
))

S.append(section('ninety', 'The moment you hit 90',
  'The first hour at cap, in order. After this the <a href="../gear/#fresh90">gear page</a> takes over.',
  prio([
    ('"The Last Push" from Lor\'themar Theron in Silvermoon', 'Turns on world quests and the rest of the endgame.'),
    ('"Midnight: World Tour" and "Feeding the Flame"', 'One of each weekly event. World Tour pays the first Spark of Tides.'),
    ('"Midnight Delves!" and Valeera Sanguinar', 'Delver\'s Headquarters, Silvermoon 52.5, 78.3. Then "The Season Starts: Midnight".'),
    ('Two Apex Cache weeklies outside the bank', 'Veteran gear for showing up.'),
    ('Field Accolades to Maren Silverwing', '200 for an Adventurer cache, 500 for a random Veteran piece, 750 for a chosen slot.'),
    ('Professions', 'Trainers just north of the Sanctum of Light: Talmar (Leatherworking) 43.2, 55.8 and Tyn (Skinning) 43.3, 55.6, or Danwe (Engineering) 43.6, 54.1.'),
    ('Heroic dungeons at 266, the Lair at 273, Delves to tier 8', 'The ladder is on the gear page.'),
  ])
))

S.append(section('sources', 'Sources', 'Checked 3 Nov 2026. Wowhead\'s own 12.1.5 Marksmanship leveling guide exists but would not load for the research pass; the hunter section above is built from Method, the wiki and the Blizzard notes instead.',
  sources([
    ('Warcraft Wiki: Midnight (quest)', 'https://warcraft.wiki.gg/wiki/Midnight_(quest)', ''),
    ('Warcraft Wiki: Image of Lady Liadrin', 'https://warcraft.wiki.gg/wiki/Image_of_Lady_Liadrin', 'coordinates'),
    ('Warcraft Wiki: Something on the Horizon', 'https://warcraft.wiki.gg/wiki/Something_on_the_Horizon', 'why it is not Midnight'),
    ('Warcraft Wiki: Midnight intro experience', 'https://warcraft.wiki.gg/wiki/Midnight_intro_experience', 'zone level bands'),
    ('Warcraft Wiki: Character Boost', 'https://warcraft.wiki.gg/wiki/Character_Boost', 'what the boost grants'),
    ('games.gg: Midnight leveling guide to 90', 'https://games.gg/world-of-warcraft/guides/wow-midnight-leveling-guide-level-90/', 'times, dungeon levels'),
    ('Icy Veins: Harldan\'s 98 minute route', 'https://icy-veins.com/wow/news/midnight-xp-buffs-cut-harldans-80-90-leveling-route-to-98-minutes/', 'XP buffs'),
    ('Warcraft Wiki: Darkmoon Faire', 'https://warcraft.wiki.gg/wiki/Darkmoon_Faire', 'dates'),
    ('Warcraft Wiki: Steady flight', 'https://warcraft.wiki.gg/wiki/Steady_flight', 'Pathfinder removed 13 Mar 2026'),
    ('Blizzard: 12.1 patch notes', 'https://news.blizzard.com/en-us/article/24293281', 'exploration XP, Explosive Shot'),
    ('Blizzard: 12.1.5 content update notes', 'https://news.blizzard.com/en-us/article/24304162/12-1-5-content-update-notes', ''),
    ('Warcraft Wiki: The Last Push', 'https://warcraft.wiki.gg/wiki/The_Last_Push', 'and Midnight: World Tour, Midnight Delves!'),
    ('Method: Silvermoon NPC locations', 'https://www.method.gg/guides/location-of-the-auction-house-bank-notable-npcs-and-vendors-in-midnight-silvermoon-city', 'trainers'),
    ('Blizzard forums: Marksman pet question', 'https://us.forums.blizzard.com/en/wow/t/marksman-question/2286904', 'Unbreakable Bond while leveling'),
  ])
))

PAGE = dict(
  slug='leveling/', title='Leveling 80 to 90 · Alaranarises', crest='achievement_level_90',
  kicker='Midnight · Patch 12.1.5 · the boost ends at 80, the cap is 90',
  h1='Leveling 80 to 90', lede='Where the real Midnight start is (not where the boost points you), the four zones in order, the XP buffs that are free this week, how a Marksman levels without dying, and the first hour at 90.',
  tags=['Image of Lady Liadrin', 'Eversong first', '~3.7M XP', 'Darkmoon Faire until 7 Nov'],
  jump=[('door', 'The door'), ('road', 'The road'), ('xp', 'Free XP'), ('hunter', 'As a Marksman'), ('ninety', 'At 90')],
  sections=S,
)
