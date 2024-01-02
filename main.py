import numpy as np
print(np.array([1, 2, 3]))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)