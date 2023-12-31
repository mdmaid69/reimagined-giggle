def calculate_roi(gain, cost):
        return (gain - cost) / cost
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")