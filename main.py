  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)