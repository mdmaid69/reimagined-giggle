  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)