import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")