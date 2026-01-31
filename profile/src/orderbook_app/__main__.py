from __future__ import annotations

import asyncio
import json

from orderbook_app.config import AppConfig
from orderbook_app.services.simulated import generate_simulated_update
from orderbook_app.storage.db import init_db, insert_update


async def run_simulated_ingest() -> None:
    config = AppConfig.from_env()
    await init_db(config.db_dsn)
    update = generate_simulated_update("sim", "ETH/USDT")
    await insert_update(
        config.db_dsn,
        update.venue,
        update.symbol,
        update.ts,
        json.loads(update.model_dump_json())["bids"],
        json.loads(update.model_dump_json())["asks"],
    )


def main() -> None:
    asyncio.run(run_simulated_ingest())


if __name__ == "__main__":
    main()
