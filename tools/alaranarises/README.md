# Alaranarises guide hub generator

`python3 build.py` writes `alaranarises/<slug>/index.html` for every `content_<slug>.py`
(leveling, rotation, gear, dungeons, weekly, ui). The shared CSS is read from
`alaranarises/index.html` at build time, so the setup page stays the source of the look.
`python3 patch_index.py` re-applies the hub nav, guide cards and to-do list to the setup page
(safe to re-run). Run both from this folder. No dependencies beyond Python 3.
