  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"