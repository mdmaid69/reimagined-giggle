  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)