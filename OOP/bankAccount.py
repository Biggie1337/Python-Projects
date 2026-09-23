class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
            print(f"Current balance: {self.balance}")
        else:
            self.balance -= amount

    def get_info(self):
        return f"Account Owner: {self.owner}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += (self.balance * self.interest_rate/100)

    def get_info(self):
        return super().get_info() + f", Interest Rate: {self.interest_rate}"

bankAccount = BankAccount("Dimitar", 1200)
savingsAccount = SavingsAccount("Dimitar", 1000, 5)

print(bankAccount.get_info())
print(savingsAccount.get_info())

savingsAccount.add_interest()

print(savingsAccount.get_info())
