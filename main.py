import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets