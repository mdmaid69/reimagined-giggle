import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)