  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)