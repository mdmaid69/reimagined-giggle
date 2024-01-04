import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)