from transaction import Transaction
from client import Client
transactions = []

genesis = Client("GENESIS")
alice = Client("alice")
bob = Client("bob")
charlie = Client("charlie")
david = Client("david")


def init() -> None:

    t0 = Transaction(
        genesis,
        alice,
        500.0
    )
    t0._hash = t0.sign_transaction()
    transactions.append(t0)
    t1 = Transaction(
        alice,
        bob,
        3.3

    )
    t1.sign_transaction()
    transactions.append(t1)

    t2 = Transaction(
        alice,
        charlie,
        6.0
    )
    t2.sign_transaction()
    transactions.append(t2)
    t3 = Transaction(
        bob,
        david,
        2.0
    )
    t3.sign_transaction()
    transactions.append(t3)
    t4 = Transaction(
        charlie,
        bob,
        4.0
    )
    t4.sign_transaction()
    transactions.append(t4)
    t5 = Transaction(
        david,
        charlie,
        7.0
    )
    t5.sign_transaction()
    transactions.append(t5)
    t6 = Transaction(
        bob,
        charlie,
        3.0
    )
    t6.sign_transaction()
    transactions.append(t6)
    t7 = Transaction(
        charlie,
        alice,
        8.0
    )
    t7.sign_transaction()
    transactions.append(t7)
    t8 = Transaction(
        charlie,
        bob,
        1.0
    )
    t8.sign_transaction()
    transactions.append(t8)
    t9 = Transaction(
        david,
        alice,
        5.0
    )
    t9.sign_transaction()
    transactions.append(t9)
    t10 = Transaction(
        david,
        bob,
        3.0
    )
    t10.sign_transaction()
    transactions.append(t10)
