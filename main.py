  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)