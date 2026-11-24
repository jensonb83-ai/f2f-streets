#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
REMOTE='https://github.com/jensonb83-ai/f2f-streets.git'
command -v git >/dev/null || { echo 'Git muss zuerst installiert werden.' >&2; exit 1; }
if [ ! -d .git ]; then git init -b main; fi
git config user.name 'jensonb83-ai'
git config user.email '347982756+jensonb83-ai@users.noreply.github.com'
git branch -M main
if git remote get-url origin >/dev/null 2>&1; then
  if [ "$(git remote get-url origin)" != "$REMOTE" ]; then
    echo 'Abweichende Git-Remote vorhanden. Abbruch ohne Ueberschreibung.' >&2
    exit 1
  fi
else
  git remote add origin "$REMOTE"
fi
git add .
if ! git diff --cached --quiet; then git commit -m 'F2F Streets 2.14: Online-Spiel und Downloadshop'; fi
git push -u origin main
printf '
GitHub: https://github.com/jensonb83-ai/f2f-streets
'
