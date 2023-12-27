def calculate_average(lst):
        return sum(lst) / len(lst)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")