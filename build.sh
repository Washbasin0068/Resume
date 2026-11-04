#!/usr/bin/env bash
# Build toàn bộ CV (HTML -> PDF). Cần: Python 3 + Chromium/Chrome (uv tuỳ chọn).
set -euo pipefail
cd "$(dirname "$0")"

if command -v uv >/dev/null 2>&1; then
  exec uv run build.py "$@"
fi
exec python3 build.py "$@"
