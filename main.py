import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]