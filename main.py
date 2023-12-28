  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))