  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)