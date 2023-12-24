  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")