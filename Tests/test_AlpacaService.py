import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig
from AlpacaService import AlpacaService


class test_AlpacaService(unittest.TestCase):
    def setUp(self):
        self.alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
    def test_getAccount_returnsAccount(self):
        #TODO: figure out how to mock requests.get
        self.assertEqual(True, True)

    def test_getPosition_returnsPosition(self):
        self.assertEqual(True, True)

    def test_getPositions_returnsPositions(self):
        self.assertEqual(True, True)

    def test_deletePosition_returnsOrder(self):
        self.assertEqual(True, True)

    def test_deletePositions_returnsResponse(self):
        self.assertEqual(True, True)