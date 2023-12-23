  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import numpy as np
print(np.array([1, 2, 3]))