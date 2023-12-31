  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import os
def list_files_in_directory(path):
        return os.listdir(path)