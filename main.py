  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))