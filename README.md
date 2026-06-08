# py_bchain - Simple Blockchain

A Python implementation of a blockchain system with cryptographic signatures, proof-of-work mining, and transaction management.

## 📋 Overview

py_bchain is an educational blockchain implementation that demonstrates core blockchain concepts including:

- **Blocks & Blockchain**: Immutable ledger structure with chained blocks
- **Transactions**: Cryptographically signed transactions between clients
- **Clients & Wallets**: Entities that send and receive transactions
- **Proof-of-Work Mining**: Difficulty-based mining algorithm with mining rewards
- **Transaction Pool**: Mempool for pending transactions before mining

## 🏗️ Architecture

### Core Components

#### **Block** (`src/block.py`)
Represents a single block in the blockchain containing:
- Verified transactions
- Previous block hash (linking to parent block)
- Nonce (proof-of-work value)
- String representation for display

#### **Blockchain** (`src/blockchain.py`)
The main ledger managing:
- List of blocks
- Mining reward (20 coins per block)
- Genesis block creation
- SHA256 hashing for block identification
- Blockchain initialization and validation

#### **Transaction** (`src/transaction.py`)
Represents value transfer between clients:
- Sender and recipient (Client objects)
- Transaction amount
- Timestamp
- Digital signature using PKCS1_v1_5 with SHA hashing
- Transaction serialization via ordered dictionaries

#### **Client** (`src/client.py`)
Represents network participants:
- 1024-bit RSA key pair generation (private/public)
- Unique identity derived from public key
- PKCS1_v1_5 signing capability
- Client name

#### **Wallet** (`src/wallet.py`)
(Currently a template) Will contain:
- Client balance
- Public/private key storage
- Address generation

#### **BCController** (`src/controller.py`)
Central controller managing:
- Client registry
- Transaction pool (mempool)
- Block mining orchestration
- Mining difficulty configuration
- Blockchain ledger
- Mining reward distribution
- Proof-of-work implementation with configurable difficulty

#### **Transaction List** (`src/trans_list.py`)
Pre-defined transaction examples for testing with multiple clients.

### Application Entry Point

**mainApp.py** - Main application demonstrating:
1. Blockchain controller initialization
2. Miner and client creation
3. Genesis block creation (initial transaction from GENESIS to Alice)
4. Random transaction generation between clients
5. Mining loop with block creation and miner rewards

## 🔐 Cryptography

The system uses:
- **RSA (1024-bit)**: Key generation and digital signatures
- **SHA-256**: Hashing for transactions and proof-of-work
- **PKCS1_v1_5**: Signature scheme for transaction authentication

## ⛏️ Mining Algorithm

The mining process:
1. Collects unverified transactions from the pool (minimum BLOCK_SIZE = 10)
2. Creates a new Block with transactions
3. Performs proof-of-work:
   - Iterates through nonce values
   - Computes SHA256 hash of block + nonce
   - Continues until hash starts with required number of '1's (difficulty level)
4. Adds mined block to blockchain
5. Rewards miner with REWARD tokens (20 coins)
6. Miner reward added back to transaction pool

**Difficulty Configuration**: Set via `BCController.set_difficulty(n)` where n is the number of leading '1's required in the hash.

## 📊 Transaction Flow

```
1. Create Client with RSA keypair
   ↓
2. Create Transaction (sender → recipient, amount)
   ↓
3. Sign Transaction with sender's private key
   ↓
4. Add to Transaction Pool
   ↓
5. Miner collects BLOCK_SIZE transactions
   ↓
6. Perform Proof-of-Work
   ↓
7. Add Block to Blockchain
   ↓
8. Reward Miner (new transaction added to pool)
```

## 🚀 Quick Start

### Prerequisites
```bash
pip install pycryptodome
```

### Running the Application

```bash
cd src
python mainApp.py
```

The application will:
1. Create a blockchain with difficulty level 5
2. Initialize a miner and 4 clients (Alice, Bob, Charlie, David)
3. Create a genesis block
4. Generate 300 random transactions between clients
5. Mine blocks as transactions accumulate
6. Display mining timestamps

### Configuration

Modify `src/mainApp.py`:
- `TRANSACTIONS = 300` - Number of random transactions to generate
- `BCc.set_difficulty(5)` - Mining difficulty (1-9 recommended)
- Add more clients with `Client("name")`

## 📡 API Specification

An OpenAPI 2.0 specification is provided in `API/openapi1.yaml` defining endpoints:

- `GET /client/findByName` - Find client by name
- `POST /blocks/addblock` - Add block to blockchain
- `GET /ping` - Server health check

## 📁 Project Structure

```
py_bchain/
├── README.md                 # This file
├── LICENSE.txt              # GPL-3.0 License
├── .gitignore              # Git ignore rules
├── src/
│   ├── mainApp.py          # Application entry point
│   ├── block.py            # Block class
│   ├── blockchain.py       # Blockchain ledger
│   ├── transaction.py      # Transaction class
│   ├── client.py           # Client class with RSA keys
│   ├── wallet.py           # Wallet class (template)
│   ├── controller.py       # Blockchain controller
│   └── trans_list.py       # Transaction test data
└── API/
    └── openapi1.yaml       # OpenAPI specification
```

## 🔑 Key Features

✅ **Cryptographic Security**: RSA-based digital signatures for transaction authentication  
✅ **Proof-of-Work**: Difficulty-based mining algorithm  
✅ **Immutable Ledger**: Chained blocks with hash linking  
✅ **Mining Rewards**: Automatic miner compensation  
✅ **Transaction Pool**: Mempool for pending transactions  
✅ **Flexible Configuration**: Adjustable difficulty levels  
✅ **Multi-client Support**: Multiple simultaneous network participants  

## 📝 Implementation Notes

- **Genesis Block**: Special initial block created by GENESIS client
- **Block Capacity**: Fixed at 10 transactions per block (configurable via BLOCK_SIZE)
- **Mining Reward**: 20 coins awarded to miner per successful block
- **Transaction Validation**: Digital signature verification via PKCS1_v1_5
- **Nonce Strategy**: Iterative hash generation until difficulty met

## 🎓 Educational Use

This project is ideal for learning:
- Blockchain fundamentals and data structures
- Cryptographic signing and verification
- Proof-of-work consensus mechanisms
- Transaction processing and mempool management
- Mining algorithms and difficulty adjustment

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see [LICENSE.txt](LICENSE.txt) for details.

## 👤 Author

Created by [@xterm2000](https://github.com/xterm2000)

## 🔗 Related Resources

- [Blockchain Wikipedia](https://en.wikipedia.org/wiki/Blockchain)
- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)
- [Proof of Work](https://en.wikipedia.org/wiki/Proof_of_work)
- [Digital Signatures](https://en.wikipedia.org/wiki/Digital_signature)

---

**Note**: This is an educational implementation. For production use, comprehensive security audits and optimization are required.
