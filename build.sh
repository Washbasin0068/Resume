#!/usr/bin/env bash
# Build toàn bộ CV (HTML -> PDF). Cần: python3 + Chromium (hoặc Chrome).
set -euo pipefail
cd "$(dirname "$0")"
exec python3 build.py "$@"
