import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")