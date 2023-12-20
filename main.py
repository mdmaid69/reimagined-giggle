  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)