  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")