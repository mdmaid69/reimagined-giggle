  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino