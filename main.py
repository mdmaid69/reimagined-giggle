  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)