  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))