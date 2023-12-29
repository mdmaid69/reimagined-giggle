import math
def calculate_ceiling(x):
        return math.ceil(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")