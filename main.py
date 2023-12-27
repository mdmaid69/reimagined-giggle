import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")