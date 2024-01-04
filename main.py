import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)