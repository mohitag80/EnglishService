FROM python:3.13-slim-bookworm

LABEL maintainer="exam-platform@example.com"
LABEL service="english-service"
LABEL version="1.0.0"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl gcc libffi-dev libssl-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate --run-syncdb 2>/dev/null || true

EXPOSE 8084

ENV DJANGO_SETTINGS_MODULE=english_service.settings
ENV PORT=8084

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8084/api/english/health/ || exit 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8084"]
