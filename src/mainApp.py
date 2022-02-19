# import libraries
import datetime
from random import random, randrange
from client import Client
from controller import BCController as BCc
from transaction import Transaction
from itertools import combinations

'''
Client
The Client is the one who will buy goods from other vendors.
The client himself may become a vendor and will accept '
money from others against the goods he supplies.
We assume here that the client can both be a supplier and a recipient of TPCoins.
Thus, we will create a client class in our code that has the ability to send and receive money.

Miner
The Miner is the one who picks up the transactions from a transaction pool
and assembles them in a block. The miner has to provide a valid proof-of-work to
get the mining reward. All the money that miner collects as a fee will be for him to keep.
He may spend that money on buying goods or services from other registered vendors on the network,
just the way a Client described above does.

Blockchain
Finally, a Blockchain is a data structure that chains all the mined blocks in a chronological order.
This chain is immutable and thus temper-proof.

'''
TRANSACTIONS = 300

def main():
    # blockchain controller
    bcc = BCc()
    BCc.set_difficulty(5)
    miner = Client("miner1")
    
    # create clients
    alice = Client("Alice")
    bob = Client("Bob")
    charlie = Client("Charlie")
    david = Client("David")
    
    
    g = Client("GENESIS")
    t = Transaction(g,alice,100)
    bcc.addGenesis(t)
    

    bcc.add_client(alice)
    bcc.add_client(bob)
    bcc.add_client(charlie)
    bcc.add_client(david)
        

    combs = list(combinations(bcc.get_clients(),2))
    for i in range(TRANSACTIONS):
        x = randrange(len(combs))   
        c = randrange(10,100)
        t =  Transaction(combs[x][0],combs[x][1],c)
        t.sign_transaction()
        bcc.add_transaction(t)
    print('created ')
    while bcc.mine(miner):
        print('block mined at ' + datetime.datetime.now().strftime('%H:%M:%S'))

    print(bcc.get_block_chain_size())

if __name__ == '__main__':
    main()
