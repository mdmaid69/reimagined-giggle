import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import os
def get_file_size(filename):
        return os.path.getsize(filename)