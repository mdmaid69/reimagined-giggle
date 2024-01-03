  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True