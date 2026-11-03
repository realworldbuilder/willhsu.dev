from h import *

S = []

S.append(section('on', 'What is switched on, and where',
  'Everything below was set on Alaranarises on 3 Nov 2026 through Escape, Options. Nothing here is an addon, a macro or a script. If a setting looks off after a patch, this is the list to walk.',
  table(['Setting', 'Path', 'Why'], [
    ['<b>Combine Bags</b>', 'Gameplay › Controls', 'Five bags become one window. Clean Up Bags (the broom icon at the top of the backpack) sorts it.'],
    ['<b>Auto Loot</b>', 'Gameplay › Controls', 'Right-click a corpse and everything comes. Loot Key is Shift to hold for the window.'],
    ['<b>Assisted Highlight</b>', 'Gameplay › Gameplay Enhancements › Combat Assistant', 'Glows the next button in the rotation. No damage penalty. The Single-Button Assistant spell stays off the bars: it has one.'],
    ['<b>Enable Cooldown Manager</b>', 'Gameplay › Gameplay Enhancements › Cooldown Manager', 'Blizzard\'s WeakAuras. Essential Cooldowns above the bars, Utility Cooldowns under it, Tracked Buffs and Tracked Bars to the right. Advanced Cooldown Settings adds or hides any spell; Edit Mode moves the frames.'],
    ['<b>Enable Damage Meter</b> and <b>Auto Reset Damage Meter</b>', 'Gameplay › Gameplay Enhancements › Damage Meter (scroll to the bottom)', 'The built-in meter. It appears top left the moment it is on. Auto Reset clears it when you enter a new instance. There is no keybind; Edit Mode\'s Visibility setting hides it.'],
    ['<b>Show Numbers for Cooldowns</b>', 'Gameplay › Action Bars', 'Seconds left written on every button. Already on.'],
    ['<b>Always Show Nameplates</b>', 'Gameplay › Nameplates', 'Enemy plates were already on (V toggles). Always Show keeps them up out of combat so you can see a pack before you pull it.'],
    ['<b>Personal Resource Display</b>', 'Gameplay › Combat', 'Your health and Focus under your own character. Focus is the bar you watch for Aimed Shot.'],
    ['<b>Target of Target</b>', 'Gameplay › Combat', 'A small frame showing who your target is hitting. In a dungeon that tells you the second a mob turns to you.'],
    ['<b>Show Silhouette when Obscured</b>', 'Gameplay › Combat', 'You stay visible behind pillars and doorframes.'],
    ['<b>Loss of Control Alerts</b>', 'Gameplay › Combat (on by default)', 'Big text when you are stunned or silenced, with the time left.'],
    ['Boss Warnings, Boss Abilities, Spell Support Iconography', 'Gameplay › Gameplay Enhancements › Boss Warnings (on by default)', 'Blizzard\'s built-in boss mod: warnings, countdowns and the icons on dangerous casts. Leave all three on.'],
    ['Lock Action Bars', 'Gameplay › Action Bars', 'Ticked. Untick only while dragging spells, then tick it again.'],
    ['Action Bars 2, 3, 5 shown; 4 hidden', 'Gameplay › Action Bars', 'Bar 2 is the Shift row, bar 3 the Ctrl row, bar 5 the click-only column on the right. Bar 4 holds the parked pet buttons; bar 5 sits inside bar 4 in the default layout, so hiding the wrong one hides both.'],
  ])
))

