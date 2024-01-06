  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))