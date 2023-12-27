import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time