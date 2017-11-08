from time import time
from uuid import uuid4
from hashlib import sha256


class Block(object):
    def __init__(self, key, index, pending, prev_hash):
        """An element of the Blockchain.
        
        Args:
            key: Proof of work.
            index: Position in the chain.
            pending: List of transactions to verify.
            prev_hash: Hash value of the preceding Block.
        """
        self.key = key
        self.index = index
        self.pending = pending
        self.prev_hash = prev_hash
        self.timestamp = time()

    def __repr__(self):
        """SHA-256 representation of this Block."""
        encoding = str(self.serialize()).encode()
        return sha256(encoding).hexdigest()

    def serialize(self):
        fields = {
            'proof': self.key,
            'index': self.index,
            'transactions': self.pending,
            'prev_hash': self.prev_hash,
            'timestamp': self.timestamp
        }
        return str(fields)


class Transaction(object):
    def __init__(self, source, recipient, amount):
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
        self.address = str(uuid4())

    def __str__(self):
        return self.address
