  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)