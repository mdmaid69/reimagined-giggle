  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)