import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")