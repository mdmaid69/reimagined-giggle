  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import numpy as np
print(np.array([1, 2, 3]))