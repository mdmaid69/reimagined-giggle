import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time