  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)