  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)