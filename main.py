import numpy as np
print(np.array([1, 2, 3]))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)