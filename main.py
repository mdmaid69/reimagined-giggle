import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")