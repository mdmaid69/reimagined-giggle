import array
def set_array_item(array, i, item):
        array[i] = item
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")