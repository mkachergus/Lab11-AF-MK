# https://github.com/mkachergus/Lab11-AF-MK
# Partner 1: Alejandro Fernandez
# Partner 2: Michael Kachergus

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
    def test_add(self):
        self.assertEqual(calculator.add(3, 5), 8)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 3)
    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3.0)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

if __name__ == "__main__":
    unittest.main()
