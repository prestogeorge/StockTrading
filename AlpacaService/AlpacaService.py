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

    @staticmethod
    def getPositions(alpacaClientConfig):
        url = alpacaClientConfig.baseUrl + "/positions"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        r = requests.get(url, headers=headers)
        positions = []
        for position in r.json():
            positions.append(Position(position))
        return positions

    @staticmethod
    def deletePosition(alpacaClientConfig, symbol):
        url = alpacaClientConfig.baseUrl + "/positions"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        url += str(symbol)
        r = requests.delete(url, headers=headers)
        #return order

    @staticmethod
    def deletePositions(alpacaClientConfig):
        url = alpacaClientConfig.baseUrl + "/positions"
        headers = {'APCA-API-KEY-ID': alpacaClientConfig.keyId,
                   'APCA-API-SECRET-KEY': alpacaClientConfig.secretKeyId}
        r = requests.delete(url, headers=headers)
        #return HTTP 207 Multi-Status with body; an array of objects that include the order id and http status code for each status request.