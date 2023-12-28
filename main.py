import array
def get_array_buffer_info(array):
        return array.buffer_info()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")