import random

class Weapon:
    def strike(self, warrior, opponent):
        warrior.hp -= self.self_damage()
        opponent.hp -= self.damage()

    def damage(self):
        raise "Not implemented"

    def self_damage(self):
        raise "Not implemented"

class Sword(Weapon):
    def damage(self):
        return 10

    def self_damage(self):
        return 0

class Flamethrower(Weapon):
    def damage(self):
        return 100

    def self_damage(self):
        return random.randint(0,10)

# use a decorator class to "Wrap" a weapon
class Magical(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.self_damage() / 2

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, enemy):
        self.weapon.strike(self, enemy)

    def __repr__(self):
        return "hp = {}".format(self.hp)

warrior = Warrior(Magical(Flamethrower()))
print(warrior)
enemy = Warrior(Sword())
print(enemy)

warrior.strike(enemy)
print(warrior)
print(enemy)
