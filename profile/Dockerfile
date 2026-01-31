FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml README.md ./
COPY src ./src

RUN uv pip install --system -e ".[dev]"

ENV DATABASE_URL=postgresql://postgres:postgres@db:5432/orderbook

CMD ["orderbook-app"]
