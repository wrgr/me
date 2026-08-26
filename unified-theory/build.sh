#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: > index.html
for f in parts/*.html; do cat "$f" >> index.html; printf '\n' >> index.html; done
