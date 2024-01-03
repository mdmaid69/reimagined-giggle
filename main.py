  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")