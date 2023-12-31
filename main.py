import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)