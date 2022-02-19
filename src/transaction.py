import collections
import datetime
import binascii
from client import Client
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

###########################
class Transaction:
    '''client can be both a sender or a recipient of the money.
    When you want to receive money, some other sender will create
    a transaction and specify your public address in it.'''

    def __init__(self, sender:Client, recipient:Client, value:int):
        if value <= 0:
            print("Empty transaction.")
            return
        self._sender = sender
        self._recipient = recipient
        self._value = value
        self._time = datetime.datetime.now().strftime('%d %b %y %H: %M: %S')
        self._hash = None

    def to_dict(self):
        ''' combines properties into ordered dictionary '''
        if self._sender._name == 'Genesis':
            identity = 'Genesis'
        else:
            identity = self._sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self._recipient.identity,
            'value': self._value,
            'time': self._time,
            'hash': self._hash
        })

    def sign_transaction(self):
        ''' sign this dictionary object using the private key of the sender. 
        As before, we use the built-in PKI with SHA algorithm. 
        The generated signature is decoded to get the ASCII representation for 
        printing and storing it in our blockchain.'''
        private_key = self._sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new( str( self.to_dict() ).encode('utf8') )
        self._hash = h
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def __str__(self):
        # for transaction in transactions:
        dict = self.to_dict()
        return "--- TRANSACTION START -----------\n" \
            + "sender: " \
            + dict['sender'] \
            + ('\n-----\n') \
            + ("recipient: " \
            + dict['recipient']) \
            + ('\n-----\n') \
            + ("value: " \
            + str(dict['value'])) \
            + ('\n-----\n') \
            + ("time: " \
            + str(dict['time'])) \
            + '\n' \
            + '--- TRANSACTION END -------------\n'
###########################