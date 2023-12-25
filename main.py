  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")