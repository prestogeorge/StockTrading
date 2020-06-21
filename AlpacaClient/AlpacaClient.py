from AlpacaService.AlpacaService import AlpacaService
class AlpacaClient(object):
    @staticmethod
    def getAccount(alpacaClientConfig):
        return AlpacaService.getAccount(alpacaClientConfig)