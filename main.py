def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")