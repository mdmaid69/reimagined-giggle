import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")