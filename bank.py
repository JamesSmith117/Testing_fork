class Account:
    def __init__(self, owner, balance=0):
        """Initialize an account with an owner name and an optional starting balance.

        Args:
            owner (str): The name of the account owner.
            balance (float): The initial balance of the account (default is 0).
        """


    def deposit(self, amount):
        """Deposit a positive amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.

        Returns:
            float: The new balance after the deposit.
        """
        balence = balence
        new = balence + amount
        return new


    def withdraw(self, amount):
        """Withdraw a positive amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the balance.

        Returns:
            float: The new balance after the withdrawal.
        """
        balence = balence
        new = balence - amount
        return new

    def get_balance(self):
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        balence = balence
        return balence
 

    def transfer(self, amount, to_account):
        """Transfer a positive amount to another account.

        Args:
            amount (float): The amount to transfer.
            to_account (Account): The account to which the amount is transferred.

        Raises:
            ValueError: If the transfer amount is not positive or exceeds the balance.
        """
