#!/usr/bin/env bash
# Salin mesin video dari repo sebelumnya ke folder baru dan ganti nama komposisi.
# Pemakaian: new-video.sh <repo_mesin> <topik> <KomposisiPascal> "<Judul workflow>" [branch]
#   contoh: new-video.sh video-ikatan-valensi orbital-molekul OrbitalMolekul "Orbital Molekul" ccr-xxxx
set -euo pipefail
BASE="$1"; TOPIK="$2"; KOMP="$3"; JUDUL="$4"; BR="${5:-$(git -C /home/user/$BASE rev-parse --abbrev-ref HEAD)}"
SRC=/home/user/$BASE
DST=/home/user/video-$TOPIK
[ -e "$DST" ] && { echo "Folder $DST sudah ada — berhenti."; exit 1; }
OLD=$(grep -o 'id="[A-Za-z0-9]*"' "$SRC/src/Root.tsx" | head -1 | sed 's/id="//; s/"//')
OLDSLUG=$(grep -o 'out/[a-z0-9-]*-' "$SRC/scripts/assemble.sh" | head -1 | sed 's|out/||; s|-$||')
mkdir -p "$DST"
git -C "$SRC" archive HEAD | tar -x -C "$DST"
cd "$DST"
git init -q -b "$BR"
if [ -d "$SRC/node_modules" ] && [ ! -L "$SRC/node_modules" ]; then ln -s "$SRC/node_modules" node_modules
elif [ -L "$SRC/node_modules" ]; then ln -s "$(readlink -f "$SRC/node_modules")" node_modules
else npm ci --no-audit --no-fund; fi
grep -rlE "$OLD|$OLDSLUG" scripts src .github package.json 2>/dev/null | xargs -r sed -i "s/$OLD/$KOMP/g; s/$OLDSLUG/$TOPIK/g"
sed -i "1s/.*/name: Render $JUDUL 2K 30FPS/" .github/workflows/render-video.yml
sed -i "s/\"name\": \"[^\"]*\"/\"name\": \"video-$TOPIK\"/" package.json
rm -rf public/voiceover/*.mp3 2>/dev/null || true
echo "Mesin disalin: $SRC → $DST (komposisi $OLD → $KOMP, slug $OLDSLUG → $TOPIK, branch $BR)"
echo "Berikutnya: tulis src/script.ts (generator), stub adegan, index.ts + scripts/scene-files.ts, merek (Title/Outro/Thumbnail/ChapterHeading), AUDIT, CLAUDE.md."
grep -rn "$OLD" src scripts .github package.json 2>/dev/null | head -3 || true
