#!/bin/bash
# Render every card in posts/card.html to assets/posts/<id>.png at 1600x900.
# Usage: tools/render-cards.sh [id ...]
# Needs Playwright's Chromium once: npx -y playwright install chromium
# (the installed Google Chrome hangs in headless mode on the mini)
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
out="$root/assets/posts"
mkdir -p "$out"

if [ $# -gt 0 ]; then
  ids="$*"
else
  ids=$(grep -o '<section class="card[^"]*" id="[^"]*"' "$root/posts/card.html" | sed 's/.*id="//; s/"//')
fi

for id in $ids; do
  npx -y playwright screenshot -b chromium --viewport-size "1600,900" \
    --wait-for-timeout 1500 \
    "file://$root/posts/card.html?c=$id" "$out/$id.png" >/dev/null
  echo "$out/$id.png"
done
