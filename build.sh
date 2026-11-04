#!/usr/bin/env bash
# Build CV PDFs from the HTML sources (Chromium headless print).
set -euo pipefail
cd "$(dirname "$0")"

CHROME="${CHROME:-chromium}"

build() { # <html> <out.pdf>
  "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$2" "file://$PWD/$1" >/dev/null 2>&1
  echo "built: $2"
}

build html/CV_FullStackDev.html     CV_VuHuuDo_FullStack.pdf
build html/CV_FullStackDev_ATS.html CV_VuHuuDo_FullStack_ATS.pdf
build html/CV_VuHuuDo_VI.html       CV_VuHuuDo_VI.pdf
