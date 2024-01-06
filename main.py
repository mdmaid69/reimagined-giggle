  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)