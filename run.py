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
        'message': 'New Block',
        'block': block.serialize()
    }
    return jsonify(res)


@instance.route('/chain', methods=['GET'])
def chain():
    chain = [b.serialize() for b in blockchain.chain]
    res = {
        'blockchain': chain,
        'length': len(blockchain.chain)
    }
    return jsonify(res)


if __name__ == '__main__':
    instance.run()
