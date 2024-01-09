  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)