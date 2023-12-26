  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)