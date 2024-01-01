  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import numpy as np
print(np.array([1, 2, 3]))