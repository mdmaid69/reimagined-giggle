  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)