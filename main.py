import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")