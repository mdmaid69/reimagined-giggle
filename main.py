  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)