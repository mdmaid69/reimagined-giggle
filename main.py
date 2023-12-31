  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)