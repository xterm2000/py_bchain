class Block:
    '''simple Block class '''
    def __init__(self) -> None:
        self._verified_transactions = []
        self._previous_block_hash = ""
        self._nonce = ""
    def __str__(self) -> str:
        s = '\n--- BLOCK START --------------\n'
        for x in self._verified_transactions:
            s+= str(x) + '\n'
        s+= '\n--- BLOCK END ----------------\n\n'            
        return s

