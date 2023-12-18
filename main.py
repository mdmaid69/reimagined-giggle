import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")