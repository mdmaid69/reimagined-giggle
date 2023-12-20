  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")