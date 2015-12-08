from character import Character

class Barbarian(Character):
    def strike(self, enemy):
        enemy.hp -= self.damage * 2
