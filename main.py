  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")