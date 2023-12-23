  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))