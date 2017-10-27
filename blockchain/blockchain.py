from .components import Block


class Blockchain(object):
    def __init__(self):
        self._chain = []
        self.pending = []

        # Block 0
        self.create(0, 0)

    def peek(self):
        return self._chain[-1]

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
                      index=len(self._chain)+1,
                      pending=self.pending,
                      prev_hash=prev_hash)

        # Clear pending transactions, then add the block
        self.pending.clear()
        self._chain.append(block)
        return block
