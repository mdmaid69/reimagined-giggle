  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()