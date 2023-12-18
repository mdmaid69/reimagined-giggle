  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)