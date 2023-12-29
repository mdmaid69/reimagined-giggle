def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")