  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))