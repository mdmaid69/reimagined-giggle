import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)