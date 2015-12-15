import unittest
from menuitems import create_main_menu
# from menu import Menu, MenuItem

class TestMainMenuCreator(unittest.TestCase):
    def test_existence(self):
        menu = create_main_menu()

    def test_created_menu(self):
        menu = create_main_menu()
        self.assertEqual(menu.get_menu(), '1 New Game\n2 Load Game\n0 Exit')

if __name__ == "__main__":
    unittest.main()
