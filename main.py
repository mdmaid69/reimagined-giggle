import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")