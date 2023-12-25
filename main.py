import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)