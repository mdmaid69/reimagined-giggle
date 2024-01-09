import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")