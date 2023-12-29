  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))