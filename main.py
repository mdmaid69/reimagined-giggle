import array
def check_if_array_contains_item(array, item):
        return item in array
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")