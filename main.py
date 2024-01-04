  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")