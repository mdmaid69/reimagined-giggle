  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)