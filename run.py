from core import Blockchain, Node
from flask import Flask, jsonify, request


api = Flask(__name__)
blockchain = Blockchain()
node = Node()


@api.route('/chain', methods=['GET'])
def chain():
    chain = [b.serialize() for b in blockchain.chain]
    res = {
        'blockchain': chain,
        'length': len(blockchain.chain)
    }
    return jsonify(res)


@api.route('/mine', methods=['GET'])
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


@api.route('/send', methods=['POST'])
def send():
    form = request.form
    fields = ['source', 'recipient', 'amount']
    if not all(form.get(f, False) for f in fields):
        return 'Requires `source`, `recipient`, `amount`', 400
    
    idx = blockchain.send(form['source'], form['recipient'], form['amount'])
    res = {
        'message': 'Transaction bound to block {}'.format(idx),
    }
    return jsonify(res)


if __name__ == '__main__':
    api.run()
