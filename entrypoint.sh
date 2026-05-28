#!/usr/bin/env sh
set -eu

mkdir -p /app/data /app/media

if [ ! -f "/app/data/db.sqlite3" ] && [ -f "/app/db.sqlite3" ]; then
  echo "Seeding SQLite database into persistent volume."
  cp /app/db.sqlite3 /app/data/db.sqlite3
fi

if [ -d "/app/media_seed" ] && [ -n "$(ls -A /app/media_seed 2>/dev/null)" ] && [ -z "$(ls -A /app/media 2>/dev/null)" ]; then
  echo "Seeding media files into persistent volume."
  cp -a /app/media_seed/. /app/media/
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn demo.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 120

