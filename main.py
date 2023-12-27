  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)