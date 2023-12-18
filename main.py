  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)