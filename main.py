  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)