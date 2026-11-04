#!/bin/sh
# Bind mount ./data mang quyền của user host, không phải user 'app' trong image.
# Chạy bằng root để nhận lại quyền, rồi hạ xuống UID/GID chỉ định (mặc định giữ 'app').
set -e
DATA="${DATA_DIR:-/data}"
if [ "$(id -u)" = "0" ]; then
  mkdir -p "$DATA"
  TARGET="app"
  if [ -n "$PUID" ] || [ -n "$PGID" ]; then
    TARGET="$(id -u app):$(id -g app)"
    [ -n "$PUID" ] && TARGET="$PUID:${PGID:-$(id -g app)}"
  fi
  chown -R "$TARGET" "$DATA" 2>/dev/null || true
  exec gosu "$TARGET" "$@"
fi
exec "$@"
