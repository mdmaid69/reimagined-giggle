  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)