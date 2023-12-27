import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"