import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import numpy as np
print(np.array([1, 2, 3]))