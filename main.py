  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)