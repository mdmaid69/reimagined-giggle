import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)