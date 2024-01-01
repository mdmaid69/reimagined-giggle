  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)