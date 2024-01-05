  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)