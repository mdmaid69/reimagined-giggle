import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)