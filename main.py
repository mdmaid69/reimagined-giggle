  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])