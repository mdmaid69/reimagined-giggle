  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)