import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)