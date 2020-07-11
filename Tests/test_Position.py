import unittest

from Response.Alpaca.Position import Position


class test_Position(unittest.TestCase):
    def test_init_castsCorrectly(self):
        positionDict = {
            "asset_id": "904837e3-3b76-47ec-b432-046db621571b",
            "symbol": "AAPL",
            "exchange": "NASDAQ",
            "asset_class": "us_equity",
            "avg_entry_price": "100.0",
            "qty": "5",
            "side": "long",
            "market_value": "600.0",
            "cost_basis": "500.0",
            "unrealized_pl": "100.0",
            "unrealized_plpc": "0.20",
            "unrealized_intraday_pl": "10.0",
            "unrealized_intraday_plpc": "0.0084",
            "current_price": "120.0",
            "lastday_price": "119.0",
            "change_today": "0.0084"
        }

        position = Position(**positionDict)

        self.assertEqual("904837e3-3b76-47ec-b432-046db621571b", position.asset_id)
        self.assertEqual("AAPL", position.symbol)
        self.assertEqual("NASDAQ", position.exchange)
        self.assertEqual("us_equity", position.asset_class)
        self.assertEqual(100.0, position.avg_entry_price)
        self.assertEqual(5, position.qty)
        self.assertEqual("long", position.side)
        self.assertEqual(600.0, position.market_value)
        self.assertEqual(500, position.cost_basis)
        self.assertEqual(100.0, position.unrealized_pl)
        self.assertEqual(0.20, position.unrealized_plpc)
        self.assertEqual(10.0, position.unrealized_intraday_pl)
        self.assertEqual(0.0084, position.unrealized_intraday_plpc)
        self.assertEqual(120.0, position.current_price)
        self.assertEqual(119.0, position.lastday_price)
        self.assertEqual(0.0084, position.change_today)
