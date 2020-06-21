import unittest

from AlpacaClient.AlpacaClient import AlpacaClient
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService.AlpacaService import AlpacaService
from unittest.mock import MagicMock


class test_AlpacaClient(unittest.TestCase):
    def test_getAccount_callsService(self):
        AlpacaService.getAccount = MagicMock(staticmethod='getAccount')
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        account = AlpacaClient.getAccount(alpacaClientConfig)
        AlpacaService.getAccount.assert_called_with(alpacaClientConfig)
        self.assertEqual(True, True)
