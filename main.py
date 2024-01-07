import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)