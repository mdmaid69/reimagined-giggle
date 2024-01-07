  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)