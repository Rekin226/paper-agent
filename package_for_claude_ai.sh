#!/usr/bin/env bash
# Build a claude.ai-compatible upload package from this Claude Code skill.
#
# claude.ai's skill validator differs from Claude Code's in three ways:
#   1. `description` must be <= 1024 characters
#   2. `name` and `description` must be quoted scalars
#   3. `allowed-tools` is not an accepted field (no Anthropic skill uses it)
# It also has no use for the local .venv (Mac-specific binaries).
#
# The SKILL.md in this directory stays the Claude Code source of truth; this
# script emits the transformed copy. Do not hand-edit the package.
#
# Usage:  ./package_for_claude_ai.sh [output_dir]     (default: ~/Downloads)
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HOME/Downloads}"
BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT

PY="$SRC/.venv/bin/python"; [ -x "$PY" ] || PY=python3

rsync -a --exclude '.venv' --exclude '.gstack' --exclude '__pycache__' \
      --exclude '*.pyc' --exclude '.DS_Store' --exclude 'package_for_claude_ai.sh' \
      --exclude '.git' --exclude '.claude' --exclude '.claude-plugin' --exclude '.local' \
      --exclude '.mcp.json' --exclude '.gitignore' \
      "$SRC/" "$BUILD/paper-agent/"

"$PY" - "$BUILD/paper-agent/SKILL.md" <<'PYEOF'
import re, sys, yaml
p = sys.argv[1]
raw = open(p).read()
_, fm, body = raw.split('---', 2)
d = yaml.safe_load(fm)

d.pop('allowed-tools', None)          # rule 3

desc = d['description']
if len(desc) > 1024:                  # rule 1
    sys.exit(f"ERROR: description is {len(desc)} chars, limit is 1024. Shorten it in SKILL.md.")

def q(v):                             # rule 2
    return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'

out = [f'name: {q(d["name"])}', f'description: {q(desc)}']
for k, v in d.items():
    if k not in ('name', 'description'):
        out.append(f'{k}: {v}')

open(p, 'w').write('---\n' + '\n'.join(out) + '\n---' + body)
print(f"  frontmatter: description {len(desc)} chars, allowed-tools dropped, values quoted")
PYEOF

"$PY" -c "
import yaml,sys
d=yaml.safe_load(open('$BUILD/paper-agent/SKILL.md').read().split('---')[1])
assert 'allowed-tools' not in d, 'allowed-tools survived'
assert len(d['description'])<=1024, 'description too long'
print('  validated: parses, no allowed-tools, description within limit')"

mkdir -p "$OUT"
rm -f "$OUT/paper-agent.zip"
( cd "$BUILD" && zip -qr "$OUT/paper-agent.zip" paper-agent )
echo "  package: $OUT/paper-agent.zip ($(du -h "$OUT/paper-agent.zip" | cut -f1))"
