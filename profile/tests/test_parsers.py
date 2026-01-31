from __future__ import annotations

from orderbook_app.connectors.binance import parse_depth_snapshot, parse_depth_update
from orderbook_app.connectors.okx import parse_snapshot, parse_update
from orderbook_app.services.simulated import generate_simulated_update


def test_binance_snapshot_parsing():
    payload = {"bids": [["3000", "1.2"]], "asks": [["3001", "0.8"]]}
    snapshot = parse_depth_snapshot(payload, "ETHUSDT", "binance")
    assert snapshot.bids[0].price == 3000.0
    assert snapshot.asks[0].size == 0.8


def test_binance_update_parsing():
    payload = {"E": 1700000000000, "b": [["3000", "1.0"]], "a": [["3001", "2.0"]]}
    update = parse_depth_update(payload, "ETHUSDT", "binance")
    assert update.bids[0].price == 3000.0
    assert update.asks[0].size == 2.0


def test_okx_snapshot_parsing():
    payload = {
        "data": [
            {
                "ts": "1700000000000",
                "bids": [["3000", "1.1"]],
                "asks": [["3001", "0.9"]],
            }
        ]
    }
    snapshot = parse_snapshot(payload, "ETH-USDT")
    assert snapshot.bids[0].price == 3000.0
    assert snapshot.asks[0].size == 0.9


def test_okx_update_parsing():
    payload = {
        "data": [
            {
                "ts": "1700000000000",
                "bids": [["2999", "1.3"]],
                "asks": [["3002", "0.7"]],
            }
        ]
    }
    update = parse_update(payload, "ETH-USDT")
    assert update.bids[0].price == 2999.0
    assert update.asks[0].size == 0.7


def test_simulated_update():
    update = generate_simulated_update("sim", "ETH/USDT")
    assert update.venue == "sim"
    assert update.symbol == "ETH/USDT"
    assert update.bids
    assert update.asks
