# Create a Game Character class:
#
# that stores it's Name
# that stores it's Health Points (HP)
# that stores it's Damage
# Methods:
#
# It should have a print_status method that describes the object:
# if the HP are zero it should print it's name and "Dead"
# if the HP are bigger than zero it should print it's name and HP
# It should have a drink_potion method that increases its HP by 10
# It should have a strike method that takes an other object and reduces it's HP by the current objects demage

class Game_Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def status(self):
        if self.hp == 0:
            print(self.name + ' is dead')
        if self.hp > 0:
            print(self.name + '\'s hp is: ' + str(self.hp))

    def drink(self):
        self.hp += 10

    def strike(self, enemy):
        enemy.hp -= self.damage

class Cerlic(Game_Character):
    def heal(self, ally):
        ally.ph += 10

norbi = Game_Character('norbi', 300, 123)
johnny = Game_Character('John', 400, 20)
melkor = Cerlic('Melkor', 1000, 80)

norbi.status()
johnny.status()
norbi.strike(johnny)
norbi.status()
johnny.status()
