import datetime
import unittest
from Response.Alpaca.Account import Account


class Account_Test(unittest.TestCase):
    def test_init_castsCorrectly(self):
        accountDict = {
            "account_blocked": False,
            "account_number": "010203ABCD",
            "buying_power": "262113.632",
            "cash": "-23140.2",
            "created_at": "2019-06-12T22:47:07.99658Z",
            "currency": "USD",
            "daytrade_count": 0,
            "daytrading_buying_power": "262113.632",
            "equity": "103820.56",
            "id": "e6fe16f3-64a4-4921-8928-cadf02f92f98",
            "initial_margin": "63480.38",
            "last_equity": "103529.24",
            "last_maintenance_margin": "38000.832",
            "long_market_value": "126960.76",
            "maintenance_margin": "38088.228",
            "multiplier": "4",
            "pattern_day_trader": False,
            "portfolio_value": "103820.56",
            "regt_buying_power": "80680.36",
            "short_market_value": "0",
            "shorting_enabled": True,
            "sma": "0",
            "status": "ACTIVE",
            "trade_suspended_by_user": False,
            "trading_blocked": False,
            "transfers_blocked": False
        }
        account = Account(accountDict)
        self.assertEqual(False, account.account_blocked)
        self.assertEqual("010203ABCD", account.account_number)
        self.assertEqual(262113.632, account.buying_power)
        self.assertEqual(-23140.2, account.cash)
        self.assertEqual(datetime.datetime.strptime("2019-06-12T22:47:07.99658Z", "%Y-%m-%dT%H:%M:%S.%fZ"), account.created_at)
        self.assertEqual("USD", account.currency)
        self.assertEqual(0, account.daytrade_count)
        self.assertEqual(262113.632, account.daytrading_buying_power)
        self.assertEqual(103820.56, account.equity)
        self.assertEqual("e6fe16f3-64a4-4921-8928-cadf02f92f98", account.id)
        self.assertEqual(63480.38, account.initial_margin)
        self.assertEqual(103529.24, account.last_equity)
        self.assertEqual(38000.832, account.last_maintenance_margin)
        self.assertEqual(126960.76, account.long_market_value)
        self.assertEqual(38088.228, account.maintenance_margin)
        self.assertEqual(4, account.multiplier)
        self.assertEqual(False, account.pattern_day_trader)
        self.assertEqual(103820.56, account.portfolio_value)
        self.assertEqual(80680.36, account.regt_buying_power)
        self.assertEqual(0, account.short_market_value)
        self.assertEqual(True, account.shorting_enabled)
        self.assertEqual(0, account.sma)
        self.assertEqual("ACTIVE", account.status)
        self.assertEqual(False, account.trade_suspended_by_user)
        self.assertEqual(False, account.trading_blocked)
        self.assertEqual(False, account.transfers_blocked)
