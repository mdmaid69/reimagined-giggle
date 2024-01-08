import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)