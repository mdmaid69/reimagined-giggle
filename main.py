import array
def convert_array_to_unicode(array):
        return array.tounicode()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")