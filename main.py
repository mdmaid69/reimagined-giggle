  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")