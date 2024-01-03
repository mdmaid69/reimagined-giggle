import array
def get_array_as_frozenset(array):
        return frozenset(array)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")