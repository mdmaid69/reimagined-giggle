  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)