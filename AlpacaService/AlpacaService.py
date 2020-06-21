import requests

from Response.Alpaca.Account import Account


class AlpacaService(object):
    @staticmethod
    def getAccount(alpacaClientConfig):
        url = alpacaClientConfig.baseUrl + "/account"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        r = requests.get(url, headers=headers)
        return Account(r.json())
