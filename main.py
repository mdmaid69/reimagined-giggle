  import os
  def get_current_directory():
        return os.getcwd()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")