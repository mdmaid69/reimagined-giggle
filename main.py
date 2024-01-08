import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)