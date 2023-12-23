  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()