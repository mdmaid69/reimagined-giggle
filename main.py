import array
def get_array_as_bytearray(array):
        return bytearray(array)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")