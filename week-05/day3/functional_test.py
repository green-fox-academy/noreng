import unittest
import functional

class Testfunc(unittest.TestCase):
    def test_apply_func(self):
        array = [1, 2, 3]
        self.assertEqual(functional.adder(array), [2, 3, 4])

    def test_filter_array(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(functional.filter_array(array), [3, 6, 9])

unittest.main()
