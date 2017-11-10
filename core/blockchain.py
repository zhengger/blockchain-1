from hashlib import sha256
from .models import Block, Transaction


class Blockchain(object):
    def __init__(self):
        self._chain = []
        self._pending = []
        self._nodes = set()

        # Add genesis block
        self.create(0, 1)

    @property
    def chain(self):
        return self._chain

    def peek(self):
        return self._chain[-1]

    def create(self, key, prev_hash=None):
        """Pairs a new block with the pending transactions, then adds it to the chain.
        
        Args:
            key: Miner's proof of work.
            index: Block's position in the chain.
            pending: Transactions to link with this block.
            prev_hash: Hash value of the preceding block.
        Returns:
            The newly forged Block object.
        """
        block = Block(key=key, 
                      index=len(self._chain)+1,
                      transactions=self._pending,
                      prev_hash=prev_hash or self.peek())

        # Clear pending transactions, then add the block
        self._pending = []
        self._chain.append(block)
        return block

    def send(self, source, recipient, amount):
        """Creates a new transaction and links it with the waiting block.

        Args:
            source: Source address of the sender.
            recipient: Destination address of the recipient.
            amount: Value to exchange.
        Returns:
            The index of the block linked to this transaction.
        """
        transaction = Transaction(source, recipient, amount)
        self._pending.append(transaction)

        # Position of the block to link with this transaction
        return self.peek().index + 1

    def mine(self, block_hash):
        """Finds a number such that the hash of itself and the top block's key ends
        with five zeros.
        
        Args:
            block_hash: The `key` attribute for the most recent block in the chain.
        """
        current = 0
        while not Blockchain.verify_hash(block_hash, current):
            current += 1
        return current

    @classmethod
    def verify_hash(cls, block_hash, current_hash):
        """Hashes a block's `key` with a value obtained through mining, then verifies it.
        A new block is forged if the resultant hash of the two values ends with five zeros.

        Args:
            block_hash: The `key` attribute for a Block object, or its proof of work.
            current_hash: A guess hash.
        """
        combination = '{}{}'.format(block_hash, current_hash).encode()
        resultant = sha256(combination).hexdigest()
        return resultant.endswith('00000')

    @classmethod
    def verify_chain(cls, chain):
        """Checks the integrity of a blockchain by inspecting each block.

        Args:
            chain: A node's copy of the blockchain.
        """
        prev_block = chain[0]
        for block in chain[1:]:
            if prev_block.__repr__ != block.prev_hash:
                return False
            # Ensure that each block's proof of work is valid
            if not cls.verify_hash(prev_block.key, block.key):
                return False
            prev_block = block
        else:
            return True
