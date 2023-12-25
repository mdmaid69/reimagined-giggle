  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")