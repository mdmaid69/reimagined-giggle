  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")