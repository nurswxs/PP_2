class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance


balance, withdrawal = map(int, input().split())
acc = Account("Owner", balance)
result = acc.withdraw(withdrawal)
print(result)
