import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a