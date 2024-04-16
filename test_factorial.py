import unittest
from main import factoriales

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factoriales(0), 1)
    def test_factorial_1(self):
        self.assertEqual(factoriales(1), 1)
    def test_factorial_2(self):
        self.assertEqual(factoriales(2), 2)
    def test_factorial_3(self):
        self.assertEqual(factoriales(3), 6)
    def test_factorial_4(self):
        self.assertEqual(factoriales(4), 24)
    def test_factorial_5(self):
        self.assertEqual(factoriales(5), 120)
    def test_factorial_6(self):
        self.assertEqual(factoriales(6), 720)
    def test_factorial_7(self):
        self.assertEqual(factoriales(7), 5040)
    def test_factorial_8(self):
        self.assertEqual(factoriales(8), 40320)
    def test_factorial_9(self):
        self.assertEqual(factoriales(9), 362880)
    def test_factorial_10(self):
        self.assertEqual(factoriales(10), 3628800)

unittest.main()