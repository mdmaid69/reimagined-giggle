  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")