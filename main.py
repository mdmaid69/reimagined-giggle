  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)