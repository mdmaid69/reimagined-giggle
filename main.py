  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)