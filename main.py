import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)