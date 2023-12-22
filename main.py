import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")