import datetime


class Account(object):
    def __init__(self, account_blocked, account_number, buying_power, cash, created_at,
                 currency, daytrade_count, daytrading_buying_power, equity, id,
                 initial_margin, last_equity, last_maintenance_margin, long_market_value,
                 maintenance_margin, multiplier, pattern_day_trader, portfolio_value,
                 regt_buying_power, short_market_value, shorting_enabled, sma, status,
                 trade_suspended_by_user, trading_blocked, transfers_blocked):
        self.account_blocked = bool(account_blocked)  # boolean
        self.account_number = account_number  # string
        self.buying_power = float(buying_power)  # string<number>
        self.cash = float(cash)  # string<number>
        self.created_at = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")  # string<timestamp>
        self.currency = currency  # string
        self.daytrade_count = daytrade_count  # string<int>
        self.daytrading_buying_power = daytrading_buying_power  # string<number>
        self.equity = equity  # string<number>
        self.id = id  # string<uuid>
        self.initial_margin = initial_margin  # string<number>
        self.last_equity = last_equity  # string<number>
        self.last_maintenance_margin = last_maintenance_margin  # string<number>
        self.long_market_value = long_market_value  # string<number>
        self.maintenance_margin = maintenance_margin  # string<number>
        self.multiplier = multiplier  # string<number>
        self.pattern_day_trader = pattern_day_trader  # boolean
        self.portfolio_value = portfolio_value  # string<number>
        self.regt_buying_power = regt_buying_power  # string<number>
        self.short_market_value = short_market_value  # string<number>
        self.shorting_enabled = shorting_enabled  # boolean
        self.sma = sma  # string<number>
        self.status = status  # string<account_status>
        self.trade_suspended_by_user = trade_suspended_by_user  # boolean
        self.trading_blocked = trading_blocked  # boolean
        self.transfers_blocked = transfers_blocked  # boolean


if __name__ == "__main__":
    account = Account(False, "010203ABCD", "262113.632", "-23140.2",
                      "2019-06-12T22:47:07.99658Z", "USD",
                      0, "262113.632", "103820.56",
                      "e6fe16f3-64a4-4921-8928-cadf02f92f98",
                      "63480.38", "103529.24", "38000.832", "126960.76",
                      "38088.228", "4", False, "103820.56", "80680.36",
                      "0", True, "0", "ACTIVE", False, False, False)
