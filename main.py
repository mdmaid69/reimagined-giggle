  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)