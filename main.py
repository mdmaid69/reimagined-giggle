  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import numpy as np
print(np.array([1, 2, 3]))