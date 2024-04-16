import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2)
    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)
    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(6), 8)

unittest.main()