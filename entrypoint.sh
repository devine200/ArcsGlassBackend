#!/usr/bin/env sh
set -eu

mkdir -p /app/data

if [ ! -f "/app/data/db.sqlite3" ] && [ -f "/app/db.sqlite3" ]; then
  echo "Seeding SQLite database into persistent volume."
  cp /app/db.sqlite3 /app/data/db.sqlite3
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn demo.wsgi:application --bind 0.0.0.0:8000

