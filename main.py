def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")