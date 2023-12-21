  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")