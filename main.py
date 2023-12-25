import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")