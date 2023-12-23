import array
def get_array_slice(array, i, j):
        return array[i:j]
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")