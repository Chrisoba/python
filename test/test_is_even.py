import unittest
from is_even import is_even

class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

    def test_odd(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-3))
        self.assertFalse(is_even(7))

if __name__ == "__main__":
    unittest.main()
