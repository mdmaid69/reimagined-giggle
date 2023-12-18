  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")