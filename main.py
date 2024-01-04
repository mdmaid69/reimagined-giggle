import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import math
def calculate_combinations(n, k):
        return math.comb(n, k)