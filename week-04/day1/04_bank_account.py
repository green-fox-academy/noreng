class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def bal(self):
        print('Balance of:')
        print(self.name)
        print('is:')
        print(self.balance)

    def transfer(self, account, amount):
        self.pay(amount)
        self.receive(amount)
        # account.balance += amount
        # self.balance -= amount

norbi = Bank_account('Norbert Pozsonyi', 50000)
feri = Bank_account('Feri *', 7000000)

norbi.transfer(feri, 40000) # norbi.balance = 50000-10000
