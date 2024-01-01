  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))