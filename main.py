import array
def get_array_as_complex(array):
        return complex(array[0])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")