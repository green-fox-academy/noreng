from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        # inherit from parent
        super().__init__(name, hp, damage)
        # add new property
        self.manna = manna

    def strike(self, enemy):
        if self.manna > 5:
            enemy.hp -= self.damage * 3
            self.manna -= 5
        else:
            enemy.hp -= self.damage / 3
