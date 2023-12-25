  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)