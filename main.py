import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"