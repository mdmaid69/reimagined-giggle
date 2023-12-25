import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")