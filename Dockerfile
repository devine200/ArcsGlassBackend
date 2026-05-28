FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps for Pillow wheels fallbacks (safe on slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo \
    zlib1g \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project (includes db.sqlite3)
COPY . .

EXPOSE 8000

# Ensure static root exists (collectstatic can write here)
RUN mkdir -p public/static

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn demo.wsgi:application --bind 0.0.0.0:8000"]

