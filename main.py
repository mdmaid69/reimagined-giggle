  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)