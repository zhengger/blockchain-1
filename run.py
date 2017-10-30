from flask import Flask
from core import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    # Start local server
    instance = Flask(__name__)
    instance.run()
