  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b