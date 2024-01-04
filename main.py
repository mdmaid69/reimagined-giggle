  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)