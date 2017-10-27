from blockchain import Blockchain
from unittest import TestCase


class BlockchainTestSuite(TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_create(self):
        # Chain formation
        block_zero = self.blockchain.peek()
        block_one = self.blockchain.create(1, 1)
        self.assertNotEqual(block_zero, block_one)

        # Unique hash generation
        block_two = self.blockchain.create(1, 1)
        self.assertNotEqual(block_one, block_two)

    def test_send(self):
        # Transaction queuing
        first = self.blockchain.send('abc', 'def', 5)
        self.assertEqual(len(self.blockchain.pending), 1)

        # Pending exchanges
        second = self.blockchain.send('def', 'abc', 5)
        self.assertEqual(first, second)
