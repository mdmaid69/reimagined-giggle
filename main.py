  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)