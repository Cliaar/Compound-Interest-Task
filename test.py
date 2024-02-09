import unittest
from unittest import mock
from parameterized import parameterized
from calculator import compoundInterestCalculator

class TestCompoundInterestCalculator(unittest.TestCase):
    @parameterized.expand([
        (100, 5, 2, 15),
        (200, 10, 3, 12),
        (300, 15, 4, 10),
        (400, 20, 5, 9),
        (500, 25, 6, 9),
        (600, .2, 2, 347),
    ])
    def testCasesValidInput(self, deposit, interest, multiplicationFactor, expected):
        self.assertEqual(compoundInterestCalculator(deposit, interest, multiplicationFactor), expected)

    @parameterized.expand([
        ("$400", 20, 5),
        (500, "25%", 6),
        (600, 30, "7x"),
        (0, 0, 0),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (None, 2, 3),
        (300, None, 3),
        (200, 2, None)
    ])
    def testCasesInvalidInput(self, deposit, interest, multiplicationFactor):
        with self.assertRaises(ValueError):
            compoundInterestCalculator(deposit, interest, multiplicationFactor)

if __name__ == '__main__':
    unittest.main()