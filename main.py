  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)