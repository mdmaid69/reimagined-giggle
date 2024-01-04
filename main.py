  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink