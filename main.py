import array
def get_array_itemsize(array):
        return array.itemsize
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")