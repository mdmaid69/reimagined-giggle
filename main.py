  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)