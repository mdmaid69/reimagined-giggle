  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)