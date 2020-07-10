import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService import AlpacaService


class test_AlpacaService(unittest.TestCase):
    def test_getAccount_returnsAccount(self):
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        #TODO: figure out how to mock requests.get
        #account = AlpacaService.AlpacaService.getAccount(alpacaClientConfig)
        self.assertEqual(True, True)

    def test_getPosition_returnsPosition(self):
        #TODO: figure out how to mock requests.get
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        self.assertEqual(True, True)
