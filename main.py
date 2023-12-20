  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)