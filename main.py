  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")