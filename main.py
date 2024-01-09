n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)