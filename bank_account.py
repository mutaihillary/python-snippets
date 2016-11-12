class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, cash):
        self.balance += int(cash)

    def withdraw(self, cash):
        if cash > self.balance:
            return "invalid transaction"
        self.balance -= cash

class MinimumBalanceAccount(BankAccount):
    pass