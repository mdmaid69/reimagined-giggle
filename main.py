n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)