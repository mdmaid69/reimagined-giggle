  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))