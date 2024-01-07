import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")