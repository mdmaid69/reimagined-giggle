  import os
  def split_path(path):
        return os.path.split(path)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)