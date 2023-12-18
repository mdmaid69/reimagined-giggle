  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)