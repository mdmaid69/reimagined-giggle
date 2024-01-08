  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")