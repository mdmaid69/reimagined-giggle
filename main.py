import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)