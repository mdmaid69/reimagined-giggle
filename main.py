import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value