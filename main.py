  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)