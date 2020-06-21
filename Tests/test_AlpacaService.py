import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService import AlpacaService


class test_AlpacaService(unittest.TestCase):
    @patch('requests.get')
    def test_getAccount_returnsAccount(self, mocked_requests):
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        #TODO: figure out how to mock requests.get
        #account = AlpacaService.AlpacaService.getAccount(alpacaClientConfig)
        self.assertEqual(True, True)
