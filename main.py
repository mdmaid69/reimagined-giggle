  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)