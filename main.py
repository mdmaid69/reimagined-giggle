import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import array
def insert_into_array(array, i, item):
        array.insert(i, item)