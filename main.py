  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)