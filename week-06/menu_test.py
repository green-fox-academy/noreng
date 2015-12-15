import unittest
from menu import Menu, MenuItem
from menuitems import *

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
        menu = create_menu(menuitems['main'])
        self.assertEqual(menu.get_menu(), '1 New Game\n2 Load Game\n0 Exit')

    def test_select_menu_item(self):
        menu = Menu([
                    MenuItem(1, 'Test', lambda : True),
                    MenuItem(2, 'Test2', lambda : False)
                    ])
        self.assertTrue(menu.select_item(1))
        self.assertFalse(menu.select_item(2))
        self.assertEqual(str(menu.select_item('8')), '8 is wrong input')
        self.assertEqual(str(menu.select_item('abc')), 'abc is wrong input')

if __name__ == "__main__":
    unittest.main()
