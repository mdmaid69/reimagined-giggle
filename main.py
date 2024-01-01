import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a