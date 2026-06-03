from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    db_dsn: str

    @staticmethod
    def from_env() -> "AppConfig":
        return AppConfig(
            db_dsn=os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/orderbook"),
        )
