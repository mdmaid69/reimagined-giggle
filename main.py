  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)