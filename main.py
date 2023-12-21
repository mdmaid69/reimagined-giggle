  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)