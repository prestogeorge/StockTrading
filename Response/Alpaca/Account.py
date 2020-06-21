import datetime
import json


class Account(object):
    def __init__(self, accountDict: dict):
        self.account_blocked = bool(accountDict["account_blocked"])  # boolean
        self.account_number = accountDict["account_number"]  # string
        self.buying_power = float(accountDict["buying_power"])  # string<number>
        self.cash = float(accountDict["cash"])  # string<number>
        self.created_at = datetime.datetime.strptime(accountDict["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")  # string<timestamp>
        self.currency = accountDict["currency"]  # string
        self.daytrade_count = int(accountDict["daytrade_count"])  # string<int>
        self.daytrading_buying_power = float(accountDict["daytrading_buying_power"])  # string<number>
        self.equity = float(accountDict["equity"])  # string<number>
        self.id = accountDict["id"]  # string<uuid>
        self.initial_margin = float(accountDict["initial_margin"])  # string<number>
        self.last_equity = float(accountDict["last_equity"])  # string<number>
        self.last_maintenance_margin = float(accountDict["last_maintenance_margin"])  # string<number>
        self.long_market_value = float(accountDict["long_market_value"])  # string<number>
        self.maintenance_margin = float(accountDict["maintenance_margin"])  # string<number>
        self.multiplier = float(accountDict["multiplier"])  # string<number>
        self.pattern_day_trader = bool(accountDict["pattern_day_trader"])  # boolean
        self.portfolio_value = float(accountDict["portfolio_value"])  # string<number>
        self.regt_buying_power = float(accountDict["regt_buying_power"])  # string<number>
        self.short_market_value = float(accountDict["short_market_value"])  # string<number>
        self.shorting_enabled = bool(accountDict["shorting_enabled"])  # boolean
        self.sma = float(accountDict["sma"])  # string<number>
        self.status = accountDict["status"]  # string<account_status>
        self.trade_suspended_by_user = bool(accountDict["trade_suspended_by_user"])  # boolean
        self.trading_blocked = bool(accountDict["trading_blocked"])  # boolean
        self.transfers_blocked = bool(accountDict["transfers_blocked"])  # boolean
