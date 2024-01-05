  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)