import array
def iterate_over_array(array):
        for item in array:
        print(item)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")