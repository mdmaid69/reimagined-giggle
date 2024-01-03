  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])