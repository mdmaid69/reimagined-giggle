  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import numpy as np
print(np.array([1, 2, 3]))