import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")