import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)