###########################
import hashlib

from numpy import block

from  block import Block
from  transaction import Transaction


class BlockChain:
    REWARD = 20    
    blocks = []
    INIT = False

    @staticmethod
    def get_num_of_blocks()->int:
        return len(BlockChain.blocks)

    ##################################
    @staticmethod
    def print_blockchain():
        print("Number of blocks in chain " + str(len(BlockChain.blocks)))
        for x in range( len(BlockChain.blocks) ):
            block_temp = BlockChain.blocks[x]
            print("block # " + str(x))
            print (block_temp)

        print('=====================================')

    ##################################
    @staticmethod
    def add_block(b: Block):
        if not BlockChain.INIT:
            print('BC empty')
            return
        BlockChain.blocks.append(b)

    ##################################
    @staticmethod
    def sha256(message: str):
        '''The sha256 function takes a message as a parameter, 
         encodes it to ASCII, generates a hexadecimal digest and returns the value to the caller.'''
        return hashlib.sha256(message.encode('ascii')).hexdigest()

    ##################################
    @staticmethod
    def addGenesis( t: Transaction ):
        if t._sender._name != 'GENESIS':
            print('the sender is not GENESIS')
            return
        block0 = Block()
        block0._previous_block_hash = None
        block0._nonce = None
        block0._verified_transactions.append(t)
        BlockChain.INIT = True
        BlockChain.add_block(block0)

    