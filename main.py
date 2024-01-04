  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)