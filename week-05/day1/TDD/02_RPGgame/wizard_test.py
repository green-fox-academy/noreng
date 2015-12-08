import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard('Merlin', 40, 10, 17)
        self.assertEqual(wizard.manna, 17)

    def test_strike_manna_reduce(self):
        wizard = Wizard('Merlin', 40, 10, 6)
        enemy = Wizard('Oz', 50, 8, 5)
        wizard.strike(enemy)
        self.assertEqual(wizard.manna, 6-5)

    def test_strike_with_manna(self):
        wizard = Wizard('Merlin', 40, 10, 6)
        enemy = Wizard('Oz', 50, 8, 5)
        wizard.strike(enemy)
        self.assertEqual(wizard.manna, 6-5)
        self.assertEqual(enemy.hp, 50-3*10)

    def test_strike_without_manna(self):
        wizard = Wizard('Merlin', 40, 9, 0)
        enemy = Wizard('Oz', 50, 8, 5)
        wizard.strike(enemy)
        self.assertEqual(wizard.manna, 0-0)
        self.assertEqual(enemy.hp, 50-9/3)








unittest.main()
