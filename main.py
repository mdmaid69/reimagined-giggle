import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time