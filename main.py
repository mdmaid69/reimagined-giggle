import math
def calculate_arc_sine(x):
        return math.asin(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")