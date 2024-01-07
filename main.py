  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)