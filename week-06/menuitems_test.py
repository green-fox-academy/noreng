import unittest
from menuitems import *

class TestMainMenuCreator(unittest.TestCase):
    def test_existence(self):
        menu = create_menu(menuitems['main'])

    def test_created_menu(self):
        menu = create_menu(menuitems['main'])
        self.assertEqual(menu.get_menu(), '1 New Game\n2 Load Game\n0 Exit')

if __name__ == "__main__":
    unittest.main()
