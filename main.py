  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)