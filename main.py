  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))