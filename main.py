import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")