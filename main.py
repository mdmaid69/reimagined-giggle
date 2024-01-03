  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)