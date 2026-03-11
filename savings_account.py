from account import BankAccount

class SavingsAccount(BankAccount):
    """
    Derived class representing a savings account.
    """

    def __init__(self, name, balance=0, interest_rate=0.02):
        """
        Initialize savings account with interest rate.
        """
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """
        Add interest to the account balance.
        """
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return f"Interest of {interest} added."

    def withdraw(self, amount):
        """
        Override withdraw method to add withdrawal limit.
        """
        if amount > 10000:
            return "Withdrawal limit exceeded for savings account"
        return super().withdraw(amount)