  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)