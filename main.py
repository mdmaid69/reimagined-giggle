import numpy as np
print(np.array([1, 2, 3]))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}