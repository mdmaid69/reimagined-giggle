import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")