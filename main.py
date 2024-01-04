  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare