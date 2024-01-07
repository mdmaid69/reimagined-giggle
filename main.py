  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))