FROM python:3.14-slim AS builder

WORKDIR /app

RUN python -m venv /app/.venv

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache /app/.venv/bin/pip install -r requirements.txt

FROM python:3.14-slim

RUN groupadd -r appuser -g 1000 && useradd -r -g appuser -u 1000 appuser

WORKDIR /app

COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --chown=appuser:appuser templates/impress.j2 /app/templates/impress.j2
COPY --chown=appuser:appuser main.py events.py .

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

CMD ["python3", "main.py"]