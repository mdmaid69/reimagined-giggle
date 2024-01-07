  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)