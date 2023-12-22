import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")