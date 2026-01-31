from __future__ import annotations

from datetime import datetime, timezone

from orderbook_app.models import OrderBookSnapshot, OrderBookUpdate, parse_levels


def parse_depth_snapshot(payload: dict, symbol: str, venue: str) -> OrderBookSnapshot:
    return OrderBookSnapshot(
        venue=venue,
        symbol=symbol,
        ts=datetime.now(timezone.utc),
        bids=parse_levels(payload.get("bids", [])),
        asks=parse_levels(payload.get("asks", [])),
    )


def parse_depth_update(payload: dict, symbol: str, venue: str) -> OrderBookUpdate:
    event_time = payload.get("E")
    ts = datetime.fromtimestamp(event_time / 1000, tz=timezone.utc) if event_time else datetime.now(timezone.utc)
    return OrderBookUpdate(
        venue=venue,
        symbol=symbol,
        ts=ts,
        bids=parse_levels(payload.get("b", [])),
        asks=parse_levels(payload.get("a", [])),
    )
