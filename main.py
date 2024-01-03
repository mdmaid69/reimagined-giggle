import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")