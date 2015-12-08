from character import Character

class Monster(Character):
    def strike(self, enemy):
        self.hp += 2
        # call and use the parent class's strike() method
        super().strike(enemy)
