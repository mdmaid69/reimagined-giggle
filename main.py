  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])