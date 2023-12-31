import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)