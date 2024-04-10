# test_main.py

import unittest
from circleci.main import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        # Test case 1: Positive numbers
        self.assertEqual(add_numbers(5, 3), 8)

        # Test case 2: Negative numbers
        self.assertEqual(add_numbers(-5, -3), -8)

        # Test case 3: Positive and negative numbers
        self.assertEqual(add_numbers(5, -3), 2)

        # Test case 4: Zero
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
