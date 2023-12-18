n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)