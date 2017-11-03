from core import Blockchain
from flask import Flask, jsonify


instance = Flask(__name__)
blockchain = Blockchain()


@instance.route('/mine', methods=['GET'])
def mine():
    pass


if __name__ == '__main__':
    instance.run()
