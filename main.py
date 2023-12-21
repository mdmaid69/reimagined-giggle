  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid