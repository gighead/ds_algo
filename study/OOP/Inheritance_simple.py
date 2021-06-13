class Account:

    def __init__(self, title=None, balance=None):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):

    def __init__(self, title=None, balance=None, interestRate=None):
        self.interestRate = interestRate
        super().__init__(title,balance)


o1 = Account("Mark", 5000)

o2 = SavingsAccount("Mark", 5000, 5)
print(o2)
