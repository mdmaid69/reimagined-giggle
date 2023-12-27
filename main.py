  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]