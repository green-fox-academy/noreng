import unittest
from monster import Monster

class TestMonster(unittest.TestCase):
    def test_existance(self):
        monster = Monster('Susu', 20, 1)

    def test_inheritance(self):
        monster = Monster('Susu', 20, 1)
        self.assertEqual(monster.hp, 20)

    def test_strike(self):
        monster = Monster('Susu', 20, 1)
        enemy = Monster('Godzilla', 20, 2)
        monster.strike(enemy)
        self.assertEqual(monster.hp, 22)
        self.assertEqual(enemy.hp, 19)



unittest.main()
