n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)