  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)