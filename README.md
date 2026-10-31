# willhsu.dev

Source for [willhsu.dev](https://willhsu.dev): recent projects, shown as an item shop.

Static site, no build step. Edit `index.html`, push to `main`, GitHub Pages deploys it.

To add a project, copy an `<article class="card ...">` block in `index.html` and set its rarity class (`legendary`, `epic`, `rare`, `uncommon`) and `data-cats`.

The moving backdrop is `assets/azeroth.js`: three procedural zones (Teldrassil, Darkshore, the Deadmines) drawn with three.js from a CDN on a fixed canvas behind the page. Every page loads it lazily and only on machines with WebGL2 and a few cores; the footer's `zones/…` button steps to the next zone, and `?scene=darkshore` (or `?scene=2`) opens a page on a given one.
