from time import time
from uuid import uuid4
from hashlib import sha256


class Block(object):
    def __init__(self, key, index, transactions, prev_hash):
        """An element of the blockchain.
        
        Args:
            key: Proof of work.
            index: Position in the chain.
            transactions: Confirmed transactions bound to this block.
            prev_hash: Hash value of the preceding block.
        """
        self.key = key
        self.index = index
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.timestamp = time()

    def __repr__(self):
        """SHA-256 representation of this block."""
        encoding = str(self.serialize()).encode()
        return sha256(encoding).hexdigest()

    def serialize(self):
        transactions = [t.serialize() for t in self.pending]
        fields = {
            'proof': self.key,
            'index': self.index,
            'transactions': transactions,
            'prev_hash': self.prev_hash,
            'timestamp': self.timestamp
        }
        return str(fields)


class Transaction(object):
    def __init__(self, source, recipient, amount):
        """Handshake between two members, signed by their addresses.
    
        Args:
            source: Sending node's UUID.
            recipient: Receiving node's UUID.
            amount: Value to transfer.
        """
        self.source = source
        self.recipient = recipient
        self.amount = amount

    def serialize(self):
        fields = {
            'source': self.source,
            'recipient': self.recipient,
            'amount': self.amount
        }
        return str(fields)


class Node(object):
    def __init__(self):
        """Pairs each connection to the network with a unique identifer."""
        self.address = str(uuid4())

    def __str__(self):
        return self.address
