import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")