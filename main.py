  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import numpy as np
print(np.array([1, 2, 3]))