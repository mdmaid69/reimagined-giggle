import numpy as np
print(np.array([1, 2, 3]))
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink