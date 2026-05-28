FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DJANGO_SQLITE_PATH=/app/data/db.sqlite3 \
    DJANGO_STATIC_ROOT=/app/staticfiles

WORKDIR /app

# System deps for Pillow wheels fallbacks (safe on slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libjpeg62-turbo \
    zlib1g \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project (includes db.sqlite3)
COPY . .

EXPOSE 8000

# Ensure scripts are executable
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

