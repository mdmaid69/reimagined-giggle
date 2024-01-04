import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")