  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")