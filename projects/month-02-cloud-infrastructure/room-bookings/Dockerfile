FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"

ENV UV_NO_DEV=1

COPY ./pyproject.toml .

RUN --mount=type=cache,target=/root/.cache uv sync

FROM python:3.14-slim

RUN groupadd --system --gid 999 appuser \
    && useradd --system --gid 999 --uid 999 appuser

WORKDIR /app

COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --chown=appuser:appuser ./app.py /bookings.py ./fetcher.py ./
COPY --chown=appuser:appuser ./templates ./templates
RUN mkdir -p /app/data && chown appuser:appuser /app/data

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000

CMD ["granian", "--host", "0.0.0.0", "--port", "5000", "--interface", "wsgi", "app:app"]

