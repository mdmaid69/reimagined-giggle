  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])