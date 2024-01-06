  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)