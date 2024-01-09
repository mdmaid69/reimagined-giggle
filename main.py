import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")