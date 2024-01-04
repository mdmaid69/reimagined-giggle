  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)