  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import numpy as np
print(np.array([1, 2, 3]))