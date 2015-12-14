import unittest
from commands import *

class TestResult(unittest.TestCase):
    def test_existence(self):
        result = Result(True)

    def test_result_parameters(self):
        result = Result(True)
        result2 = Result(False, 'Error Message')
        self.assertTrue(result.success)
        self.assertEqual(result.text, None)
        self.assertFalse(result2.success)
        self.assertEqual(result2.text, 'Error Message')

if __name__ == "__main__":
    unittest.main()
