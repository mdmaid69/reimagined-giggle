import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a