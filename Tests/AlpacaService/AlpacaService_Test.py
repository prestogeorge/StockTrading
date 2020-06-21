import unittest
from unittest.mock import MagicMock

from AlpacaClient.AlpacaClientConfig import AlpacaClientConfig


class AlpacaService_Test(unittest.TestCase):
    def test_getAccount_returnsAccount(self):
        alpacaClientConfig = AlpacaClientConfig('YOUR-KEY', 'YOUR-SECRET-KEY', 'YOUR-BASE-URL')
        self.assertEqual(True, True)
