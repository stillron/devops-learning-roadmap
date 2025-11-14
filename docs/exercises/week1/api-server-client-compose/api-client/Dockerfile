FROM python:3.14-slim AS builder

WORKDIR /app

RUN python -m venv /app/.venv

COPY requirements.txt .

# Use cache mount to speed up rebuilds while keeping image size small
RUN --mount=type=cache,target=/root/.cache /app/.venv/bin/pip install -r requirements.txt

FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY ./main.py .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-I", "main.py"]