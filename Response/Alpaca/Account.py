from datetime import datetime

from undictify import type_checked_constructor, optional_converter
from dataclasses import dataclass
from iso4217 import Currency


# Example from https://github.com/Dobiasd/undictify
def parse_timestamp(datetime_repr: str) -> datetime:
    return datetime.strptime(datetime_repr, "%Y-%m-%dT%H:%M:%S.%fZ")


@type_checked_constructor(convert=True, skip=True, converters={'created_at': optional_converter(parse_timestamp)})
@dataclass
class Account(object):
    account_blocked: bool
    account_number: str
    buying_power: float
    cash: float
    created_at: datetime
    currency: Currency
    daytrade_count: int
    daytrading_buying_power: float
    equity: float
    id: str  # change to uuid type?
    initial_margin: float
    last_equity: float
    last_maintenance_margin: float
    long_market_value: float
    maintenance_margin: float
    multiplier: float
    pattern_day_trader: bool
    portfolio_value: float
    regt_buying_power: float
    short_market_value: float
    shorting_enabled: bool
    sma: float
    status: str
    trade_suspended_by_user: bool
    trading_blocked: bool
    transfers_blocked: bool
