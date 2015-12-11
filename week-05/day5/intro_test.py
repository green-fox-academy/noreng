import unittest
from intro import get_names, filter_names

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.names = [  {'id': 1, 'name': 'John'},
                        {'id': 2, 'name': 'Molly'},
                        {'id': 3, 'name': 'Jane'}]

    def test_get_names_function(self):
        self.assertEqual(get_names(self.names), ['John', 'Molly', 'Jane'])

    def test_filter_names_function(self):
        self.assertEqual(filter_names(self.names), ['John', 'Jane'])
        self.assertEqual(filter_names_list_compreh(self.names), ['John', 'Jane'])

unittest.main()
