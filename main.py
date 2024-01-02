n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)