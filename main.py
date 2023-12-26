  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()