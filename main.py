  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"