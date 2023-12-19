  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)