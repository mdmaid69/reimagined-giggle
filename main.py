  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)