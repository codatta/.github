from __future__ import annotations

from datetime import datetime, timezone

from orderbook_app.models import OrderBookSnapshot, OrderBookUpdate, parse_levels


def parse_snapshot(payload: dict, symbol: str) -> OrderBookSnapshot:
    data = payload.get("data", [{}])[0]
    ts_ms = int(data.get("ts", 0))
    ts = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc) if ts_ms else datetime.now(timezone.utc)
    return OrderBookSnapshot(
        venue="okx",
        symbol=symbol,
        ts=ts,
        bids=parse_levels(data.get("bids", [])),
        asks=parse_levels(data.get("asks", [])),
    )


def parse_update(payload: dict, symbol: str) -> OrderBookUpdate:
    data = payload.get("data", [{}])[0]
    ts_ms = int(data.get("ts", 0))
    ts = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc) if ts_ms else datetime.now(timezone.utc)
    return OrderBookUpdate(
        venue="okx",
        symbol=symbol,
        ts=ts,
        bids=parse_levels(data.get("bids", [])),
        asks=parse_levels(data.get("asks", [])),
    )
