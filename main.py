  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")