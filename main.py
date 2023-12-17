  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)