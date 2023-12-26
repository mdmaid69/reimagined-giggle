def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")