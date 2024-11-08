import pytest
from bank import Account

def test_initial_balance():
    # TODO
    # when we initialize the balance, we want it to be 0. This tests that.
    acc = Account
    assert acc.get_balence == 0

def test_deposit():
   # TODO
   # After we deposit, we want to make sure the account isn't empty
   # and we want to check it has more than it did before
   acc = Account
   first = acc.get_balance()
   acc.deposit(10.5)
   second = acc.get_balance()
   assert second == 10.5 and first < second

def test_withdraw():
   # TODO
    acc = Account
    while acc.get_balance == 0:
        acc.deposit(10.5)
    first = acc.get_balance()
    acc.withdraw(5.5)
    second = acc.get_balance()
    assert second == 5 and first > second