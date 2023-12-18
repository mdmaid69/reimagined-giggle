import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)