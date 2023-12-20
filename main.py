  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)