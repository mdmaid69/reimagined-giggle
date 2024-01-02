  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))