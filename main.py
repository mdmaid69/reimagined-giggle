  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"