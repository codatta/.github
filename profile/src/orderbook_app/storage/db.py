from __future__ import annotations

import json

import asyncpg


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS orderbook_updates (
    id bigserial PRIMARY KEY,
    venue text NOT NULL,
    symbol text NOT NULL,
    ts timestamptz NOT NULL,
    bids jsonb NOT NULL,
    asks jsonb NOT NULL
);
"""


async def init_db(dsn: str) -> None:
    conn = await asyncpg.connect(dsn)
    try:
        await conn.execute(CREATE_TABLE_SQL)
    finally:
        await conn.close()


async def insert_update(dsn: str, venue: str, symbol: str, ts, bids, asks) -> None:
    conn = await asyncpg.connect(dsn)
    try:
        await conn.execute(
            """
            INSERT INTO orderbook_updates (venue, symbol, ts, bids, asks)
            VALUES ($1, $2, $3, $4, $5)
            """,
            venue,
            symbol,
            ts,
            json.dumps(bids),
            json.dumps(asks),
        )
    finally:
        await conn.close()
