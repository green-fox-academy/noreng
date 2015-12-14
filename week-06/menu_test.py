import unittest
from menu import MenuItem, Menu, create_main_menu
from commands import *

class TestMenuItem(unittest.TestCase):
    def test_existence(self):
        menu1 = MenuItem('0', 'New Game')

    def test_menu_item_parameters(self):
        menu1 = MenuItem('0', 'New Game')
        self.assertEqual(menu1.id, '0')
        self.assertEqual(menu1.text, 'New Game' )

    def test_menu_item_representation(self):
        menuitem = MenuItem('1', 'Load Game')
        menuitem = str(menuitem)
        self.assertEqual(menuitem, '1 Load Game')

class TestMenu(unittest.TestCase):

    def test_existence(self):
        menu = Menu(MenuItem('0', 'New Game'))

    def test_get_menu_items(self):
        menu = create_main_menu()
        self.assertEqual(menu.get_menu(), '1 New Game\n2 Load Game\n0 Exit')

    def test_select_menu_item(self):
        menu = create_main_menu()
        self.assertEqual(str(menu.select_item('0')), 'exit')
        self.assertEqual(str(menu.select_item('1')), 'Not yet implemented')
        self.assertEqual(str(menu.select_item('2')), 'Not yet implemented')
        self.assertEqual(str(menu.select_item('8')), 'Wrong input')
        self.assertEqual(str(menu.select_item('abc')), 'Wrong input')

if __name__ == "__main__":
    unittest.main()
