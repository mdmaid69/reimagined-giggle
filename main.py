import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")