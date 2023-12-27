import math
def calculate_gamma_function(x):
        return math.gamma(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")