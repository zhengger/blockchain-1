from hashlib import sha256
from .components import Block, Transaction


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending = []

        # Block 0
        self.create(0, 0)

    def peek(self):
        return self.chain[-1]

    def create(self, key, prev_hash):
        """Pairs a new block with the pending transactions, then adds it to the chain.
        
        Parameters
        ----------
        key
            Miner's proof of work.
        index
            Block's position in the chain.
        pending
            Transactions to link with this block.
        prev_hash
            Hash value of the preceding block.
        """
        block = Block(key=key, 
                      index=len(self.chain)+1,
                      pending=self.pending,
                      prev_hash=prev_hash)

        # Clear pending transactions, then add the block
        self.pending.clear()
        self.chain.append(block)
        return block

    def send(self, source, recipient, amount):
        """Adds a new transaction to link with the next mined block.
        
        Parameters
        ----------
        source
            Source address of the sender.
        recipient
            Destination address of the recipient.
        amount
            Value to exchange.
        """
        transaction = Transaction(source, recipient, amount)
        self.pending.append(transaction)

        # Position of the block to link with this transaction
        return self.peek().index + 1

    @staticmethod
    def verify(block_hash, current_hash):
        """Compares a block's hash `key` with an arbitrary hash.
        A new block is forged if the resultant hash of the two values leads with two zeros.

        Parameters
        ----------
        block_hash
            The `key` attribute for a Block object.
        current_hash
            A guess hash.
        """
        combination = '{}{}'.format(block_hash, current_hash).encode()
        resultant = sha256(combination).hexdigest()
        return resultant.startswith('00')
