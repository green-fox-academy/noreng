class BankAccount:
    def __init__(self, name, startBalance = 0):
        self.name = name
        self.balance = startBalance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
