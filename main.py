import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)