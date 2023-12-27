import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import math
def calculate_logarithm(base, x):
        return math.log(x, base)