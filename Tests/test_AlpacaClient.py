import unittest

from AlpacaClient.AlpacaClient import AlpacaClient
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService.AlpacaService import AlpacaService
from unittest.mock import MagicMock


class test_AlpacaClient(unittest.TestCase):
    def test_getAccount_callsService(self):
        AlpacaService.getAccount = MagicMock(staticmethod='getAccount')
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        alpacaClient = AlpacaClient(alpacaClientConfig)
        account = alpacaClient.getAccount()
        AlpacaService.getAccount.assert_called_with(alpacaClientConfig)

    def test_getPosition_callsService(self):
        AlpacaService.getPosition = MagicMock(staticmethod='getPosition')
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        alpacaClient = AlpacaClient(alpacaClientConfig)
        position = alpacaClient.getPosition("SYM")
        AlpacaService.getPosition.assert_called_with(alpacaClientConfig, "SYM")
