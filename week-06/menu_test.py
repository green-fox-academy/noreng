import unittest
from menu import MenuItem, Menu, menu_items
from commands import *

class TestMenuItem(unittest.TestCase):
    def test_existence(self):
        menu1 = MenuItem(0, 'New Game')

    def test_menu_item_parameters(self):
        menu1 = MenuItem(0, 'New Game')
        self.assertEqual(menu1.id, 0)
        self.assertEqual(menu1.text, 'New Game' )

    def test_menu_item_representation(self):
        menuitem = MenuItem(1, 'Load Game')
        menuitem = str(menuitem)
        self.assertEqual(menuitem, '1 Load Game')

class TestMenu(unittest.TestCase):
    def setUp(self):
        items = [
            MenuItem(1, 'New Game', 'new'),
            MenuItem(2, 'Load Game', 'load'),
            MenuItem(0, 'Exit', 'exit')
            ]
        self.testmenu = Menu(items)

    def test_existence(self):
        self.testmenu

    def test_get_menu_items(self):
        menu = self.testmenu
        self.assertEqual(menu.get_menu(), '1 New Game\n2 Load Game\n0 Exit')

    def test_select_menu_item(self):
        menu = self.testmenu
        user_choice = [0, 1, 2, 8]
        self.assertEqual(menu.select_item(user_choice[0]), 'exit')
        self.assertEqual(menu.select_item(user_choice[1]), 'new')
        self.assertEqual(menu.select_item(user_choice[2]), 'load')
        self.assertEqual(str(menu.select_item(user_choice[3])), 'Wrong input')

if __name__ == "__main__":
    unittest.main()
