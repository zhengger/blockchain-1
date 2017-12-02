# blockchain [![Build Status](https://travis-ci.com/jdr023/blockchain.svg?token=MJAVVCPapY3bjg5PYxsH&branch=master)](https://travis-ci.com/jdr023/blockchain)

## Layout
    .
    ├── core
    │   ├── __init__.py
    │   ├── blockchain.py
    │   ├── models.py
    ├── tests
    │   ├── __init__.py
    │   └── test_blockchain.py
    ├── .gitignore
    ├── .travis.yml
    ├── LICENSE
    ├── README.md
    └── run.py
    
Build
- 
Tested on [Python 3.6](https://www.python.org/downloads/release/python-360/), but should work on any 3+ release.

Clone the repo:
```Shell
$ git clone https://github.com/jdr023/blockchain.git
```

#### Test
From the `blockchain/` directory, you can run the test suite with the following command:
```Shell
$ python -m unittest tests.test_blockchain
```

#### Run
From the `blockchain/` directory, start the development server:
```Shell
$ python run.py
```
Endpoints can be reached through http://localhost:5000.

Reference
-
* [Protocol](http://www.michaelnielsen.org/ddi/how-the-bitcoin-protocol-actually-works/)
* [Consensus](https://www.persistent.com/wp-content/uploads/2017/04/WP-Understanding-Blockchain-Consensus-Models.pdf)
* [Proof of work](https://en.bitcoin.it/wiki/Proof_of_work)

Contribute
-
Feel free to open an [Issue](https://github.com/jdr023/blockchain/issues/new) or submit a pull request.

License
-
This project is licensed under the AGPL-3.0 License — see the LICENSE file for details.
