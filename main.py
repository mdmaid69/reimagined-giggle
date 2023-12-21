import os
def list_files_in_directory(path):
        return os.listdir(path)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")