import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import array
def get_array_length(array):
        return len(array)