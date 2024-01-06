  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b