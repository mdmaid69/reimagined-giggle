  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)