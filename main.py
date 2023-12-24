def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)