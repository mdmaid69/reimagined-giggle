import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a