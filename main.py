import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)