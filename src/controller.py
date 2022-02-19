from transaction import Transaction
from blockchain import BlockChain
from client import Client
from block import Block


class BCController:
    ''' Controller class '''

    BLOCK_SIZE = 10
    DIFFICULTY = 5
    ledger = BlockChain()
    '''the main ledger'''
    controller_client = Client("Controller" + str(id))
    tr_pool = []
    '''pool of unprocessed transactions'''

    last_block_hash: str = ""

    def __init__(self, id=0) -> None:
        self._clients = []

    def init_treasury(self, amount: int) -> None:
        self._money = amount

    def add_client(self, client_name: str):
        c = Client(client_name)
        self._clients.append(c)

   

    def add_client(self, c: Client):
        self._clients.append(c)

    def get_clients(self):
        return self._clients

    def get_client(self, client_id: int) -> int:
        return self._clients[client_id]

    def add_transaction(self, t: Transaction) -> None:
        BCController.tr_pool.append(t)

    def find_client_by_name(self, name) -> Client:
        return next(t for t in self._clients if name == t.name)

    @staticmethod
    def get_block_chain_size()->int:
        return BCController.ledger.get_num_of_blocks()

    @staticmethod
    def set_difficulty(d: int):
        '''set mining difficulty'''
        BCController.DIFFICULTY = d

    @staticmethod
    def addGenesis(t: Transaction):
        '''hardcoded ganesis block '''
        BCController.ledger.addGenesis(t)

    @staticmethod
    def mine2(message: str, difficulty: int = 1):
        '''We now develop the mine function that implements our own mining strategy. 
        Our strategy in this case would be to generate a hash on the given message that 
        is prefixed with a given number of 1's. The given number of 1's is specified as a 
        parameter to mine function specified as the difficulty level.
        For example, if you specify a difficulty level of 2, 
        the generated hash on a given message should start with two 1's - 
        like 11xxxxxxxx. If the difficulty level is 3, 
        the generated hash should start with three 1's - like 111xxxxxxxx. 
        Given these requirements, we will now develop the mining function as shown 
        in the steps given below.'''

        assert difficulty >= 1 and difficulty < 10
        prefix = '1' * difficulty
        for i in range(1000000000):
            digest = BlockChain.sha256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                print("after " + str(i) + " iterations found nonce: " + digest)
                return digest

    @staticmethod
    def mine(miner: Client) -> bool:
        ''' add block to the block chain and reward Miner'''

        # 3 and more transactions
        if len(BCController.tr_pool) < BCController.BLOCK_SIZE:
            print('not enough transactions')
            return False

        block = Block()
        #  3 transactions / Block FIFO
        for i in range(BCController.BLOCK_SIZE):
            temp_transaction = BCController.tr_pool.pop(0)
            # validate transaction
            # if valid
            block._verified_transactions.append(temp_transaction)

        block._previous_block_hash = BCController.last_block_hash
        block._nonce = BCController.mine2(block, BCController.DIFFICULTY)

        # hash and add block
        digest = hash(block)
        BCController.last_block_hash = digest
        BCController.ledger.add_block(block)

        # send reward to miner
        t = Transaction(BCController.controller_client,
                        miner,
                        BCController.ledger.REWARD)
        BCController.tr_pool.append(t)
        return True