S.append(section('cdm', 'The Cooldown Manager',
  'Once it is on, Edit Mode owns it: Escape › Edit Mode, tick Cooldown Manager under Combat, drag the four frames where you want them. Advanced Cooldown Settings (the button in Options, or the one that appears when you click a frame in Edit Mode) decides what is in them.',
  habits([
    ('Essential Cooldowns', 'The big row directly above the main bar. Keep it in rotation order so it reads like the bar: Black Arrow, Explosive Shot, Volley, Aimed Shot, Rapid Fire, Trueshot, Wailing Arrow. Charges show as a number in the corner.'),
    ('Utility Cooldowns', 'The smaller row under it: Counter Shot, Exhilaration, Survival of the Fittest, Turtle, Disengage, Feign Death, Misdirection, Tranquilizing Shot. Set it to Hide When Inactive so it only appears when something is ticking.'),
    ('Tracked Buffs', 'Procs that only show while active: Precise Shots, Trick Shots, Deathblow, Lock and Load, trinket procs. Watching Precise Shots fall off is how you learn not to cap it.'),
    ('Tracked Bars', 'Timers where the exact seconds matter: Trueshot, Withering Fire, Hunter\'s Mark on the target.'),
    ('Moving a spell', 'In Advanced Cooldown Settings, drag an icon between Essential, Utility and Not Displayed; dragging within a row reorders. Right-click an icon for Add Alert: a sound or a flash when Trueshot comes back, or a Pandemic box on Black Arrow. Up to three alerts per spell. Trinkets and potions are in the Items tab since 12.1.'),
    ('Per-frame settings in Edit Mode', 'Orientation, Icon Size, Icon Padding, rows and columns, Opacity, Visibility (Always, In Combat, Hidden), Hide When Inactive, Show Timer. In Combat on every frame keeps town clean.'),
    ('Layouts', 'The settings panel has Import and Copy To Clipboard, so a finished layout can be pasted to another hunter. There is a Starter Layout entry if it ever gets tangled.'),
    ('Why not WeakAuras', 'Midnight\'s addon rules stopped addons reading combat in real time. The Cooldown Manager, Boss Warnings and the Damage Meter are Blizzard\'s replacements and a patch cannot break them.'),
  ])
))

S.append(section('editmode', 'Edit Mode',
  'Escape › Edit Mode. Everything on screen becomes a box you can drag, scale and hide. Save when you are done; the layout is per character unless you pick an account-wide one.',
  habits([
    ('Frames you can tick on and off', 'Target and Focus, Party, Raid, Pet, Boss, Arena. Combat: Buffs and Debuffs, Cast Bar, Stance, Extra Abilities, Pet Bar, Possess Bar, Encounter Bar, Cooldown Manager, Personal Resource Display, Boss Warnings, Damage Meter, External Defensives, Loss of Control. Misc: Talking Head, Durability, Vehicle Seats, HUD Tooltip, Duration Bars, Archaeology Bar, Raid Warnings.'),
    ('Action bars', 'Click any bar in Edit Mode: # of Icons (6 to 12), # of Rows, Icon Size (50% to 200%, this is the scale), Icon Padding, Bar Visible (Always, In Combat, Out of Combat, Hidden), Always Show Buttons (untick to hide empty slots). Hide Bar Art and Hide Bar Scrolling tidy the main one. There is no mouseover-only setting in the default UI.'),
    ('Showing bars 2 to 8', 'Not in Edit Mode. Options › Gameplay › Action Bars has the eight checkboxes; this character has 2, 3 and 5 on.'),
    ('Why bar 5 lives inside bar 4', 'Blizzard\'s preset gives bars 4 and 5 the same right-edge anchor and then stacks bar 5 off bar 4\'s width at runtime. Dragging bar 5 once detaches it; Reset To Default Position puts it back.'),
    ('Presets', 'The Layout dropdown at the top: Modern (what this character uses) or Classic. Presets cannot be saved over, so New Layout, name it, then Save. Import and Share move a layout between characters.'),
    ('Show Grid, Snap to Elements', 'Grid for lining things up; snap so frames stick to each other\'s edges. Both are top of the Edit Mode window.'),
    ('Damage Meter', 'Listed under Combat. Its details are below.'),
  ])
))

