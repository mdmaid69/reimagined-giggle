import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)