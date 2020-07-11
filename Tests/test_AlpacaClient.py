import unittest

from AlpacaClient.AlpacaClient import AlpacaClient
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService.AlpacaService import AlpacaService
from unittest.mock import MagicMock


class test_AlpacaClient(unittest.TestCase):

    def setUp(self):
        self.alpacaClient = AlpacaClient(AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL'))

    def test_getAccount_callsService(self):
        AlpacaService.getAccount = MagicMock(staticmethod='getAccount')
        account = self.alpacaClient.getAccount()
        AlpacaService.getAccount.assert_called_with(self.alpacaClient.alpacaClientConfig)

    def test_getPosition_callsService(self):
        AlpacaService.getPosition = MagicMock(staticmethod='getPosition')
        position = self.alpacaClient.getPosition("SYM")
        AlpacaService.getPosition.assert_called_with(self.alpacaClient.alpacaClientConfig, "SYM")

    def test_getPositions_callsService(self):
        AlpacaService.getPositions = MagicMock(staticmethod='getPositions')
        positions = self.alpacaClient.getPositions()
        AlpacaService.getPositions.assert_called_with(self.alpacaClient.alpacaClientConfig)

    def test_deletePosition_callsService(self):
        AlpacaService.deletePosition = MagicMock(staticmethod='deletePosition')
        order = self.alpacaClient.deletePosition("SYM")
        AlpacaService.deletePosition.assert_called_with(self.alpacaClient.alpacaClientConfig, "SYM")

    def test_deletePositions_callsService(self):
        AlpacaService.deletePositions = MagicMock(staticmethod='deletePositions')
        response = self.alpacaClient.deletePositions()
        AlpacaService.deletePositions.assert_called_with(self.alpacaClient.alpacaClientConfig)