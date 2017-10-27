from blockchain import Blockchain
from unittest import TestCase


class BlockchainTestSuite(TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_create(self):
        # Test unique hash generation
        block_zero = self.blockchain.peek()
        block_one = self.blockchain.create(1, 1)
        block_two = self.blockchain.create(1, 1)
        self.assertNotEqual(block_zero, block_one)
        self.assertNotEqual(block_one, block_two)
