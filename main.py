  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)