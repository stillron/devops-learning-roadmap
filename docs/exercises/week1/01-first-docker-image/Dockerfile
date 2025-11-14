FROM python:3.13-slim

WORKDIR /app

RUN useradd --create-home appuser

COPY ./main.py .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python3","main.py"]