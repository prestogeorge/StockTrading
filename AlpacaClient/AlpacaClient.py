from AlpacaService.AlpacaService import AlpacaService
class AlpacaClient(object):
    @staticmethod
    def getAccount(self, alpacaClientConfig):
        return AlpacaService.getAccount(alpacaClientConfig)