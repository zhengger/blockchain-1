from flask import Flask, jsonify
from core import Blockchain, Node


instance = Flask(__name__)
blockchain = Blockchain()
node = Node()


@instance.route('/mine', methods=['GET'])
def mine():
    prev_block = blockchain.peek()
    proof = blockchain.mine(prev_block.key)

    # Reward the miner and forge the new block
    blockchain.send(0, node.address, 1)
    block = blockchain.create(proof)

    res = {
        'message': 'NEW BLOCK',
        'index': block.index,
        'transactions': block.pending,
        'proof': block.key,
        'prev_hash': block.prev_hash
    }
    return jsonify(res), 200


if __name__ == '__main__':
    instance.run()
