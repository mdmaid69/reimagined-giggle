import array
def get_array_index(array, item):
        return array.index(item)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")