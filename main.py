import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import glob
def find_files(pattern):
        return glob.glob(pattern)