# https://github.com/mkachergus/Lab11-AF-MK
# Partner 1: Alejandro Fernandez
# Partner 2: Your partner's name

import unittest
import calculator
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(2, 5), 2.5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
# Do not touch this
if __name__ == "__main__":
    unittest.main()