S.append(section('dmg', 'The built-in damage meter',
  'New in Midnight. Replaces Details for anyone who only wants to see the number.',
  habits([
    ('Switching it on', 'Options › Gameplay › Gameplay Enhancements, scroll to the bottom: Enable Damage Meter, and Auto Reset Damage Meter so each instance starts clean. Until that box is ticked, the Damage Meter line in Edit Mode is greyed out. It is on for this character.'),
    ('What it shows', 'Damage Done, DPS, Damage Taken, Avoidable Damage Taken; Healing, HPS, Absorbs; Interrupts, Dispels, Deaths. The O and C buttons switch between Overall and the Current Segment; the last 30 fights are kept. Click a bar for the per-spell breakdown.'),
    ('Placing and styling it', 'Edit Mode › Combat › Damage Meter: Style (Default, Thin, Bordered, Full Background), Numbers (Compact, Complete, Minimal), width, height, bar height, opacity, class colours, spec icons. Visibility can be In Combat or In Group so it is not on screen in town. The gear icon on the meter has Lock Window, Reset Data and Create New Window (up to three).'),
    ('How to read your own bar', 'In a key, the question is not first place. It is: did Black Arrow and Explosive Shot sit at the top of your breakdown, and was Steady Shot small. If Steady Shot is large, you were out of Focus or standing in the wrong place for Aimed Shot.'),
  ])
))

S.append(section('journal', 'Mounts, bags, quests',
  'Small things that stop being annoying once they are set.',
  habits([
    ('Favourite mounts', 'Shift-P › Mounts. Right-click a mount in the list › Set Favorite. Favourites sort to the top with a star. Ctrl-1 is Summon Random Favorite Mount and now picks from five: Highland Drake, Renewed Proto-Drake, Cliffside Wylderdrake, Lightwing Dragonhawk, Cerulean Prideclaw.'),
    ('Flight Style', 'The button at the top of the mount journal switches between Skyriding and Steady Flight. Both work in every Midnight zone since March 2026; no Pathfinder needed.'),
    ('Clean Up Bags', 'The broom icon at the top of the combined bag. Right-click a bag\'s top-left icon to assign it an item type if you ever want equipment or consumables kept apart.'),
    ('Quest tracker', 'The Campaign block at the top of the objectives list is the 80 to 90 road. Shift-click a quest in the log (L) to track or untrack it; keep the tracker under about eight lines so the one you are doing is readable.'),
    ('Talent loadouts', 'N, then the dropdown at the bottom left of the panel. Import takes a string and always makes a new loadout (so repeated imports make duplicates); it gets a name and a slot in that dropdown, and swapping AoE and single-target is two clicks out of combat. Loadouts are per specialisation. Starter Build at the top of the list is Blizzard\'s default if you ever want to start over.'),
    ('The one chat command worth knowing', 'The game drops every newly learned spell onto your bars, which is how a boosted layout gets scrambled. There is no checkbox for it in 12.x; the only switch is typing <span class="code">/console AutoPushSpellToActionBar 0</span> in chat once per character. It is a settings command, not a script, and it changes nothing but that. Skip it if you would rather tidy the bar by hand after each level.'),
  ])
))

S.append(section('keys', 'Keybinds the game set for you',
  'Defaults that matter and were left alone.',
  table(['Key', 'Does'], [
    ['V', 'Toggle enemy nameplates (they are set to always show, so this is a quick way to hide them for a screenshot)'],
    ['Shift-P', 'Collections: mounts, pets, toys, appearances'],
    ['N', 'Talents and specialisation'],
    ['P', 'Spellbook'],
    ['B', 'Bags'],
    ['I', 'Group Finder'],
    ['L', 'Quest log'],
    ['M', 'Map'],
    ['C', 'Character pane, with the item level in the middle'],
    ['Escape', 'Game menu: Options, Edit Mode, Macros (empty on purpose)'],
    ['Space while mounted', 'Skyriding: take off and climb'],
  ])
))

PAGE = dict(
  slug='ui/', title='UI without addons · Alaranarises', crest='inv_misc_gear_01',
  kicker='Blizzard options only · Patch 12.1.5 · no addons, no macros, no scripts',
  h1='UI without addons', lede='Every option this character has turned on, with its exact menu path, so it can be rebuilt on any hunter in five minutes. The Cooldown Manager, the built-in damage meter and Edit Mode cover what WeakAuras and Details used to.',
  tags=['No addons', 'Cooldown Manager on', 'Nameplates always', 'Combined bags'],
  jump=[('on', 'Switched on'), ('cdm', 'Cooldown Manager'), ('editmode', 'Edit Mode'), ('dmg', 'Damage meter'), ('journal', 'Mounts & bags'), ('keys', 'Default keys')],
  sections=S,
)
