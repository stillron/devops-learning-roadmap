FROM python:3.14-slim AS builder

WORKDIR /app

RUN python -m venv /app/.venv

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache /app/.venv/bin/pip install -r requirements.txt

FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY ./db.py .
COPY ./app.py .

ENV PATH="/app/.venv/bin:$PATH"

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
 CMD curl -f http://localhost:5000/health || exit 1

EXPOSE 5000

CMD ["granian", "--host", "0.0.0.0", "--port", "5000", "--interface", "wsgi", "app:app"]