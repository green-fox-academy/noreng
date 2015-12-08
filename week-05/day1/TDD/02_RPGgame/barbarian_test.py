import unittest
from barbarian import Barbarian

class TestBarbarian(unittest.TestCase):
    def test_existance(self):
        barbarian = Barbarian('Conan', 100, 10)

    def test_inheritance(self):
        barbarian = Barbarian('Conan', 100, 10)
        self.assertEqual(barbarian.hp, 100)

    def test_strike(self):
        barbarian = Barbarian('Conan', 100, 10)
        enemy = Barbarian('Xena', 100, 10)
        barbarian.strike(enemy)
        self.assertEqual(enemy.hp, 80)


unittest.main()
