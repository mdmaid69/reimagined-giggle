  import os
  def get_current_directory():
        return os.getcwd()
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)