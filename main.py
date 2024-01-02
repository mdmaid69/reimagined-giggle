import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)