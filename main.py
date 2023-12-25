  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)