import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import shutil
def delete_directory(path):
        shutil.rmtree(path)