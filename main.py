import os
def remove_directory(path):
        os.rmdir(path)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)