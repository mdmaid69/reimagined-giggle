def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")