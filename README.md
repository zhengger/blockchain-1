# blockchain [![Build Status](https://travis-ci.com/jdr023/blockchain.svg?token=MJAVVCPapY3bjg5PYxsH&branch=master)](https://travis-ci.com/jdr023/blockchain)

## Layout
    .
    ├── core
    │   ├── __init__.py
    │   ├── blockchain.py
    │   ├── components.py
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
Tested on [Python 3.6](https://www.python.org/downloads/release/python-360/), though it should work on any 3+ release.

Clone the repo:
```Shell
$ git clone https://github.com/jdr023/blockchain.git
```

#### Testing
From the `blockchain/` directory, you can run the test suite with the following command:
```Shell
$ python -m unittest tests.test_blockchain
```

#### Running
From the `blockchain/` directory, start a local Flask server:
```Shell
$ python run.py
```

Contribute
-
Feel free to open an [Issue](https://github.com/jdr023/blockchain/issues/new) or submit a pull request.

License
-
This project is licensed under the AGPL-3.0 License — see the LICENSE.txt file for details.