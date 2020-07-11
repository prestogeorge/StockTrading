from AlpacaService.AlpacaService import AlpacaService


class AlpacaClient(object):
    def __init__(self, alpacaClientConfig):
        self.alpacaClientConfig = alpacaClientConfig

    def getAccount(self):
        return AlpacaService.getAccount(self.alpacaClientConfig)

    def getPosition(self, symbol):
        return AlpacaService.getPosition(self.alpacaClientConfig, symbol)

    def getPositions(self):
        return AlpacaService.getPositions(self.alpacaClientConfig)

    def deletePosition(self, symbol):
        return AlpacaService.deletePosition(self.alpacaClientConfig, symbol)

    def deletePositions(self):
        return AlpacaService.deletePositions(self.alpacaClientConfig)