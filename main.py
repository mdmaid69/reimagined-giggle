  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)