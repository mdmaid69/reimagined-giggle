import numpy as np
print(np.array([1, 2, 3]))
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize