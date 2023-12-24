  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)