import Crypto
import Crypto.Random
import binascii
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA



class Client:
    def __init__(self, name: str = "noname"):
        random = Crypto.Random.new().read
        # self.time = datetime.datetime.now().
        self._private_key = RSA.generate(1024,random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        self._name = name       

    

    def print(self) -> None:
        print(u" Name: {self._name},  identity: {self.identity}")
        

    @property
    def identity(self) -> str:
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
