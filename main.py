def calculate_perpetuity(payment, rate):
        return payment / rate
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")