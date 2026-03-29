#!/usr/bin/env bash
set -euo pipefail

cd /root/.openclaw/workspace

if [ ! -d ".git" ]; then
  git init
fi

if [ ! -f ".gitignore" ]; then
cat > .gitignore << 'GI'
.env
.env.*
*.key
*.pem
*.p12
secrets/
token*
*credentials*
openclaw.json
logs/
*.log
tmp/
.cache/
node_modules/
GI
fi

git add .
git commit -m "backup: daily state $(date -u +'%Y-%m-%d %H:%M UTC')" || true

if git remote get-url origin >/dev/null 2>&1; then
  git push origin HEAD || true
fi
