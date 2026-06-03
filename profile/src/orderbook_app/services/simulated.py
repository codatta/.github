from __future__ import annotations

from datetime import datetime, timezone
from random import random

from orderbook_app.models import OrderBookUpdate


def generate_simulated_update(venue: str, symbol: str) -> OrderBookUpdate:
    base_price = 3000.0
    bids = [[base_price - i, 1 + random()] for i in range(3)]
    asks = [[base_price + i, 1 + random()] for i in range(3)]
    return OrderBookUpdate(
        venue=venue,
        symbol=symbol,
        ts=datetime.now(timezone.utc),
        bids=[{"price": price, "size": size} for price, size in bids],
        asks=[{"price": price, "size": size} for price, size in asks],
    )
