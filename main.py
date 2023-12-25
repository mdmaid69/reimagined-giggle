import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)