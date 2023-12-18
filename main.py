import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")