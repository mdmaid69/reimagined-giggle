numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)