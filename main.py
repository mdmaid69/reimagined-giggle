  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")