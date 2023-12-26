  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)