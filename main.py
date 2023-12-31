n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)