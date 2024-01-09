  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")