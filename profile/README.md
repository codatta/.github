# Orderbook Ingestion (Binance + OKX)

This repository provides a Python (uv-managed) foundation to ingest **real-time** and **historical** orderbook data for **ETH/USDT** from **Binance** and **OKX**, store snapshots/updates in **PostgreSQL**, and prepare for future order placement.

## Goals

- Real-time orderbook streaming (WebSocket) for ETH/USDT (spot + perp as needed).
- Historical snapshot pulls (REST) for ETH/USDT.
- Store snapshots and updates in PostgreSQL.
- Prepare for order placement (spot/perp) with API keys.
- Provide simulated data generators for fast tests.
- Docker + docker-compose for easy deployment.

## Required APIs & Credentials

You can prepare these API permissions up front:

### Binance

**Public (no key required)**
- **REST snapshot (spot)**: `GET /api/v3/depth?symbol=ETHUSDT&limit=1000`
- **REST snapshot (perp)**: `GET /fapi/v1/depth?symbol=ETHUSDT&limit=1000`
- **WebSocket stream (spot)**: `wss://stream.binance.com:9443/ws/ethusdt@depth@100ms`
- **WebSocket stream (perp)**: `wss://fstream.binance.com/ws/ethusdt@depth@100ms`

**Private (key required)**
- **Spot order placement**: `POST /api/v3/order`
- **Futures order placement**: `POST /fapi/v1/order`

Required permissions: **Spot Trading** and/or **Futures Trading**; enable **Read** for account and order status.

### OKX

**Public (no key required)**
- **REST snapshot**: `GET /api/v5/market/books?instId=ETH-USDT&sz=400`
- **WebSocket stream**: `wss://ws.okx.com:8443/ws/v5/public` with subscribe message:
  ```json
  {"op": "subscribe", "args": [{"channel": "books", "instId": "ETH-USDT"}]}
  ```

**Private (key required)**
- **Order placement (spot/perp)**: `POST /api/v5/trade/order`

Required permissions: **Trade** and **Read** for account/order status. Ensure passphrase is set.

## Quick Start (uv)

```bash
uv venv
source .venv/bin/activate
uv pip install -e .[dev]
```

## Docker

```bash
docker compose up --build
```

## Project Layout

```
src/orderbook_app/
  connectors/         # Binance + OKX parsers
  services/           # Simulated data generators
  storage/            # PostgreSQL helpers
```

## Notes

- This code currently focuses on parsing and schema setup for ETH/USDT orderbooks.
- Use the simulated data generator to validate ingestion logic without API calls.
- Extend `storage/db.py` for historical storage policies (rollups, TTL, etc.).

