import array
def get_array_item_count(array, item):
        return array.count(item)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")