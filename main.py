import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)