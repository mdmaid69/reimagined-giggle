  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)