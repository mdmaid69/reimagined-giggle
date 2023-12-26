import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)