  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)