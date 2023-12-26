  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)