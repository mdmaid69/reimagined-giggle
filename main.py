import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable