  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)