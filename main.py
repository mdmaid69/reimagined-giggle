  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)