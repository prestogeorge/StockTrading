import requests

from Response.Alpaca.Account import Account
from Response.Alpaca.Position import Position


class AlpacaService(object):
    @staticmethod
    def getAccount(alpacaClientConfig):
        url = alpacaClientConfig.baseUrl + "/account"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        r = requests.get(url, headers=headers)
        return Account(r.json())

    @staticmethod
    def getPosition(alpacaClientConfig, symbol):
        url = alpacaClientConfig.baseUrl + "/positions"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        url += str(symbol)
        r = requests.get(url, headers=headers)
        return Position(r.json())

