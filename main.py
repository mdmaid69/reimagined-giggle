  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)