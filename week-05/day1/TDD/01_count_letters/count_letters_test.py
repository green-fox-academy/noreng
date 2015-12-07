import unittest
from count_letters import count_letters

class LetterCounterTest(unittest.TestCase):
    def test_if_exists(self):
        self.assertEqual(count_letters(''), {})

    def test_same_letters(self):
        self.assertEqual(count_letters('a'), {'a': 1})
        self.assertEqual(count_letters('aa'), {'a': 2})
        self.assertEqual(count_letters('b'), {'b': 1})
        self.assertEqual(count_letters('bbb'), {'b': 3})

    def test_different_letters(self):
        self.assertEqual(count_letters('ab'), {'a':1, 'b': 1})
        self.assertEqual(count_letters('abc'), {'a':1, 'b':1, 'c':1})
        self.assertEqual(count_letters('abcb'), {'a':1, 'b':2, 'c':1})
        self.assertEqual(count_letters('kacsa'), {'a':2, 'k':1, 'c':1, 's':1})

unittest.main()
