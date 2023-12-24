  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)