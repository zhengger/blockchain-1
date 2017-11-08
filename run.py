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

    res = jsonify(message='New Block', block=block.serialize())
    return res, 200


@instance.route('/chain', methods=['GET'])
def chain():
    chain = [block.serialize() for block in blockchain.chain]
    res = jsonify(blockchain=chain, length=len(chain))
    return res, 200


if __name__ == '__main__':
    instance.run()
