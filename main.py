import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")