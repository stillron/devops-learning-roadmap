FROM python:3.14-slim AS builder

WORKDIR /app

RUN python -m venv /app/.venv

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache /app/.venv/bin/pip install -r requirements.txt

FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY ./db.py .
COPY ./app.py .

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000

CMD ["granian", "--host", "0.0.0.0", "--port", "5000", "--interface", "wsgi", "app:app"]