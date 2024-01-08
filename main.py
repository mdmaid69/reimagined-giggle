  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")