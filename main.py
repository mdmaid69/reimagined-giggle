import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import numpy as np
print(np.array([1, 2, 3]))