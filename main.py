import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)