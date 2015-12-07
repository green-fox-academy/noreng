import unittest
from anagramm import *

class Test_is_anagramm(unittest.TestCase):
    def test_anagramm(self):
        self.assertEqual(is_anagramm('',''), True)
        self.assertEqual(is_anagramm('a',''), False)
        self.assertEqual(is_anagramm('ab','ba'), True)
        self.assertEqual(is_anagramm('abc','bac'), True)
        self.assertEqual(is_anagramm('435','345'), True)

unittest.main()
