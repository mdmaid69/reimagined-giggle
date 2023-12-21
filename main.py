  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")