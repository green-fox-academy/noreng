class Warrior:
    def __init__(self):
        self.hp = 100
        self.companions = []

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

    def heal(self, hp):
        self.hp += hp

class Healer:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(10)

    def __repr__(self):
        return 'a shaman'

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)
print(rabbit.companions)

wolf.strike(rabbit)
print(rabbit.hp)
