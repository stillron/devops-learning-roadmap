FROM postgres:18-alpine

COPY init.sql /docker-entrypoint-initdb.d/

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
  CMD pg_isready

