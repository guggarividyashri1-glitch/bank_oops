class BankAccount:
    """
    Base class representing a generic bank account.
    """

    def __init__(self, name, balance=0):
        """
        Initialize account holder name and balance.
        """
        self.name = name
        self.__balance = balance  

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount > 0:
            self.__balance += amount
            return f"{amount} deposited successfully."
        return "Invalid deposit amount"

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"{amount} withdrawn successfully."

    def get_balance(self):
        """
        Return the current account balance.
        """
        return self.__balance

    def display_account(self):
        """
        Display account holder details.
        """
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)