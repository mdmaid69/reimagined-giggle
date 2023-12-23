def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")