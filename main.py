  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)