  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")