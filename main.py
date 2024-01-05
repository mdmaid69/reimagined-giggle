import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")