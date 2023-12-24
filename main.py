  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")