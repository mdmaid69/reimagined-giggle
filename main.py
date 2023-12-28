  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)