  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)