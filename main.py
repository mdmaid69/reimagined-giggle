import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity