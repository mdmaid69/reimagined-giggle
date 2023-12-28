import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")