FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /srv

COPY dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl \
 && rm -f /tmp/*.whl \
 && useradd --create-home appuser

USER appuser
EXPOSE 8000

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT} app.web:app"]
