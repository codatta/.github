from __future__ import annotations

from datetime import datetime
from typing import Iterable

from pydantic import BaseModel, Field


class OrderBookLevel(BaseModel):
    price: float
    size: float


class OrderBookSnapshot(BaseModel):
    venue: str
    symbol: str
    ts: datetime
    bids: list[OrderBookLevel] = Field(default_factory=list)
    asks: list[OrderBookLevel] = Field(default_factory=list)


class OrderBookUpdate(BaseModel):
    venue: str
    symbol: str
    ts: datetime
    bids: list[OrderBookLevel] = Field(default_factory=list)
    asks: list[OrderBookLevel] = Field(default_factory=list)


def parse_levels(levels: Iterable[Iterable[str | float]]) -> list[OrderBookLevel]:
    return [OrderBookLevel(price=float(row[0]), size=float(row[1])) for row in levels]
