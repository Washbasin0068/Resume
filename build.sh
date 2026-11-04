#!/usr/bin/env bash
# Build CV PDFs from the HTML sources (Chromium headless print).
set -euo pipefail
cd "$(dirname "$0")"

CHROME="${CHROME:-$(command -v chromium chromium-browser google-chrome 2>/dev/null | head -1)}"
CHROME="${CHROME:-$(ls ~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | tail -1)}"

build() { # <html> <out.pdf>
  "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$2" "file://$PWD/$1" >/dev/null 2>&1
  echo "built: $2"
}

# --- CV chính (full-stack) ---
build html/CV_FullStackDev.html     CV_VuHuuDo_FullStack.pdf
build html/CV_FullStackDev_ATS.html CV_VuHuuDo_FullStack_ATS.pdf
build html/CV_VuHuuDo_VI.html       CV_VuHuuDo_VI.pdf

# --- CV theo role (roles/<id>/, EN + VI) ---
CHROME="$CHROME" uv run build_cvs.py
