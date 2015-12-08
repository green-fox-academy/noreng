class Fibonacci:
    def __init__(self, count):
        self.count = count
        self.a = 0
        self.b = 1
        self.i = 0

    def __next__(self):
        if self.i >= self.count:
            raise StopIteration()
        self.i += 1
        curr = self.a
        self.a, self.b = self.a + self.b, self.a
        return curr

    def __iter__(self):
        return self

for n in Fibonacci(5):
    print(n)
# > 0 1 1 2 3

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    # make this object iterable
    def __iter__(self):
        return iter(self.items)

class Sword:
    def __repr__(self):
        return "It is a sword object"

class Coin:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Coin: {}".format(self.value)


inventory = Inventory()
inventory.add(Coin(5))
inventory.add(Coin(1))
inventory.add(Coin(2))
inventory.add(Sword())

for item in inventory:
    print(item)
# > Coin: 5
# > Coin: 1
# > Coin: 2
# > It is a sword
