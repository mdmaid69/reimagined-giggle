import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)