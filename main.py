  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import shutil
def delete_directory(path):
        shutil.rmtree(path)