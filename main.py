  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)