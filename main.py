  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))