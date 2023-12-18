  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)